# Test Case: Recursive Directory Prevention

## Overview

This test case prevents the recursive creation of `out/html` directories in the Markdown to HTML converter.

## Problem

The converter was potentially creating nested `out/html` directories when converting Markdown files to HTML, which could lead to:

- Inconsistent output directory structures
- Confusion about where HTML files are being generated
- Potential issues with deployment and file organization

## Solution

The test case `test_recursive_directory_prevention.py` validates that:

1. **Exactly one `out` directory** exists in the output path
2. **Exactly one `html` directory** exists in the output path  
3. **Correct order**: `html` comes immediately after `out` in the path
4. **No nesting**: No additional `out` or `html` directories are created
5. **Multiple conversions**: Multiple file conversions maintain the same structure
6. **Existing directories**: Handles existing `out/html` directories correctly

## Test Coverage

### Test Cases

1. **`test_no_recursive_out_html_directories`**
   - Validates the basic directory structure
   - Ensures exactly one `out` and one `html` directory
   - Verifies correct ordering

2. **`test_converter_creates_correct_directory_structure`**
   - Tests actual file conversion
   - Validates the complete conversion process
   - Checks that files are created in the correct location

3. **`test_multiple_conversions_same_structure`**
   - Tests multiple file conversions
   - Ensures consistent structure across multiple runs
   - Validates no nested directories are created

4. **`test_existing_out_html_directory_handling`**
   - Tests behavior with pre-existing directories
   - Ensures existing files are not overwritten
   - Validates proper handling of existing structures

## Usage

Run the test with:

```bash
python MODEL_for_framework/90_tool/converter/test_recursive_directory_prevention.py
```

## Expected Output

```
Running tests to prevent recursive out/html directory creation...
======================================================================
test_converter_creates_correct_directory_structure (__main__.TestRecursiveDirectoryPrevention.test_converter_creates_correct_directory_structure)
Test that converter creates the correct directory structure without nesting. ... ok
test_existing_out_html_directory_handling (__main__.TestRecursiveDirectoryPrevention.test_existing_out_html_directory_handling)
Test that converter handles existing out/html directories correctly. ... ok
test_multiple_conversions_same_structure (__main__.TestRecursiveDirectoryPrevention.test_multiple_conversions_same_structure)
Test that multiple conversions don't create nested directories. ... ok
test_no_recursive_out_html_directories (__main__.TestRecursiveDirectoryPrevention.test_no_recursive_out_html_directories)
Test that converter doesn't create nested out/html directories. ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.177s

OK
======================================================================
All tests passed! Recursive out/html directory creation is prevented.
```

## Implementation Details

The test uses temporary directories to isolate test runs and ensure clean state. Each test:

1. Creates a temporary project structure
2. Runs the converter with various scenarios
3. Validates the output directory structure
4. Cleans up temporary files

## Integration

This test should be run as part of the converter's test suite to ensure the directory structure remains consistent and prevents recursive directory creation issues.