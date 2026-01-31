#!/usr/bin/env python3
"""
Test Cases for Index Generator Tool

This test suite validates the index_generator.py tool functionality,
specifically ensuring that index.md files are created when README.md files are present.

Test Cases:
1. Basic index.md creation when README.md exists
2. Index.md creation in nested directories with README.md
3. Multiple README.md files handling
4. Index.md creation with different README formats
5. Recursive index.md creation
6. Index.md content validation
7. Existing index.md file handling
8. Error handling for invalid paths

CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.1.0  | 2026-01-31 | Added comprehensive changelog following framework conventions | Framework Steward | Align with framework documentation standards and provide clear version history |
| V1.0.0  | 2026-01-31 | Initial test suite implementation with comprehensive test coverage | AI Coder | Core test functionality for validating index generator behavior |
"""

import os
import sys
import tempfile
import shutil
import unittest
from pathlib import Path
from unittest.mock import patch

# Add the converter path to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'converter'))

from index_generator import IndexGenerator

class TestIndexGenerator(unittest.TestCase):
    """Test cases for IndexGenerator functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp(prefix='index_generator_test_')
        self.generator = IndexGenerator(self.test_dir)
        
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def create_test_structure(self, structure):
        """
        Create a test directory structure.
        
        Args:
            structure (dict): Directory structure to create
        """
        for path, content in structure.items():
            full_path = Path(self.test_dir) / path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            if content is None:
                # Create directory
                full_path.mkdir(parents=True, exist_ok=True)
            else:
                # Create file with content
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(content)
    
    def test_basic_index_creation_with_readme(self):
        """Test that index.md is created when README.md exists."""
        # Create test structure with README.md
        structure = {
            'README.md': '# Test Folder\nThis is a test folder.',
            'file1.txt': 'Content of file1',
            'file2.py': '# Python file\nprint("hello")'
        }
        self.create_test_structure(structure)
        
        # Generate index
        self.generator.create_index_files(self.test_dir, format='md')
        
        # Verify index.md was created
        index_file = Path(self.test_dir) / 'index.md'
        self.assertTrue(index_file.exists(), "index.md should be created when README.md exists")
        
        # Verify index.md content
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertIn('# Index of .', content, "Index should have correct title")
        self.assertIn('## [📁 README.md](README.md)', content, "README should be featured as jump address")
        self.assertIn('- [file1.txt](file1.txt)', content, "File1 should be listed")
        self.assertIn('- [file2.py](file2.py)', content, "File2 should be listed")
    
    def test_nested_directories_with_readme(self):
        """Test index.md creation in nested directories with README.md."""
        structure = {
            'README.md': '# Root Folder',
            'subfolder/README.md': '# Subfolder',
            'subfolder/file1.txt': 'Content',
            'subfolder/deep/README.md': '# Deep Folder',
            'subfolder/deep/file2.py': 'print("deep")'
        }
        self.create_test_structure(structure)
        
        # Generate index recursively
        self.generator.create_index_files(self.test_dir, format='md', recursive=True)
        
        # Verify index files were created
        root_index = Path(self.test_dir) / 'index.md'
        sub_index = Path(self.test_dir) / 'subfolder' / 'index.md'
        deep_index = Path(self.test_dir) / 'subfolder' / 'deep' / 'index.md'
        
        self.assertTrue(root_index.exists(), "Root index.md should be created")
        self.assertTrue(sub_index.exists(), "Subfolder index.md should be created")
        self.assertTrue(deep_index.exists(), "Deep folder index.md should be created")
        
        # Verify subfolder index content
        with open(sub_index, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('## [📁 README.md](README.md)', content, "Subfolder README should be featured")
    
    def test_multiple_readme_formats(self):
        """Test index.md creation with different README formats."""
        readme_formats = ['README.md', 'README.txt', 'readme.md', 'readme.txt']
        
        for readme_file in readme_formats:
            with self.subTest(readme_format=readme_file):
                # Clean up previous test
                for item in Path(self.test_dir).iterdir():
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item)
                
                # Create README in different format
                structure = {
                    readme_file: f'# {readme_file}\nTest content',
                    'file1.txt': 'Content'
                }
                self.create_test_structure(structure)
                
                # Generate index
                self.generator.create_index_files(self.test_dir, format='md')
                
                # Verify index.md was created
                index_file = Path(self.test_dir) / 'index.md'
                self.assertTrue(index_file.exists(), f"index.md should be created for {readme_file}")
                
                # Verify README is featured
                with open(index_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.assertIn(f'## [📁 {readme_file}]({readme_file})', content, 
                             f"{readme_file} should be featured in index")
    
    def test_recursive_index_creation(self):
        """Test recursive index.md creation for all directories with README.md."""
        structure = {
            'README.md': '# Root',
            'folder1/README.md': '# Folder1',
            'folder1/file1.txt': 'Content1',
            'folder2/README.md': '# Folder2',
            'folder2/subfolder/README.md': '# Subfolder',
            'folder2/subfolder/file2.py': 'print("test")',
            'folder3/file3.txt': 'No README here'
        }
        self.create_test_structure(structure)
        
        # Generate index recursively
        self.generator.create_index_files(self.test_dir, format='md', recursive=True)
        
        # Verify index files were created only where README exists
        expected_indices = [
            Path(self.test_dir) / 'index.md',
            Path(self.test_dir) / 'folder1' / 'index.md',
            Path(self.test_dir) / 'folder2' / 'index.md',
            Path(self.test_dir) / 'folder2' / 'subfolder' / 'index.md'
        ]
        
        for index_path in expected_indices:
            self.assertTrue(index_path.exists(), f"Index should be created for {index_path.parent}")
        
        # Verify no index for folder3 (no README)
        folder3_index = Path(self.test_dir) / 'folder3' / 'index.md'
        self.assertFalse(folder3_index.exists(), "No index should be created for folder without README")
    
    def test_index_content_validation(self):
        """Test that generated index.md has correct content structure."""
        structure = {
            'README.md': '# Test Folder\nDetailed description here.',
            'file1.txt': 'Text content',
            'file2.py': 'Python code',
            'file3.md': '# Markdown file',
            'subfolder/README.md': '# Subfolder'
        }
        self.create_test_structure(structure)
        
        self.generator.create_index_files(self.test_dir, format='md')
        
        with open(Path(self.test_dir) / 'index.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check structure
        lines = content.split('\n')
        
        # Should start with title
        self.assertTrue(lines[0].startswith('# Index of'), "Should start with index title")
        
        # Should have README featured
        self.assertIn('## [📁 README.md](README.md)', content, "README should be featured")
        self.assertIn('*Jump to main documentation for this folder*', content, "Should have jump description")
        
        # Should have Files section
        self.assertIn('## Files', content, "Should have Files section")
        
        # Should list files (excluding README)
        self.assertIn('- [file1.txt](file1.txt)', content, "Should list file1.txt")
        self.assertIn('- [file2.py](file2.py)', content, "Should list file2.py")
        self.assertIn('- [file3.md](file3.md)', content, "Should list file3.md")
        
        # Should have Subdirectories section
        self.assertIn('## Subdirectories', content, "Should have Subdirectories section")
        self.assertIn('- [subfolder/](subfolder/)', content, "Should list subfolder")
        
        # Should have footer
        self.assertIn('Generated on', content, "Should have generation timestamp")
        self.assertIn('IndexGenerator', content, "Should mention IndexGenerator")
    
    def test_existing_index_file_handling(self):
        """Test that existing index.md files are not overwritten."""
        structure = {
            'README.md': '# Test',
            'index.md': '# Existing Index\nThis should not be overwritten'
        }
        self.create_test_structure(structure)
        
        # Generate index (should not overwrite)
        self.generator.create_index_files(self.test_dir, format='md')
        
        # Verify existing content is preserved
        with open(Path(self.test_dir) / 'index.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertEqual(content, '# Existing Index\nThis should not be overwritten', 
                        "Existing index.md should not be overwritten")
    
    def test_no_readme_no_index(self):
        """Test that no index.md is created when no README exists."""
        structure = {
            'file1.txt': 'Content',
            'file2.py': 'Code'
        }
        self.create_test_structure(structure)
        
        self.generator.create_index_files(self.test_dir, format='md')
        
        # Verify no index.md was created
        index_file = Path(self.test_dir) / 'index.md'
        self.assertFalse(index_file.exists(), "No index.md should be created without README")
    
    def test_html_format_with_readme(self):
        """Test HTML index creation when README.md exists."""
        structure = {
            'README.md': '# Test Folder',
            'file1.txt': 'Content'
        }
        self.create_test_structure(structure)
        
        self.generator.create_index_files(self.test_dir, format='html')
        
        # Verify index.html was created
        index_file = Path(self.test_dir) / 'index.html'
        self.assertTrue(index_file.exists(), "index.html should be created when README.md exists")
        
        # Verify HTML content
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertIn('<title>Index of .</title>', content, "Should have correct HTML title")
        self.assertIn('<a href="README.md">README.md</a>', content, "Should link to README")
        self.assertIn('<a href="file1.txt">file1.txt</a>', content, "Should link to file1.txt")
    
    def test_invalid_path_handling(self):
        """Test error handling for invalid paths."""
        # Test non-existent path
        result = self.generator.create_index_files('/non/existent/path', format='md')
        self.assertFalse(result, "Should return False for non-existent path")
        
        # Test file instead of directory
        test_file = Path(self.test_dir) / 'test.txt'
        test_file.write_text('test')
        
        result = self.generator.create_index_files(test_file, format='md')
        self.assertFalse(result, "Should return False for file path")
    
    def test_empty_directory_with_readme(self):
        """Test index.md creation for empty directory with only README.md."""
        structure = {
            'README.md': '# Empty Folder\nJust a README file.'
        }
        self.create_test_structure(structure)
        
        self.generator.create_index_files(self.test_dir, format='md')
        
        index_file = Path(self.test_dir) / 'index.md'
        self.assertTrue(index_file.exists(), "index.md should be created")
        
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertIn('## [📁 README.md](README.md)', content, "README should be featured")
        self.assertIn('No subdirectories.', content, "Should indicate no subdirectories")
    
    def test_hidden_directory_handling(self):
        """Test that hidden directories are skipped in recursive mode."""
        structure = {
            'README.md': '# Root',
            '.hidden/README.md': '# Hidden',
            'normal/README.md': '# Normal'
        }
        self.create_test_structure(structure)
        
        self.generator.create_index_files(self.test_dir, format='md', recursive=True)
        
        # Check which indices were created
        root_index = Path(self.test_dir) / 'index.md'
        hidden_index = Path(self.test_dir) / '.hidden' / 'index.md'
        normal_index = Path(self.test_dir) / 'normal' / 'index.md'
        
        self.assertTrue(root_index.exists(), "Root index should be created")
        self.assertFalse(hidden_index.exists(), "Hidden directory index should be skipped")
        self.assertTrue(normal_index.exists(), "Normal directory index should be created")

def run_tests():
    """Run all test cases."""
    unittest.main(verbosity=2)

if __name__ == '__main__':
    run_tests()