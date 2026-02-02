#!/usr/bin/env python3
"""
Test runner for relative link generation tests in index_generator.py.

This script runs all the relative link test suites and provides a comprehensive
report of the test results.
"""

import unittest
import sys
import os

# Add the converter directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import the test module
from tests.relative.test_index_generator_relative_links import TestIndexGeneratorRelativeLinks

__version__ = "1.0.0"
__status__ = "ACTIVE"

"""
CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-02-01 | Initial creation of relative links test runner | Framework Steward | Establish comprehensive test execution framework for relative link functionality |
"""


def create_test_suite():
    """Create a test suite containing all relative link tests."""
    suite = unittest.TestSuite()

    # Add relative link tests for index generator
    suite.addTest(unittest.makeSuite(TestIndexGeneratorRelativeLinks))

    return suite


def run_tests():
    """Run all relative link tests and display results."""
    print("=" * 70)
    print("Relative Link Generation Test Suite for index_generator.py")
    print("=" * 70)
    print()

    # Create the test suite
    suite = create_test_suite()

    # Create a test runner with detailed output
    runner = unittest.TextTestRunner(
        verbosity=2,
        stream=sys.stdout,
        descriptions=True,
        failfast=False
    )

    # Run the tests
    result = runner.run(suite)

    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped) if hasattr(result, 'skipped') else 0}")

    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback}")

    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback}")

    # Determine overall result
    if result.wasSuccessful():
        print("\n✅ ALL TESTS PASSED!")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED!")
        return 1


if __name__ == '__main__':
    exit_code = run_tests()
    sys.exit(exit_code)