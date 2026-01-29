#!/usr/bin/env python3
"""
Script to apply version changelog update rule to all files in MODEL_for_framework directory
"""

import os
import re
from datetime import datetime
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).parent.parent.parent / "SVC"
RULE_FILE = Path(__file__).parent.parent / "12_rule" / "04_rule_for_version_changelog_update.md"
CHANGELOG_TEMPLATE = """## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | {date} | Initial creation | Framework Maintenance Team | Establish foundational structure |
"""

def get_current_date():
    """Get current date in ISO format"""
    return datetime.now().strftime("%Y-%m-%d")

def needs_changelog(file_path):
    """Check if file needs a changelog section"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file already has a changelog section
        if re.search(r'##\s+Changelog', content, re.IGNORECASE):
            return False

        # Check if file is a markdown file (most likely to need changelog)
        if file_path.suffix.lower() == '.md':
            return True

        # Check if file is a Python file with version info
        if file_path.suffix.lower() == '.py':
            if re.search(r'__version__\s*=', content):
                return True

        return False

    except Exception as e:
        print(f"Error checking {file_path}: {e}")
        return False

def add_changelog(file_path):
    """Add changelog section to file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove trailing whitespace
        content = content.rstrip()

        # Add changelog section
        changelog = CHANGELOG_TEMPLATE.format(date=get_current_date())
        new_content = content + "\n\n" + changelog

        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Added changelog to: {file_path}")
        return True

    except Exception as e:
        print(f"Error adding changelog to {file_path}: {e}")
        return False

def process_files():
    """Process all files in MODEL_for_framework directory"""
    files_processed = 0
    files_with_changelog = 0
    files_needing_changelog = 0

    # Walk through all files in the directory
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            file_path = Path(root) / file
            files_processed += 1

            if needs_changelog(file_path):
                files_needing_changelog += 1
                if add_changelog(file_path):
                    files_with_changelog += 1

    print(f"\nProcessing complete:")
    print(f"Files processed: {files_processed}")
    print(f"Files needing changelog: {files_needing_changelog}")
    print(f"Files with changelog added: {files_with_changelog}")

def main():
    print("Applying version changelog update rule to SVC directory...")
    print(f"Base directory: {BASE_DIR}")
    print(f"Current date: {get_current_date()}")
    print()

    process_files()

if __name__ == "__main__":
    main()
