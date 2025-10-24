# Python Project Template with Copier & uv

This repository contains a customizable Python project template powered by [Copier](https://copier.readthedocs.io/) and modern Python packaging standards (`pyproject.toml`).  
It allows you to quickly scaffold robust Python projects with a standardized, reproducible structure and preconfigured developer tools.

---

## Features

- **Dynamic Configuration:** Set your project name, author, and more at generation time.
- **uv & PEP 621 Compatible:** Uses a modern `pyproject.toml` for dependencies and metadata. No `requirements.txt` needed!
- **Flexible Directory Structure:** Standard scientific/data science layout:  
  - Source in `src/`
  - Data in `data/`
  - Notebooks in `notebooks/`
  - Tests in `tests/`
- **Preconfigured Tools:**  
  - [`uv`](https://github.com/astral-sh/uv): Fast dependency management
  - [`pytest`](https://docs.pytest.org/): For testing
  - [`black`](https://black.readthedocs.io/): For code formatting
  - [`isort`](https://pycqa.github.io/isort/): For import sorting
  - [`ruff`](https://docs.astral.sh/ruff/): Fast linting
  - [`jupyter`](https://jupyter.org/): Notebooks
  - [`marimo`](https://github.com/marimo-team/marimo): Reactive Python notebooks

---

## Project Structure

A generated project will look like:

```plaintext
your-project/
├── pyproject.toml      # Project metadata and dependencies (PEP 621)
├── README.md           # Project readme (templated)
├── Makefile            # Dev workflow tasks (lint, test, notebooks, etc.)
├── .gitignore
├── data/               # Data directory (with .gitkeep)
├── notebooks/          # Jupyter & Marimo notebooks
├── src/                # Source code (as package)
│   └── {{ project_slug }}/
│       ├── __init__.py
│       └── config.py
└── tests/              # Test suite

