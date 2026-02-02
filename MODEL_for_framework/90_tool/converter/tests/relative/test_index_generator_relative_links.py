#!/usr/bin/env python3
"""
Test cases for relative link generation in index_generator.py.

This module tests that the index generator creates relative links instead of absolute paths,
ensuring portability and cross-platform compatibility.
"""

import unittest
import tempfile
import os
import shutil
from pathlib import Path

# Import the index generator module
from index_generator import IndexGenerator

__version__ = "1.0.0"
__status__ = "ACTIVE"

"""
CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-02-01 | Initial creation of relative links test cases for index_generator | Framework Steward | Establish comprehensive test coverage for relative link generation in index files |
"""


class TestIndexGeneratorRelativeLinks(unittest.TestCase):
    """Test cases for relative link generation in index_generator.py."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.temp_dir = tempfile.mkdtemp()
        self.generator = IndexGenerator(self.temp_dir)

    def tearDown(self):
        """Clean up after each test method."""
        shutil.rmtree(self.temp_dir)

    def create_test_structure(self):
        """Create a test directory structure with files and subdirectories."""
        # Create main directory with files
        main_dir = os.path.join(self.temp_dir, "main")
        os.makedirs(main_dir, exist_ok=True)

        # Create files in main directory
        with open(os.path.join(main_dir, "README.md"), 'w') as f:
            f.write("# Main Directory\n\nThis is the main directory.")
        with open(os.path.join(main_dir, "file1.md"), 'w') as f:
            f.write("# File 1\n\nContent of file 1.")
        with open(os.path.join(main_dir, "file2.md"), 'w') as f:
            f.write("# File 2\n\nContent of file 2.")

        # Create subdirectory with files
        sub_dir = os.path.join(main_dir, "subdir")
        os.makedirs(sub_dir, exist_ok=True)

        with open(os.path.join(sub_dir, "README.md"), 'w') as f:
            f.write("# Sub Directory\n\nThis is a subdirectory.")
        with open(os.path.join(sub_dir, "subfile1.md"), 'w') as f:
            f.write("# Sub File 1\n\nContent of sub file 1.")

        # Create nested subdirectory
        nested_dir = os.path.join(sub_dir, "nested")
        os.makedirs(nested_dir, exist_ok=True)

        with open(os.path.join(nested_dir, "README.md"), 'w') as f:
            f.write("# Nested Directory\n\nThis is a nested directory.")
        with open(os.path.join(nested_dir, "nestedfile.md"), 'w') as f:
            f.write("# Nested File\n\nContent of nested file.")

        return main_dir, sub_dir, nested_dir

    def read_index_file(self, index_path):
        """Read and return the content of an index file."""
        with open(index_path, 'r', encoding='utf-8') as f:
            return f.read()

    def test_relative_links_in_main_directory(self):
        """Test that main directory index uses relative links."""
        main_dir, _, _ = self.create_test_structure()

        # Generate index for main directory
        self.generator.create_index_files(main_dir, format='md')

        index_path = os.path.join(main_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path))

        index_content = self.read_index_file(index_path)

        # Check that links are relative (no absolute paths)
        self.assertIn('[file1.md](file1.md)', index_content)
        self.assertIn('[file2.md](file2.md)', index_content)
        self.assertIn('[subdir/](subdir/)', index_content)

        # Ensure no absolute paths are present
        self.assertNotIn(self.temp_dir, index_content)

    def test_relative_links_in_subdirectory(self):
        """Test that subdirectory index uses relative links."""
        _, sub_dir, _ = self.create_test_structure()

        # Generate index for subdirectory
        self.generator.create_index_files(sub_dir, format='md')

        index_path = os.path.join(sub_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path))

        index_content = self.read_index_file(index_path)

        # Check that links are relative
        self.assertIn('[subfile1.md](subfile1.md)', index_content)
        self.assertIn('[nested/](nested/)', index_content)

        # Check that parent directory links use relative paths
        self.assertIn('[../](../)', index_content)

        # Ensure no absolute paths are present
        self.assertNotIn(self.temp_dir, index_content)

    def test_relative_links_in_nested_directory(self):
        """Test that nested directory index uses relative links."""
        _, _, nested_dir = self.create_test_structure()

        # Generate index for nested directory
        self.generator.create_index_files(nested_dir, format='md')

        index_path = os.path.join(nested_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path))

        index_content = self.read_index_file(index_path)

        # Check that links are relative
        self.assertIn('[nestedfile.md](nestedfile.md)', index_content)

        # Check that parent directory links use relative paths
        self.assertIn('[../](../)', index_content)
        self.assertIn('[../../](../../)', index_content)

        # Ensure no absolute paths are present
        self.assertNotIn(self.temp_dir, index_content)

    def test_relative_links_with_recursive_generation(self):
        """Test relative links when generating indexes recursively."""
        main_dir, _, _ = self.create_test_structure()

        # Generate indexes recursively
        self.generator.create_index_files(main_dir, format='md', recursive=True)

        # Check main directory index
        main_index = os.path.join(main_dir, 'index.md')
        self.assertTrue(os.path.exists(main_index))
        main_content = self.read_index_file(main_index)

        self.assertIn('[subdir/](subdir/)', main_content)
        self.assertNotIn(self.temp_dir, main_content)

        # Check subdirectory index
        sub_index = os.path.join(main_dir, 'subdir', 'index.md')
        self.assertTrue(os.path.exists(sub_index))
        sub_content = self.read_index_file(sub_index)

        self.assertIn('[nested/](nested/)', sub_content)
        self.assertIn('[../](../)', sub_content)
        self.assertNotIn(self.temp_dir, sub_content)

        # Check nested directory index
        nested_index = os.path.join(main_dir, 'subdir', 'nested', 'index.md')
        self.assertTrue(os.path.exists(nested_index))
        nested_content = self.read_index_file(nested_index)

        self.assertIn('[../](../)', nested_content)
        self.assertIn('[../../](../../)', nested_content)
        self.assertNotIn(self.temp_dir, nested_content)

    def test_relative_links_with_deep_nesting(self):
        """Test relative links with deeply nested directory structures."""
        # Create deeply nested structure
        deep_dir = self.temp_dir
        path_parts = ['level1', 'level2', 'level3', 'level4', 'level5']
        current_path = deep_dir

        for part in path_parts:
            current_path = os.path.join(current_path, part)
            os.makedirs(current_path, exist_ok=True)

            # Create README in each level
            with open(os.path.join(current_path, 'README.md'), 'w') as f:
                f.write(f"# {part}\n\nThis is {part}.")

        # Generate index for deepest directory
        self.generator.create_index_files(current_path, format='md')

        index_path = os.path.join(current_path, 'index.md')
        self.assertTrue(os.path.exists(index_path))

        index_content = self.read_index_file(index_path)

        # Check that parent links use correct relative paths
        self.assertIn('[../](../)', index_content)
        self.assertIn('[../../](../../)', index_content)
        self.assertIn('[../../../](../../../)', index_content)
        self.assertIn('[../../../../](../../../../)', index_content)
        self.assertIn('[../../../../../](../../../../../)', index_content)

        # Ensure no absolute paths
        self.assertNotIn(self.temp_dir, index_content)

    def test_relative_links_with_special_characters(self):
        """Test relative links with directories and files containing special characters."""
        special_dir = os.path.join(self.temp_dir, "special dir with spaces")
        os.makedirs(special_dir, exist_ok=True)

        # Create files with special characters
        with open(os.path.join(special_dir, "README.md"), 'w') as f:
            f.write("# Special Directory\n\nThis has special characters.")
        with open(os.path.join(special_dir, "file with spaces.md"), 'w') as f:
            f.write("# File with Spaces\n\nContent.")
        with open(os.path.join(special_dir, "file-with-dashes.md"), 'w') as f:
            f.write("# File with Dashes\n\nContent.")
        with open(os.path.join(special_dir, "file_with_underscores.md"), 'w') as f:
            f.write("# File with Underscores\n\nContent.")

        # Create subdirectory with special characters
        special_sub = os.path.join(special_dir, "sub-dir with spaces")
        os.makedirs(special_sub, exist_ok=True)

        with open(os.path.join(special_sub, "README.md"), 'w') as f:
            f.write("# Special Sub Directory\n\nThis is a special subdirectory.")

        # Generate index
        self.generator.create_index_files(special_dir, format='md')

        index_path = os.path.join(special_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path))

        index_content = self.read_index_file(index_path)

        # Check that special characters are handled correctly in relative links
        self.assertIn('[file with spaces.md](file with spaces.md)', index_content)
        self.assertIn('[file-with-dashes.md](file-with-dashes.md)', index_content)
        self.assertIn('[file_with_underscores.md](file_with_underscores.md)', index_content)
        self.assertIn('[sub-dir with spaces/](sub-dir with spaces/)', index_content)

        # Check parent link
        self.assertIn('[../](../)', index_content)

        # Ensure no absolute paths
        self.assertNotIn(self.temp_dir, index_content)

    def test_relative_links_with_unicode_content(self):
        """Test relative links with Unicode directory and file names."""
        unicode_dir = os.path.join(self.temp_dir, "unicode_测试_тест_テスト")
        os.makedirs(unicode_dir, exist_ok=True)

        # Create files with Unicode names
        with open(os.path.join(unicode_dir, "README.md"), 'w') as f:
            f.write("# Unicode Directory\n\nThis has Unicode characters.")
        with open(os.path.join(unicode_dir, "文件_тест_テスト.md"), 'w') as f:
            f.write("# Unicode File\n\nContent with Unicode.")

        # Create subdirectory with Unicode
        unicode_sub = os.path.join(unicode_dir, "子目录_подкаталог_サブディレクトリ")
        os.makedirs(unicode_sub, exist_ok=True)

        with open(os.path.join(unicode_sub, "README.md"), 'w') as f:
            f.write("# Unicode Sub Directory\n\nThis is a Unicode subdirectory.")

        # Generate index
        self.generator.create_index_files(unicode_dir, format='md')

        index_path = os.path.join(unicode_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path))

        index_content = self.read_index_file(index_path)

        # Check that Unicode characters are preserved in relative links
        self.assertIn('[文件_тест_テスト.md](文件_тест_テスト.md)', index_content)
        self.assertIn('[子目录_подкаталог_サブディレクトリ/](子目录_подкаталог_サブディレクトリ/)', index_content)

        # Check parent link
        self.assertIn('[../](../)', index_content)

        # Ensure no absolute paths
        self.assertNotIn(self.temp_dir, index_content)

    def test_relative_links_portability(self):
        """Test that generated relative links work when moved to different locations."""
        main_dir, _, _ = self.create_test_structure()

        # Generate index
        self.generator.create_index_files(main_dir, format='md')

        index_path = os.path.join(main_dir, 'index.md')
        self.assertTrue(os.path.exists(index_path))

        # Read the original index content
        original_content = self.read_index_file(index_path)

        # Create a new location for the directory
        new_location = tempfile.mkdtemp()
        new_main_dir = os.path.join(new_location, "moved_main")

        try:
            # Copy the entire directory structure to new location
            shutil.copytree(main_dir, new_main_dir)

            # Read the copied index content
            copied_index_path = os.path.join(new_main_dir, 'index.md')
            copied_content = self.read_index_file(copied_index_path)

            # Content should be identical (relative links should work in new location)
            self.assertEqual(original_content, copied_content)

            # Verify that relative links in copied content don't contain the new absolute path
            self.assertNotIn(new_location, copied_content)

            # Verify that relative links are still present and correct
            self.assertIn('[file1.md](file1.md)', copied_content)
            self.assertIn('[subdir/](subdir/)', copied_content)

        finally:
            shutil.rmtree(new_location)

    def test_relative_links_performance_with_large_structure(self):
        """Test relative link generation performance with large directory structures."""
        # Create a moderately large directory structure
        main_dir = os.path.join(self.temp_dir, "large_structure")
        os.makedirs(main_dir, exist_ok=True)

        # Create many files and subdirectories
        for i in range(20):
            # Create files
            with open(os.path.join(main_dir, f"file_{i:03d}.md"), 'w') as f:
                f.write(f"# File {i}\n\nContent of file {i}.")

            # Create subdirectories
            sub_dir = os.path.join(main_dir, f"subdir_{i:03d}")
            os.makedirs(sub_dir, exist_ok=True)

            with open(os.path.join(sub_dir, "README.md"), 'w') as f:
                f.write(f"# Sub Directory {i}\n\nThis is subdirectory {i}.")

            with open(os.path.join(sub_dir, f"subfile_{i:03d}.md"), 'w') as f:
                f.write(f"# Sub File {i}\n\nContent of sub file {i}.")

        # Generate index
        self.generator.create_index_files(main_dir, format='md', recursive=True)

        # Check that main index was created
        main_index = os.path.join(main_dir, 'index.md')
        self.assertTrue(os.path.exists(main_index))

        main_content = self.read_index_file(main_index)

        # Verify relative links are present and correct
        self.assertIn('[file_000.md](file_000.md)', main_content)
        self.assertIn('[subdir_000/](subdir_000/)', main_content)

        # Verify no absolute paths
        self.assertNotIn(self.temp_dir, main_content)

        # Check that subdirectory indexes were created with relative links
        sub_index = os.path.join(main_dir, 'subdir_000', 'index.md')
        self.assertTrue(os.path.exists(sub_index))

        sub_content = self.read_index_file(sub_index)
        self.assertIn('[subfile_000.md](subfile_000.md)', sub_content)
        self.assertIn('[../](../)', sub_content)
        self.assertNotIn(self.temp_dir, sub_content)


if __name__ == '__main__':
    unittest.main()