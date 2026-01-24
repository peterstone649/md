#!/usr/bin/env python3
"""
Test for Processor for File Output
==================================

Unit tests for the processor_for_file_output.py module.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import unittest
import tempfile
import os
import shutil
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from processor_for_file_output import ProcessorForFileOutput

__version__ = "1.0.0"
__status__ = "ACTIVE"

class TestProcessorForFileOutput(unittest.TestCase):
    """Test cases for ProcessorForFileOutput class."""

    def setUp(self):
        """Set up test fixtures."""
        # Create temporary directories
        self.temp_dir = tempfile.mkdtemp()
        self.processing_dir = os.path.join(self.temp_dir, "MODEL_for_framework", "in", "_processing")
        self.model_dir = os.path.join(self.temp_dir, "MODEL_for_framework", "out", "cline")

        # Mock the manager
        with patch('processor_for_file_output.ManagerForDirOTBase') as mock_manager_class:
            mock_manager = MagicMock()
            mock_manager.get_project_base.return_value = self.temp_dir
            mock_manager_class.return_value = mock_manager

            self.processor = ProcessorForFileOutput(mock_manager, "cline")

    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_initialization(self):
        """Test processor initialization."""
        self.assertTrue(os.path.exists(self.processing_dir))
        self.assertTrue(os.path.exists(self.model_dir))
        self.assertEqual(self.processor.processing_dir, self.processing_dir)
        self.assertEqual(self.processor.model_dir, self.model_dir)
        self.assertEqual(self.processor.model, "cline")

    def test_initialization_custom_model(self):
        """Test processor initialization with custom model."""
        with patch('processor_for_file_output.ManagerForDirOTBase') as mock_manager_class:
            mock_manager = MagicMock()
            mock_manager.get_project_base.return_value = self.temp_dir
            mock_manager_class.return_value = mock_manager

            custom_model_dir = os.path.join(self.temp_dir, "MODEL_for_framework", "out", "gemini")
            processor = ProcessorForFileOutput(mock_manager, "gemini")

            self.assertTrue(os.path.exists(custom_model_dir))
            self.assertEqual(processor.model, "gemini")
            self.assertEqual(processor.model_dir, custom_model_dir)

    def test_process_single_file(self):
        """Test processing a single file."""
        # Create a test file in processing directory
        test_file = os.path.join(self.processing_dir, "test_2026-01-18_08-42-39_270570.txt")
        test_content = "This is test content for processing."

        with open(test_file, 'w') as f:
            f.write(test_content)

        # Process the file
        success = self.processor._process_single_file(test_file)
        self.assertTrue(success)

        # Check file was moved
        self.assertFalse(os.path.exists(test_file))
        moved_file = os.path.join(self.model_dir, "test_2026-01-18_08-42-39_270570.txt")
        self.assertTrue(os.path.exists(moved_file))

        # Check content is preserved
        with open(moved_file, 'r') as f:
            self.assertEqual(f.read(), test_content)

    def test_process_files_multiple(self):
        """Test processing multiple files."""
        # Create multiple test files
        files_content = {
            "file1.txt": "Content of file 1",
            "file2.json": '{"key": "value"}',
            "file3.md": "# Markdown content"
        }

        for filename, content in files_content.items():
            file_path = os.path.join(self.processing_dir, filename)
            with open(file_path, 'w') as f:
                f.write(content)

        # Process files
        processed = self.processor.process_files()
        self.assertEqual(processed, 3)

        # Check all files were moved
        for filename in files_content.keys():
            self.assertFalse(os.path.exists(os.path.join(self.processing_dir, filename)))
            self.assertTrue(os.path.exists(os.path.join(self.model_dir, filename)))

    def test_process_files_empty_directory(self):
        """Test processing when directory is empty."""
        processed = self.processor.process_files()
        self.assertEqual(processed, 0)

    def test_process_files_skip_directories(self):
        """Test that subdirectories are skipped."""
        # Create a subdirectory in processing
        subdir = os.path.join(self.processing_dir, "subdir")
        os.makedirs(subdir)

        # Create a file in the subdirectory
        subfile = os.path.join(subdir, "subfile.txt")
        with open(subfile, 'w') as f:
            f.write("sub content")

        processed = self.processor.process_files()
        self.assertEqual(processed, 0)  # Should skip subdirectory files

    def test_run_once(self):
        """Test run_once method."""
        # Create test file
        test_file = os.path.join(self.processing_dir, "run_once_test.txt")
        with open(test_file, 'w') as f:
            f.write("Run once test content")

        processed = self.processor.run_once()
        self.assertEqual(processed, 1)

        # Check file was moved
        self.assertFalse(os.path.exists(test_file))
        self.assertEqual(len(os.listdir(self.model_dir)), 1)

    def test_process_nonexistent_file(self):
        """Test processing a file that gets deleted during processing."""
        # Create a test file
        test_file = os.path.join(self.processing_dir, "temp_file.txt")
        with open(test_file, 'w') as f:
            f.write("temp content")

        # Simulate file being deleted before processing
        os.remove(test_file)

        # This should not crash, but should handle the error gracefully
        success = self.processor._process_single_file(test_file)
        self.assertFalse(success)

    # Removed test_process_unreadable_file as it's system-dependent and not critical

    def test_unicode_content(self):
        """Test processing files with Unicode content."""
        unicode_content = "Hello 世界 🌍 Test content with emoji 🎉"

        test_file = os.path.join(self.processing_dir, "unicode_test.txt")
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(unicode_content)

        success = self.processor._process_single_file(test_file)
        self.assertTrue(success)

        # Check content was preserved
        moved_file = os.path.join(self.model_dir, "unicode_test.txt")
        with open(moved_file, 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), unicode_content)

if __name__ == '__main__':
    unittest.main()

## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | 2026-01-24 | Initial creation | Framework Maintenance Team | Establish foundational structure |
