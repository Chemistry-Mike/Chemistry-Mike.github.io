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
