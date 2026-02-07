requirement with the flag# Converter for Markdown to HTML - Command Line Flags Documentation

## Overview

The `converter_for_md_to_html.py` tool provides several command-line flags to control its behavior and functionality.

## Command Line Flags

### Basic Usage

```bash
python converter_for_md_to_html.py [OPTIONS] <input_path>
```

### Available Flags

#### `-r, --recursive`
**Purpose**: Enable recursive processing of directories
**Usage**: 
```bash
python converter_for_md_to_html.py -r /path/to/directory
```
**Description**: 
- When the input path is a directory, this flag tells the converter to process all Markdown files recursively through all subdirectories
- Without this flag, if you provide a directory path, the converter will exit with an error
- This is the primary flag for batch processing entire project structures

#### `--project-base`
**Purpose**: Specify the project base path for calculating relative output paths
**Usage**:
```bash
python converter_for_md_to_html.py --project-base /custom/project/path /path/to/input
```
**Description**:
- Overrides the default project base path used for calculating relative output paths
- Defaults to the `PROJECT_BASE_PATH` environment variable from `.env` file
- If no environment variable is set, defaults to `E:\2025_11\_29`
- Essential for maintaining proper directory structure in the output

#### `-h, --help`
**Purpose**: Display help information
**Usage**:
```bash
python converter_for_md_to_html.py --help
```
**Description**: Shows all available options and their descriptions

## Input Path Requirements

### File Input
- Must be a valid Markdown file (`.md` or `.markdown` extension)
- Example: `python converter_for_md_to_html.py document.md`

### Directory Input
- Must be a valid directory path
- **Must** be used with the `-r` or `--recursive` flag
- Example: `python converter_for_md_to_html.py -r ./docs/`

## Output Behavior

### Fixed Output Directory
The converter always outputs to a fixed directory structure:
```
<PROJECT_BASE_PATH>\out\html\
```

### Path Resolution
- Input paths are resolved relative to the project base
- Output files mirror the source directory structure within the fixed output directory
- Example: Input `docs/guide.md` → Output `<PROJECT_BASE_PATH>\out\html\docs\guide.html`

## Examples

### Convert a Single File
```bash
python converter_for_md_to_html.py README.md
```

### Convert All Files in a Directory Recursively
```bash
python converter_for_md_to_html.py -r ./docs/
```

### Use Custom Project Base Path
```bash
python converter_for_md_to_html.py --project-base /custom/project ./docs/
```

### Combine Flags
```bash
python converter_for_md_to_html.py -r --project-base /custom/project ./docs/
```

## Error Handling

### Common Errors
1. **Directory without recursive flag**:
   ```
   Error: Input path is a directory, but --recursive flag was not provided.
   ```

2. **Non-Markdown file**:
   ```
   Error: Input file does not appear to be a Markdown file.
   ```

3. **File not found**:
   ```
   Error: Input path not found: <path>
   ```

## Environment Configuration

### .env File Support
Create a `.env` file in your project root:
```
PROJECT_BASE_PATH=/your/custom/project/path
```

This will be automatically loaded and used as the default project base path.

## Integration with Test Cases

The converter's flags are extensively tested in the test suite:

- `test_recursive_flag_behavior.py` - Tests recursive flag functionality
- `test_flat_output_structure.py` - Tests output directory structure
- `test_recursive_directory_prevention.py` - Tests prevention of nested directory creation

## Version Information

Current version: **1.6.1**
- Added automatic image copying for SVG and other image files
- Enhanced Markdown processing with fenced_code and tables extensions
- Fixed syntax warnings and improved error handling

## Directory Exclusion Requirements

### Out Folder Exclusion Policy

**Requirement**: The `out` folder is normally excluded from conversion by default to prevent recursive directory creation issues.

#### Default Behavior
- The converter automatically excludes any `out` folder from processing
- This prevents the creation of nested `out/html` directories within source `out` folders
- Ensures clean output structure without circular references

#### Include Override (Future Enhancement)
**Note**: Currently, the converter does not have an `--include` flag. The `out` folder exclusion is implemented at the directory scanning level in the code.

**Proposed Enhancement**: To include an `out` folder in conversion, a future `--include` flag should be implemented:

```bash
# Future: Include specific out folder
python converter_for_md_to_html.py --include out/special_folder

# Future: Include entire out directory (if needed)
python converter_for_md_to_html.py --include out
```

#### Implementation Details
- The exclusion is implemented at the directory scanning level
- Only applies to directories named exactly `out` (case-sensitive)
- Does not affect files named `out.md` or similar
- Maintains the fixed output directory structure at `<PROJECT_BASE_PATH>\out\html\`

#### Use Cases for Include
- Special documentation that needs to be converted from an `out` folder
- Temporary conversion of output files for review purposes
- Migration scenarios where output files need processing

#### Safety Measures
- Include flag validation ensures proper path specification
- Warning messages displayed when including `out` folders
- Clear documentation of potential circular reference risks
