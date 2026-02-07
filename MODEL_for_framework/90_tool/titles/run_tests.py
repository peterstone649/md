#!/usr/bin/env python3
"""
Simple test runner for the Title Extractor tests.
This script sets up the Python path correctly to run the tests.
"""

import sys
import os
import unittest

# Add the current directory to the Python path so imports work correctly
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Now import and run the tests
if __name__ == '__main__':
    # Import the test module
    from tests.test_extract_titles import TestTitleExtractor
    
    # Create a test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes to the suite
    suite.addTests(loader.loadTestsFromTestCase(TestTitleExtractor))
    
    # Run the tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)