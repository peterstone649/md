#!/usr/bin/env python3
"""
Test for Writer for Input for Model
===================================

Unit tests for the writer_for_input_for_model.py module.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import unittest
import tempfile
import os
import shutil
import time
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from writer_for_input_for_model import WriterForInputForModel

__version__ = "1.0.0"
__status__ = "ACTIVE"

class TestWriterForInputForModel(unittest.TestCase):
    """Test cases for WriterForInputForModel class."""

    def setUp(self):
        """Set up test fixtures."""
        # Create temporary directories
        self.temp_dir = tempfile.mkdtemp()
        self.input_dir = os.path.join(self.temp_dir, "md", "MODEL_for_framework", "in")
        self.processing_dir = os.path.join(self.input_dir, "_processing")

        # Mock the manager
        with patch('writer_for_input_for_model.ManagerForDirOTBase') as mock_manager_class:
            mock_manager = MagicMock()
            mock_manager.get_project_base.return_value = self.temp_dir
            mock_manager_class.return_value = mock_manager

            self.writer = WriterForInputForModel(mock_manager)

    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_initialization(self):
        """Test writer initialization."""
        self.assertTrue(os.path.exists(self.input_dir))
        self.assertTrue(os.path.exists(self.processing_dir))
        self.assertEqual(self.writer.input_dir, self.input_dir)
        self.assertEqual(self.writer.processing_dir, self.processing_dir)

    def test_generate_timestamp_name(self):
        """Test timestamp name generation."""
        original = "test_file.txt"
        timestamped = self.writer.generate_timestamp_name(original)

        # Check format starts with YYYYMMDD_HHMMSS_ffffff_
        parts = timestamped.split('_', 3)  # Split only first 3 underscores
        self.assertEqual(len(parts), 4)  # date_time_micro_rest

        # Check date part
        date_part = parts[0]
        self.assertEqual(len(date_part), 8)  # YYYYMMDD
        self.assertTrue(date_part.isdigit())

        # Check time part
        time_part = parts[1]
        self.assertEqual(len(time_part), 6)  # HHMMSS
        self.assertTrue(time_part.isdigit())

        # Check microsecond part
        micro_part = parts[2]
        self.assertEqual(len(micro_part), 6)  # ffffff
        self.assertTrue(micro_part.isdigit())

        # Check original name is preserved
        self.assertIn("test_file.txt", timestamped)

    def test_generate_timestamp_name_no_extension(self):
        """Test timestamp name generation for files without extension."""
        original = "testfile"
        timestamped = self.writer.generate_timestamp_name(original)

        parts = timestamped.split('_', 3)  # Split only first 3 underscores
        self.assertEqual(len(parts), 4)
        self.assertIn("testfile", timestamped)

    def test_move_file_to_processing(self):
        """Test moving file to processing directory."""
        # Create a test file
        test_file = os.path.join(self.input_dir, "test.txt")
        test_content = "test content"

        with open(test_file, 'w') as f:
            f.write(test_content)

        # Move the file
        success = self.writer.move_file_to_processing(test_file)
        self.assertTrue(success)

        # Check file was moved and renamed
        self.assertFalse(os.path.exists(test_file))
        files_in_processing = os.listdir(self.processing_dir)
        self.assertEqual(len(files_in_processing), 1)

        moved_file = os.path.join(self.processing_dir, files_in_processing[0])
        self.assertTrue(os.path.exists(moved_file))

        # Check content is preserved
        with open(moved_file, 'r') as f:
            self.assertEqual(f.read(), test_content)

        # Check filename has timestamp
        filename = files_in_processing[0]
        parts = filename.split('_')
        self.assertGreaterEqual(len(parts), 4)

    def test_move_file_nonexistent(self):
        """Test moving nonexistent file."""
        nonexistent = os.path.join(self.input_dir, "nonexistent.txt")
        success = self.writer.move_file_to_processing(nonexistent)
        self.assertFalse(success)

    def test_scan_and_process_files(self):
        """Test scanning and processing files."""
        # Create test files
        file1 = os.path.join(self.input_dir, "file1.txt")
        file2 = os.path.join(self.input_dir, "file2.json")

        with open(file1, 'w') as f:
            f.write("content1")
        with open(file2, 'w') as f:
            f.write('{"test": "content2"}')

        # Process files
        processed = self.writer.scan_and_process_files()
        self.assertEqual(processed, 2)

        # Check files were moved
        self.assertFalse(os.path.exists(file1))
        self.assertFalse(os.path.exists(file2))

        processing_files = os.listdir(self.processing_dir)
        self.assertEqual(len(processing_files), 2)

        # Check processed files tracking
        self.assertIn("file1.txt", self.writer.processed_files)
        self.assertIn("file2.json", self.writer.processed_files)

    def test_scan_and_process_no_files(self):
        """Test scanning when no files present."""
        processed = self.writer.scan_and_process_files()
        self.assertEqual(processed, 0)

    def test_scan_and_process_directories_ignored(self):
        """Test that directories are ignored."""
        subdir = os.path.join(self.input_dir, "subdir")
        os.makedirs(subdir)

        # Create a file in the subdirectory
        subfile = os.path.join(subdir, "subfile.txt")
        with open(subfile, 'w') as f:
            f.write("sub content")

        processed = self.writer.scan_and_process_files()
        self.assertEqual(processed, 0)  # Directories should be ignored

    def test_run_single_scan(self):
        """Test single scan execution."""
        # Create test file
        test_file = os.path.join(self.input_dir, "single_test.txt")
        with open(test_file, 'w') as f:
            f.write("single test")

        processed = self.writer.run_single_scan()
        self.assertEqual(processed, 1)

        # Check file was moved
        self.assertFalse(os.path.exists(test_file))
        self.assertEqual(len(os.listdir(self.processing_dir)), 1)

    def test_processed_files_tracking(self):
        """Test that already processed files are not reprocessed."""
        # Create test file
        test_file = os.path.join(self.input_dir, "track_test.txt")
        with open(test_file, 'w') as f:
            f.write("track test")

        # First scan
        processed1 = self.writer.scan_and_process_files()
        self.assertEqual(processed1, 1)

        # Second scan should not process again
        processed2 = self.writer.scan_and_process_files()
        self.assertEqual(processed2, 0)

        # Check only one file in processing
        self.assertEqual(len(os.listdir(self.processing_dir)), 1)

    def test_generate_timestamp_name_uniqueness(self):
        """Test that timestamp names are unique."""
        name1 = self.writer.generate_timestamp_name("test.txt")
        time.sleep(0.001)  # Small delay to ensure different timestamp
        name2 = self.writer.generate_timestamp_name("test.txt")

        self.assertNotEqual(name1, name2)

    def test_error_handling_scan(self):
        """Test error handling during scanning."""
        # Make input_dir unreadable (simulate permission error)
        original_mode = os.stat(self.input_dir).st_mode
        try:
            # This might not work on all systems, but test the error handling
            with patch('os.listdir', side_effect=OSError("Permission denied")):
                processed = self.writer.scan_and_process_files()
                self.assertEqual(processed, 0)
        finally:
            # Restore permissions if changed
            pass

if __name__ == '__main__':
    unittest.main()
