# Quantum Pharmacy

Michael Bakker’s academic website, built with Jekyll and AcademicPages for GitHub Pages.

## Edit the site

- `_pages/about.md`: homepage
- `_data/navigation.yml`: main navigation
- `_data/research.yml`: research themes and project cards
- `_pages/`: section landing pages
- `_portfolio/`, `_publications/`, `_teaching/`, `_talks/`, `_posts/`: detailed content
- `assets/css/site.css`: visual design (plain CSS, loaded after the legacy theme stylesheet)

Existing project, publication, CV, and blog URLs remain available.

## Preview locally

Install Ruby and Bundler, then run:

```sh
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

Open http://localhost:4000. Restart Jekyll after editing configuration.

## Validate

```sh
bundle exec jekyll build
python3 scripts/check_site.py _site
```

## Send changes to GitHub

The overhaul is developed on `website-overhaul`. Review and commit the files, then push with an authenticated GitHub account:

```sh
git add .
git commit -m "Redesign Quantum Pharmacy and organize research content"
git push -u origin website-overhaul
```

If Git asks for an author identity, configure your own name and GitHub email with `git config user.name` and `git config user.email` in this repository.

Open a pull request from `website-overhaul` into `master`. Confirm the repository’s Settings → Pages deployment branch or workflow before merging. Publication depends on that configuration.

## Backup

Before editing, a complete repository archive and a verified Git bundle were saved in the workspace’s `backups/` directory (outside this repository). The original commit is `ec1001f217f5c428de708ec8444e4b8ce7d75ae0`; `master` remains at that commit during local development.

## Related publications on project pages

Add a `related_publications` list to a portfolio document’s YAML front matter, using the exact `permalink` values from `_publications/`. The shared layout displays matching papers below the project title, ordered newest first, with summary and publisher links. Projects without a list show no publication section.

```yaml
related_publications:
  - /publication/2024-JCTC-Expansion
  - /publication/2024-JCTC-PTM
```

## Publication metrics

The Publications page counts `_publications/` automatically at each Jekyll build. First-author publications are counted from `first_author: true` in publication front matter; the same flag displays a yellow star beside their titles. Set this flag when adding a new paper. Scholar h-index and citations are stored in `_data/publication_metrics.yml`. Update those values and `last_checked` together when refreshing them. These citation figures are a dated snapshot, not a live Google Scholar connection.

## Project status badges

Set `awaiting_publication: true` or `patent_related: true` in a `_portfolio/` document’s YAML front matter. Shared templates display an hourglass or lock with a visible label on its research card and detail page. Patent-related pages also show “Details withheld due to ongoing patent work.” These are disclosure labels; they do not restrict access or remove content. Only flag projects identified by the author as patent-related.

## Homepage slideshow

Add figures under `images/`, then add an `image` filename and descriptive `alt` text to `_data/hero_images.yml`. The homepage fades between all listed figures every six seconds, with previous/next and pause controls. Reduced-motion visitors start with autoplay paused; without JavaScript the first figure remains visible. The slideshow pauses in background tabs and skips unloaded or failed images.

## p53 conference-poster landing pages

Stable poster destinations (preserve these URLs):

- `/research/p53-gsm-sequence-context/`
- `/research/p53-gsm-short-md-pipeline/`

Page sources are `_pages/p53-gsm-*.md`. Original figure assets are under `images/research/p53-gsm/`; downloadable data and the public SHA-256 manifest are under `files/research/p53-gsm/`. QR PNGs, vector PDFs, TeX sources, and `destinations.json` are in `images/research/p53-gsm/qr/`. Only public handoff assets are copied; private manuscript/provenance notes remain outside the repository.

Checks from the repository root:

```sh
python3 scripts/check_p53_poster.py
python3 scripts/verify_poster_qr.py
bundle exec jekyll build
python3 scripts/check_p53_poster.py --site _site
python3 scripts/check_site.py _site
```

The QR check uses ImageMagick `convert` to read the supplied pristine, axis-aligned version-5/M PNGs. It decodes their URL payloads and compares them exactly with the manifest; it is not a general camera decoder or a printed-poster scan test.

After merging and deployment, open both HTTPS routes and test images/downloads on a phone, then scan each QR at its intended printed size (roughly 30–40 mm including the white quiet zone). Do not finalize poster printing until both destinations are live and public. A local source/data check does not verify live deployment or mobile rendering.
