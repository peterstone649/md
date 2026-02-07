#!/usr/bin/env python3
"""
Test case to ensure recursive flag only finds source files 
and does not create deep folder structure in output path.

This test validates that the converter maintains a flat output structure
while the recursive flag is used solely for source file discovery.

CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-02-07 | Initial test case to enforce flat output structure with recursive source discovery | Framework Steward | Ensure output directory structure remains consistent and flat regardless of source file depth |
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


class TestFlatOutputStructure(unittest.TestCase):
    """Test cases to ensure flat output structure with recursive source discovery."""
    
    def setUp(self):
        """Set up test environment with nested source directories."""
        self.temp_dir = tempfile.mkdtemp(prefix="test_converter_flat_")
        self.project_base = os.path.join(self.temp_dir, "project_base")
        
        # Create nested source directory structure
        self.nested_source_dir = os.path.join(self.project_base, "docs", "deep", "nested", "structure")
        os.makedirs(self.nested_source_dir, exist_ok=True)
        
        # Create test markdown files at different depths
        self.test_md_file1 = os.path.join(self.project_base, "root_file.md")
        self.test_md_file2 = os.path.join(self.project_base, "docs", "subdir", "level1_file.md")
        self.test_md_file3 = os.path.join(self.nested_source_dir, "deep_file.md")
        
        # Create the files
        test_files = [
            (self.test_md_file1, "# Root File\n\nThis is a root level markdown file."),
            (self.test_md_file2, "# Level 1 File\n\nThis is a level 1 markdown file."),
            (self.test_md_file3, "# Deep File\n\nThis is a deeply nested markdown file.")
        ]
        
        for file_path, content in test_files:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
    
    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_recursive_source_discovery_with_mirrored_structure(self):
        """
        Test that recursive flag discovers source files and creates mirrored output structure
        without recursive nesting of out/html directories.
        """
        # Test individual file conversion at different depths
        test_files = [self.test_md_file1, self.test_md_file2, self.test_md_file3]
        
        for source_file in test_files:
            with self.subTest(source_file=source_file):
                converter = Converter_for_Md_to_Html(source_file, self.project_base)
                success = converter.convert()
                self.assertTrue(success, f"Conversion should succeed for {source_file}")
                
                # Get the output path
                output_path = converter.generate_for_html_path()
                output_dir = os.path.dirname(output_path)
                
                # Verify output is under the correct root: project_base/out/html/
                expected_output_root = os.path.join(self.project_base, "out", "html")
                self.assertTrue(output_dir.startswith(expected_output_root), 
                               f"Output should be under {expected_output_root}, got: {output_dir}")
                
                # Verify the structure mirrors the source structure relative to project_base
                source_rel = os.path.relpath(source_file, self.project_base)
                output_rel = os.path.relpath(output_path, expected_output_root)
                
                # The output should mirror the source structure (without .md extension)
                expected_output_rel = os.path.splitext(source_rel)[0]
                self.assertEqual(output_rel, expected_output_rel, 
                               f"Output structure should mirror source structure. Expected: {expected_output_rel}, Got: {output_rel}")
    
    def test_recursive_directory_conversion_flat_output(self):
        """
        Test that recursive conversion of directory maintains flat output structure.
        """
        # Simulate recursive conversion by converting all files
        source_files = [self.test_md_file1, self.test_md_file2, self.test_md_file3]
        output_paths = []
        
        for source_file in source_files:
            converter = Converter_for_Md_to_Html(source_file, self.project_base)
            success = converter.convert()
            self.assertTrue(success, f"Conversion should succeed for {source_file}")
            
            output_path = converter.generate_for_html_path()
            output_paths.append(output_path)
        
        # Verify all outputs are under the same flat structure
        expected_output_root = os.path.join(self.project_base, "out", "html")
        
        for output_path in output_paths:
            output_dir = os.path.dirname(output_path)
            self.assertTrue(output_dir.startswith(expected_output_root), 
                           f"All outputs should be under {expected_output_root}")
            
            # Verify no deep nesting
            relative_output = os.path.relpath(output_dir, expected_output_root)
            if relative_output != '.':
                path_parts = relative_output.split(os.sep)
                self.assertLessEqual(len(path_parts), 1, 
                                   f"Output should be flat, found nesting: {relative_output}")
    
    def test_output_structure_consistency(self):
        """
        Test that output structure is consistent regardless of source file depth.
        """
        source_files = [self.test_md_file1, self.test_md_file2, self.test_md_file3]
        output_dirs = []
        
        for source_file in source_files:
            converter = Converter_for_Md_to_Html(source_file, self.project_base)
            output_path = converter.generate_for_html_path()
            output_dirs.append(os.path.dirname(output_path))
        
        # All outputs should be under the same root
        expected_output_root = os.path.join(self.project_base, "out", "html")
        
        for output_dir in output_dirs:
            self.assertTrue(output_dir.startswith(expected_output_root), 
                           f"Output should be under {expected_output_root}")
        
        # Verify the depth is consistent (all should be at same level or root)
        depths = []
        for output_dir in output_dirs:
            relative_path = os.path.relpath(output_dir, expected_output_root)
            if relative_path == '.':
                depth = 0
            else:
                depth = len(relative_path.split(os.sep))
            depths.append(depth)
        
        # All depths should be 0 (root level) or at most 1 (one subdirectory level)
        for depth in depths:
            self.assertLessEqual(depth, 1, 
                               f"Output depth should be at most 1, found depth: {depth}")
    
    def test_file_naming_preserves_uniqueness(self):
        """
        Test that files with same name at different depths get unique output names.
        """
        # Create files with same name at different depths
        file1_path = os.path.join(self.project_base, "test.md")
        file2_path = os.path.join(self.project_base, "docs", "test.md")
        file3_path = os.path.join(self.nested_source_dir, "test.md")
        
        for file_path in [file1_path, file2_path, file3_path]:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# Test File in {os.path.dirname(file_path)}\n\nContent.")
        
        # Convert all files
        output_paths = []
        for source_file in [file1_path, file2_path, file3_path]:
            converter = Converter_for_Md_to_Html(source_file, self.project_base)
            output_path = converter.generate_for_html_path()
            output_paths.append(output_path)
        
        # All output paths should be unique
        self.assertEqual(len(output_paths), len(set(output_paths)), 
                        "All output paths should be unique")
        
        # All should be under flat structure
        expected_output_root = os.path.join(self.project_base, "out", "html")
        for output_path in output_paths:
            output_dir = os.path.dirname(output_path)
            self.assertTrue(output_dir.startswith(expected_output_root), 
                           f"Output should be under {expected_output_root}")


def run_tests():
    """Run the test suite."""
    print("Running tests to ensure flat output structure with recursive source discovery...")
    print("=" * 80)
    
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFlatOutputStructure)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 80)
    if result.wasSuccessful():
        print("All tests passed! Recursive flag only affects source discovery, not output structure.")
        return True
    else:
        print("Some tests failed! Output structure may not be flat.")
        return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)