#!/usr/bin/env python3
"""
Test Cases for AI_LOCK Handling in Index Generator

This test suite validates that the index_generator.py tool properly handles
AI_LOCK and AI_UNLOCK tags when processing README files for index generation.

Test Cases:
1. Basic AI_LOCK handling in README files
2. AI_LOCK with multiple sections in README
3. AI_LOCK with special characters and formatting
4. AI_LOCK with nested markdown elements
5. AI_LOCK preservation in index generation
6. AI_LOCK with large README content
7. AI_LOCK with Unicode content
8. AI_LOCK edge cases and error handling

CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-02-01 | Initial test suite implementation for AI_LOCK handling in index generator | Framework Steward | Ensure AI_LOCK sections are properly preserved and handled during index generation |
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

class TestAILockHandling(unittest.TestCase):
    """Test cases for AI_LOCK/AI_UNLOCK tag handling in index generator."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp(prefix='ai_lock_test_')
        self.generator = IndexGenerator(self.test_dir)
        
    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)
    
    def create_test_readme(self, content, filename="README.md"):
        """Create a test README file with the given content."""
        readme_path = os.path.join(self.test_dir, filename)
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return readme_path
    
    def read_index_file(self, index_path):
        """Read and return the content of an index file."""
        with open(index_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def test_ai_lock_basic_handling(self):
        """Test basic AI_LOCK/AI_UNLOCK handling in README files."""
        readme_content = """# Test Directory
        
This is a test directory with AI_LOCK content.
        
[AI_LOCK] This is important content that should be preserved [AI_UNLOCK]
        
Regular content continues here."""
        
        self.create_test_readme(readme_content)
        
        # Generate index for the directory
        self.generator.create_index_files(self.test_dir, format='md')
        
        index_path = os.path.join(self.test_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify that the README is featured in the index
        self.assertIn('📁 README.md', index_content, "README should be featured in index")
        self.assertIn('Jump to main documentation', index_content, "README should have jump description")
    
    def test_ai_lock_multiple_sections(self):
        """Test AI_LOCK with multiple sections in README files."""
        readme_content = """# Test Directory
        
[AI_LOCK] First important section [AI_UNLOCK]
        
Regular content.
        
[AI_LOCK] Second important section [AI_UNLOCK]
        
More regular content.
        
[AI_LOCK] Third important section [AI_UNLOCK]""" * 3
        
        self.create_test_readme(readme_content)
        
        # Generate index for the directory
        self.generator.create_index_files(self.test_dir, format='md')
        
        index_path = os.path.join(self.test_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify that the README is featured in the index
        self.assertIn('📁 README.md', index_content, "README should be featured in index")
        self.assertIn('Jump to main documentation', index_content, "README should have jump description")
    
    def test_ai_lock_with_special_characters(self):
        """Test AI_LOCK with special characters and formatting in README."""
        special_content = """# Test Directory
        
[AI_LOCK] Content with **bold** and *italic* text [AI_UNLOCK]
        
[AI_LOCK] Content with `inline code` and [links](http://example.com) [AI_UNLOCK]
        
[AI_LOCK] Content with special chars: !@#$%^&*()<>\"'{}[]|\\/? [AI_UNLOCK]"""
        
        self.create_test_readme(special_content)
        
        # Generate index for the directory
        self.generator.create_index_files(self.test_dir, format='md')
        
        index_path = os.path.join(self.test_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify that the README is featured in the index
        self.assertIn('📁 README.md', index_content, "README should be featured in index")
        self.assertIn('Jump to main documentation', index_content, "README should have jump description")
    
    def test_ai_lock_with_nested_elements(self):
        """Test AI_LOCK with nested markdown elements in README."""
        nested_content = """# Test Directory
        
[AI_LOCK] 
## Important Section
        
- List item 1
- List item 2 with **bold** text
        
> Blockquote content
        
```python
def important_function():
    pass
```
[AI_UNLOCK]
        
Regular content continues."""
        
        self.create_test_readme(nested_content)
        
        # Generate index for the directory
        self.generator.create_index_files(self.test_dir, format='md')
        
        index_path = os.path.join(self.test_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify that the README is featured in the index
        self.assertIn('📁 README.md', index_content, "README should be featured in index")
        self.assertIn('Jump to main documentation', index_content, "README should have jump description")
    
    def test_ai_lock_preservation_in_index(self):
        """Test that AI_LOCK sections are preserved during index generation."""
        readme_content = """# Test Directory
        
[AI_LOCK] Critical information that must be preserved [AI_UNLOCK]
        
Regular documentation content.
        
[AI_LOCK] Another important section [AI_UNLOCK]"""
        
        self.create_test_readme(readme_content)
        
        # Generate index for the directory
        self.generator.create_index_files(self.test_dir, format='md')
        
        index_path = os.path.join(self.test_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify that the index contains the README link
        self.assertIn('📁 README.md', index_content, "README should be featured in index")
        self.assertIn('Jump to main documentation', index_content, "README should have jump description")
        
        # The index should not contain the actual AI_LOCK content, just reference to README
        self.assertNotIn('Critical information that must be preserved', index_content, 
                        "Index should not contain actual AI_LOCK content")
    
    def test_ai_lock_with_large_content(self):
        """Test AI_LOCK handling with large README content."""
        large_content = "# Test Directory\n\n"
        
        for i in range(20):
            large_content += f"""
## Section {i + 1}
            
[AI_LOCK] Important content for section {i + 1} [AI_UNLOCK]
            
Regular content for section {i + 1}.
            
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            """
        
        self.create_test_readme(large_content)
        
        # Generate index for the directory
        self.generator.create_index_files(self.test_dir, format='md')
        
        index_path = os.path.join(self.test_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify that the README is featured in the index
        self.assertIn('📁 README.md', index_content, "README should be featured in index")
        self.assertIn('Jump to main documentation', index_content, "README should have jump description")
    
    def test_ai_lock_with_unicode_content(self):
        """Test AI_LOCK with Unicode content in README."""
        unicode_content = """# Test Directory
        
[AI_LOCK] Unicode content: 你好世界 🌍 🚀 📱 ñáéíóú üöä €£¥₹ [AI_UNLOCK]
        
[AI_LOCK] More Unicode: Ελληνικά العربية русский עברית [AI_UNLOCK]
        
Regular content with Unicode: 🎉🎊🎈""" * 5
        
        self.create_test_readme(unicode_content)
        
        # Generate index for the directory
        self.generator.create_index_files(self.test_dir, format='md')
        
        index_path = os.path.join(self.test_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify that the README is featured in the index
        self.assertIn('📁 README.md', index_content, "README should be featured in index")
        self.assertIn('Jump to main documentation', index_content, "README should have jump description")
    
    def test_ai_lock_edge_cases(self):
        """Test AI_LOCK edge cases in README files."""
        edge_cases_content = """# Test Directory
        
[AI_LOCK] Empty content [AI_UNLOCK]
        
[AI_LOCK]   [AI_UNLOCK]  <!-- Whitespace only -->
        
[AI_LOCK]Multiple   spaces   here[AI_UNLOCK]
        
[AI_LOCK]
Multi-line
content
[AI_UNLOCK]
        
[AI_LOCK]Content with [nested] brackets [AI_UNLOCK]"""
        
        self.create_test_readme(edge_cases_content)
        
        # Generate index for the directory
        self.generator.create_index_files(self.test_dir, format='md')
        
        index_path = os.path.join(self.test_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path), "Index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify that the README is featured in the index
        self.assertIn('📁 README.md', index_content, "README should be featured in index")
        self.assertIn('Jump to main documentation', index_content, "README should have jump description")
    
    def test_ai_lock_html_format(self):
        """Test AI_LOCK handling in HTML index generation."""
        readme_content = """# Test Directory
        
[AI_LOCK] Important HTML content [AI_UNLOCK]
        
Regular content for HTML test."""
        
        self.create_test_readme(readme_content)
        
        # Generate HTML index for the directory
        self.generator.create_index_files(self.test_dir, format='html')
        
        # HTML files go to standardized output directory
        from manager_for_dir_OT_base import ManagerForDirOTBase
        dir_manager = ManagerForDirOTBase(self.test_dir)
        html_path = dir_manager.generate_html_path(os.path.join(self.test_dir, 'index.html'))
        index_path = Path(html_path)
        
        self.assertTrue(index_path.exists(), "HTML index file should be created")
        
        index_content = self.read_index_file(index_path)
        
        # Verify that the README is featured in the HTML index
        self.assertIn('📁 <a href="README.md">README.md</a>', index_content, "README should be featured in HTML index")
        self.assertIn('Jump to main documentation', index_content, "README should have jump description in HTML")
    
    def test_ai_lock_with_no_readme(self):
        """Test that index generation works correctly when no README exists (AI_LOCK not relevant)."""
        # Create a file that's not README
        other_file = os.path.join(self.test_dir, "other.md")
        with open(other_file, 'w', encoding='utf-8') as f:
            f.write("# Other File\n\nContent without AI_LOCK.")
        
        # Generate index for the directory
        self.generator.create_index_files(self.test_dir, format='md')
        
        index_path = os.path.join(self.test_dir, 'index.md')
        # Index should NOT be created when no README exists
        self.assertFalse(os.path.exists(index_path), "Index file should NOT be created when no README exists")

def run_tests():
    """Run all test cases."""
    unittest.main(verbosity=2)

if __name__ == '__main__':
    run_tests()