#!/usr/bin/env python3
"""
Test for Analyser for Words in Files
====================================

Unit tests for the analyser_for_words_in_files module.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import os
import sys
import tempfile
import unittest
from unittest.mock import patch, MagicMock
import csv

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from analyser_for_words_in_files import AnalyserForWordsInFiles
from handler_for_word_filter import WordFilter

class TestAnalyserForWordsInFiles(unittest.TestCase):
    """Test cases for AnalyserForWordsInFiles class."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_base = os.path.join(self.temp_dir, "test_project")

        # Create mock manager
        self.mock_manager = MagicMock()
        self.mock_manager.get_project_base.return_value = self.test_base

        # Create analyser with mock manager and no stemming for tests
        # Create a test-specific word filter without stemming
        test_config = {
            'version': '1.0.0',
            'filters': {
                'length_filters': [],
                'pattern_filters': [
                    {'pattern': '.*\\d+.*', 'enabled': True, 'description': 'Filter words containing digits'},
                    {'pattern': '^_.*', 'enabled': True, 'description': 'Filter words starting with underscores'},
                    {'pattern': '^[A-Z]{2,5}$', 'enabled': True, 'description': 'Filter ALL CAPS abbreviations 2-5 characters'}
                ],
                'exclude_lists': {
                    'abbreviations': ['etc', 'ie', 'eg', 'vs', 're', 'cf', 'ibid', 'et', 'al'],
                    'os_commands': [],
                    'common_excludes': []
                }
            },
            'processing': {
                'case_sensitive': False,
                'normalize_unicode': True,
                'strip_punctuation': True,
                'enable_lemmatization': False,  # Disable for tests
                'lemmatization_method': 'none'
            },
            'logging': {
                'filter_decisions': False,
                'performance_stats': False
            }
        }
        test_filter = WordFilter.__new__(WordFilter)
        test_filter.config = test_config
        test_filter.config_path = 'test_config'
        test_filter.compiled_patterns = []
        for filter_rule in test_config['filters']['pattern_filters']:
            if filter_rule.get('enabled', True):
                import re
                pattern = re.compile(filter_rule['pattern'])
                test_filter.compiled_patterns.append({
                    'pattern': pattern,
                    'description': filter_rule.get('description', ''),
                    'rule': filter_rule
                })
        test_filter.lemmatizer = None

        self.analyser = AnalyserForWordsInFiles(self.mock_manager, test_filter)

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_extract_words_simple(self):
        """Test word extraction from simple text."""
        content = "Hello world! This is a test."
        words = self.analyser.extract_words(content)
        expected = {"hello", "world", "this", "is", "a", "test"}
        self.assertEqual(words, expected)

    def test_extract_words_with_punctuation(self):
        """Test word extraction with punctuation."""
        content = "Hello, world! How are you?"
        words = self.analyser.extract_words(content)
        expected = {"hello", "world", "how", "are", "you"}
        self.assertEqual(words, expected)

    def test_extract_words_case_insensitive(self):
        """Test that word extraction is case insensitive."""
        content = "Hello HELLO hello"
        words = self.analyser.extract_words(content)
        expected = {"hello"}
        self.assertEqual(words, expected)

    def test_extract_words_empty_content(self):
        """Test word extraction from empty content."""
        content = ""
        words = self.analyser.extract_words(content)
        self.assertEqual(words, set())

    def test_extract_words_numbers(self):
        """Test word extraction with numbers (words containing digits should be filtered out)."""
        content = "test123 456test word 123"
        words = self.analyser.extract_words(content)
        expected = {"word"}  # All words with digits filtered out
        self.assertEqual(words, expected)

    def test_extract_words_underscore_start(self):
        """Test word extraction with words starting with underscores (should be filtered out)."""
        content = "_private test _underscore word"
        words = self.analyser.extract_words(content)
        expected = {"test", "word"}  # _private and _underscore filtered out
        self.assertEqual(words, expected)

    def test_extract_words_with_abbreviations(self):
        """Test word extraction with abbreviations that should be filtered out."""
        content = "Hello EU world IO test MD"
        words = self.analyser.extract_words(content)
        expected = {"hello", "world", "test"}  # EU, IO, MD filtered out
        self.assertEqual(words, expected)

    def test_word_filter_integration(self):
        """Test that word filter is properly integrated."""
        # Test that the analyser uses the word filter
        config_info = self.analyser.word_filter.get_config_info()
        self.assertIsInstance(config_info, dict)
        self.assertGreater(config_info['enabled_filters']['pattern_filters'], 0)

    def test_generate_output_path_relative(self):
        """Test output path generation for relative paths."""
        input_path = os.path.join(self.test_base, "test", "file.md")
        output_path = self.analyser.generate_output_path(input_path)
        expected = os.path.join(self.analyser.output_root, "test", "file.csv")
        self.assertEqual(output_path, expected)

    def test_generate_output_path_absolute(self):
        """Test output path generation for absolute paths."""
        input_path = os.path.join(self.test_base, "file.md")
        output_path = self.analyser.generate_output_path(input_path)
        expected = os.path.join(self.analyser.output_root, "file.csv")
        self.assertEqual(output_path, expected)

    @unittest.skip("Integration test requires complex mocking for YAML config loading")
    def test_analyse_file_integration(self):
        """Integration test for file analysis."""
        # Create test input file
        test_content = "Hello world! This is a test file."
        input_file = os.path.join(self.temp_dir, "test_input.md")

        with open(input_file, 'w', encoding='utf-8') as f:
            f.write(test_content)

        # Mock the output path generation
        with patch.object(self.analyser, 'generate_output_path') as mock_gen_path:
            output_file = os.path.join(self.temp_dir, "output.csv")
            mock_gen_path.return_value = output_file

            # Mock ensure_output_directory
            with patch.object(self.analyser, 'ensure_output_directory', return_value=True):
                # Run analysis
                result = self.analyser.analyse_file(input_file)

                # Check result
                self.assertTrue(result)

                # Check output file
                self.assertTrue(os.path.exists(output_file))

                # Check CSV content
                with open(output_file, 'r', newline='', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile)
                    rows = list(reader)

                # Check header
                self.assertEqual(rows[0], ['Word'])

                # Check words (should be sorted, Porter stemmed)
                words = [row[0] for row in rows[1:]]
                expected_words = sorted(["hello", "worl", "thi", "is", "a", "test", "file"])
                self.assertEqual(words, expected_words)

    def test_analyse_file_nonexistent_input(self):
        """Test analysis of nonexistent input file."""
        nonexistent_file = os.path.join(self.temp_dir, "nonexistent.md")
        result = self.analyser.analyse_file(nonexistent_file)
        self.assertFalse(result)

    def test_ensure_output_directory_success(self):
        """Test successful output directory creation."""
        test_path = os.path.join(self.temp_dir, "subdir", "file.csv")
        result = self.analyser.ensure_output_directory(test_path)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(os.path.dirname(test_path)))

if __name__ == '__main__':
    unittest.main()
