#!/usr/bin/env python3
"""
Unit tests for MODEL_for_framework HTML converters.
Tests both yaml_to_html_converter.py and md_to_html_converter.py.
"""

import os
import tempfile
import pytest
from io import StringIO
from MODEL_for_framework.90_tool.yaml_to_html_converter import YAMLToHTMLConverter
from MODEL_for_framework.90_tool.md_to_html_converter import HTMLConverter

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

class TestYAMLToHTMLConverter:
    """Test cases for YAML to HTML converter."""

    def test_initialization(self):
        """Test converter initialization."""
        converter = YAMLToHTMLConverter("test.yaml", "output", "_29")
        assert converter.input_path is not None
        assert converter.output_root is not None
        assert converter.project_base is not None
        assert converter.stats == {'success': 0, 'failed': 0, 'processed_files': []}

    def test_html_path_generation(self):
        """Test HTML path generation."""
        with tempfile.NamedTemporaryFile(suffix='.yaml', delete=False) as tmp:
            tmp_path = tmp.name

        try:
            converter = YAMLToHTMLConverter(tmp_path, "output", "_29")
            html_path = converter._generate_html_path()
            assert html_path.endswith('.html')
            assert 'output' in html_path
        finally:
            os.unlink(tmp_path)

    def test_yaml_conversion_with_valid_input(self):
        """Test YAML conversion with valid input."""
        with tempfile.NamedTemporaryFile(suffix='.yaml', mode='w', delete=False) as tmp:
            tmp.write(TEST_YAML_CONTENT)
            tmp_path = tmp.name

        try:
            with tempfile.TemporaryDirectory() as output_dir:
                converter = YAMLToHTMLConverter(tmp_path, output_dir, "_29")
                result = converter.convert()
                assert result is True
                assert converter.stats['success'] == 1
                assert converter.stats['failed'] == 0

                # Check that HTML file was created
                html_path = converter._generate_html_path()
                assert os.path.exists(html_path)

                # Check HTML content
                with open(html_path, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                    assert 'Test User Story' in html_content
                    assert 'US_TEST_001' in html_content
                    assert 'Test Document' in html_content
        finally:
            os.unlink(tmp_path)

    def test_yaml_conversion_with_invalid_input(self):
        """Test YAML conversion with invalid input."""
        converter = YAMLToHTMLConverter("nonexistent.yaml", "output", "_29")
        result = converter.convert()
        assert result is False
        assert converter.stats['failed'] == 1

    def test_yaml_conversion_with_non_yaml_file(self):
        """Test YAML conversion with non-YAML file."""
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as tmp:
            tmp.write("This is not YAML content")
            tmp_path = tmp.name

        try:
            converter = YAMLToHTMLConverter(tmp_path, "output", "_29")
            result = converter.convert()
            assert result is False
            assert converter.stats['failed'] == 1
        finally:
            os.unlink(tmp_path)

class TestHTMLConverter:
    """Test cases for Markdown to HTML converter."""

    def test_initialization(self):
        """Test converter initialization."""
        converter = HTMLConverter("test.md", "output")
        assert converter.input_path is not None
        assert converter.output_root is not None
        assert converter.project_base is not None

    def test_html_path_generation(self):
        """Test HTML path generation."""
        with tempfile.NamedTemporaryFile(suffix='.md', delete=False) as tmp:
            tmp_path = tmp.name

        try:
            converter = HTMLConverter(tmp_path, "output")
            html_path = converter._generate_html_path()
            assert html_path.endswith('.html')
            assert 'output' in html_path
        finally:
            os.unlink(tmp_path)

    def test_markdown_conversion_with_valid_input(self):
        """Test Markdown conversion with valid input."""
        with tempfile.NamedTemporaryFile(suffix='.md', mode='w', delete=False) as tmp:
            tmp.write(TEST_MD_CONTENT)
            tmp_path = tmp.name

        try:
            with tempfile.TemporaryDirectory() as output_dir:
                converter = HTMLConverter(tmp_path, output_dir)
                result = converter.convert()
                assert result is True

                # Check that HTML file was created
                html_path = converter._generate_html_path()
                assert os.path.exists(html_path)

                # Check HTML content
                with open(html_path, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                    assert 'Test Markdown Document' in html_content
                    assert 'Hello World' in html_content  # Code block content
                    assert '<table' in html_content  # Table should be converted
        finally:
            os.unlink(tmp_path)

    def test_markdown_conversion_with_invalid_input(self):
        """Test Markdown conversion with invalid input."""
        converter = HTMLConverter("nonexistent.md", "output")
        result = converter.convert()
        assert result is False

    def test_markdown_conversion_with_non_markdown_file(self):
        """Test Markdown conversion with non-Markdown file."""
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as tmp:
            tmp.write("This is not Markdown content")
            tmp_path = tmp.name

        try:
            converter = HTMLConverter(tmp_path, "output")
            result = converter.convert()
            assert result is False
        finally:
            os.unlink(tmp_path)

class TestPerformanceOptimizations:
    """Test performance optimizations."""

    def test_large_file_handling(self):
        """Test handling of large files."""
        # Create a large YAML file
        large_content = TEST_YAML_CONTENT * 100  # Make it larger
        with tempfile.NamedTemporaryFile(suffix='.yaml', mode='w', delete=False) as tmp:
            tmp.write(large_content)
            tmp_path = tmp.name

        try:
            with tempfile.TemporaryDirectory() as output_dir:
                converter = YAMLToHTMLConverter(tmp_path, output_dir, "_29")
                result = converter.convert()
                assert result is True

                # Verify the HTML file was created and contains expected content
                html_path = converter._generate_html_path()
                assert os.path.exists(html_path)
        finally:
            os.unlink(tmp_path)

class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_yaml_file(self):
        """Test conversion of empty YAML file."""
        with tempfile.NamedTemporaryFile(suffix='.yaml', delete=False) as tmp:
            tmp_path = tmp.name

        try:
            with tempfile.TemporaryDirectory() as output_dir:
                converter = YAMLToHTMLConverter(tmp_path, output_dir, "_29")
                result = converter.convert()
                # Empty YAML should still be processed (results in empty data)
                assert result is True
        finally:
            os.unlink(tmp_path)

    def test_empty_markdown_file(self):
        """Test conversion of empty Markdown file."""
        with tempfile.NamedTemporaryFile(suffix='.md', delete=False) as tmp:
            tmp_path = tmp.name

        try:
            with tempfile.TemporaryDirectory() as output_dir:
                converter = HTMLConverter(tmp_path, output_dir)
                result = converter.convert()
                # Empty Markdown should still be processed
                assert result is True
        finally:
            os.unlink(tmp_path)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])