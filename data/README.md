# Data

Local data artifacts for development live here.

- `downloads/` holds raw source files fetched from SEC EDGAR, grouped by year.
- `markdown/` holds Markdown converted from the downloaded source files.
- Downloaded and converted payloads are gitignored because the corpus can get large.
- Fetch a sample corpus with `uv run data/download.py` 
- Convert the downloaded filings with `uv run data/convert_to_markdown.py`.
