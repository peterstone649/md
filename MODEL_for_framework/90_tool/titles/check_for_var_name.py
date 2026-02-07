#!/usr/bin/env python3
"""
Simple variable name checker for template placeholders.

Author: AI Framework Steward
Created: 2026-02-07
"""

import re

# Version variable
__version__ = "1.0.0"


def check_name(varname: str) -> bool:
    """Check if a variable name contains placeholder syntax."""
    return bool(re.search(r'<[^>]+>', varname))


if __name__ == "__main__":
    # Simple test
    test_cases = [
        "Rule for <name_ot_hierarchical>",
        "Rule Statement",
        "<variable>",
        "No placeholders here"
    ]
    
    for test in test_cases:
        result = check_name(test)
        print(f"'{test}' -> {result}")
"""
## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|------------|
| V1.0.0 | 2026-02-07 | Initial creation of check_for_var_name.py with minimal check_name function | AI Framework Steward | Establish foundational placeholder detection functionality |
"""
