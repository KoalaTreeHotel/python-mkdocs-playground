# Testing out MkDocs

Will be adding MkDocs to a large project, using this repo for testing out ideas.
This repo is based on the tutorial from: <https://realpython.com/python-project-documentation-with-mkdocs/>

- `pyenv exec python -m venv .venv` create virtual environment
- `.\.venv\Scripts\activate` activate virtual environment
- (.venv) `python -m pip install mkdocs`
- (.venv) `python -m pip install "mkdocstrings[python]"`
- (.venv) `python -m pip install mkdocs-material`
- `mkdocs serve` to serve up static document webpage (for development)
- `mkdocs build` to build a static webpage (in "site/")
  - `mkdocs gh-deploy` if using GitHub, this will rebuild the
  documentation from the markdown files and source code then
  push it to a branch called "gh-pages"
  - "gh-pages" branches within a GitHub repo are automatically
  served as static content
