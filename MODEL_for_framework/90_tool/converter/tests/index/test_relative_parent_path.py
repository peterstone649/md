#!/usr/bin/env python3
"""
Test Cases for Relative Parent Path Navigation

This test suite validates that the index_generator.py tool uses relative paths
instead of absolute paths for parent folder navigation links in index.md files.

Test Cases:
1. Basic relative parent path navigation
2. Relative parent path in nested directories
3. Multiple levels of relative parent navigation
4. Relative parent path with special characters
5. Relative parent path with Unicode directories
6. Verification that absolute paths are NOT used

CHANGELOG

| Version | Date       | Change Content | Stakeholders | Motivation |
|---------|------------|----------------|--------------|------------|
| V1.0.0  | 2026-02-01 | Initial test suite implementation for relative parent path navigation | Framework Steward | Ensure parent folder navigation uses relative paths for portability and compatibility |
"""

import os
import sys
import tempfile
import shutil
import unittest
from pathlib import Path

# Add the converter path to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'converter'))

from index_generator import IndexGenerator

class TestRelativeParentPath(unittest.TestCase):
    """Test cases for relative parent path navigation functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp(prefix='relative_path_test_')
        self.generator = IndexGenerator(self.test_dir)
        
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def create_test_structure(self):
        """Create a test directory structure with nested folders."""
        # Create main directory with README
        main_dir = os.path.join(self.test_dir, "main")
        os.makedirs(main_dir, exist_ok=True)
        
        with open(os.path.join(main_dir, "README.md"), 'w', encoding='utf-8') as f:
            f.write("# Main Directory\n\nThis is the main directory.")
        
        # Create subdirectory with README
        sub_dir = os.path.join(main_dir, "subdir")
        os.makedirs(sub_dir, exist_ok=True)
        
        with open(os.path.join(sub_dir, "README.md"), 'w', encoding='utf-8') as f:
            f.write("# Sub Directory\n\nThis is a subdirectory.")
        
        # Create nested subdirectory with README
        nested_dir = os.path.join(sub_dir, "nested")
        os.makedirs(nested_dir, exist_ok=True)
        
        with open(os.path.join(nested_dir, "README.md"), 'w', encoding='utf-8') as f:
            f.write("# Nested Directory\n\nThis is a nested directory.")
        
        return main_dir, sub_dir, nested_dir
    
    def read_index_file(self, index_path):
        """Read and return the content of an index file."""
        with open(index_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def test_relative_parent_path_in_subdirectory(self):
        """Test that subdirectory index uses relative path for parent folder navigation."""
        main_dir, sub_dir, _ = self.create_test_structure()
        
        # Generate index for subdirectory
        self.generator.create_index_files(sub_dir, format='md')
        
        index_path = os.path.join(sub_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify that parent folder navigation uses relative path
        self.assertIn('](../)', index_content, "Should have relative parent folder link")
        
        # Verify that absolute paths are NOT used
        absolute_path_indicators = [
            '/main/', '/subdir/', '/nested/',
            'E:/', 'C:/', 'D:/',
            '/Users/', '/home/', '/var/',
            'http://', 'https://'
        ]
        
        for indicator in absolute_path_indicators:
            self.assertNotIn(indicator, index_content, 
                           f"Should not contain absolute path indicator: {indicator}")
    
    def test_relative_parent_path_in_nested_directory(self):
        """Test that nested directory index uses relative paths for parent folder navigation."""
        _, sub_dir, nested_dir = self.create_test_structure()
        
        # Generate index for nested directory
        self.generator.create_index_files(nested_dir, format='md')
        
        index_path = os.path.join(nested_dir, 'index.md')
        self.assertTrue(index_path.exists(), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify relative parent navigation
        self.assertIn('[../](../)', index_content, "Should have relative parent folder link")
        self.assertIn('[../../](../../)', index_content, "Should have relative grandparent folder link")
        
        # Verify no absolute paths
        absolute_path_indicators = [
            '/main/', '/subdir/', '/nested/',
            'E:/', 'C:/', 'D:/',
            '/Users/', '/home/', '/var/'
        ]
        
        for indicator in absolute_path_indicators:
            self.assertNotIn(indicator, index_content, 
                           f"Should not contain absolute path indicator: {indicator}")
    
    def test_multiple_levels_relative_parent_path(self):
        """Test relative parent path navigation across multiple directory levels."""
        # Create deeply nested structure
        deep_dir = self.test_dir
        path_parts = ['level1', 'level2', 'level3', 'level4']
        current_path = deep_dir
        
        for part in path_parts:
            current_path = os.path.join(current_path, part)
            os.makedirs(current_path, exist_ok=True)
            
            # Create README in each level
            with open(os.path.join(current_path, 'README.md'), 'w', encoding='utf-8') as f:
                f.write(f"# {part}\n\nThis is {part}.")
        
        # Generate index for deepest directory
        self.generator.create_index_files(current_path, format='md')
        
        index_path = os.path.join(current_path, 'index.md')
        self.assertTrue(index_path.exists(), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify all parent levels use relative paths
        expected_relative_links = [
            '[../](../)',
            '[../../](../../)', 
            '[../../../](../../../)',
            '[../../../../](../../../../)'
        ]
        
        for link in expected_relative_links:
            self.assertIn(link, index_content, f"Should have relative {link} navigation")
        
        # Verify no absolute paths in any parent navigation
        absolute_path_indicators = [
            '/level1/', '/level2/', '/level3/', '/level4/',
            'E:/', 'C:/', 'D:/',
            '/Users/', '/home/', '/var/'
        ]
        
        for indicator in absolute_path_indicators:
            self.assertNotIn(indicator, index_content, 
                           f"Should not contain absolute path indicator: {indicator}")
    
    def test_relative_parent_path_special_characters(self):
        """Test relative parent path navigation with special character directories."""
        # Create directory with special characters
        special_dir = os.path.join(self.test_dir, "special dir with spaces")
        os.makedirs(special_dir, exist_ok=True)
        
        with open(os.path.join(special_dir, "README.md"), 'w', encoding='utf-8') as f:
            f.write("# Special Directory\n\nThis has special characters.")
        
        # Create subdirectory with special characters
        special_sub = os.path.join(special_dir, "sub-dir with spaces")
        os.makedirs(special_sub, exist_ok=True)
        
        with open(os.path.join(special_sub, "README.md"), 'w', encoding='utf-8') as f:
            f.write("# Special Sub Directory\n\nThis is a special subdirectory.")
        
        # Generate index
        self.generator.create_index_files(special_sub, format='md')
        
        index_path = os.path.join(special_sub, 'index.md')
        self.assertTrue(index_path.exists(), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify relative parent navigation works with special characters
        self.assertIn('[../](../)', index_content, "Should have relative parent navigation")
        
        # Verify no absolute paths with special characters
        absolute_path_indicators = [
            '/special dir with spaces/',
            '/sub-dir with spaces/',
            'E:/', 'C:/', 'D:/',
            '/Users/', '/home/', '/var/'
        ]
        
        for indicator in absolute_path_indicators:
            self.assertNotIn(indicator, index_content, 
                           f"Should not contain absolute path indicator: {indicator}")
    
    def test_relative_parent_path_unicode_directories(self):
        """Test relative parent path navigation with Unicode directory names."""
        # Create directory with Unicode characters
        unicode_dir = os.path.join(self.test_dir, "unicode_测试_тест_テスト")
        os.makedirs(unicode_dir, exist_ok=True)
        
        with open(os.path.join(unicode_dir, "README.md"), 'w', encoding='utf-8') as f:
            f.write("# Unicode Directory\n\nThis has Unicode characters.")
        
        # Create subdirectory with Unicode
        unicode_sub = os.path.join(unicode_dir, "子目录_подкаталог_サブディレクトリ")
        os.makedirs(unicode_sub, exist_ok=True)
        
        with open(os.path.join(unicode_sub, "README.md"), 'w', encoding='utf-8') as f:
            f.write("# Unicode Sub Directory\n\nThis is a Unicode subdirectory.")
        
        # Generate index
        self.generator.create_index_files(unicode_sub, format='md')
        
        index_path = os.path.join(unicode_sub, 'index.md')
        self.assertTrue(index_path.exists(), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify relative parent navigation works with Unicode
        self.assertIn('[../](../)', index_content, "Should have relative parent navigation")
        
        # Verify no absolute paths with Unicode
        absolute_path_indicators = [
            '/unicode_测试_тест_テスト/',
            '/子目录_подкаталог_サブディレクトリ/',
            'E:/', 'C:/', 'D:/',
            '/Users/', '/home/', '/var/'
        ]
        
        for indicator in absolute_path_indicators:
            self.assertNotIn(indicator, index_content, 
                           f"Should not contain absolute path indicator: {indicator}")
    
    def test_relative_parent_path_content_structure(self):
        """Test that relative parent path navigation maintains proper content structure."""
        main_dir, sub_dir, _ = self.create_test_structure()
        
        # Generate index for subdirectory
        self.generator.create_index_files(sub_dir, format='md')
        
        index_path = os.path.join(sub_dir, 'index.md')
        self.assertTrue(index_path.exists(), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify the content structure is maintained
        lines = index_content.split('\n')
        
        # Should have title
        self.assertTrue(any(line.startswith('# Index of') for line in lines), 
                       "Should have index title")
        
        # Should have Files section
        self.assertIn('## Files', index_content, "Should have Files section")
        
        # Should have Subdirectories section
        self.assertIn('## Subdirectories', index_content, "Should have Subdirectories section")
        
        # Should have relative parent navigation
        self.assertIn('[../](../)', index_content, "Should have relative parent navigation")
        
        # Should NOT have absolute parent navigation
        absolute_indicators = ['/main/', '/subdir/', '/nested/', 'E:/', 'C:/']
        for indicator in absolute_indicators:
            self.assertNotIn(indicator, index_content, 
                           f"Should not contain absolute path indicator: {indicator}")
        
        # Should have footer
        self.assertIn('Generated on', index_content, "Should have generation timestamp")
        self.assertIn('IndexGenerator', index_content, "Should mention IndexGenerator")
    
    def test_relative_parent_path_vs_absolute_path(self):
        """Test that explicitly verifies relative paths are used instead of absolute paths."""
        main_dir, sub_dir, _ = self.create_test_structure()
        
        # Generate index for subdirectory
        self.generator.create_index_files(sub_dir, format='md')
        
        index_path = os.path.join(sub_dir, 'index.md')
        self.assertTrue(index_path.exists(), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify relative paths are present
        relative_indicators = ['../', '../../', '../../../']
        relative_found = any(indicator in index_content for indicator in relative_indicators)
        self.assertTrue(relative_found, "Should contain relative path indicators")
        
        # Verify absolute paths are absent
        absolute_indicators = [
            '/main/', '/subdir/', '/nested/',
            'E:/', 'C:/', 'D:/',
            '/Users/', '/home/', '/var/',
            'http://', 'https://',
            'file://', 'ftp://'
        ]
        
        absolute_found = any(indicator in index_content for indicator in absolute_indicators)
        self.assertFalse(absolute_found, "Should not contain any absolute path indicators")
        
        # Specifically check for the problematic absolute path that was fixed
        self.assertNotIn('/MODEL_for_framework/', index_content, 
                        "Should not contain the problematic absolute path that was fixed")

def run_tests():
    """Run all test cases."""
    unittest.main(verbosity=2)

if __name__ == '__main__':
    run_tests()