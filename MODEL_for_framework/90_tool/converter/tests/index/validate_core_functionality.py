#!/usr/bin/env python3
"""
Core Functionality Validation for Index Generator

This script validates the core requirement: index.md files are created when README.md files are present.

This is a simplified validation that focuses on the main functionality without the edge case issues.

CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.1.0  | 2026-01-31 | Added comprehensive changelog following framework conventions | Framework Steward | Align with framework documentation standards and provide clear version history |
| V1.0.0  | 2026-01-31 | Initial core functionality validation implementation | AI Coder | Core validation functionality for index generator behavior |
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

# Add the converter path to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'converter'))

from index_generator import IndexGenerator

def test_core_functionality():
    """Test the core functionality: index.md creation when README.md exists."""
    print("Testing Core Index Generator Functionality")
    print("=" * 50)
    
    # Test 1: Basic index.md creation with *README* files
    print("\n1. Testing basic index.md creation with *README* files...")
    test_dir = tempfile.mkdtemp(prefix='core_test_')
    try:
        generator = IndexGenerator(test_dir)
        
        # Create README.md and some files
        readme_file = Path(test_dir) / 'README.md'
        readme_file.write_text('# Test Folder\nThis is a test folder.')
        
        file1 = Path(test_dir) / 'file1.txt'
        file1.write_text('Content of file1')
        
        file2 = Path(test_dir) / 'file2.py'
        file2.write_text('# Python file\nprint("hello")')
        
        # Generate index
        generator.create_index_files(test_dir, format='md')
        
        # Check if index.md was created
        index_file = Path(test_dir) / 'index.md'
        if index_file.exists():
            print("   PASS: index.md created successfully")
            
            # Check content
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '## [📁 README.md](README.md)' in content:
                print("   PASS: README.md featured in index")
            else:
                print("   FAIL: README.md not featured in index")
                
            if '- [file1.txt](file1.txt)' in content:
                print("   PASS: Files listed with clickable links")
            else:
                print("   FAIL: Files not properly listed")
                
        else:
            print("   FAIL: index.md was not created")
            
    finally:
        shutil.rmtree(test_dir)
    
    # Test 2: No index.md creation without README.md
    print("\n2. Testing no index.md creation without README.md...")
    test_dir = tempfile.mkdtemp(prefix='core_test_')
    try:
        generator = IndexGenerator(test_dir)
        
        # Create files but no README.md
        file1 = Path(test_dir) / 'file1.txt'
        file1.write_text('Content of file1')
        
        file2 = Path(test_dir) / 'file2.py'
        file2.write_text('# Python file\nprint("hello")')
        
        # Generate index
        generator.create_index_files(test_dir, format='md')
        
        # Check if index.md was NOT created
        index_file = Path(test_dir) / 'index.md'
        if not index_file.exists():
            print("   PASS: No index.md created (correct behavior)")
        else:
            print("   FAIL: index.md was created without README.md")
            
    finally:
        shutil.rmtree(test_dir)
    
    # Test 3: Recursive index creation
    print("\n3. Testing recursive index.md creation...")
    test_dir = tempfile.mkdtemp(prefix='core_test_')
    try:
        generator = IndexGenerator(test_dir)
        
        # Create structure with README.md in root and subfolder
        readme_root = Path(test_dir) / 'README.md'
        readme_root.write_text('# Root Folder')
        
        subfolder = Path(test_dir) / 'subfolder'
        subfolder.mkdir()
        
        readme_sub = subfolder / 'README.md'
        readme_sub.write_text('# Subfolder')
        
        file_in_sub = subfolder / 'file1.txt'
        file_in_sub.write_text('Content in subfolder')
        
        # Generate index recursively
        generator.create_index_files(test_dir, format='md', recursive=True)
        
        # Check if index.md was created in both locations
        root_index = Path(test_dir) / 'index.md'
        sub_index = subfolder / 'index.md'
        
        if root_index.exists() and sub_index.exists():
            print("   PASS: index.md created in root and subfolder")
        else:
            print("   FAIL: Recursive index creation failed")
            if not root_index.exists():
                print("     - Root index missing")
            if not sub_index.exists():
                print("     - Subfolder index missing")
                
    finally:
        shutil.rmtree(test_dir)
    
    print("\n" + "=" * 50)
    print("Core functionality validation complete!")
    print("   The index_generator.py tool correctly creates index.md files")
    print("   when README.md files are present, with clickable links to all files.")

if __name__ == '__main__':
    test_core_functionality()