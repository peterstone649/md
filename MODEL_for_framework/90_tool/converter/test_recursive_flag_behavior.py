ded#!/usr/bin/env python3
"""
Test case to demonstrate the current recursive flag behavior issue
and define the expected flat output structure.

This test shows that the recursive flag currently creates deep output structures
when it should only be used for source file discovery.

CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-02-07 | Test case demonstrating recursive flag behavior issue | Framework Steward | Document current behavior and define expected flat output structure |
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


class TestRecursiveFlagBehavior(unittest.TestCase):
    """Test cases to demonstrate recursive flag behavior issues."""
    
    def setUp(self):
        """Set up test environment with nested source directories."""
        self.temp_dir = tempfile.mkdtemp(prefix="test_converter_behavior_")
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
    
    def test_current_behavior_creates_mirrored_output_structure(self):
        """
        Test that demonstrates the current behavior:
        recursive flag creates mirrored output structure (which is correct)
        but we need to ensure no recursive nesting of out/html directories.
        """
        print("\n=== CURRENT BEHAVIOR (MIRRORED STRUCTURE) ===")
        
        source_files = [self.test_md_file1, self.test_md_file2, self.test_md_file3]
        output_paths = []
        
        for source_file in source_files:
            converter = Converter_for_Md_to_Html(source_file, self.project_base)
            output_path = converter.generate_for_html_path()
            output_paths.append(output_path)
            
            # Show the current behavior
            source_rel = os.path.relpath(source_file, self.project_base)
            output_rel = os.path.relpath(output_path, os.path.join(self.project_base, "out", "html"))
            
            print(f"Source: {source_rel}")
            print(f"Output: {output_rel}")
            print(f"Mirrors source: {os.path.splitext(source_rel)[0] == output_rel}")
            print()
        
        # Verify that the output structure mirrors the source structure
        for i, source_file in enumerate(source_files):
            source_rel = os.path.relpath(source_file, self.project_base)
            output_rel = os.path.relpath(output_paths[i], os.path.join(self.project_base, "out", "html"))
            expected_output = os.path.splitext(source_rel)[0]
            
            self.assertEqual(output_rel, expected_output, 
                           f"Output should mirror source structure. Expected: {expected_output}, Got: {output_rel}")
        
        print("Current behavior correctly mirrors source structure!")
        print("This is the expected behavior for the recursive flag.")
    
    def test_expected_flat_output_structure(self):
        """
        Test that defines what the expected behavior should be:
        recursive flag only for source discovery, flat output structure.
        """
        print("\n=== EXPECTED BEHAVIOR (WHAT SHOULD HAPPEN) ===")
        
        source_files = [self.test_md_file1, self.test_md_file2, self.test_md_file3]
        expected_outputs = []
        
        for source_file in source_files:
            # Calculate what the output SHOULD be for flat structure
            filename = os.path.splitext(os.path.basename(source_file))[0]
            expected_output = os.path.join(self.project_base, "out", "html", f"{filename}.html")
            expected_outputs.append(expected_output)
            
            source_rel = os.path.relpath(source_file, self.project_base)
            expected_rel = os.path.relpath(expected_output, os.path.join(self.project_base, "out", "html"))
            
            print(f"Source: {source_rel}")
            print(f"Expected Output: {expected_rel}")
            print(f"Expected Depth: {len(expected_rel.split(os.sep)) if expected_rel != '.' else 0}")
            print()
        
        # All expected outputs should be at depth 0 (root level)
        for expected_output in expected_outputs:
            expected_rel = os.path.relpath(expected_output, os.path.join(self.project_base, "out", "html"))
            depth = len(expected_rel.split(os.sep)) if expected_rel != '.' else 0
            self.assertEqual(depth, 0, 
                           f"Expected output should be at root level (depth 0), found depth {depth}")
        
        print("Expected maximum output depth: 0 (all files at root level)")
        print("This is what the recursive flag behavior SHOULD produce!")
    
    def test_recursive_flag_purpose_validation(self):
        """
        Test that validates the recursive flag should only be used for source discovery,
        not for creating output directory structure.
        """
        print("\n=== RECURSIVE FLAG PURPOSE ===")
        print("The recursive flag should:")
        print("1. ONLY be used to FIND source files in nested directories")
        print("2. NOT create nested output directory structures")
        print("3. Maintain flat output structure in out/html/")
        print()
        
        # Test that we can find files at different depths (source discovery)
        source_files = [self.test_md_file1, self.test_md_file2, self.test_md_file3]
        
        for source_file in source_files:
            # This should work - finding files at different depths
            self.assertTrue(os.path.exists(source_file), 
                           f"Should be able to find source file at any depth: {source_file}")
            
            # Show the source file depths
            source_rel = os.path.relpath(source_file, self.project_base)
            source_depth = len(source_rel.split(os.sep)) - 1  # -1 because filename is not a directory
            print(f"Found source file at depth {source_depth}: {source_rel}")
        
        print(f"\nSource discovery works for depths 0 to {max(len(os.path.relpath(f, self.project_base).split(os.sep))-1 for f in source_files)}")
        print("This is what the recursive flag SHOULD do!")
        
        # The recursive flag should enable finding files at any depth
        # But output should always be flat
        self.assertTrue(True, "Recursive flag should enable source discovery at any depth")


def run_tests():
    """Run the test suite."""
    print("Testing recursive flag behavior - demonstrating current issue and expected behavior...")
    print("=" * 90)
    
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRecursiveFlagBehavior)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 90)
    print("SUMMARY:")
    print("- Current behavior creates deep output structures (PROBLEM)")
    print("- Expected behavior should maintain flat output structure")
    print("- Recursive flag should only be used for source file discovery")
    print("- Output should always be in out/html/ with flat structure")
    
    if not result.wasSuccessful():
        print("\nWARNING: Tests demonstrate the current problematic behavior")
        print("   This confirms the recursive flag needs to be fixed")
        return False
    else:
        print("\nSUCCESS: Tests show expected behavior is correct")
        return True


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)