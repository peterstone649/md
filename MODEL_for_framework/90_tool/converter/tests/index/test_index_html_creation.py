#!/usr/bin/env python3
"""
Test for Index HTML Creation

This test ensures that the index.html file is always created in the comparable folder
when using the index_generator.py tool, following the pattern established by
manager_for_dir_OT_base.py.

CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-01-31 | Initial creation of test for index.html creation | Framework Steward | Ensure consistent HTML index generation across all directories |
"""

import os
import sys
import unittest
import tempfile
import shutil
from pathlib import Path

# Add the converter directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'converter'))

try:
    from index_generator import generate_index
except ImportError:
    print("ERROR: Could not import index_generator. Make sure it's in the converter directory.")
    sys.exit(1)


class TestIndexHTMLCreation(unittest.TestCase):
    """Test class for index.html creation functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp()
        self.original_dir = os.getcwd()
        
    def tearDown(self):
        """Clean up test environment."""
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_index_html_creation_in_comparable_folder(self):
        """Test that index.html is created in the same directory as the source files."""
        # Create some test markdown files
        test_files = [
            "test1.md",
            "test2.md", 
            "subfolder/test3.md",
            "subfolder/nested/test4.md"
        ]
        
        for file_path in test_files:
            full_path = os.path.join(self.test_dir, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(f"# Test file: {file_path}\n\nThis is test content for {file_path}.")
        
        # Change to test directory
        os.chdir(self.test_dir)
        
        # Run the index generator
        generate_index()
        
        # Check that index.html was created in the same directory
        index_html_path = os.path.join(self.test_dir, "index.html")
        self.assertTrue(os.path.exists(index_html_path), 
                       f"index.html should be created in {self.test_dir}")
        
        # Check that index.md was also created
        index_md_path = os.path.join(self.test_dir, "index.md")
        self.assertTrue(os.path.exists(index_md_path), 
                       f"index.md should be created in {self.test_dir}")
        
        # Verify the content of index.html
        with open(index_html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        self.assertIn("<html>", html_content, "index.html should contain HTML structure")
        self.assertIn("<title>Index of Files</title>", html_content, "index.html should have title")
        self.assertIn("test1.md", html_content, "index.html should list test files")
        self.assertIn("test2.md", html_content, "index.html should list test files")
        
        # Verify the content of index.md
        with open(index_md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        self.assertIn("# Index of Files", md_content, "index.md should have header")
        self.assertIn("test1.md", md_content, "index.md should list test files")
        self.assertIn("test2.md", md_content, "index.md should list test files")
    
    def test_index_html_creation_with_no_files(self):
        """Test index.html creation when directory has no markdown files."""
        os.chdir(self.test_dir)
        
        # Run the index generator on empty directory
        generate_index()
        
        # Check that index.html was still created
        index_html_path = os.path.join(self.test_dir, "index.html")
        self.assertTrue(os.path.exists(index_html_path), 
                       f"index.html should be created even in empty directory")
        
        # Check that index.md was also created
        index_md_path = os.path.join(self.test_dir, "index.md")
        self.assertTrue(os.path.exists(index_md_path), 
                       f"index.md should be created even in empty directory")
        
        # Verify the content indicates no files
        with open(index_html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        self.assertIn("0 total", html_content, "index.html should indicate 0 files")
        
        with open(index_md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        self.assertIn("0 total", md_content, "index.md should indicate 0 files")
    
    def test_index_html_creation_with_mixed_files(self):
        """Test index.html creation with mixed file types."""
        # Create test files with different extensions
        test_files = [
            ("test1.md", "# Markdown file\nContent here"),
            ("test2.txt", "Plain text file"),
            ("test3.py", "# Python file\nprint('hello')"),
            ("README.md", "# README\nProject documentation"),
            ("subfolder/test4.md", "# Nested file\nContent in subfolder")
        ]
        
        for file_path, content in test_files:
            full_path = os.path.join(self.test_dir, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        os.chdir(self.test_dir)
        generate_index()
        
        # Check that index files were created
        index_html_path = os.path.join(self.test_dir, "index.html")
        index_md_path = os.path.join(self.test_dir, "index.md")
        
        self.assertTrue(os.path.exists(index_html_path), "index.html should be created")
        self.assertTrue(os.path.exists(index_md_path), "index.md should be created")
        
        # Verify only .md files are listed
        with open(index_html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        # Should list markdown files but not .txt or .py
        self.assertIn("test1.md", html_content, "Should list markdown files")
        self.assertIn("README.md", html_content, "Should list README.md")
        self.assertIn("test4.md", html_content, "Should list nested markdown files")
        self.assertNotIn("test2.txt", html_content, "Should not list .txt files")
        self.assertNotIn("test3.py", html_content, "Should not list .py files")
        
        with open(index_md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        self.assertIn("test1.md", md_content, "Should list markdown files in MD")
        self.assertNotIn("test2.txt", md_content, "Should not list .txt files in MD")
    
    def test_index_html_creation_preserves_directory_structure(self):
        """Test that index.html creation preserves directory structure in links."""
        # Create files in nested directories
        test_files = [
            "level1/file1.md",
            "level1/level2/file2.md", 
            "level1/level2/level3/file3.md",
            "root_file.md"
        ]
        
        for file_path in test_files:
            full_path = os.path.join(self.test_dir, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(f"# {file_path}\nContent for {file_path}")
        
        os.chdir(self.test_dir)
        generate_index()
        
        index_html_path = os.path.join(self.test_dir, "index.html")
        self.assertTrue(os.path.exists(index_html_path))
        
        with open(index_html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # All files should be listed with their relative paths
        for file_path in test_files:
            self.assertIn(file_path, html_content, f"Should list {file_path} in index")
    
    def test_index_html_creation_handles_special_characters(self):
        """Test index.html creation with files containing special characters."""
        # Create files with special characters
        test_files = [
            "file with spaces.md",
            "file-with-dashes.md",
            "file_with_underscores.md",
            "file.with.dots.md",
            "file(1).md"
        ]
        
        for file_path in test_files:
            full_path = os.path.join(self.test_dir, file_path)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(f"# {file_path}\nContent")
        
        os.chdir(self.test_dir)
        generate_index()
        
        index_html_path = os.path.join(self.test_dir, "index.html")
        self.assertTrue(os.path.exists(index_html_path))
        
        with open(index_html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # All files should be listed correctly
        for file_path in test_files:
            self.assertIn(file_path, html_content, f"Should handle special characters in {file_path}")


if __name__ == '__main__':
    unittest.main()