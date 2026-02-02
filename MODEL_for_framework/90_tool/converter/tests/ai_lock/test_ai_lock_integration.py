#!/usr/bin/env python3
"""
Integration test cases for AI_LOCK and AI_UNLOCK tags in HTML conversion.

This module tests the integration of AI_LOCK/AI_UNLOCK handling with the
overall markdown to HTML conversion process.
"""

import unittest
import tempfile
import os
import shutil
from pathlib import Path

# Import the converter module
from converter_for_md_to_html import MDToHTMLConverter

__version__ = "1.0.0"
__status__ = "ACTIVE"

"""
CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-02-01 | Initial creation of integration AI_LOCK test cases | Framework Steward | Establish comprehensive test coverage for AI_LOCK integration scenarios |
"""


class TestAILockIntegration(unittest.TestCase):
    """Integration test cases for AI_LOCK/AI_UNLOCK tag handling."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.temp_dir = tempfile.mkdtemp()
        self.output_dir = tempfile.mkdtemp()
        self.converter = MDToHTMLConverter()

    def tearDown(self):
        """Clean up after each test method."""
        shutil.rmtree(self.temp_dir)
        shutil.rmtree(self.output_dir)

    def create_test_md_file(self, content, filename="test.md"):
        """Create a temporary markdown file with the given content."""
        file_path = os.path.join(self.temp_dir, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path

    def read_html_file(self, html_path):
        """Read and return the content of an HTML file."""
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()

    def test_ai_lock_with_recursive_conversion(self):
        """Test AI_LOCK handling in recursive directory conversion."""
        # Create a nested directory structure
        subdir = os.path.join(self.temp_dir, "subdir")
        os.makedirs(subdir)

        # Create markdown files with AI_LOCK content
        main_content = """# Main Document

[AI_LOCK] Main content warning [AI_UNLOCK]

Regular content."""

        sub_content = """# Sub Document

[AI_LOCK] Sub content warning [AI_UNLOCK]

More content."""

        main_file = self.create_test_md_file(main_content, "main.md")
        sub_file = self.create_test_md_file(sub_content, os.path.join("subdir", "sub.md"))

        # Run recursive conversion
        self.converter.convert_directory(self.temp_dir, self.output_dir, recursive=True)

        # Check that both files were converted with AI_LOCK handling
        main_html = os.path.join(self.output_dir, "main.html")
        sub_html = os.path.join(self.output_dir, "subdir", "sub.html")

        self.assertTrue(os.path.exists(main_html))
        self.assertTrue(os.path.exists(sub_html))

        main_html_content = self.read_html_file(main_html)
        sub_html_content = self.read_html_file(sub_html)

        self.assertIn('<div class="ai-lock">Main content warning</div>', main_html_content)
        self.assertIn('<div class="ai-lock">Sub content warning</div>', sub_html_content)

    def test_ai_lock_with_index_generation(self):
        """Test AI_LOCK handling when combined with index generation."""
        # Create a directory with multiple files containing AI_LOCK
        file1_content = """# File 1

[AI_LOCK] Warning for file 1 [AI_UNLOCK]""" * 3

        file2_content = """# File 2

[AI_LOCK] Warning for file 2 [AI_UNLOCK]""" * 3

        file1 = self.create_test_md_file(file1_content, "file1.md")
        file2 = self.create_test_md_file(file2_content, "file2.md")

        # Run conversion with index generation
        self.converter.convert_directory(self.temp_dir, self.output_dir, recursive=True, generate_index=True)

        # Check that index file was created and contains proper links
        index_file = os.path.join(self.output_dir, "index.html")
        self.assertTrue(os.path.exists(index_file))

        index_content = self.read_html_file(index_file)
        self.assertIn('file1.html', index_content)
        self.assertIn('file2.html', index_content)

        # Check that individual files have AI_LOCK content
        file1_html = os.path.join(self.output_dir, "file1.html")
        file2_html = os.path.join(self.output_dir, "file2.html")

        file1_content = self.read_html_file(file1_html)
        file2_content = self.read_html_file(file2_html)

        self.assertIn('<div class="ai-lock">Warning for file 1</div>', file1_content)
        self.assertIn('<div class="ai-lock">Warning for file 2</div>', file2_content)

    def test_ai_lock_with_existing_html_files(self):
        """Test AI_LOCK handling when some HTML files already exist."""
        # Create markdown file with AI_LOCK
        md_content = """# Test Document

[AI_LOCK] Existing warning [AI_UNLOCK]

