#!/usr/bin/env python3
"""
Test case to prevent recursive creation of out/html directories.

This test ensures that the converter doesn't create nested 'out/html' directories
when converting Markdown files to HTML.

CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-02-07 | Initial test case to prevent recursive out/html directory creation | Framework Steward | Ensure consistent output directory structure and prevent nested directories |
"""

import os
import sys
import tempfile
import shutil
import unittest
from pathlib import Path

# Add the converter directory to the path so we can import the converter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from converter_for_md_to_html import Converter_for_Md_to_Html


class TestRecursiveDirectoryPrevention(unittest.TestCase):
    """Test cases to prevent recursive creation of out/html directories."""
    
    def setUp(self):
        """Set up test environment with temporary directories."""
        self.temp_dir = tempfile.mkdtemp(prefix="test_converter_")
        self.project_base = os.path.join(self.temp_dir, "project_base")
        self.input_dir = os.path.join(self.project_base, "docs", "subdir")
        
        # Create the directory structure
        os.makedirs(self.input_dir, exist_ok=True)
        
        # Create a test markdown file
        self.test_md_file = os.path.join(self.input_dir, "test.md")
        with open(self.test_md_file, 'w', encoding='utf-8') as f:
            f.write("# Test Document\n\nThis is a test markdown file.")
    
    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_no_recursive_out_html_directories(self):
        """Test that converter doesn't create nested out/html directories."""
        # Create converter instance
        converter = Converter_for_Md_to_Html(self.test_md_file, self.project_base)
        
        # Get the expected output path
        expected_html_path = converter.generate_for_html_path()
        expected_output_dir = os.path.dirname(expected_html_path)
        
        # Verify the expected output directory structure
        expected_parts = expected_output_dir.split(os.sep)
        out_html_count = sum(1 for part in expected_parts if part == 'out' or part == 'html')
        
        # Should have exactly one 'out' and one 'html' in the path
        self.assertIn('out', expected_parts, "Output path should contain 'out' directory")
        self.assertIn('html', expected_parts, "Output path should contain 'html' directory")
        
        # Count occurrences of 'out' and 'html' - should be exactly one each
        out_count = expected_parts.count('out')
        html_count = expected_parts.count('html')
        
        self.assertEqual(out_count, 1, f"Should have exactly one 'out' directory, found {out_count}")
        self.assertEqual(html_count, 1, f"Should have exactly one 'html' directory, found {html_count}")
        
        # Verify that 'out' and 'html' appear in the correct order (out before html)
        out_index = expected_parts.index('out')
        html_index = expected_parts.index('html')
        self.assertEqual(html_index, out_index + 1, 
                        f"'html' should come immediately after 'out' in path, got indices {out_index} and {html_index}")
    
    def test_converter_creates_correct_directory_structure(self):
        """Test that converter creates the correct directory structure without nesting."""
        # Create converter instance
        converter = Converter_for_Md_to_Html(self.test_md_file, self.project_base)
        
        # Run the conversion
        success = converter.convert()
        self.assertTrue(success, "Conversion should succeed")
        
        # Get the actual output path
        expected_html_path = converter.generate_for_html_path()
        
        # Verify the file was created
        self.assertTrue(os.path.exists(expected_html_path), 
                       f"HTML file should be created at: {expected_html_path}")
        
        # Verify the directory structure
        output_dir = os.path.dirname(expected_html_path)
        self.assertTrue(os.path.exists(output_dir), 
                       f"Output directory should exist: {output_dir}")
        
        # Check that we don't have nested out/html directories
        path_parts = output_dir.split(os.sep)
        
        # Find all occurrences of 'out' and 'html'
        out_indices = [i for i, part in enumerate(path_parts) if part == 'out']
        html_indices = [i for i, part in enumerate(path_parts) if part == 'html']
        
        # Should have exactly one of each
        self.assertEqual(len(out_indices), 1, f"Should have exactly one 'out' directory, found {len(out_indices)}")
        self.assertEqual(len(html_indices), 1, f"Should have exactly one 'html' directory, found {len(html_indices)}")
        
        # Verify 'html' comes immediately after 'out'
        out_idx = out_indices[0]
        html_idx = html_indices[0]
        self.assertEqual(html_idx, out_idx + 1, 
                        f"'html' should come immediately after 'out' in path, got indices {out_idx} and {html_idx}")
    
    def test_multiple_conversions_same_structure(self):
        """Test that multiple conversions don't create nested directories."""
        # Create a second test file
        test_md_file2 = os.path.join(self.input_dir, "test2.md")
        with open(test_md_file2, 'w', encoding='utf-8') as f:
            f.write("# Second Test Document\n\nThis is another test markdown file.")
        
        # Convert first file
        converter1 = Converter_for_Md_to_Html(self.test_md_file, self.project_base)
        success1 = converter1.convert()
        self.assertTrue(success1, "First conversion should succeed")
        
        # Convert second file
        converter2 = Converter_for_Md_to_Html(test_md_file2, self.project_base)
        success2 = converter2.convert()
        self.assertTrue(success2, "Second conversion should succeed")
        
        # Get output paths
        html_path1 = converter1.generate_for_html_path()
        html_path2 = converter2.generate_for_html_path()
        
        # Both should have the same output directory structure
        output_dir1 = os.path.dirname(html_path1)
        output_dir2 = os.path.dirname(html_path2)
        
        # Verify no nested directories were created - check that each has exactly one 'out' and one 'html'
        for output_dir in [output_dir1, output_dir2]:
            path_parts = output_dir.split(os.sep)
            out_count = path_parts.count('out')
            html_count = path_parts.count('html')
            
            self.assertEqual(out_count, 1, f"Should have exactly one 'out' directory, found {out_count}")
            self.assertEqual(html_count, 1, f"Should have exactly one 'html' directory, found {html_count}")
            
            # Verify that 'out' and 'html' appear in the correct order (out before html)
            out_index = path_parts.index('out')
            html_index = path_parts.index('html')
            self.assertEqual(html_index, out_index + 1, 
                            f"'html' should come immediately after 'out' in path, got indices {out_index} and {html_index}")
    
    def test_existing_out_html_directory_handling(self):
        """Test that converter handles existing out/html directories correctly."""
        # Pre-create the out/html directory structure
        existing_out_html = os.path.join(self.project_base, "out", "html")
        os.makedirs(existing_out_html, exist_ok=True)
        
        # Create a file in the existing directory to ensure it's not overwritten
        existing_file = os.path.join(existing_out_html, "existing.html")
        with open(existing_file, 'w', encoding='utf-8') as f:
            f.write("<html><body>Existing file</body></html>")
        
        # Create converter and run conversion
        converter = Converter_for_Md_to_Html(self.test_md_file, self.project_base)
        success = converter.convert()
        self.assertTrue(success, "Conversion should succeed even with existing out/html directory")
        
        # Verify the existing file is still there
        self.assertTrue(os.path.exists(existing_file), 
                       "Existing file should not be deleted")
        
        # Verify our new file was created
        expected_html_path = converter.generate_for_html_path()
        self.assertTrue(os.path.exists(expected_html_path), 
                       "New HTML file should be created")
        
        # Verify directory structure is still correct
        output_dir = os.path.dirname(expected_html_path)
        path_parts = output_dir.split(os.sep)
        out_count = path_parts.count('out')
        html_count = path_parts.count('html')
        
        self.assertEqual(out_count, 1, f"Should have exactly one 'out' directory, found {out_count}")
        self.assertEqual(html_count, 1, f"Should have exactly one 'html' directory, found {html_count}")


def run_tests():
    """Run the test suite."""
    print("Running tests to prevent recursive out/html directory creation...")
    print("=" * 70)
    
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRecursiveDirectoryPrevention)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print("All tests passed! Recursive out/html directory creation is prevented.")
        return True
    else:
        print("Some tests failed! There may be issues with directory structure handling.")
        return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)