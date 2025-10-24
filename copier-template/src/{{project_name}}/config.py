from pathlib import Path

# Base directory of the project (usually the root folder containing pyproject.toml)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Data directory
DATA_DIR = BASE_DIR / "data"

# Notebooks directory
NOTEBOOKS_DIR = BASE_DIR / "notebooks"

# Source directory (your package folder)
SRC_DIR = BASE_DIR / "src" / "{{ project_slug }}"

# Tests directory
TESTS_DIR = BASE_DIR / "tests"

