.PHONY: dev install lint format test notebooks marimo clean

# Install all dependencies (including dev)
install:
	uv pip install .[dev]

dev: install

# Run Ruff linter
lint:
	ruff check src

# Auto-format with Black
format:
	black src

# Run tests
test:
	pytest tests

# Run Jupyter notebooks
notebooks:
	jupyter notebook notebooks/

# Run Marimo notebook demo
marimo:
	marimo run notebooks/marimo_demo.marimo.py


# Remove the virtual environment
clean:
	rm -rf .venv

