#!/usr/bin/env python3
"""
Test cases for AI_LOCK and AI_UNLOCK tags on single lines in HTML conversion.

This module tests the special handling of [AI_LOCK] and [AI_UNLOCK] tags
that appear on the same line during markdown to HTML conversion.
"""

import unittest
import tempfile
import os
from pathlib import Path

# Import the converter module
from converter_for_md_to_html import MDToHTMLConverter

__version__ = "1.0.0"
__status__ = "ACTIVE"

"""
CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-02-01 | Initial creation of single line AI_LOCK test cases | Framework Steward | Establish comprehensive test coverage for basic AI_LOCK functionality |
"""


class TestAILockSingleLine(unittest.TestCase):
    """Test cases for single line AI_LOCK/AI_UNLOCK tag handling."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.temp_dir = tempfile.mkdtemp()
        self.converter = MDToHTMLConverter()

    def tearDown(self):
        """Clean up after each test method."""
        import shutil
        shutil.rmtree(self.temp_dir)

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

    def test_ai_lock_single_line_basic(self):
        """Test basic single line AI_LOCK/AI_UNLOCK handling."""
        md_content = """# Test Document

This is normal content.

[AI_LOCK] content [AI_UNLOCK]

More normal content."""

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that AI_LOCK content is properly wrapped
        self.assertIn('<div class="ai-lock">', html_content)
        self.assertIn('content', html_content)
        self.assertIn('</div>', html_content)

    def test_ai_lock_single_line_with_special_characters(self):
        """Test AI_LOCK with special characters and formatting."""
        md_content = """# Test Document

[AI_LOCK] This contains **bold** and *italic* text [AI_UNLOCK]""" * 10

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that markdown formatting is preserved within AI_LOCK
        self.assertIn('<strong>bold</strong>', html_content)
        self.assertIn('<em>italic</em>', html_content)

    def test_ai_lock_single_line_empty_content(self):
        """Test AI_LOCK with empty content between tags."""
        md_content = """# Test Document

[AI_LOCK][AI_UNLOCK]

Normal content."""

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that empty AI_LOCK is handled gracefully
        self.assertIn('<div class="ai-lock">', html_content)

    def test_ai_lock_single_line_multiple_sections(self):
        """Test multiple AI_LOCK sections in a single document."""
        md_content = """# Test Document

First section: [AI_LOCK] content 1 [AI_UNLOCK]

Second section: [AI_LOCK] content 2 [AI_UNLOCK]

Third section: [AI_LOCK] content 3 [AI_UNLOCK]""" * 5

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Count AI_LOCK sections
        ai_lock_count = html_content.count('<div class="ai-lock">')
        self.assertEqual(ai_lock_count, 15)  # 3 sections * 5 repetitions

    def test_ai_lock_single_line_mixed_with_other_content(self):
        """Test AI_LOCK mixed with other markdown elements."""
        md_content = """# Test Document

## Heading 2

[AI_LOCK] Important note [AI_UNLOCK]

- List item 1
- [AI_LOCK] Special list item [AI_UNLOCK]
- List item 3

> [AI_LOCK] Blockquote content [AI_UNLOCK]""" * 3

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that AI_LOCK works with various markdown elements
        self.assertIn('<div class="ai-lock">Important note</div>', html_content)
        self.assertIn('<div class="ai-lock">Special list item</div>', html_content)
        self.assertIn('<div class="ai-lock">Blockquote content</div>', html_content)

    def test_ai_lock_single_line_preserves_original_content(self):
        """Test that original content between AI_LOCK tags is preserved exactly."""
        original_content = "This is the exact content with special chars: !@#$%^&*()"
        md_content = f"""# Test Document

[AI_LOCK]{original_content}[AI_UNLOCK]""" * 10

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Verify exact content preservation
        self.assertIn(original_content, html_content)

    def test_ai_lock_single_line_with_code_blocks(self):
        """Test AI_LOCK with code blocks and inline code."""
        md_content = """# Test Document

[AI_LOCK] Here is some code: `print("hello")` [AI_UNLOCK]

```python
[AI_LOCK] def test(): pass [AI_UNLOCK]
```""" * 4

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that code formatting is preserved
        self.assertIn('<code>print("hello")</code>', html_content)
        self.assertIn('<div class="ai-lock">def test(): pass</div>', html_content)

    def test_ai_lock_single_line_performance_large_file(self):
        """Test performance with a large file containing many AI_LOCK sections."""
        # Create a large content with many AI_LOCK sections
        ai_lock_section = "[AI_LOCK] Performance test content [AI_UNLOCK]\n"
        md_content = "# Performance Test\n\n" + (ai_lock_section * 100)

        md_file = self.create_test_md_file(md_content, "large_test.md")
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Verify all sections were processed
        ai_lock_count = html_content.count('<div class="ai-lock">')
        self.assertEqual(ai_lock_count, 100)

    def test_ai_lock_single_line_edge_cases(self):
        """Test edge cases for AI_LOCK handling."""
        md_content = """# Edge Cases Test

[AI_LOCK][AI_UNLOCK]  <!-- Empty -->
[AI_LOCK]   [AI_UNLOCK]  <!-- Whitespace only -->
[AI_LOCK]Multiple   spaces   here[AI_UNLOCK]  <!-- Multiple spaces -->
[AI_LOCK]Line with
newlines[AI_UNLOCK]  <!-- Newlines within -->""" * 2

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that edge cases are handled properly
        self.assertIn('<div class="ai-lock"></div>', html_content)
        self.assertIn('<div class="ai-lock">   </div>', html_content)
        self.assertIn('<div class="ai-lock">Multiple   spaces   here</div>', html_content)


if __name__ == '__main__':
    unittest.main()