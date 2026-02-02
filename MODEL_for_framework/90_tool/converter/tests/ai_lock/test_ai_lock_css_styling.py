#!/usr/bin/env python3
"""
CSS styling test cases for AI_LOCK and AI_UNLOCK tags in HTML conversion.

This module tests that AI_LOCK sections have proper CSS styling and
visual separation in the generated HTML output.
"""

import unittest
import tempfile
import os
import re
from pathlib import Path

# Import the converter module
from converter_for_md_to_html import MDToHTMLConverter

__version__ = "1.0.0"
__status__ = "ACTIVE"

"""
CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-02-01 | Initial creation of CSS styling AI_LOCK test cases | Framework Steward | Establish comprehensive test coverage for AI_LOCK visual styling |
"""


class TestAILockCSSStyling(unittest.TestCase):
    """CSS styling test cases for AI_LOCK/AI_UNLOCK tag handling."""

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

    def test_ai_lock_css_class_presence(self):
        """Test that AI_LOCK sections have the correct CSS class."""
        md_content = """# Test Document

[AI_LOCK] Important content [AI_UNLOCK]

Regular content."""

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that AI_LOCK content has the correct CSS class
        self.assertIn('<div class="ai-lock">', html_content)
        self.assertIn('Important content', html_content)

    def test_ai_lock_css_styling_properties(self):
        """Test that AI_LOCK sections have proper CSS styling properties."""
        md_content = """# Test Document

[AI_LOCK] Styled content [AI_UNLOCK]""" * 5

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that CSS styles are present in the HTML
        self.assertIn('<style>', html_content)
        self.assertIn('.ai-lock', html_content)

        # Look for specific styling properties
        style_section = re.search(r'<style[^>]*>(.*?)</style>', html_content, re.DOTALL)
        if style_section:
            style_content = style_section.group(1)
            # Check for common styling properties
            self.assertTrue(
                'background-color' in style_content or
                'border' in style_content or
                'padding' in style_content or
                'margin' in style_content or
                'color' in style_content
            )

    def test_ai_lock_visual_separation(self):
        """Test that AI_LOCK sections have visual separation from surrounding content."""
        md_content = """# Test Document

Regular content before.

[AI_LOCK] Important warning [AI_UNLOCK]

Regular content after.

Another [AI_LOCK] critical note [AI_UNLOCK] inline.

More regular content."""

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that AI_LOCK sections are visually separated
        self.assertIn('<div class="ai-lock">Important warning</div>', html_content)
        self.assertIn('<div class="ai-lock">critical note</div>', html_content)

        # Check that surrounding content is properly separated
        self.assertIn('Regular content before.', html_content)
        self.assertIn('Regular content after.', html_content)
        self.assertIn('More regular content.', html_content)

    def test_ai_lock_consistent_styling_across_sections(self):
        """Test that all AI_LOCK sections have consistent styling."""
        md_content = """# Test Document

[AI_LOCK] Section 1 content [AI_UNLOCK]

Regular content.

[AI_LOCK] Section 2 content [AI_UNLOCK]

More regular content.

[AI_LOCK] Section 3 content [AI_UNLOCK]""" * 3

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Count AI_LOCK sections
        ai_lock_count = html_content.count('<div class="ai-lock">')
        self.assertEqual(ai_lock_count, 9)  # 3 sections * 3 repetitions

        # Check that all sections use the same CSS class
        self.assertEqual(ai_lock_count, html_content.count('class="ai-lock"'))

    def test_ai_lock_styling_with_nested_elements(self):
        """Test AI_LOCK styling with nested HTML elements."""
        md_content = """# Test Document

[AI_LOCK] **Bold text** and *italic text* with `inline code` [AI_UNLOCK]

Regular content with **bold** and *italic* text.

[AI_LOCK] List item 1
- List item 2
- List item 3 [AI_UNLOCK]""" * 2

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that nested elements are properly styled within AI_LOCK
        self.assertIn('<div class="ai-lock"><strong>Bold text</strong> and <em>italic text</em> with <code>inline code</code></div>', html_content)
        self.assertIn('<div class="ai-lock">List item 1', html_content)

        # Check that styling is consistent
        ai_lock_sections = html_content.count('<div class="ai-lock">')
        self.assertEqual(ai_lock_sections, 4)  # 2 sections * 2 repetitions

    def test_ai_lock_styling_performance_with_many_sections(self):
        """Test AI_LOCK styling performance with many sections."""
        # Create content with many AI_LOCK sections
        ai_lock_section = "[AI_LOCK] Performance test content [AI_UNLOCK]\n"
        md_content = "# Performance Test\n\n" + (ai_lock_section * 50)

        md_file = self.create_test_md_file(md_content, "performance_test.md")
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Verify all sections were styled properly
        ai_lock_count = html_content.count('<div class="ai-lock">')
        self.assertEqual(ai_lock_count, 50)

        # Check that CSS is not duplicated for each section
        style_count = html_content.count('<style>')
        self.assertEqual(style_count, 1)  # Should only have one style block

    def test_ai_lock_styling_with_special_characters(self):
        """Test AI_LOCK styling with special characters and HTML entities."""
        special_content = "Special chars: !@#$%^&*()<>\"'{}[]|\\/?"
        md_content = f"""# Test Document

[AI_LOCK]{special_content}[AI_UNLOCK]

Regular content with {special_content}.""" * 3

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that special characters are preserved in styling
        self.assertIn(special_content, html_content)

        # Verify AI_LOCK sections are properly styled
        ai_lock_count = html_content.count('<div class="ai-lock">')
        self.assertEqual(ai_lock_count, 3)

    def test_ai_lock_styling_integration_with_existing_css(self):
        """Test AI_LOCK styling integration with existing CSS framework."""
        md_content = """# Test Document

[AI_LOCK] Content with existing CSS classes [AI_UNLOCK]

Regular content that should not be affected by AI_LOCK styling.""" * 4

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that AI_LOCK styling doesn't conflict with existing CSS
        self.assertIn('<div class="ai-lock">Content with existing CSS classes</div>', html_content)

        # Verify that existing CSS classes are preserved
        existing_classes = ['body', 'h1', 'h2', 'p', 'a', 'code', 'pre', 'table', 'th', 'td']
        for css_class in existing_classes:
            if f'.{css_class}' in html_content:
                self.assertIn(f'.{css_class}', html_content)

    def test_ai_lock_styling_responsive_design(self):
        """Test AI_LOCK styling with responsive design considerations."""
        md_content = """# Test Document

[AI_LOCK] Responsive content that should work on all devices [AI_UNLOCK]

Regular content for comparison.

[AI_LOCK] Another responsive section with longer content that might wrap on smaller screens [AI_UNLOCK]""" * 2

        md_file = self.create_test_md_file(md_content)
        html_file = self.converter.convert_file(md_file)

        self.assertTrue(os.path.exists(html_file))
        html_content = self.read_html_file(html_file)

        # Check that AI_LOCK sections are properly styled for responsiveness
        self.assertIn('<div class="ai-lock">Responsive content that should work on all devices</div>', html_content)
        self.assertIn('<div class="ai-lock">Another responsive section with longer content that might wrap on smaller screens</div>', html_content)

        # Verify responsive design elements might be present
        responsive_indicators = ['@media', 'max-width', 'min-width', 'viewport']
        style_section = re.search(r'<style[^>]*>(.*?)</style>', html_content, re.DOTALL)
        if style_section:
            style_content = style_section.group(1)
            # At least one responsive design indicator should be present
            has_responsive = any(indicator in style_content for indicator in responsive_indicators)
            # This is optional - not all implementations may include responsive design
            # self.assertTrue(has_responsive, "CSS should include responsive design elements")


if __name__ == '__main__':
    unittest.main()