#!/usr/bin/env python3
"""
Analyser for Words in Files
===========================

Extracts unique words from file contents and outputs them as an alphabetically ordered CSV file.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import os
import sys
import csv
import re
import argparse
import logging
from typing import List, Set
from pathlib import Path

# Add converter path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'converter'))
from manager_for_dir_OT_base import ManagerForDirOTBase

# Import word filter
from handler_for_word_filter import WordFilter

__version__ = "1.0.0"
__status__ = "ACTIVE"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AnalyserForWordsInFiles:
    """
    Analyses files to extract unique words and save them as CSV.
    """

    def __init__(self, manager: ManagerForDirOTBase = None, word_filter: WordFilter = None):
        """
        Initialize the analyser.

        Args:
            manager: Directory manager instance (optional)
            word_filter: Word filter instance (optional)
        """
        self.manager = manager or ManagerForDirOTBase()
        self.base_dir = self.manager.get_project_base()
        # Use out/word instead of out/html
        self.output_root = os.path.join(self.base_dir, "out", "word")

        # Initialize word filter
        if word_filter is None:
            word_filter_config = os.path.join(os.path.dirname(__file__), "word_filter.yaml")
            self.word_filter = WordFilter(word_filter_config)
        else:
            self.word_filter = word_filter

        # Ensure output directory exists
        os.makedirs(self.output_root, exist_ok=True)

        logger.info(f"Analyser initialized with base_dir: {self.base_dir}")
        logger.info(f"Output root directory: {self.output_root}")

    def is_abbreviation(self, word: str) -> bool:
        """
        Check if a word appears to be an abbreviation based on case patterns.

        Args:
            word: Word to check

        Returns:
            bool: True if word appears to be an abbreviation
        """
        # ALL CAPS abbreviations (2-5 characters)
        if word.isupper() and 2 <= len(word) <= 5:
            return True

        return False

    def extract_words(self, content: str) -> Set[str]:
        """
        Extract unique words from content, filtering out unwanted words based on configuration.

        Args:
            content: Text content to analyse

        Returns:
            Set of unique words
        """
        # Use regex to find words (starting with letter, followed by letters/digits)
        # This filters out numbers and words starting with underscores at the regex level
        words = re.findall(r'\b[a-zA-Z][a-zA-Z0-9]*\b', content)

        # Apply configurable word filtering
        filtered_words = self.word_filter.filter_words(set(words))

        # Apply lemmatization if enabled
        lemmatized_words = self.word_filter.lemmatize_words(filtered_words)

        # Convert to lowercase for case-insensitive uniqueness
        final_words = {word.lower() for word in lemmatized_words}

        return final_words

    def generate_output_path(self, input_path: str) -> str:
        """
        Generate the output CSV path, mirroring the source directory structure
        within the word output directory.

        Args:
            input_path: Absolute path to the input file

        Returns:
            str: Absolute path to the output CSV file
        """
        try:
            # Ensure input path is absolute
            abs_input_path = os.path.abspath(input_path)

            # Calculate relative path from project base
            relative_path = os.path.relpath(abs_input_path, self.base_dir)

            # Handle case where paths are on different drives
            if relative_path.startswith('..'):
                # Use just the filename in this case
                base = os.path.splitext(os.path.basename(abs_input_path))[0]
                return os.path.join(self.output_root, f"{base}.csv")

            # Generate CSV path maintaining directory structure
            base, _ = os.path.splitext(relative_path)
            return os.path.join(self.output_root, f"{base}.csv")

        except ValueError as e:
            logger.warning(f"Could not calculate relative path for {input_path}: {e}")
            # Fallback: use just the filename
            base = os.path.splitext(os.path.basename(input_path))[0]
            return os.path.join(self.output_root, f"{base}.csv")

    def ensure_output_directory(self, output_path: str) -> bool:
        """
        Ensure the output directory exists for the given output path.

        Args:
            output_path: Absolute path to the output file

        Returns:
            bool: True if directory exists or was created successfully, False otherwise
        """
        output_dir = os.path.dirname(output_path)

        try:
            os.makedirs(output_dir, exist_ok=True)
            return True
        except OSError as e:
            logger.error(f"Failed to create output directory {output_dir}: {e}")
            return False

    def analyse_file(self, input_path: str) -> bool:
        """
        Analyse a single file and generate CSV output.

        Args:
            input_path: Path to the input file

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Read file content
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract unique words
            words = self.extract_words(content)

            # Sort alphabetically
            sorted_words = sorted(words)

            # Generate output path
            output_path = self.generate_output_path(input_path)

            # Ensure output directory exists
            if not self.ensure_output_directory(output_path):
                return False

            # Write CSV
            with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Word'])  # Header
                for word in sorted_words:
                    writer.writerow([word])

            logger.info(f"Analysed file '{input_path}' and saved to '{output_path}'")
            return True

        except Exception as e:
            logger.error(f"Failed to analyse file '{input_path}': {e}")
            return False

def main():
    """Main function for the analyser."""
    parser = argparse.ArgumentParser(
        description="Analyser for Words in Files - Extracts unique words from files and saves as CSV"
    )
    parser.add_argument(
        'input_file',
        help='Path to the input file to analyse'
    )
    parser.add_argument(
        '--project-base',
        help='Custom project base path'
    )

    args = parser.parse_args()

    # Create manager
    manager = ManagerForDirOTBase(args.project_base) if args.project_base else None

    # Create analyser
    analyser = AnalyserForWordsInFiles(manager)

    # Analyse the file
    success = analyser.analyse_file(args.input_file)

    if success:
        print(f"Successfully analysed file: {args.input_file}")
    else:
        print(f"Failed to analyse file: {args.input_file}")
        sys.exit(1)

if __name__ == "__main__":
    main()
