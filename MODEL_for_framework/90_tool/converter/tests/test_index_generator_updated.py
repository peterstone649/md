#!/usr/bin/env python3
"""
Updated test cases for Index Generator with ManagerForDirOTBase integration.

This test suite covers the new dual output path behavior:
- MD files created in the same folder as README files
- HTML files created in <PROJECT_BASE_PATH>/out/html directory
- ManagerForDirOTBase integration for consistent path handling

CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-01-31 | Initial creation of comprehensive test suite for updated index_generator.py | Framework Steward | Ensure proper testing of dual output path behavior and ManagerForDirOTBase integration |
"""

import os
import sys
import unittest
import tempfile
import shutil
from pathlib import Path

# Add the converter directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'converter'))

try:
    from index_generator import IndexGenerator, generate_index_for_folder
    from manager_for_dir_OT_base import ManagerForDirOTBase
except ImportError as e:
    # Try alternative import paths
    try:
        # Try importing from parent directory
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
        from index_generator import IndexGenerator, generate_index_for_folder
        from manager_for_dir_OT_base import ManagerForDirOTBase
    except ImportError as e2:
        print(f"ERROR: Could not import required modules: {e}")
        print(f"ERROR: Alternative import also failed: {e2}")
        sys.exit(1)


class TestIndexGeneratorUpdated(unittest.TestCase):
    """Test class for updated index_generator.py with dual output paths."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp()
        self.original_dir = os.getcwd()
        
    def tearDown(self):
        """Clean up test environment."""
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_dual_output_path_behavior(self):
        """Test that MD files go to source folder and HTML files go to out/html."""
        # Create test directory with README file
        test_folder = os.path.join(self.test_dir, "test_folder")
        os.makedirs(test_folder)
        
        # Create README file to trigger index generation
        readme_path = os.path.join(test_folder, "README.md")
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write("# Test README\nThis is a test README file.")
        
        # Create some test files
        test_files = ["file1.md", "file2.txt", "script.py"]
        for filename in test_files:
            file_path = os.path.join(test_folder, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# {filename}\nContent for {filename}")
        
        # Test with both formats
        generator = IndexGenerator(project_base=self.test_dir)
        result = generator.create_index_files(test_folder, format='both')
        
        self.assertTrue(result, "Index generation should succeed")
        
        # Check MD file is in source folder
        md_index_path = os.path.join(test_folder, "index.md")
        self.assertTrue(os.path.exists(md_index_path), 
                       "MD index should be created in source folder")
        
        # Check HTML file is in out/html directory
        expected_html_path = os.path.join(self.test_dir, "out", "html", "test_folder", "index.html")
        self.assertTrue(os.path.exists(expected_html_path), 
                       "HTML index should be created in out/html directory")
        
        # Verify content of both files
        with open(md_index_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            self.assertIn("README.md", md_content, "MD index should reference README")
            self.assertIn("file1.md", md_content, "MD index should list markdown files")
        
        with open(expected_html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            self.assertIn("<!DOCTYPE html>", html_content, "HTML index should have HTML structure")
            self.assertIn("README.md", html_content, "HTML index should reference README")
            self.assertIn("file1.md", html_content, "HTML index should list markdown files")
    
    def test_html_only_output_path(self):
        """Test that HTML files go to out/html directory when format is 'html' only."""
        test_folder = os.path.join(self.test_dir, "test_folder")
        os.makedirs(test_folder)
        
        # Create README file
        readme_path = os.path.join(test_folder, "README.md")
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write("# Test README")
        
        generator = IndexGenerator(project_base=self.test_dir)
        result = generator.create_index_files(test_folder, format='html')
        
        self.assertTrue(result, "HTML index generation should succeed")
        
        # Check HTML file is in out/html directory
        expected_html_path = os.path.join(self.test_dir, "out", "html", "test_folder", "index.html")
        self.assertTrue(os.path.exists(expected_html_path), 
                       "HTML index should be created in out/html directory")
        
        # MD file should NOT exist in source folder
        md_index_path = os.path.join(test_folder, "index.md")
        self.assertFalse(os.path.exists(md_index_path), 
                        "MD index should not be created when format is 'html' only")
    
    def test_md_only_output_path(self):
        """Test that MD files go to source folder when format is 'md' only."""
        test_folder = os.path.join(self.test_dir, "test_folder")
        os.makedirs(test_folder)
        
        # Create README file
        readme_path = os.path.join(test_folder, "README.md")
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write("# Test README")
        
        generator = IndexGenerator(project_base=self.test_dir)
        result = generator.create_index_files(test_folder, format='md')
        
        self.assertTrue(result, "MD index generation should succeed")
        
        # Check MD file is in source folder
        md_index_path = os.path.join(test_folder, "index.md")
        self.assertTrue(os.path.exists(md_index_path), 
                       "MD index should be created in source folder")
        
        # HTML file should NOT exist in out/html directory
        expected_html_path = os.path.join(self.test_dir, "out", "html", "test_folder", "index.html")
        self.assertFalse(os.path.exists(expected_html_path), 
                        "HTML index should not be created when format is 'md' only")
    
    def test_no_readme_skips_md_generation(self):
        """Test that MD generation is skipped when no README file exists."""
        test_folder = os.path.join(self.test_dir, "test_folder")
        os.makedirs(test_folder)
        
        # Create test files but NO README
        test_files = ["file1.md", "file2.txt"]
        for filename in test_files:
            file_path = os.path.join(test_folder, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# {filename}\nContent")
        
        generator = IndexGenerator(project_base=self.test_dir)
        result = generator.create_index_files(test_folder, format='both')
        
        self.assertTrue(result, "Index generation should succeed even without README")
        
        # MD file should NOT be created (no README)
        md_index_path = os.path.join(test_folder, "index.md")
        self.assertFalse(os.path.exists(md_index_path), 
                        "MD index should not be created without README")
        
        # HTML file should still be created in out/html directory
        expected_html_path = os.path.join(self.test_dir, "out", "html", "test_folder", "index.html")
        self.assertTrue(os.path.exists(expected_html_path), 
                       "HTML index should be created even without README")
    
    def test_manager_for_dir_ot_base_integration(self):
        """Test integration with ManagerForDirOTBase for path handling."""
        # Test with custom project base
        custom_base = os.path.join(self.test_dir, "custom_base")
        os.makedirs(custom_base)
        
        test_folder = os.path.join(custom_base, "test_folder")
        os.makedirs(test_folder)
        
        # Create README file
        readme_path = os.path.join(test_folder, "README.md")
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write("# Test README")
        
        generator = IndexGenerator(project_base=custom_base)
        
        # Verify the directory manager is properly initialized
        self.assertIsInstance(generator.dir_manager, ManagerForDirOTBase)
        self.assertEqual(generator.dir_manager.get_project_base(), custom_base)
        
        # Test path generation
        html_path = generator.dir_manager.generate_html_path(os.path.join(test_folder, "index.html"))
        expected_path = os.path.join(custom_base, "out", "html", "test_folder", "index.html")
        self.assertEqual(html_path, expected_path, "HTML path should be generated correctly")
        
        # Test directory creation
        generator.dir_manager.ensure_output_directory(html_path)
        output_dir = os.path.dirname(html_path)
        self.assertTrue(os.path.exists(output_dir), "Output directory should be created")
    
    def test_generate_index_for_folder_function(self):
        """Test the generate_index_for_folder function with new signature."""
        test_folder = os.path.join(self.test_dir, "test_folder")
        os.makedirs(test_folder)
        
        # Create README file
        readme_path = os.path.join(test_folder, "README.md")
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write("# Test README")
        
        # Test with project_base parameter
        result = generate_index_for_folder(test_folder, format='both', project_base=self.test_dir)
        
        self.assertTrue(result, "Function should return True on success")
        
        # Verify files are created in correct locations
        md_index_path = os.path.join(test_folder, "index.md")
        expected_html_path = os.path.join(self.test_dir, "out", "html", "test_folder", "index.html")
        
        self.assertTrue(os.path.exists(md_index_path), "MD index should be created")
        self.assertTrue(os.path.exists(expected_html_path), "HTML index should be created")
    
    def test_recursive_processing(self):
        """Test recursive processing of subdirectories."""
        # Create nested directory structure
        root_folder = os.path.join(self.test_dir, "root")
        subfolder1 = os.path.join(root_folder, "sub1")
        subfolder2 = os.path.join(root_folder, "sub2")
        nested_folder = os.path.join(subfolder1, "nested")
        
        for folder in [root_folder, subfolder1, subfolder2, nested_folder]:
            os.makedirs(folder)
            # Create README in each folder
            readme_path = os.path.join(folder, "README.md")
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(f"# README for {os.path.basename(folder)}")
        
        generator = IndexGenerator(project_base=self.test_dir)
        result = generator.create_index_files(root_folder, format='both', recursive=True)
        
        self.assertTrue(result, "Recursive index generation should succeed")
        
        # Check that index files were created in all directories
        for folder in [root_folder, subfolder1, subfolder2, nested_folder]:
            # MD file in source folder
            md_path = os.path.join(folder, "index.md")
            self.assertTrue(os.path.exists(md_path), f"MD index should exist in {folder}")
            
            # HTML file in out/html directory
            rel_path = os.path.relpath(folder, self.test_dir)
            html_path = os.path.join(self.test_dir, "out", "html", rel_path, "index.html")
            self.assertTrue(os.path.exists(html_path), f"HTML index should exist for {folder}")
    
    def test_environment_configuration(self):
        """Test environment-based configuration support."""
        # Test with environment variable
        os.environ['PROJECT_BASE_PATH'] = self.test_dir
        
        test_folder = os.path.join(self.test_dir, "test_folder")
        os.makedirs(test_folder)
        
        readme_path = os.path.join(test_folder, "README.md")
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write("# Test README")
        
        # Create generator without explicit project_base (should use env var)
        generator = IndexGenerator()
        
        # Verify it uses the environment variable
        self.assertEqual(generator.dir_manager.get_project_base(), self.test_dir)
        
        result = generator.create_index_files(test_folder, format='both')
        self.assertTrue(result)
        
        # Verify files are created in correct locations
        md_index_path = os.path.join(test_folder, "index.md")
        expected_html_path = os.path.join(self.test_dir, "out", "html", "test_folder", "index.html")
        
        self.assertTrue(os.path.exists(md_index_path))
        self.assertTrue(os.path.exists(expected_html_path))
        
        # Clean up environment variable
        del os.environ['PROJECT_BASE_PATH']
    
    def test_error_handling(self):
        """Test error handling for various edge cases."""
        generator = IndexGenerator(project_base=self.test_dir)
        
        # Test with non-existent folder
        result = generator.create_index_files("nonexistent_folder", format='both')
        self.assertFalse(result, "Should return False for non-existent folder")
        
        # Test with file instead of directory
        test_file = os.path.join(self.test_dir, "test.txt")
        with open(test_file, 'w') as f:
            f.write("test")
        
        result = generator.create_index_files(test_file, format='both')
        self.assertFalse(result, "Should return False for file instead of directory")
        
        # Test with invalid format
        test_folder = os.path.join(self.test_dir, "test_folder")
        os.makedirs(test_folder)
        
        readme_path = os.path.join(test_folder, "README.md")
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write("# Test README")
        
        # This should still work but only process valid formats
        generator.create_index_files(test_folder, format='invalid')
        # Should not create any files for invalid format


if __name__ == '__main__':
    unittest.main()