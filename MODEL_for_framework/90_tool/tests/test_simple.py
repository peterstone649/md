#!/usr/bin/env python3
"""
Simple unit tests for MODEL_for_framework HTML converters.
Tests both yaml_to_html_converter.py and md_to_html_converter.py using direct execution.
"""

import os
import tempfile
import subprocess
import sys
from pathlib import Path

# Test data
TEST_YAML_CONTENT = """
title: "Test User Story"
id: "US_TEST_001"
priority: "HIGH"

metadata:
  version: "V1.0.0"
  status: "TEST"
  date: "2026-01-10"

story: >
  As a test user, I want to verify the YAML to HTML conversion works correctly.

acceptance_criteria:
  - id: "TC-01"
    steps:
      - "Given I have a valid YAML file"
      - "When I run the converter"
      - "Then it should generate proper HTML"

related_documents:
  - type: "Test Document"
    path: "./test_document.md"
"""

TEST_MD_CONTENT = """
# Test Markdown Document

This is a test Markdown file for conversion testing.

## Features

- Supports **bold** and *italic* text
- Includes [links](https://example.com)
- Has code blocks:

```python
def test_function():
    return "Hello World"
```

| Table | Example |
|-------|---------|
| Row 1 | Data 1  |
| Row 2 | Data 2  |
"""

def run_command(cmd):
    """Run a command and return the result."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr

def test_yaml_converter():
    """Test YAML to HTML converter."""
    print("Testing YAML converter...")

    # Create test YAML file
    with tempfile.NamedTemporaryFile(suffix='.yaml', mode='w', delete=False) as tmp:
        tmp.write(TEST_YAML_CONTENT)
        yaml_path = tmp.name

    try:
        # Create temp output directory
        with tempfile.TemporaryDirectory() as output_dir:
            # Run the converter
            cmd = f'python MODEL_for_framework/90_tool/yaml_to_html_converter.py "{yaml_path}" "{output_dir}"'
            returncode, stdout, stderr = run_command(cmd)

            if returncode == 0:
                print("✅ YAML converter executed successfully")

                # Check if HTML file was created
                converter = __import__('MODEL_for_framework.90_tool.yaml_to_html_converter', fromlist=['YAMLToHTMLConverter'])
                html_converter = converter.YAMLToHTMLConverter(yaml_path, output_dir, "_29")
                html_path = html_converter._generate_html_path()

                if os.path.exists(html_path):
                    print("✅ HTML file created successfully")

                    # Check HTML content
                    with open(html_path, 'r', encoding='utf-8') as f:
                        html_content = f.read()
                        if 'Test User Story' in html_content and 'US_TEST_001' in html_content:
                            print("✅ HTML content is correct")
                            return True
                        else:
                            print("❌ HTML content is incorrect")
                            return False
                else:
                    print("❌ HTML file was not created")
                    return False
            else:
                print(f"❌ YAML converter failed: {stderr}")
                return False
    finally:
        os.unlink(yaml_path)

def test_markdown_converter():
    """Test Markdown to HTML converter."""
    print("Testing Markdown converter...")

    # Create test Markdown file
    with tempfile.NamedTemporaryFile(suffix='.md', mode='w', delete=False) as tmp:
        tmp.write(TEST_MD_CONTENT)
        md_path = tmp.name

    try:
        # Create temp output directory
        with tempfile.TemporaryDirectory() as output_dir:
            # Run the converter
            cmd = f'python MODEL_for_framework/90_tool/md_to_html_converter.py "{md_path}" "{output_dir}"'
            returncode, stdout, stderr = run_command(cmd)

            if returncode == 0:
                print("✅ Markdown converter executed successfully")

                # Check if HTML file was created
                converter = __import__('MODEL_for_framework.90_tool.md_to_html_converter', fromlist=['HTMLConverter'])
                html_converter = converter.HTMLConverter(md_path, output_dir)
                html_path = html_converter._generate_html_path()

                if os.path.exists(html_path):
                    print("✅ HTML file created successfully")

                    # Check HTML content
                    with open(html_path, 'r', encoding='utf-8') as f:
                        html_content = f.read()
                        if 'Test Markdown Document' in html_content and 'Hello World' in html_content:
                            print("✅ HTML content is correct")
                            return True
                        else:
                            print("❌ HTML content is incorrect")
                            return False
                else:
                    print("❌ HTML file was not created")
                    return False
            else:
                print(f"❌ Markdown converter failed: {stderr}")
                return False
    finally:
        os.unlink(md_path)

def test_performance_with_large_file():
    """Test performance with large files."""
    print("Testing performance with large file...")

    # Create a large YAML file
    large_content = TEST_YAML_CONTENT * 100  # Make it larger
    with tempfile.NamedTemporaryFile(suffix='.yaml', mode='w', delete=False) as tmp:
        tmp.write(large_content)
        yaml_path = tmp.name

    try:
        with tempfile.TemporaryDirectory() as output_dir:
            # Run the converter
            cmd = f'python MODEL_for_framework/90_tool/yaml_to_html_converter.py "{yaml_path}" "{output_dir}"'
            returncode, stdout, stderr = run_command(cmd)

            if returncode == 0:
                print("✅ Large file conversion successful")
                return True
            else:
                print(f"❌ Large file conversion failed: {stderr}")
                return False
    finally:
        os.unlink(yaml_path)

def main():
    """Run all tests."""
    print("Running MODEL_for_framework converter tests...")
    print("=" * 50)

    tests = [
        test_yaml_converter,
        test_markdown_converter,
        test_performance_with_large_file
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            print()

    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())