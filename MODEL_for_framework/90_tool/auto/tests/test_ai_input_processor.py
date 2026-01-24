#!/usr/bin/env python3
"""
Test for AI Input Processor
===========================

Unit tests for the ai_input_processor.py module.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import unittest
import tempfile
import os
import json
import yaml
import csv
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from ai_input_processor import InputProcessor

__version__ = "1.0.0"
__status__ = "ACTIVE"

class TestInputProcessor(unittest.TestCase):
    """Test cases for InputProcessor class."""

    def setUp(self):
        """Set up test fixtures."""
        self.processor = InputProcessor()

    def test_process_text_input_plain(self):
        """Test processing plain text input."""
        result = self.processor.process_input("Hello World")

        self.assertEqual(result['format'], 'text')
        self.assertEqual(result['processed_data'], "Hello World")
        self.assertIn('timestamp', result)
        self.assertIn('metadata', result)

    def test_process_text_input_json(self):
        """Test processing JSON text input."""
        json_text = '{"key": "value", "number": 42}'
        result = self.processor.process_input(json_text)

        self.assertEqual(result['format'], 'json')
        self.assertEqual(result['processed_data'], {"key": "value", "number": 42})
        self.assertTrue(result['metadata']['is_structured'])

    def test_process_text_input_yaml(self):
        """Test processing YAML text input."""
        yaml_text = "key: value\nnumber: 42\n"
        result = self.processor.process_input(yaml_text)

        self.assertEqual(result['format'], 'yaml')
        self.assertEqual(result['processed_data'], {"key": "value", "number": 42})
        self.assertTrue(result['metadata']['is_structured'])

    def test_process_text_input_csv(self):
        """Test processing CSV text input."""
        csv_text = "name,age\nJohn,30\nJane,25"
        result = self.processor.process_input(csv_text)

        self.assertEqual(result['format'], 'csv')
        self.assertEqual(len(result['processed_data']), 2)
        self.assertEqual(result['processed_data'][0]['name'], 'John')
        self.assertEqual(result['processed_data'][0]['age'], '30')
        self.assertTrue(result['metadata']['is_structured'])

    def test_process_dict_input(self):
        """Test processing dictionary input."""
        test_dict = {"test": "value", "number": 123}
        result = self.processor.process_input(test_dict)

        self.assertEqual(result['format'], 'dict')
        self.assertEqual(result['processed_data'], test_dict)
        self.assertTrue(result['metadata']['is_structured'])
        self.assertEqual(result['metadata']['keys_count'], 2)

    def test_process_list_input(self):
        """Test processing list input."""
        test_list = [1, 2, 3, "test"]
        result = self.processor.process_input(test_list)

        self.assertEqual(result['format'], 'list')
        self.assertEqual(result['processed_data'], test_list)
        self.assertTrue(result['metadata']['is_structured'])
        self.assertEqual(result['metadata']['items_count'], 4)

    def test_process_bytes_input_text(self):
        """Test processing bytes input containing text."""
        test_bytes = b"Hello from bytes"
        result = self.processor.process_input(test_bytes)

        self.assertEqual(result['format'], 'text')
        self.assertEqual(result['processed_data'], "Hello from bytes")

    def test_process_bytes_input_binary(self):
        """Test processing binary bytes input."""
        test_bytes = b'\x00\x01\x02\x03\xff\xfe\xfd'
        result = self.processor.process_input(test_bytes)

        self.assertEqual(result['format'], 'binary')
        self.assertIn('binary data', result['processed_data'])
        self.assertEqual(result['metadata']['size'], 7)
        self.assertTrue(result['metadata']['is_binary'])

    def test_process_file_json(self):
        """Test processing JSON file."""
        test_data = {"test": "file_data", "items": [1, 2, 3]}

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(test_data, f)
            temp_path = f.name

        try:
            result = self.processor.process_file(temp_path)
            self.assertEqual(result['format'], 'dict')
            self.assertEqual(result['processed_data'], test_data)
        finally:
            os.unlink(temp_path)

    def test_process_file_yaml(self):
        """Test processing YAML file."""
        test_data = {"test": "yaml_file", "value": 42}

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(test_data, f)
            temp_path = f.name

        try:
            result = self.processor.process_file(temp_path)
            self.assertEqual(result['format'], 'dict')
            self.assertEqual(result['processed_data'], test_data)
        finally:
            os.unlink(temp_path)

    def test_process_file_csv(self):
        """Test processing CSV file."""
        csv_content = "name,age\nAlice,25\nBob,30"

        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            f.write(csv_content)
            temp_path = f.name

        try:
            result = self.processor.process_file(temp_path)
            self.assertEqual(result['format'], 'list')
            self.assertEqual(len(result['processed_data']), 2)
            self.assertEqual(result['processed_data'][0]['name'], 'Alice')
        finally:
            os.unlink(temp_path)

    def test_process_file_text(self):
        """Test processing text file."""
        text_content = "This is a test file content."

        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(text_content)
            temp_path = f.name

        try:
            result = self.processor.process_file(temp_path)
            self.assertEqual(result['format'], 'text')
            self.assertEqual(result['processed_data'], text_content)
        finally:
            os.unlink(temp_path)

    def test_process_file_nonexistent(self):
        """Test processing nonexistent file."""
        with self.assertRaises(FileNotFoundError):
            self.processor.process_file("/nonexistent/file.txt")

    def test_batch_processing(self):
        """Test batch processing of multiple inputs."""
        inputs = [
            "Plain text",
            '{"json": "data"}',
            [1, 2, 3],
            {"dict": "input"}
        ]

        results = self.processor.process_batch(inputs)

        self.assertEqual(len(results), 4)
        self.assertEqual(results[0]['format'], 'text')
        self.assertEqual(results[1]['format'], 'json')
        self.assertEqual(results[2]['format'], 'list')
        self.assertEqual(results[3]['format'], 'dict')

    def test_real_time_processing(self):
        """Test real-time processing functionality."""
        # Start real-time processing in a separate thread
        self.processor.start_real_time_processing()

        # Add some inputs
        self.processor.add_input("Test input 1")
        self.processor.add_input({"test": "input2"})

        # Give some time for processing
        import time
        time.sleep(0.1)

        # Check results
        result1 = self.processor.get_processed_output(timeout=0.1)
        result2 = self.processor.get_processed_output(timeout=0.1)

        self.assertIsNotNone(result1)
        self.assertIsNotNone(result2)

        # Stop processing
        self.processor.stop_real_time_processing()

    def test_path_input(self):
        """Test processing Path object input."""
        test_path = Path("test_file.txt")
        result = self.processor.process_input(test_path)

        self.assertEqual(result['input_type'], 'Path')
        self.assertEqual(result['format'], 'text')

    def test_error_handling(self):
        """Test error handling for invalid inputs."""
        # Test with None (should not crash)
        result = self.processor.process_input(None)
        self.assertIn('error', result)

        # Test with invalid JSON in file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write('{"invalid": json syntax}')
            temp_path = f.name

        try:
            result = self.processor.process_file(temp_path)
            self.assertIn('error', result)
        finally:
            os.unlink(temp_path)

if __name__ == '__main__':
    unittest.main()

## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | 2026-01-24 | Initial creation | Framework Maintenance Team | Establish foundational structure |
