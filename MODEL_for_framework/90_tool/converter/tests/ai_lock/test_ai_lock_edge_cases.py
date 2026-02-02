#!/usr/bin/env python3
"""
Edge case test cases for AI_LOCK and AI_UNLOCK tags in HTML conversion.

This module tests edge cases, error conditions, and unusual scenarios
for AI_LOCK/AI_UNLOCK tag handling during markdown to HTML conversion.
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
| V1.0.0  | 2026-02-01 | Initial creation of edge cases AI_LOCK test cases | Framework Steward | Establish comprehensive test coverage for AI_LOCK edge cases and error handling |
"""


class TestAILockEdgeCases(unittest.TestCase):
    """Edge case test cases for AI_LOCK/AI_UNLOCK tag handling."""

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

    def test_ai_lock_mismatched_tags(self):
        """Test handling of mismatched AI_LOCK/AI_UNLOCK tags."""
        md_content = """# Test Document

[AI_LOCK] Only opening tag

Regular content.

[AI_UNLOCK] Only closing tag

[AI_LOCK] Proper pair [AI_UNLOCK]""" * 3

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Should handle mismatched tags gracefully
        # The proper pair should still be processed
        self.assertIn('<div class="ai-lock">Proper pair</div>', html_content)

    def test_ai_lock_nested_tags(self):
        """Test handling of nested AI_LOCK tags (should not occur but test anyway)."""
        md_content = """# Test Document

[AI_LOCK] Outer content [AI_LOCK] Inner content [AI_UNLOCK] Outer continued [AI_UNLOCK]""" * 2

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Should handle nested tags without breaking
        self.assertIn('Outer content', html_content)
        self.assertIn('Inner content', html_content)

    def test_ai_lock_case_sensitivity(self):
        """Test case sensitivity of AI_LOCK/AI_UNLOCK tags."""
        md_content = """# Test Document

[AI_LOCK] Proper case [AI_UNLOCK]

[ai_lock] lowercase [ai_unlock]

[AI_lock] Mixed case [AI_UNLOCK]

[AI_LOCK] Another proper [AI_UNLOCK]""" * 2

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Should handle case sensitivity properly
        self.assertIn('<div class="ai-lock">Proper case</div>', html_content)
        self.assertIn('<div class="ai-lock">Another proper</div>', html_content)

    def test_ai_lock_with_unicode_content(self):
        """Test AI_LOCK with Unicode and international characters."""
        unicode_content = "Unicode: 你好世界 🌍 🚀 📱 ñáéíóú üöä €£¥₹ ₹€£¥₣ ₽₩₪₮₯₲₴₸₺₼₾₿"
        md_content = f"""# Unicode Test Document

[AI_LOCK]{unicode_content}[AI_UNLOCK]

Regular content with {unicode_content}.""" * 3

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Should preserve Unicode content properly
        self.assertIn(unicode_content, html_content)
        self.assertIn('<div class="ai-lock">', html_content)

    def test_ai_lock_with_very_long_content(self):
        """Test AI_LOCK with very long content strings."""
        long_content = "A" * 10000  # 10KB of content
        md_content = f"""# Long Content Test

[AI_LOCK]{long_content}[AI_UNLOCK]

Regular content.""" * 2

        md_file = self.create_test_md_file(md_content, "long_content.md")
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Should handle very long content without issues
        self.assertIn(long_content, html_content)
        self.assertIn('<div class="ai-lock">', html_content)

    def test_ai_lock_with_empty_file(self):
        """Test AI_LOCK handling with empty or minimal files."""
        md_content = ""  # Empty file

        md_file = self.create_test_md_file(md_content, "empty.md")
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Should handle empty files gracefully
        self.assertIn('<html>', html_content)
        self.assertIn('<body>', html_content)

    def test_ai_lock_with_only_ai_lock_tags(self):
        """Test file containing only AI_LOCK tags."""
        md_content = """[AI_LOCK] Only content [AI_UNLOCK]""" * 10

        md_file = self.create_test_md_file(md_content, "only_ai_lock.md")
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Should handle files with only AI_LOCK content
        ai_lock_count = html_content.count('<div class="ai-lock">')
        self.assertEqual(ai_lock_count, 10)

    def test_ai_lock_with_special_file_permissions(self):
        """Test AI_LOCK handling with files that have special permissions."""
        md_content = """# Permission Test

[AI_LOCK] Content with special permissions [AI_UNLOCK]"""

        md_file = self.create_test_md_file(md_content, "permissions.md")

        # Set special permissions (read-only)
        os.chmod(md_file, 0o444)  # Read-only

        try:
            html_file = self.converter.convert_file(md_file)

            self.assertTrue(os.path.exists(html_file))
            html_content = self.read_html_file(html_file)

            # Should handle read-only files
            self.assertIn('<div class="ai-lock">Content with special permissions</div>', html_content)
        finally:
            # Restore permissions for cleanup
            os.chmod(md_file, 0o644)  # Read-write

    def test_ai_lock_with_corrupted_markdown(self):
        """Test AI_LOCK handling with corrupted or malformed markdown."""
        corrupted_content = """# Corrupted Document

# Improper heading

[AI_LOCK] Corrupted content with [improper] [nesting] [AI_UNLOCK]

## Another heading

- [AI_LOCK] List item with [AI_UNLOCK] improper tags

[AI_LOCK] Final content [AI_UNLOCK]""" * 3

        md_file = self.create_test_md_file(corrupted_content, "corrupted.md")
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Should handle corrupted markdown gracefully
        self.assertIn('<div class="ai-lock">Corrupted content with [improper] [nesting]</div>', html_content)
        self.assertIn('<div class="ai-lock">List item with</div>', html_content)
        self.assertIn('<div class="ai-lock">Final content</div>', html_content)

    def test_ai_lock_with_concurrent_access(self):
        """Test AI_LOCK handling with concurrent file access scenarios."""
        md_content = """# Concurrent Test

[AI_LOCK] Concurrent content [AI_UNLOCK]""" * 5

        md_file = self.create_test_md_file(md_content, "concurrent.md")

        # Simulate concurrent access by creating multiple converter instances
        converter1 = MDToHTMLConverter()
        converter2 = MDToHTMLConverter()

        html_file1 = converter1.convert_file(md_file)
        html_file2 = converter2.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file1))
        self.assertTrue(os.path.exists(html_file2))

        html_content1 = self.read_html_file(html_file1)
        html_content2 = self.read_html_file(html_file2)

        # Both should produce consistent results
        self.assertIn('<div class="ai-lock">Concurrent content</div>', html_content1)
        self.assertIn('<div class="ai-lock">Concurrent content</div>', html_content2)

        # Content should be identical
        self.assertEqual(html_content1, html_content2)

    def test_ai_lock_with_memory_constrained_environment(self):
        """Test AI_LOCK handling in memory-constrained environments."""
        # Create a file that would be large in memory when processed
        large_content = "# Memory Test\n\n"
        for i in range(100):
            large_content += f"[AI_LOCK] Memory test content {i} [AI_UNLOCK]\n\n"

        md_file = self.create_test_md_file(large_content, "memory_test.md")
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Should handle large content without memory issues
        ai_lock_count = html_content.count('<div class="ai-lock">')
        self.assertEqual(ai_lock_count, 100)

        # Verify content preservation
        self.assertIn('Memory test content 0', html_content)
        self.assertIn('Memory test content 99', html_content)

    def test_ai_lock_with_network_paths(self):
        """Test AI_LOCK handling with network or special path scenarios."""
        md_content = """# Network Path Test

[AI_LOCK] Content from network path [AI_UNLOCK]"""

        md_file = self.create_test_md_file(md_content, "network_test.md")

        # Test with absolute path
        abs_path = os.path.abspath(md_file)
        html_file = self.converter.convert_file(abs_path)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Should handle absolute paths properly
        self.assertIn('<div class="ai-lock">Content from network path</div>', html_content)


if __name__ == '__main__':
    unittest.main()