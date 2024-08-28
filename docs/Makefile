# Makefile for Sphinx documentation

.PHONY: help clean html

help:
	@echo "Available targets:"
	@echo "  html   - Build HTML documentation"
	@echo "  clean  - Clean build directories"

clean:
	rm -rf _build

html:
	sphinx-build -b html . _build/html
