#!/usr/bin/env python3
"""
Title Extractor Tool

Extracts all title lines (starting with #) from Markdown files and saves them
to corresponding .title.txt files in the out/txt directory with preserved folder structure.

Based on the structure and patterns from converter_for_md_to_html.py
"""

import os
import sys
import argparse
import re
import logging
from datetime import datetime
from pathlib import Path

# Import the base directory manager for consistent path handling
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from converter.manager_for_dir_OT_base import ManagerForDirOTBase

__version__ = "1.0.0"
__status__ = "ACTIVE"

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TitleExtractor:
    """
    Extracts title lines from Markdown files and saves them to .title.txt files.
    """
    
    def __init__(self, input_path, output_base=None):
        """
        Initialize the title extractor.
        
        Args:
            input_path (str): Path to input file or directory
            output_base (str): Base output directory. Defaults to 'out/txt' in current working directory
        """
        self.input_path = os.path.abspath(input_path)
        if output_base is None:
            # Use the base directory manager for consistent path handling
            manager = ManagerForDirOTBase()
            # Get the project base and create out/txt relative to it
            project_base = manager.get_project_base()
            output_base = os.path.join(project_base, "out", "txt")
        self.output_base = os.path.abspath(output_base)
        self.manager = ManagerForDirOTBase()
        
    def extract_titles_from_content(self, content):
        """
        Extract all title lines from markdown content.
        
        Args:
            content (str): Markdown content
            
        Returns:
            list: List of title lines with their hierarchy levels
        """
        titles = []
        lines = content.split('\n')
        
        for line in lines:
            # Match lines starting with 1 or more # characters followed by space and content
            match = re.match(r'^(#+)\s+(.+)$', line.strip())
            if match:
                level = len(match.group(1))
                title_text = match.group(2).strip()
                titles.append(f"{'#' * level} {title_text}")
                
        return titles
    
    def get_output_path(self, input_file_path):
        """
        Generate output path for the title file, preserving directory structure.
        
        Args:
            input_file_path (str): Path to input markdown file
            
        Returns:
            str: Path to output .title.txt file
        """
        # Use the base directory manager for consistent path handling
        try:
            # Get relative path from project base
            rel_path = self.manager.get_relative_path(input_file_path)
            
            # Handle case where paths are on different drives
            if rel_path.startswith('..'):
                # Use just the filename in this case
                base = os.path.splitext(os.path.basename(input_file_path))[0]
                return os.path.join(self.output_base, f"{base}.title.txt")
                
        except ValueError:
            # Fallback: use just the filename
            base = os.path.splitext(os.path.basename(input_file_path))[0]
            return os.path.join(self.output_base, f"{base}.title.txt")
            
        # Remove .md extension and add .title.txt
        base_name = os.path.splitext(rel_path)[0]
        output_filename = f"{base_name}.title.txt"
        
        # Combine with output base directory
        output_path = os.path.join(self.output_base, output_filename)
        
        return output_path
    
    def process_file(self, input_file):
        """
        Process a single markdown file and extract titles.
        
        Args:
            input_file (str): Path to input markdown file
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not os.path.isfile(input_file):
            logging.error(f"Input file not found: {input_file}")
            return False
            
        if not input_file.lower().endswith(('.md', '.markdown')):
            logging.warning(f"Skipping non-markdown file: {input_file}")
            return False
            
        try:
            # Read markdown content
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract titles
            titles = self.extract_titles_from_content(content)
            
            if not titles:
                logging.info(f"No titles found in: {input_file}")
                return True  # File processed successfully, just no titles
                
            # Generate output path
            output_path = self.get_output_path(input_file)
            
            # Create output directory if needed
            output_dir = os.path.dirname(output_path)
            os.makedirs(output_dir, exist_ok=True)
            
            # Write titles to output file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# Extracted Titles from {os.path.basename(input_file)}\n")
                f.write(f"# Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} by {os.path.basename(__file__)} v{__version__}\n")
                f.write(f"# Source: {input_file}\n")
                f.write("\n")
                
                for title in titles:
                    f.write(f"{title}\n")
                    
            logging.info(f"Extracted {len(titles)} titles from '{input_file}' to '{output_path}'")
            return True
            
        except Exception as e:
            logging.error(f"Error processing file {input_file}: {e}")
            return False
    
    def process_directory(self, input_dir, recursive=False):
        """
        Process all markdown files in a directory.
        
        Args:
            input_dir (str): Path to input directory
            recursive (bool): Whether to process subdirectories recursively
            
        Returns:
            tuple: (success_count, total_count)
        """
        if not os.path.isdir(input_dir):
            logging.error(f"Input directory not found: {input_dir}")
            return 0, 0
            
        success_count = 0
        total_count = 0
        
        if recursive:
            # Process all files recursively
            for root, dirs, files in os.walk(input_dir):
                for file in files:
                    if file.lower().endswith(('.md', '.markdown')):
                        input_file = os.path.join(root, file)
                        total_count += 1
                        if self.process_file(input_file):
                            success_count += 1
        else:
            # Process only top-level files
            for file in os.listdir(input_dir):
                file_path = os.path.join(input_dir, file)
                if os.path.isfile(file_path) and file.lower().endswith(('.md', '.markdown')):
                    total_count += 1
                    if self.process_file(file_path):
                        success_count += 1
                        
        return success_count, total_count

def main():
    """Main function to handle command-line arguments and execute the tool."""
    parser = argparse.ArgumentParser(
        description="Extract title lines from Markdown files and save to .title.txt files.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("input_path", 
                       help="Path to a Markdown file or directory containing Markdown files.")
    
    parser.add_argument("-r", "--recursive",
                       action="store_true",
                       help="If input_path is a directory, process all subdirectories recursively.")
    
    parser.add_argument("-o", "--output",
                       default=None,
                       help="Base output directory for .title.txt files. Defaults to 'out/txt' in current working directory.")
    
    parser.add_argument("--version", 
                       action="version", 
                       version=f"TitleExtractor v{__version__}")
    
    args = parser.parse_args()
    
    extractor = TitleExtractor(args.input_path, args.output)
    
    if os.path.isfile(args.input_path):
        # Process single file
        if extractor.process_file(args.input_path):
            logging.info("Successfully processed single file.")
        else:
            logging.error("Failed to process single file.")
            sys.exit(1)
            
    elif os.path.isdir(args.input_path):
        # Process directory
        logging.info(f"Starting title extraction from directory: {args.input_path}")
        if args.recursive:
            logging.info("Processing recursively...")
            
        success_count, total_count = extractor.process_directory(args.input_path, args.recursive)
        
        logging.info(f"Title extraction complete. Processed {success_count}/{total_count} files successfully.")
        
        if success_count == 0:
            logging.warning("No files were successfully processed.")
            sys.exit(1)
            
    else:
        logging.error(f"Input path not found: {args.input_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()

"""
CHANGELOG:
| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.3  | 2026-02-07 | Added comprehensive changelog section with proper version tracking and stakeholder documentation | AI Coder | Ensure framework compliance with version changelog update rule and provide complete change traceability |
| V1.0.2  | 2026-02-07 | Updated regex pattern to allow all heading levels (1...n) instead of limiting to 1-3 levels | AI Coder | Allow extraction of all markdown heading levels for comprehensive analysis |
| V1.0.1  | 2026-02-07 | Fixed import issues and regex pattern to match all heading levels (1-6) | AI Coder | Ensure compatibility with test suite and extract all title levels |
| V1.0.0  | 2026-02-07 | Initial creation | AI Coder | Extract title lines from Markdown files for analysis and indexing |
"""
