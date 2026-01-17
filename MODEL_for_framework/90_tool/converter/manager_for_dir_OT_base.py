"""
Manager for Directory of Type Base
===================================

A shared module for managing base directory operations across converter tools.
This module provides centralized handling of project base paths, output directories,
and path generation logic used by various converters in the MODEL_for_framework.

CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.1.0  | 2026-01-17 | Added logging functionality with generate_log_path and write_log methods, updated validation to include log directory | Framework Steward | Enable centralized logging support for framework tools using out/log directory structure |
| V1.0.0  | 2026-01-13 | Initial creation with base directory management functionality | Framework Steward | Extract common base directory logic from converter tools for better maintainability and reusability |
"""

import os
import logging
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ManagerForDirOTBase:
    """
    Manages base directory operations for converter tools.

    This class provides centralized handling of:
    - Project base path resolution
    - Output directory structure
    - Path generation relative to project base
    - Directory creation utilities
    """

    def __init__(self, project_base: Optional[str] = None):
        """
        Initialize the base directory manager.

        Args:
            project_base: Custom project base path. If None, uses environment variable
                         or default path.
        """
        # Use environment variable if available, otherwise use default
        if project_base is None:
            project_base = os.getenv('PROJECT_BASE_PATH', r"E:\2025_11\_29")

        self.project_base = os.path.abspath(project_base)
        # Fixed output directory: <PROJECT_BASE_PATH>\out\html
        self.output_root = os.path.join(self.project_base, "out", "html")
        # Fixed log directory: <PROJECT_BASE_PATH>\out\log
        self.log_root = os.path.join(self.project_base, "out", "log")

        logging.info(f"ManagerForDirOTBase initialized with project_base: {self.project_base}")
        logging.info(f"Output root directory: {self.output_root}")
        logging.info(f"Log root directory: {self.log_root}")

    def get_project_base(self) -> str:
        """
        Get the absolute path of the project base directory.

        Returns:
            str: Absolute path to project base directory
        """
        return self.project_base

    def get_output_root(self) -> str:
        """
        Get the absolute path of the output root directory.

        Returns:
            str: Absolute path to output root directory
        """
        return self.output_root

    def get_log_root(self) -> str:
        """
        Get the absolute path of the log root directory.

        Returns:
            str: Absolute path to log root directory
        """
        return self.log_root

    def generate_html_path(self, input_path: str) -> str:
        """
        Generate the output HTML path, mirroring the source directory structure
        relative to the project base within the fixed output directory.

        Args:
            input_path: Absolute path to the input file

        Returns:
            str: Absolute path to the output HTML file
        """
        try:
            # Ensure input path is absolute
            abs_input_path = os.path.abspath(input_path)

            # Calculate relative path from project base
            relative_path = os.path.relpath(abs_input_path, self.project_base)

            # Handle case where paths are on different drives
            if relative_path.startswith('..'):
                # Use just the filename in this case
                base = os.path.splitext(os.path.basename(abs_input_path))[0]
                return os.path.join(self.output_root, f"{base}.html")

            # Generate HTML path maintaining directory structure
            base, _ = os.path.splitext(relative_path)
            return os.path.join(self.output_root, f"{base}.html")

        except ValueError as e:
            logging.warning(f"Could not calculate relative path for {input_path}: {e}")
            # Fallback: use just the filename
            base = os.path.splitext(os.path.basename(input_path))[0]
            return os.path.join(self.output_root, f"{base}.html")

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
            logging.error(f"Failed to create output directory {output_dir}: {e}")
            return False

    def generate_log_path(self, log_name: str = "client.log") -> str:
        """
        Generate the log file path within the log root directory.

        Args:
            log_name: Name of the log file (default: client.log)

        Returns:
            str: Absolute path to the log file
        """
        return os.path.join(self.log_root, log_name)

    def write_log(self, message: str, log_name: str = "client.log", mode: str = "a") -> bool:
        """
        Write a message to the specified log file.

        Args:
            message: Message to write to the log
            log_name: Name of the log file (default: client.log)
            mode: File mode ('a' for append, 'w' for write)

        Returns:
            bool: True if successful, False otherwise
        """
        log_path = self.generate_log_path(log_name)

        # Ensure log directory exists
        if not self.ensure_output_directory(log_path):
            return False

        try:
            with open(log_path, mode, encoding='utf-8') as f:
                f.write(message + '\n')
            return True
        except OSError as e:
            logging.error(f"Failed to write to log file {log_path}: {e}")
            return False

    def is_within_project(self, file_path: str) -> bool:
        """
        Check if a file path is within the project base directory.

        Args:
            file_path: Absolute or relative path to check

        Returns:
            bool: True if the path is within the project base, False otherwise
        """
        abs_file_path = os.path.abspath(file_path)
        try:
            # Check if the file path starts with the project base path
            return abs_file_path.startswith(self.project_base)
        except ValueError:
            return False

    def get_relative_path(self, file_path: str) -> str:
        """
        Get the path relative to the project base.

        Args:
            file_path: Absolute path to the file

        Returns:
            str: Relative path from project base, or original path if calculation fails
        """
        try:
            return os.path.relpath(file_path, self.project_base)
        except ValueError:
            logging.warning(f"Could not calculate relative path for {file_path}")
            return file_path

    def validate_project_structure(self) -> dict:
        """
        Validate that the expected project structure exists.

        Returns:
            dict: Validation results with status and details
        """
        validation_results = {
            'project_base_exists': os.path.exists(self.project_base),
            'project_base_is_dir': os.path.isdir(self.project_base) if os.path.exists(self.project_base) else False,
            'output_root_exists': os.path.exists(self.output_root),
            'output_root_is_dir': os.path.isdir(self.output_root) if os.path.exists(self.output_root) else False,
            'log_root_exists': os.path.exists(self.log_root),
            'log_root_is_dir': os.path.isdir(self.log_root) if os.path.exists(self.log_root) else False,
            'can_create_output': False,
            'can_create_log': False
        }

        # Test if we can create the output directory
        if not validation_results['output_root_exists']:
            try:
                os.makedirs(self.output_root, exist_ok=True)
                validation_results['can_create_output'] = True
                # Clean up the test directory
                if not os.listdir(self.output_root):
                    os.rmdir(self.output_root)
            except OSError:
                validation_results['can_create_output'] = False
        else:
            validation_results['can_create_output'] = True

        # Test if we can create the log directory
        if not validation_results['log_root_exists']:
            try:
                os.makedirs(self.log_root, exist_ok=True)
                validation_results['can_create_log'] = True
                # Clean up the test directory
                if not os.listdir(self.log_root):
                    os.rmdir(self.log_root)
            except OSError:
                validation_results['can_create_log'] = False
        else:
            validation_results['can_create_log'] = True

        return validation_results

    def get_project_info(self) -> dict:
        """
        Get information about the current project configuration.

        Returns:
            dict: Project configuration information
        """
        return {
            'project_base': self.project_base,
            'output_root': self.output_root,
            'log_root': self.log_root,
            'env_project_base': os.getenv('PROJECT_BASE_PATH'),
            'validation': self.validate_project_structure()
        }


# Convenience function for quick access
def create_manager(project_base: Optional[str] = None) -> ManagerForDirOTBase:
    """
    Create a ManagerForDirOTBase instance.

    Args:
        project_base: Optional custom project base path

    Returns:
        ManagerForDirOTBase: Configured manager instance
    """
    return ManagerForDirOTBase(project_base)
