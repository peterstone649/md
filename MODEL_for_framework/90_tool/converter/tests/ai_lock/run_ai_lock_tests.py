#!/usr/bin/env python3
"""
Test runner for AI_LOCK/AI_UNLOCK special handling tests.

This script runs all the AI_LOCK test suites and provides a comprehensive
report of the test results.
"""

import unittest
import sys
import os

# Add the converter directory to the path so we can import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import all test modules
from tests.ai_lock.test_ai_lock_single_line import TestAILockSingleLine
from tests.ai_lock.test_ai_lock_integration import TestAILockIntegration
from tests.ai_lock.test_ai_lock_css_styling import TestAILockCSSStyling
from tests.ai_lock.test_ai_lock_edge_cases import TestAILockEdgeCases

__version__ = "1.0.0"
__status__ = "ACTIVE"

"""
CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-02-01 | Initial creation of AI_LOCK test runner | Framework Steward | Establish comprehensive test execution framework for AI_LOCK functionality |
"""


def create_test_suite():
    """Create a test suite containing all AI_LOCK tests."""
    suite = unittest.TestSuite()

    # Add single line tests
    suite.addTest(unittest.makeSuite(TestAILockSingleLine))

    # Add integration tests
    suite.addTest(unittest.makeSuite(TestAILockIntegration))

    # Add CSS styling tests
    suite.addTest(unittest.makeSuite(TestAILockCSSStyling))

    # Add edge case tests
    suite.addTest(unittest.makeSuite(TestAILockEdgeCases))

    return suite


def run_tests():
    """Run all AI_LOCK tests and display results."""
    print("=" * 70)
    print("AI_LOCK/AI_UNLOCK Special Handling Test Suite")
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


def run_specific_test_suite(suite_name):
    """Run a specific test suite."""
    print(f"Running {suite_name} tests...")
    print("-" * 50)

    if suite_name == "single_line":
        suite = unittest.makeSuite(TestAILockSingleLine)
    elif suite_name == "integration":
        suite = unittest.makeSuite(TestAILockIntegration)
    elif suite_name == "css_styling":
        suite = unittest.makeSuite(TestAILockCSSStyling)
    elif suite_name == "edge_cases":
        suite = unittest.makeSuite(TestAILockEdgeCases)
    else:
        print(f"Unknown test suite: {suite_name}")
        return 1

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Run specific test suite if provided
        suite_name = sys.argv[1]
        exit_code = run_specific_test_suite(suite_name)
    else:
        # Run all tests
        exit_code = run_tests()

    sys.exit(exit_code)