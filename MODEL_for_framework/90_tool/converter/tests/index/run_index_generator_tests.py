#!/usr/bin/env python3
"""
Test Runner for Index Generator Tests

This script provides a simple way to run the index generator tests
and validate that the tool always creates index.md files when README.md files are present.

Usage:
    python run_index_generator_tests.py [--verbose]

CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.1.0  | 2026-01-31 | Added comprehensive changelog following framework conventions | Framework Steward | Align with framework documentation standards and provide clear version history |
| V1.0.0  | 2026-01-31 | Initial test runner implementation with verbose output support | AI Coder | Core test runner functionality for index generator validation |
"""

import sys
import os
import unittest
import argparse

# Add the converter path to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'converter'))

def run_tests(verbose=False):
    """Run all index generator tests."""
    # Import the test module
    import test_index_generator
    from test_index_generator import TestIndexGenerator
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestIndexGenerator)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
    result = runner.run(suite)
    
    # Return success status
    return result.wasSuccessful()

def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(
        description="Run index generator tests to validate README.md index creation"
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Run tests with verbose output'
    )
    
    args = parser.parse_args()
    
    print("Running Index Generator Tests")
    print("=" * 50)
    print("Testing that index.md files are created when README.md files are present...")
    print()
    
    success = run_tests(verbose=args.verbose)
    
    print()
    print("=" * 50)
    if success:
        print("✅ All tests passed! Index generator works correctly.")
        print("   - index.md files are created when README.md exists")
        print("   - Content is properly formatted with clickable links")
        print("   - Recursive functionality works as expected")
        sys.exit(0)
    else:
        print("❌ Some tests failed. Please check the output above.")
        sys.exit(1)

if __name__ == '__main__':
    main()