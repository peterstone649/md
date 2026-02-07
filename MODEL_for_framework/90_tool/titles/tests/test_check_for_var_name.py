#!/usr/bin/env python3
"""
Test file for check_for_var_name.py

Author: AI Framework Steward
Created: 2026-02-07
"""

import sys
import os

# Add the parent directory to Python path to import our module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from check_for_var_name import check_name

# Version variable
__version__ = "1.0.0"


def test_check_name():
    """Test the check_name function with various inputs."""
    
    # Test cases: (input, expected_result, description)
    test_cases = [
        ("Rule for <name_ot_hierarchical> [<name_ot_hierarchical_constant>] **[PRIO: <priority_ot_allowed>]**", True, "Template with multiple placeholders"),
        ("Rule Statement **[STATUS: <status_ot_allowed>]**", True, "Template with status placeholder"),
        ("Rule Statement", False, "Plain section name without placeholders"),
        ("Rule Requirements", False, "Plain section name without placeholders"),
        ("Formal Statement", False, "Plain section name without placeholders"),
        ("Integration with Other Framework Components", False, "Plain section name without placeholders"),
        ("Changelog", False, "Plain section name without placeholders"),
        ("<variable>", True, "Simple placeholder"),
        ("No placeholders here", False, "No placeholders"),
        ("Mixed <placeholder> and text", True, "Mixed content with placeholder"),
        ("", False, "Empty string"),
    ]
    
    print("Testing check_name function:")
    print("=" * 50)
    
    all_passed = True
    for i, (input_str, expected, description) in enumerate(test_cases, 1):
        result = check_name(input_str)
        status = "PASS" if result == expected else "FAIL"
        
        if result != expected:
            all_passed = False
            
        print(f"Test {i:2d}: {status} - {description}")
        print(f"         Input: '{input_str}'")
        print(f"         Expected: {expected}, Got: {result}")
        print()
    
    print("=" * 50)
    if all_passed:
        print("All tests PASSED! (PASS)")
    else:
        print("Some tests FAILED! (FAIL)")
    
    return all_passed


if __name__ == "__main__":
    test_check_name()


"""
## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|------------|
| V1.0.0 | 2026-02-07 | Initial creation of test_check_for_var_name.py with comprehensive test suite for check_name function | AI Framework Steward | Establish foundational testing for placeholder detection functionality |
"""
