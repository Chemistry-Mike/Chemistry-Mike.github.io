#!/usr/bin/env python3
"""Verify the two poster landing pages against their unchanged downloadable data.
Run from the repository root. Optionally pass --site _site after a Jekyll build.
This validates data and source structure; it does not substitute for a build/browser test.
"""
import argparse
import csv
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'files/research/p53-gsm'
ROUTES = {
    'sequence-context': '/research/p53-gsm-sequence-context/',
    'short-md-pipeline': '/research/p53-gsm-short-md-pipeline/',
}

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tables = {}
        self.table = None
        self.row = None
        self.cell = None
        self.urls = []
        self.stack = []
        self.ids = set()
        self.labels = []
        self.figure_count = 0
    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag not in {'img', 'br', 'hr', 'meta', 'link', 'input', 'source', 'wbr'}:
            self.stack.append(tag)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, 'Duplicate HTML ID'
            self.ids.add(attrs['id'])
        self.labels.extend(attrs.get('aria-labelledby', '').split())
        for key in ('href', 'src'):
            if key in attrs: self.urls.append(attrs[key])
        if tag == 'img':
            assert attrs.get('alt'), 'Figure needs descriptive alt text'
            assert int(attrs['width']) > 0 and int(attrs['height']) > 0
            self.figure_count += 1
        if tag == 'table':
            self.table = attrs.get('data-poster-table')
            if self.table: self.tables[self.table] = []
        if tag == 'tr' and self.table: self.row = []
        if tag in ('td', 'th') and self.row is not None: self.cell = ''
    def handle_data(self, value):
        if self.cell is not None: self.cell += value
    def handle_endtag(self, tag):
        assert self.stack and self.stack.pop() == tag, f'Unbalanced HTML: {tag}'
        if tag in ('td', 'th') and self.cell is not None:
            self.row.append(self.cell.strip()); self.cell = None
        if tag == 'tr' and self.row is not None:
            self.tables[self.table].append(self.row); self.row = None
        if tag == 'table': self.table = None

def rows(study, filename):
    path = DATA / study / filename
    with path.open(newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t' if path.suffix == '.tsv' else ','))

def rendered_source(path):
    text = path.read_text().split('---', 2)[2]
    # Resolve only the literal relative_url expressions used by these pages.
    return re.sub(r"{{\s*'([^']+)'\s*\|\s*relative_url\s*}}", r'\1', text)

def parse(text):
    page = Page(); page.feed(text)
    assert not page.stack, 'Unclosed HTML element'
    assert all(label in page.ids for label in page.labels)
    return page

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path)
    args = parser.parse_args()
    manifest = json.loads((DATA / 'asset-checksums.json').read_text())
    for record in manifest:
        source = ROOT / record['path']
        assert hashlib.sha256(source.read_bytes()).hexdigest() == record['sha256'], record['path']
        if args.site:
            deployed = args.site / record['path']
            assert deployed.read_bytes() == source.read_bytes(), str(deployed)
    destinations = json.loads((ROOT/'images/research/p53-gsm/qr/destinations.json').read_text())
    pages = {}
    for name, route in ROUTES.items():
        source = ROOT / '_pages' / ('p53-gsm-' + name + '.md')
        text = source.read_text()
        assert 'permalink: ' + route in text
        assert destinations[name] == 'https://Chemistry-Mike.github.io' + route
        source_body = rendered_source(source)
        page = parse(source_body)
        page.urls.extend(re.findall(r"\]\(([^)]+)\)", source_body))
        pages[name] = page
        assert page.figure_count == (6 if name == 'sequence-context' else 4)
        for url in page.urls:
            if urlsplit(url).scheme: continue
            assert url in ROUTES.values() or url == '/research/' or (ROOT/unquote(url.lstrip('/'))).is_file(), url
        assert any(url == ROUTES['short-md-pipeline' if name == 'sequence-context' else 'sequence-context'] for url in page.urls)
        if args.site:
            target = args.site / route.lstrip('/') / 'index.html'
            assert target.is_file(), str(target)
            actual = parse(target.read_text())
            assert actual.tables == page.tables, 'Rendered table differs from source'
    metrics = rows('context', 'chemical_shift_metrics.csv')
    distance = rows('context', 'ca_distances.csv')
    matches = rows('context', 'chemical_shift_matches.csv')
    context_names = ['TAD','TAD_PRD','TAD_PRD_DBD','Full']
    expected_counts = [4950,4995,4620,4419]
    for displayed, ctx, count in zip(pages['sequence-context'].tables['context-summary'][1:], context_names, expected_counts):
        assert int(displayed[1].replace(',', '')) == count
        frame_counts = {int(r['n_frames']) for r in matches if r['context'] == ctx}
        assert frame_counts == {count}, (ctx, frame_counts)
        d = next(r for r in distance if r['context']==ctx and r['residue_i']=='1' and r['residue_j']=='28')
        assert displayed[2] == f"{float(d['mean_nm']):.2f}"
        for value, atom in zip(displayed[3:], ['C','CA','CB','N','HN']):
            metric = next(r for r in metrics if r['context']==ctx and r['atom']==atom)
            assert value == f"{float(metric['rmse_ppm']):.3f}"
        assert sum(int(r['n_pairs']) for r in metrics if r['context']==ctx) == 124
    heat = rows('pipeline', 'nmr_heatmap_data_v11.tsv')
    for displayed, method in zip(pages['short-md-pipeline'].tables['pipeline-errors'][1:], ['AF3','Boltz','AlphaFlow','BioEmu','idpSAM','IDPFold']):
        for value,(atom,state) in zip(displayed[1:], [('HN','Original'),('HN','Relaxed'),('CA','Original'),('CA','Relaxed')]):
            metric = next(r for r in heat if r['metric']=='rmse_ppm' and r['method']==method and r['state']==state and r['nucleus']==atom)
            assert value == f"{float(metric['value']):.3f}"
    for displayed, source in zip(pages['short-md-pipeline'].tables['pipeline-counts'][1:], rows('pipeline','rmsf_alignment_v2.tsv')):
        assert displayed == [source['method'],source['original_frames'],source['relaxed_frames']]
    assert len(pages['sequence-context'].tables['context-summary'])==5
    assert len(pages['short-md-pipeline'].tables['pipeline-errors'])==7
    assert len(pages['short-md-pipeline'].tables['pipeline-counts'])==7
    print(f'PASS: 2 routes, 10 figures, 3 data tables, all download links, and {len(manifest)} original asset checksums.')
    print('PASS: summary values agree with the downloadable CSV/TSV files; context counts match shift frame counts.')

if __name__ == '__main__': main()
