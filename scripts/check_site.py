#!/usr/bin/env python3
"""Check local links and assets in Jekyll's rendered HTML (standard library only)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                self.urls.append(value)

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
    if not (root / 'index.html').is_file():
        sys.exit('No rendered homepage found. Run bundle exec jekyll build first.')
    errors = set()
    pages = list(root.rglob('*.html'))
    for page in pages:
        parser = Links()
        parser.feed(page.read_text())
        for url in parser.urls:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            target = (root / unquote(parts.path).lstrip('/')) if parts.path.startswith('/') else (page.parent / unquote(parts.path))
            if not (target.is_file() or (target / 'index.html').is_file()):
                errors.add(f'{page.relative_to(root)}: {url}')
    for error in sorted(errors):
        print(error)
    print(f'Checked {len(pages)} HTML pages; {len(errors)} missing local targets.')
    return bool(errors)

if __name__ == '__main__':
    sys.exit(main())
