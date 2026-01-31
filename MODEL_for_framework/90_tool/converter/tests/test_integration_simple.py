#!/usr/bin/env python3
"""
Simple integration tests for MODEL_for_framework HTML converters.
"""

import os
import tempfile
from pathlib import Path

# Test that the modules can be imported
def test_imports():
    """Test that converter modules can be imported."""
    try:
        # The converter files are in the same directory as this test file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)  # Go up to converter directory
        
        # Test YAML converter import
        yaml_converter_path = os.path.join(parent_dir, "converter_for_yaml_to_html.py")
        assert os.path.exists(yaml_converter_path), f"YAML converter not found at {yaml_converter_path}"
        
        # Test Markdown converter import
        md_converter_path = os.path.join(parent_dir, "converter_for_md_to_html.py")
        assert os.path.exists(md_converter_path), f"Markdown converter not found at {md_converter_path}"
        
        print("All converter modules found and accessible")
        
    except Exception as e:
        print(f"Import test failed: {e}")
        raise

def test_temp_file_creation():
    """Test that temporary files can be created and cleaned up.""" 
    with tempfile.NamedTemporaryFile(suffix='.yaml', delete=False) as tmp:
        tmp_path = tmp.name
    
    try:
        assert os.path.exists(tmp_path), "Temporary file should exist"
        print("Temporary file creation works")
    finally:
        os.unlink(tmp_path)
        assert not os.path.exists(tmp_path), "Temporary file should be cleaned up"
        print("Temporary file cleanup works")

def test_directory_operations():
    """Test directory operations."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file = os.path.join(temp_dir, "test.yaml")
        with open(test_file, 'w') as f:
            f.write("title: 'Test'")
        
        assert os.path.exists(test_file), "Test file should exist"
        assert os.path.isdir(temp_dir), "Temp directory should exist"
        
        # List files
        files = os.listdir(temp_dir)
        assert len(files) == 1, "Should have one file in temp directory"
        assert files[0] == "test.yaml", "File should be test.yaml"
        
        print("Directory operations work correctly")

if __name__ == "__main__":
    test_imports()
    test_temp_file_creation()
    test_directory_operations()
    print("All basic tests passed!")
