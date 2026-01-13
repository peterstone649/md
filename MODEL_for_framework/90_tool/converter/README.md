# Converter Tools

This directory contains Python-based conversion tools e.g. for markdown & yaml for easy reuse.

## Tools

### Markdown to HTML Converter (`converter_for_md_to_html.py`)
Converts Markdown files to styled HTML documents with support for:
- Fenced code blocks
- Tables
- Recursive directory processing
- Fixed output directory structure

**Usage:**
```bash
python converter_for_md_to_html.py input.md
python converter_for_md_to_html.py /path/to/directory -r
```

### YAML to HTML Converter (`converter_for_yaml_to_html.py`)
Converts YAML user story files to styled HTML documents with structured sections for:
- Metadata
- User story content
- Acceptance criteria
- Related documents

**Usage:**
```bash
python converter_for_yaml_to_html.py input.yaml
python converter_for_yaml_to_html.py /path/to/directory -r --summary
```

## Requirements
- Python 3.x
- `markdown` library
- `pyyaml` library
- `python-dotenv` library

## Output
All HTML files are generated in `<PROJECT_BASE_PATH>/out/html/` directory, maintaining the source directory structure.

## Configuration
Uses `.env` file for `PROJECT_BASE_PATH` configuration.
