# Requirements Analyser for Words in Files [REQUI_WORD_ANALYSER] [PRIO: MEDIUM]

## Overview

This document specifies the requirements for an analyser tool that extracts unique words from text files and outputs them as alphabetically ordered CSV files.

## Functional Requirements

### 1. Command Line Interface
- Accept a file path as command line argument
- Support optional project base path override via --project-base flag
- Provide clear success/failure output messages

### 2. Directory Management
- Use `manager_for_dir_OT_base.py` for base directory operations
- Output files to `out/word` directory structure
- Maintain relative directory paths in output filenames
- Automatically create output directories as needed

### 3. Word Extraction
- Extract unique words from file contents using regex pattern `\b[a-zA-Z][a-zA-Z0-9]*\b`
- Apply comprehensive word filtering based on configurable YAML rules:
  - **Number filtering**: Filter words containing digits anywhere (e.g., "test123", "v2.1", "file_1.txt")
  - **Underscore filtering**: Filter words starting with underscores (e.g., "_private", "_internal")
  - **File extension filtering**: Filter standalone file extensions (e.g., "txt", "md", "py") AND words ending with file extensions (e.g., "README.md", "script.py")
  - **Abbreviation filtering**: Filter ALL CAPS abbreviations 2-5 characters (e.g., "EU", "IO", "API", "HTTP")
  - **OS command filtering**: Filter common operating system commands (e.g., "cd", "ls", "git", "python", "docker")
- Apply Porter stemming to reduce morphological variants to common stems (e.g., "contributing/contribution/contributor" → "contribut")
- Convert all words to lowercase for case-insensitive uniqueness
- Sort words alphabetically before output

#### Detailed Filtering Requirements
- **Pattern-based filters** (configurable via YAML):
  - Words containing numbers: `.*\\d+.*`
  - Words starting with underscores: `^_.*`
  - File extensions: `^(ext|.*\\.ext)$` for each extension type
  - ALL CAPS abbreviations: `^[A-Z]{2,5}$`
- **Exclusion lists** (configurable via YAML):
  - **Operating system commands** (40+ commands): cd, ls, dir, mkdir, cp, mv, rm, cat, echo, pwd, git, svn, docker, kubectl, python, pip, npm, node, java, gcc, make, etc.
  - **Common abbreviations**: etc, ie, eg, vs, re, cf, ibid, et, al
  - **File extensions** (40+ extensions): txt, md, py, js, java, c, cpp, h, html, css, xml, json, yaml, yml, ini, cfg, conf, log, csv, tsv, sql, sh, bat, ps1, exe, dll, so, dylib, etc.
- **Lemmatization options**:
  - Porter stemmer (default): Aggressive stemming for grouping related terms
  - WordNet lemmatizer: Linguistic lemmatization with POS tagging
  - None: No lemmatization

### 4. CSV Output
- Generate CSV files with "Word" as header column
- Output one word per row
- Use UTF-8 encoding for file operations

### 5. Testing
- Include comprehensive unit tests in `test/` subfolder
- Test word extraction logic
- Test output path generation
- Test file analysis integration
- Test error handling for nonexistent files

## Non-Functional Requirements

### Performance
- Process files efficiently for typical text file sizes
- Handle large files without excessive memory usage

### Reliability
- Handle file I/O errors gracefully
- Validate input file existence
- Ensure output directory creation succeeds

### Compatibility
- Compatible with Python 3.x
- Use standard library modules where possible
- Follow framework coding conventions

## Implementation Details

### Dependencies
- `manager_for_dir_OT_base.py` for directory management
- `nltk` (Natural Language Toolkit) for WordNet lemmatization
- Standard library: `os`, `sys`, `csv`, `re`, `argparse`, `logging`

### Configuration
- **YAML-based configuration** (`word_filter.yaml`):
  - Version management
  - Pattern-based filters with regex rules
  - Exclusion lists for commands and abbreviations
  - Processing options (case sensitivity, lemmatization method)
  - Logging configuration

### File Structure
```
MODEL_for_framework/90_tool/word_ot_unique/
├── analyser_for_words_in_files.py          # Main analyser script
├── handler_for_word_filter.py              # Word filtering logic
├── lemmatizer_wordnet.py                   # WordNet lemmatizer module
├── word_filter.yaml                        # Configuration file
├── requi_analyser_for_words_in_files.md    # Requirements documentation
└── test/
    └── test_analyser_for_words_in_files.py # Unit tests
```

### Usage Example
```bash
python analyser_for_words_in_files.py path/to/input/file.md
```

This will create `out/word/path/to/input/file.csv` containing unique words from the input file.

## Changelog

| Version | Date | Changes | Stakeholder | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V0.9.0 | 2026-01-18 | Added file extension filtering and updated number filtering to exclude words containing digits anywhere | Framework Steward | Improve filtering of technical terms, version numbers, and file references in text |
| V0.8.0 | 2026-01-18 | Added Porter stemmer as default lemmatization method and OS commands filtering | Framework Steward | Implement aggressive stemming for better word grouping and filter technical commands |
| V0.7.0 | 2026-01-18 | Added WordNet lemmatizer module and integrated lemmatization pipeline | Framework Steward | Improve word analysis by normalizing related word forms |
| V0.6.0 | 2026-01-18 | Renamed handle_word_filter.py to handler_for_word_filter.py for consistency | Framework Steward | Improve naming consistency across the codebase |
| V0.5.0 | 2026-01-18 | Implemented configurable YAML-based word filtering system with handle_word_filter.py | Framework Steward | Make word filtering configurable and extensible |
| V0.4.0 | 2026-01-18 | Added case pattern analysis to filter abbreviations (ALL CAPS and mixed-case) | Framework Steward | Improve word extraction by removing technical abbreviations |
| V0.3.0 | 2026-01-18 | Updated word extraction to filter out numbers and words starting with underscores | Framework Steward | Improve word extraction quality by excluding non-text elements |
| V0.2.0 | 2026-01-18 | Added comprehensive functional and non-functional requirements sections | Framework Steward | Complete requirements specification for analyser implementation |
| V0.1.0 | 2026-01-18 | Initial creation | Framework Steward | Establish requirements for analyser for words in files |
