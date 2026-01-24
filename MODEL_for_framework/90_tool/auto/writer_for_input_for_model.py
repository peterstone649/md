#!/usr/bin/env python3
"""
Writer for Input for Model
==========================

Monitors incoming files in the input directory, processes them with timestamp names,
and moves them to the processing directory for AI model consumption.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import os
import sys
import shutil
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Set

# Add converter path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'converter'))
from manager_for_dir_OT_base import ManagerForDirOTBase
from converter_for_timestamp import TimestampConverter

__version__ = "1.0.0"
__status__ = "ACTIVE"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WriterForInputForModel:
    """
    Monitors input directory for new files, timestamps them, and moves to processing directory.
    """

    def __init__(self, manager: Optional[ManagerForDirOTBase] = None):
        """
        Initialize the writer.

        Args:
            manager: Directory manager instance (optional)
        """
        self.manager = manager or ManagerForDirOTBase()
        self.base_dir = self.manager.get_project_base()
        self.timestamp_converter = TimestampConverter()

        # Define paths
        self.input_dir = os.path.join(self.base_dir, "MODEL_for_framework", "in")
        self.processing_dir = os.path.join(self.base_dir, "MODEL_for_framework", "in", "_processing")

        # Ensure directories exist
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.processing_dir, exist_ok=True)

        # Track processed files
        self.processed_files: Set[str] = set()

        logger.info(f"Writer initialized with input_dir: {self.input_dir}")
        logger.info(f"Writer initialized with processing_dir: {self.processing_dir}")

    def generate_timestamp_name(self, original_filename: str) -> str:
        """
        Generate a timestamp-based filename using the timestamp converter.

        Args:
            original_filename: Original filename

        Returns:
            Timestamped filename
        """
        return self.timestamp_converter.generate_filename_timestamp(original_filename)

    def move_file_to_processing(self, file_path: str) -> bool:
        """
        Move a file to the processing directory with timestamp name.

        Args:
            file_path: Path to the file to move

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            filename = os.path.basename(file_path)
            timestamped_name = self.generate_timestamp_name(filename)
            destination_path = os.path.join(self.processing_dir, timestamped_name)

            shutil.move(file_path, destination_path)

            logger.info(f"Moved file '{filename}' to '{timestamped_name}' in processing directory")
            return True

        except Exception as e:
            logger.error(f"Failed to move file '{file_path}': {e}")
            return False

    def scan_and_process_files(self) -> int:
        """
        Scan input directory for new files and process them.

        Returns:
            int: Number of files processed
        """
        processed_count = 0

        try:
            # Get all files in input directory
            for filename in os.listdir(self.input_dir):
                file_path = os.path.join(self.input_dir, filename)

                # Skip directories and already processed files
                if os.path.isdir(file_path) or filename in self.processed_files:
                    continue

                # Process the file
                if self.move_file_to_processing(file_path):
                    self.processed_files.add(filename)
                    processed_count += 1

        except Exception as e:
            logger.error(f"Error scanning input directory: {e}")

        return processed_count

    def run_continuous_monitor(self, interval: float = 1.0):
        """
        Run continuous monitoring of the input directory.

        Args:
            interval: Time interval between scans in seconds
        """
        logger.info(f"Starting continuous monitoring with {interval}s interval")

        try:
            while True:
                processed = self.scan_and_process_files()
                if processed > 0:
                    logger.info(f"Processed {processed} files in this scan")

                time.sleep(interval)

        except KeyboardInterrupt:
            logger.info("Monitoring stopped by user")
        except Exception as e:
            logger.error(f"Error in continuous monitoring: {e}")

    def run_single_scan(self) -> int:
        """
        Run a single scan of the input directory.

        Returns:
            int: Number of files processed
        """
        logger.info("Running single scan")
        processed = self.scan_and_process_files()
        logger.info(f"Single scan complete: {processed} files processed")
        return processed

def main():
    """Main function for the writer."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Writer for Input for Model - Monitors and processes input files"
    )
    parser.add_argument(
        '--continuous',
        action='store_true',
        help='Run continuous monitoring instead of single scan'
    )
    parser.add_argument(
        '--interval',
        type=float,
        default=1.0,
        help='Scan interval in seconds for continuous mode (default: 1.0)'
    )
    parser.add_argument(
        '--project-base',
        help='Custom project base path'
    )

    args = parser.parse_args()

    # Create manager
    manager = ManagerForDirOTBase(args.project_base) if args.project_base else None

    # Create writer
    writer = WriterForInputForModel(manager)

    if args.continuous:
        writer.run_continuous_monitor(args.interval)
    else:
        processed = writer.run_single_scan()
        print(f"Processed {processed} files")

if __name__ == "__main__":
    main()

## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | 2026-01-24 | Initial creation | Framework Maintenance Team | Establish foundational structure |