Regular content."""

        md_file = self.create_test_md_file(md_content, "test.md")

        # Create existing HTML file (simulating previous conversion)
        existing_html_dir = os.path.join(self.output_dir, "existing")
        os.makedirs(existing_html_dir, exist_ok=True)

        existing_html = os.path.join(existing_html_dir, "existing.html")
        with open(existing_html, 'w', encoding='utf-8') as f:
            f.write("<html><body><p>Existing content</p></body></html>")

        # Run conversion
        self.converter.convert_directory(self.temp_dir, self.output_dir, recursive=True)

        # Check that new file was created with AI_LOCK handling
        new_html = os.path.join(self.output_dir, "test.html")
        self.assertTrue(os.path.exists(new_html))

        html_content = self.read_html_file(new_html)
        self.assertIn('<div class="ai-lock">Existing warning</div>', html_content)

        # Check that existing file was not modified
        existing_content = self.read_html_file(existing_html)
        self.assertIn("Existing content", existing_content)

    def test_ai_lock_with_special_file_names(self):
        """Test AI_LOCK handling with special file names and paths."""
        special_files = {
            "file with spaces.md": """# File with Spaces

[AI_LOCK] Warning in spaced file [AI_UNLOCK]""",
            "file-with-dashes.md": """# File with Dashes

[AI_LOCK] Warning in dashed file [AI_UNLOCK]""",
            "file_with_underscores.md": """# File with Underscores

[AI_LOCK] Warning in underscored file [AI_UNLOCK]""",
            "file.with.dots.md": """# File with Dots

[AI_LOCK] Warning in dotted file [AI_UNLOCK]""",
        }

        for filename, content in special_files.items():
            self.create_test_md_file(content, filename)

        # Run conversion
        self.converter.convert_directory(self.temp_dir, self.output_dir, recursive=True)

        # Check that all files were converted properly
        for filename in special_files.keys():
            html_filename = os.path.splitext(filename)[0] + ".html"
            html_path = os.path.join(self.output_dir, html_filename)

            self.assertTrue(os.path.exists(html_path))

            html_content = self.read_html_file(html_path)
            self.assertIn('<div class="ai-lock">', html_content)

    def test_ai_lock_with_large_content(self):
        """Test AI_LOCK handling with large content files."""
        # Create a large content with AI_LOCK sections
        large_content = "# Large Document\n\n"

        for i in range(50):
            large_content += f"""
## Section {i + 1}

This is section content {i + 1}.

[AI_LOCK] Warning for section {i + 1} [AI_UNLOCK]

More content for section {i + 1}.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
"""

        md_file = self.create_test_md_file(large_content, "large_document.md")

        # Run conversion
        self.converter.convert_file(md_file)

        # Check that file was converted properly
        html_file = os.path.join(self.output_dir, "large_document.html")
        self.assertTrue(os.path.exists(html_file))

        html_content = self.read_html_file(html_file)

        # Verify all AI_LOCK sections were processed
        ai_lock_count = html_content.count('<div class="ai-lock">')
        self.assertEqual(ai_lock_count, 50)

        # Verify content preservation
        self.assertIn("Warning for section 1", html_content)
        self.assertIn("Warning for section 50", html_content)

    def test_ai_lock_with_mixed_markdown_elements(self):
        """Test AI_LOCK handling with complex markdown structures."""
        complex_content = """# Complex Document

## Table of Contents

- [Section 1](#section-1)
- [Section 2](#section-2)

## Section 1

[AI_LOCK] Important note for section 1 [AI_UNLOCK]

### Subsection 1.1

Regular content with **bold** and *italic* text.

```python
[AI_LOCK] def important_function(): pass [AI_UNLOCK]
```

## Section 2

[AI_LOCK] Critical warning for section 2 [AI_UNLOCK]

> [AI_LOCK] Important blockquote [AI_UNLOCK]

### Lists

- Item 1 with [AI_LOCK] special note [AI_UNLOCK]
- Item 2
- Item 3 with [AI_LOCK] another note [AI_UNLOCK]

## Conclusion

[AI_LOCK] Final important message [AI_UNLOCK]""" * 5

        md_file = self.create_test_md_file(complex_content, "complex.md")

        # Run conversion
        self.converter.convert_file(md_file)

        # Check that file was converted properly
        html_file = os.path.join(self.output_dir, "complex.html")
        self.assertTrue(os.path.exists(html_file))

        html_content = self.read_html_file(html_file)

        # Verify all AI_LOCK sections were processed
        ai_lock_count = html_content.count('<div class="ai-lock">')
        self.assertEqual(ai_lock_count, 10)  # 2 sections * 5 repetitions

        # Verify complex elements work with AI_LOCK
        self.assertIn('<strong>bold</strong>', html_content)
        self.assertIn('<em>italic</em>', html_content)
        self.assertIn('<code>def important_function(): pass</code>', html_content)


if __name__ == '__main__':
    unittest.main()