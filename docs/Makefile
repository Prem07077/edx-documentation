# Makefile for Sphinx documentation

# Define build directory
BUILD_DIR = _build

# Define Sphinx build commands
SPHINX_BUILD = sphinx-build

# Define Sphinx build options
SPHINX_OPTS = -b html .

.PHONY: help clean html lint

# Default target
all: html

# Display available targets
help:
	@echo "Available targets:"
	@echo "  html   - Build HTML documentation"
	@echo "  clean  - Clean build directories"
	@echo "  lint   - Run linting checks on reStructuredText files"

# Clean build directories
clean:
	rm -rf $(BUILD_DIR)

# Build HTML documentation
html:
	$(SPHINX_BUILD) $(SPHINX_OPTS) $(BUILD_DIR)/html

# Lint reStructuredText files
lint:
	@echo "Linting reStructuredText files..."
	@rst-lint **/*.rst || true
