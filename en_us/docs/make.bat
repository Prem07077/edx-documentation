@echo off
if "%1"=="html" (
    sphinx-build -b html docs _build/html
) else if "%1"=="clean" (
    rmdir /s /q _build
) else (
    echo Usage: make.bat [html|clean]
)
