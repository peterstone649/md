#!/usr/bin/env python3
"""
Test suite for the Title Extractor tool.

Tests the functionality of extracting title lines from Markdown files
and saving them to .title.txt files with preserved folder structure.
"""

import os
import sys
import unittest
import tempfile
import shutil
from pathlib import Path

# Add the parent directory to the path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from extract_titles import TitleExtractor

class TestTitleExtractor(unittest.TestCase):
    """Test cases for the TitleExtractor class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_dir = tempfile.mkdtemp()
        self.output_dir = os.path.join(self.test_dir, "out", "txt")
        
    def tearDown(self):
        """Clean up after each test method."""
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def create_test_md_file(self, filename, content):
        """Helper method to create a test markdown file."""
        file_path = os.path.join(self.test_dir, filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path
    
    def test_extract_titles_from_content_basic(self):
        """Test basic title extraction from markdown content."""
        extractor = TitleExtractor("dummy.md")
        
        content = """# Main Title
Some content here.

## Subtitle
More content.

### Sub-subtitle
Even more content.
"""
        
        titles = extractor.extract_titles_from_content(content)
        
        expected = [
            "# Main Title",
            "## Subtitle", 
            "### Sub-subtitle"
        ]
        
        self.assertEqual(titles, expected)
    
    def test_extract_titles_from_content_all_levels(self):
        """Test title extraction with all heading levels."""
        extractor = TitleExtractor("dummy.md")
        
        content = """# Level 1
## Level 2
### Level 3
#### Level 4
##### Level 5
###### Level 6
####### Too many (should not match)
#No space (should not match)
"""
        
        titles = extractor.extract_titles_from_content(content)
        
        expected = [
            "# Level 1",
            "## Level 2",
            "### Level 3",
            "#### Level 4",
            "##### Level 5",
            "###### Level 6"
        ]
        
        self.assertEqual(titles, expected)
    
    def test_extract_titles_from_content_no_titles(self):
        """Test title extraction when no titles are present."""
        extractor = TitleExtractor("dummy.md")
        
        content = """This is just regular text.
No titles here.
"""
        
        titles = extractor.extract_titles_from_content(content)
        
        self.assertEqual(titles, [])
    
    def test_process_file_success(self):
        """Test successful processing of a single markdown file."""
        extractor = TitleExtractor("dummy.md", self.output_dir)
        
        content = """# Main Title
Content here.

## Subtitle
More content.
"""
        
        input_file = self.create_test_md_file("test.md", content)
        result = extractor.process_file(input_file)
        
        self.assertTrue(result)
        
        # Check that output file was created
        output_path = os.path.join(self.output_dir, "test.title.txt")
        self.assertTrue(os.path.exists(output_path))
        
        # Check output file content
        with open(output_path, 'r', encoding='utf-8') as f:
            output_content = f.read()
        
        self.assertIn("# Main Title", output_content)
        self.assertIn("## Subtitle", output_content)
        self.assertIn("Generated on", output_content)
        self.assertIn("Source: " + input_file, output_content)
    
    def test_process_file_no_titles(self):
        """Test processing a file with no titles."""
        extractor = TitleExtractor("dummy.md", self.output_dir)
        
        content = """This is just regular text.
No titles here.
"""
        
        input_file = self.create_test_md_file("test.md", content)
        result = extractor.process_file(input_file)
        
        self.assertTrue(result)  # Should return True even with no titles
        
        # Check that output file was created (should contain header only)
        output_path = os.path.join(self.output_dir, "test.title.txt")
        self.assertTrue(os.path.exists(output_path))
        
        # Check output file content
        with open(output_path, 'r', encoding='utf-8') as f:
            output_content = f.read()
        
        self.assertIn("Generated on", output_content)
        self.assertIn("Source: " + input_file, output_content)
        # Should not contain any title lines
        self.assertNotIn("# ", output_content)
    
    def test_process_file_non_markdown(self):
        """Test processing a non-markdown file."""
        extractor = TitleExtractor("dummy.md", self.output_dir)
        
        content = "This is not a markdown file."
        
        input_file = self.create_test_md_file("test.txt", content)
        result = extractor.process_file(input_file)
        
        self.assertTrue(result)  # Should return True but skip processing
        
        # Check that no output file was created
        output_path = os.path.join(self.output_dir, "test.title.txt")
        self.assertFalse(os.path.exists(output_path))
    
    def test_process_directory_single_level(self):
        """Test processing a directory with single-level markdown files."""
        extractor = TitleExtractor("dummy.md", self.output_dir)
        
        # Create test files
        content1 = """# File 1 Title
Content of file 1.
"""
        content2 = """# File 2 Title
Content of file 2.
"""
        
        file1 = self.create_test_md_file("file1.md", content1)
        file2 = self.create_test_md_file("file2.md", content2)
        
        # Create a non-markdown file that should be ignored
        self.create_test_md_file("notmarkdown.txt", "Not markdown")
        
        success_count, total_count = extractor.process_directory(self.test_dir, recursive=False)
        
        self.assertEqual(success_count, 2)
        self.assertEqual(total_count, 2)
        
        # Check that output files were created
        output1 = os.path.join(self.output_dir, "file1.title.txt")
        output2 = os.path.join(self.output_dir, "file2.title.txt")
        
        self.assertTrue(os.path.exists(output1))
        self.assertTrue(os.path.exists(output2))


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)