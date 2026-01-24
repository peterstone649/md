#!/usr/bin/env python3
"""
Processor for File Output
=========================

Processes files from the _processing directory, outputs their contents to console,
and moves them to model-specific directories.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import os
import sys
import shutil
import argparse
import logging
from pathlib import Path
from typing import Optional

# Add converter path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'converter'))
from manager_for_dir_OT_base import ManagerForDirOTBase

__version__ = "1.0.0"
__status__ = "ACTIVE"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProcessorForFileOutput:
    """
    Processes files from _processing directory and moves them to model directories.
    """

    def __init__(self, manager: Optional[ManagerForDirOTBase] = None, model: str = "cline", quiet: bool = False):
        """
        Initialize the processor.

        Args:
            manager: Directory manager instance (optional)
            model: Target model directory name (default: "cline")
            quiet: Suppress output messages if True
        """
        self.quiet = quiet

        # Temporarily suppress logging for manager initialization if quiet
        if self.quiet:
            logging.disable(logging.INFO)

        self.manager = manager or ManagerForDirOTBase()
        self.base_dir = self.manager.get_project_base()
        self.model = model

        # Re-enable logging after manager initialization
        if self.quiet:
            logging.disable(logging.NOTSET)

        # Define paths
        self.processing_dir = os.path.join(self.base_dir, "MODEL_for_framework", "in", "_processing")
        self.model_dir = os.path.join(self.base_dir, "MODEL_for_framework", "out", model)

        # Ensure directories exist
        os.makedirs(self.processing_dir, exist_ok=True)
        os.makedirs(self.model_dir, exist_ok=True)

        if not self.quiet:
            logger.info(f"Processor initialized with processing_dir: {self.processing_dir}")
            logger.info(f"Processor initialized with model_dir: {self.model_dir}")

    def process_files(self) -> int:
        """
        Process all files in the processing directory.

        Returns:
            int: Number of files processed
        """
        processed_count = 0

        try:
            # Get all files in processing directory
            for filename in os.listdir(self.processing_dir):
                file_path = os.path.join(self.processing_dir, filename)

                # Skip directories
                if os.path.isdir(file_path):
                    continue

                # Process the file
                if self._process_single_file(file_path):
                    processed_count += 1

        except Exception as e:
            logger.error(f"Error processing files: {e}")

        return processed_count

    def _process_single_file(self, file_path: str) -> bool:
        """
        Process a single file: output contents and move to model directory.

        Args:
            file_path: Path to the file to process

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            filename = os.path.basename(file_path)

            if not self.quiet:
                # Output file information
                print(f"\n--- Processing file: {filename} ---")

            # Always output file contents (as per requirements)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(content)

            # Move file to model directory
            destination_path = os.path.join(self.model_dir, filename)
            shutil.move(file_path, destination_path)

            if not self.quiet:
                print(f"--- Moved to: {destination_path} ---")
                logger.info(f"Processed and moved file '{filename}' to model directory")

            return True

        except Exception as e:
            if not self.quiet:
                logger.error(f"Failed to process file '{file_path}': {e}")
                print(f"Error processing file '{file_path}': {e}")
            return False

    def run_once(self) -> int:
        """
        Run processing once.

        Returns:
            int: Number of files processed
        """
        if not self.quiet:
            logger.info("Running file processing")
        processed = self.process_files()
        if not self.quiet:
            logger.info(f"Processing complete: {processed} files processed")
        return processed

def main():
    """Main function for the processor."""
    parser = argparse.ArgumentParser(
        description="Processor for File Output - Processes files from _processing directory"
    )
    parser.add_argument(
        '--model',
        default='cline',
        help='Target model directory name (default: cline)'
    )
    parser.add_argument(
        '--project-base',
        help='Custom project base path'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Suppress output messages and logging'
    )

    args = parser.parse_args()

    # Create manager
    manager = ManagerForDirOTBase(args.project_base) if args.project_base else None

    # Create processor
    processor = ProcessorForFileOutput(manager, args.model, args.quiet)

    # Run processing
    processed = processor.run_once()
    if not args.quiet:
        print(f"\nTotal files processed: {processed}")

if __name__ == "__main__":
    main()

## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | 2026-01-24 | Initial creation | Framework Maintenance Team | Establish foundational structure |
