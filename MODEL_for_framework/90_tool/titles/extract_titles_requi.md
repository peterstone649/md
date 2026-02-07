# Title Extraction Tool Requirements

## Overview

The Title Extraction Tool extracts title lines (starting with #) from Markdown files and saves them to corresponding .title.txt files in the out/txt directory with preserved folder structure.

## Functional Requirements

### FR-001: Extract Title Lines
- **Description**: Extract all title lines from Markdown files that start with 1 or more # characters followed by a space and content
- **Priority**: HIGH
- **Acceptance Criteria**:
  - Tool identifies lines matching pattern: `^(#+)\s+(.+)$`
  - Extracts titles from levels 1 through 6 (and beyond)
  - Preserves exact formatting of title lines
  - Handles edge cases (no space after #, too many # symbols)

### FR-002: Process Single Files
- **Description**: Process individual Markdown files and generate corresponding .title.txt output files
- **Priority**: HIGH
- **Acceptance Criteria**:
  - Accepts file path as input
  - Creates .title.txt file in out/txt directory
  - Preserves original filename (without .md extension)
  - Includes metadata header in output file

### FR-003: Process Directories
- **Description**: Process all Markdown files in a directory with optional recursive processing
- **Priority**: MEDIUM
- **Acceptance Criteria**:
  - Accepts directory path as input
  - Processes all .md and .markdown files
  - Preserves folder structure in output
  - Supports recursive processing option

### FR-004: Generate Output Files
- **Description**: Create .title.txt files with standardized format and metadata
- **Priority**: HIGH
- **Acceptance Criteria**:
  - Output file includes header with source information
  - Output file includes generation timestamp
  - Output file includes extracted titles in original order
  - Creates necessary directory structure automatically

### FR-005: Command Line Interface
- **Description**: Provide command-line interface for tool execution
- **Priority**: MEDIUM
- **Acceptance Criteria**:
  - Accepts input path as required parameter
  - Supports recursive processing flag (-r, --recursive)
  - Supports custom output directory (-o, --output)
  - Displays version information (--version)

## Non-Functional Requirements

### NFR-001: Performance
- **Description**: Process files efficiently with reasonable performance
- **Priority**: MEDIUM
- **Acceptance Criteria**:
  - Process single file in under 1 second for typical sizes (<1MB)
  - Handle directories with hundreds of files efficiently
  - Memory usage scales reasonably with file size

### NFR-002: Error Handling
- **Description**: Provide clear error messages and graceful handling of edge cases
- **Priority**: HIGH
- **Acceptance Criteria**:
  - Log appropriate messages for missing files/directories
  - Skip non-Markdown files with warning
  - Continue processing when individual files fail
  - Provide clear error messages for invalid inputs

### NFR-003: Cross-Platform Compatibility
- **Description**: Work correctly across different operating systems
- **Priority**: MEDIUM
- **Acceptance Criteria**:
  - Handle Windows and Unix-style paths correctly
  - Work with different file system encodings
  - Support both forward and backward slashes in paths

### NFR-004: Logging
- **Description**: Provide comprehensive logging for debugging and monitoring
- **Priority**: LOW
- **Acceptance Criteria**:
  - Log successful operations at INFO level
  - Log warnings for skipped files
  - Log errors for failed operations
  - Include timestamps in all log messages

## Technical Requirements

### TR-001: Python Version Compatibility
- **Description**: Support specified Python versions
- **Priority**: MEDIUM
- **Acceptance Criteria**:
  - Compatible with Python 3.8+
  - Uses standard library modules where possible
  - Handles encoding issues gracefully

### TR-002: File Encoding
- **Description**: Handle various text encodings properly
- **Priority**: MEDIUM
- **Acceptance Criteria**:
  - Read input files with UTF-8 encoding
  - Write output files with UTF-8 encoding
  - Handle encoding errors gracefully

### TR-003: Directory Structure
- **Description**: Follow project directory conventions
- **Priority**: LOW
- **Acceptance Criteria**:
  - Output files go to out/txt directory by default
  - Preserve relative directory structure in output
  - Create necessary directories automatically

## Integration Requirements

### IR-001: Framework Integration
- **Description**: Integrate with existing framework structure and conventions
- **Priority**: MEDIUM
- **Acceptance Criteria**:
  - Follow existing naming conventions
  - Use established directory structure
  - Integrate with existing tool ecosystem

### IR-002: Testing Integration
- **Description**: Support automated testing and validation
- **Priority**: LOW
- **Acceptance Criteria**:
  - Include comprehensive test suite
  - Support test execution via test runner
  - Validate output format and content

## Dependencies

- Python 3.8+
- Standard library modules: os, sys, argparse, re, logging, datetime, pathlib, tempfile, shutil
- Framework dependencies: converter.manager_for_dir_OT_base

## Assumptions

- Input files are valid Markdown files
- Output directory has write permissions
- System has sufficient disk space for output files
- Users have basic command-line interface knowledge

## Constraints

- Must preserve original title formatting exactly
- Must handle large files efficiently
- Must work with existing framework directory structure
- Must follow established coding conventions and patterns

## Changelog

| Version | Date       | Change Content | Stakeholders | Motivation |
|---------|------------|----------------|--------------|------------|
| V1.0.2  | 2026-02-07 | Updated regex pattern to allow all heading levels (1...n) instead of limiting to 1-3 levels | AI Coder | Allow extraction of all markdown heading levels for comprehensive analysis |
| V1.0.1  | 2026-02-07 | Fixed import issues and regex pattern to match all heading levels (1-6) | AI Coder | Ensure compatibility with test suite and extract all title levels |
| V1.0.0  | 2026-02-07 | Initial creation | AI Coder | Extract title lines from Markdown files for analysis and indexing |
