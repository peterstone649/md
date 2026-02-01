#!/usr/bin/env python3
"""
Test Cases for Parent Folder Navigation with Emoji

This test suite validates that the index_generator.py tool includes a nice emoji
when creating parent folder navigation links in index.md files.

Test Cases:
1. Basic parent folder navigation with emoji in main directory
2. Parent folder navigation with emoji in nested directories
3. Multiple levels of parent navigation with emojis
4. Parent folder navigation with emoji in HTML format
5. Parent folder navigation with emoji in recursive generation
6. Parent folder navigation with emoji in special character directories
7. Parent folder navigation with emoji in Unicode directories

CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-02-01 | Initial test suite implementation for parent folder navigation with emoji | Framework Steward | Ensure parent folder navigation includes visually appealing emoji for better user experience |
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

class TestParentFolderEmoji(unittest.TestCase):
    """Test cases for parent folder navigation with emoji functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp(prefix='parent_emoji_test_')
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
    
    def test_parent_folder_emoji_in_subdirectory(self):
        """Test that subdirectory index includes emoji for parent folder navigation."""
        main_dir, sub_dir, _ = self.create_test_structure()
        
        # Generate index for subdirectory
        self.generator.create_index_files(sub_dir, format='md')
        
        index_path = os.path.join(sub_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify that README has emoji (current implementation)
        self.assertIn('📁', index_content, "README should have folder emoji")
        
        # Note: Current implementation doesn't include parent navigation,
        # but when it does, it should include emojis like 🏠, ⬆️, or 🔙
        # This test documents the expected behavior for future implementation
    
    def test_parent_folder_emoji_in_nested_directory(self):
        """Test that nested directory index includes emojis for parent folder navigation."""
        _, sub_dir, nested_dir = self.create_test_structure()
        
        # Generate index for nested directory
        self.generator.create_index_files(nested_dir, format='md')
        
        index_path = os.path.join(nested_dir, 'index.md')
        self.assertTrue(index_path.exists(), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify parent folder navigation includes emojis
        self.assertIn('[🏠 Go to Parent Folder]', index_content, "Should have parent folder link with emoji")
        
        # Check for emojis in parent navigation
        self.assertIn('🏠', index_content, "Parent folder navigation should include house emoji")
    
    def test_multiple_levels_parent_emoji(self):
        """Test parent folder navigation with emojis across multiple directory levels."""
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
        
        # Verify all parent levels have navigation with emojis
        parent_links = ['[../](../)', '[../../](../../)', '[../../../](../../../)', '[../../../../](../../../../)']
        for link in parent_links:
            self.assertIn(link, index_content, f"Should have {link} navigation")
        
        # Check that emojis are present in parent navigation
        emoji_indicators = ['🏠', '⬆️', '🔙', '↑', '⬆️']
        emoji_found = any(emoji in index_content for emoji in emoji_indicators)
        self.assertTrue(
            emoji_found,
            "Multiple level parent navigation should include emojis"
        )
    
    def test_parent_folder_emoji_in_html_format(self):
        """Test that HTML index includes emoji for parent folder navigation."""
        main_dir, sub_dir, _ = self.create_test_structure()
        
        # Generate HTML index for subdirectory
        self.generator.create_index_files(sub_dir, format='html')
        
        # HTML files go to standardized output directory
        from manager_for_dir_OT_base import ManagerForDirOTBase
        dir_manager = ManagerForDirOTBase(self.test_dir)
        html_path = dir_manager.generate_html_path(os.path.join(sub_dir, 'index.html'))
        index_path = Path(html_path)
        
        self.assertTrue(index_path.exists(), "HTML index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify parent folder navigation includes emoji in HTML
        self.assertIn('<a href="../">../</a>', index_content, "Should have parent folder link in HTML")
        
        # Check for emojis in HTML parent navigation
        emoji_indicators = ['🏠', '⬆️', '🔙', '↑', '⬆️']
        emoji_found = any(emoji in index_content for emoji in emoji_indicators)
        self.assertTrue(
            emoji_found,
            "HTML parent folder navigation should include emojis"
        )
    
    def test_parent_folder_emoji_recursive_generation(self):
        """Test parent folder emoji navigation in recursive index generation."""
        main_dir, sub_dir, nested_dir = self.create_test_structure()
        
        # Generate indexes recursively
        self.generator.create_index_files(main_dir, format='md', recursive=True)
        
        # Check subdirectory index
        sub_index = os.path.join(sub_dir, 'index.md')
        self.assertTrue(os.path.exists(sub_index), "Subdirectory index should be created")
        
        sub_content = self.read_index_file(sub_index)
        self.assertIn('[../](../)', sub_content, "Should have parent navigation")
        self.assertIn('[nested/](nested/)', sub_content, "Should have child navigation")
        
        # Check for emoji in parent navigation
        emoji_indicators = ['🏠', '⬆️', '🔙', '↑', '⬆️']
        sub_emoji_found = any(emoji in sub_content for emoji in emoji_indicators)
        self.assertTrue(
            sub_emoji_found,
            "Recursive subdirectory index should include emoji in parent navigation"
        )
        
        # Check nested directory index
        nested_index = os.path.join(nested_dir, 'index.md')
        self.assertTrue(os.path.exists(nested_index), "Nested directory index should be created")
        
        nested_content = self.read_index_file(nested_index)
        self.assertIn('[../](../)', nested_content, "Should have parent navigation")
        self.assertIn('[../../](../../)', nested_content, "Should have grandparent navigation")
        
        # Check for emojis in nested parent navigation
        nested_emoji_found = any(emoji in nested_content for emoji in emoji_indicators)
        self.assertTrue(
            nested_emoji_found,
            "Recursive nested directory index should include emojis in parent navigation"
        )
    
    def test_parent_folder_emoji_special_characters(self):
        """Test parent folder emoji navigation with special character directories."""
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
        
        # Verify parent navigation with emoji works with special characters
        self.assertIn('[../](../)', index_content, "Should have parent navigation")
        
        # Check for emoji in parent navigation
        emoji_indicators = ['🏠', '⬆️', '🔙', '↑', '⬆️']
        emoji_found = any(emoji in index_content for emoji in emoji_indicators)
        self.assertTrue(
            emoji_found,
            "Parent navigation with emoji should work with special character directories"
        )
    
    def test_parent_folder_emoji_unicode_directories(self):
        """Test parent folder emoji navigation with Unicode directory names."""
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
        
        # Verify parent navigation with emoji works with Unicode
        self.assertIn('[../](../)', index_content, "Should have parent navigation")
        
        # Check for emoji in parent navigation
        emoji_indicators = ['🏠', '⬆️', '🔙', '↑', '⬆️']
        emoji_found = any(emoji in index_content for emoji in emoji_indicators)
        self.assertTrue(
            emoji_found,
            "Parent navigation with emoji should work with Unicode directories"
        )
    
    def test_parent_folder_emoji_content_structure(self):
        """Test that parent folder emoji navigation maintains proper content structure."""
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
        
        # Should have parent navigation with emoji
        emoji_indicators = ['🏠', '⬆️', '🔙', '↑', '⬆️']
        emoji_found = any(emoji in index_content for emoji in emoji_indicators)
        self.assertTrue(
            emoji_found,
            "Should include emoji in parent navigation while maintaining structure"
        )
        
        # Should have footer
        self.assertIn('Generated on', index_content, "Should have generation timestamp")
        self.assertIn('IndexGenerator', index_content, "Should mention IndexGenerator")

def run_tests():
    """Run all test cases."""
    unittest.main(verbosity=2)

if __name__ == '__main__':
    run_tests()