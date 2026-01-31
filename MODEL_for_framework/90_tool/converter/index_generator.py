#!/usr/bin/env python3
"""
Index Generator for Folder Links

This tool creates index.md and index.html files for folders that are targets of links.
When a folder is linked in documentation, this tool generates an index file that lists
all files in that folder with clickable links, making navigation easier.

Usage:
    python index_generator.py <folder_path> [--recursive] [--output-format md|html|both]

Features:
- Generates index files for folders targeted by links
- Creates clickable navigation for folder contents
- Supports both Markdown and HTML output formats
- Recursive processing option for nested folders
- Automatic detection of existing index files
- Preserves folder structure and hierarchy
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime
import logging

# Import the shared directory manager for consistent output paths
from manager_for_dir_OT_base import ManagerForDirOTBase

__version__ = "1.2.0"
__status__ = "ACTIVE"

"""
CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.2.0  | 2026-01-31 | Updated to use ManagerForDirOTBase for consistent output path creation | Framework Steward | Align with framework conventions and ensure consistent output directory structure |
| V1.1.0  | 2026-01-31 | Added comprehensive changelog following framework conventions | Framework Steward | Align with framework documentation standards and provide clear version history |
| V1.0.0  | 2026-01-31 | Initial implementation with README-driven index creation | AI Coder | Core functionality for generating index files when README files exist |
"""

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class IndexGenerator:
    def __init__(self, project_base=None):
        """Initialize the index generator with optional project base path."""
        # Use the shared directory manager for consistent path handling
        self.dir_manager = ManagerForDirOTBase(project_base)
        self.created_files = []
        self.updated_files = []

    def generate_index_content(self, folder_path, format='md'):
        """
        Generate index content for a folder.

        Args:
            folder_path (Path): Path to the folder
            format (str): Output format ('md' or 'html')

        Returns:
            str: Generated index content
        """
        folder_path = Path(folder_path)
        files = []
        subfolders = []

        # Get all files and subfolders
        for item in folder_path.iterdir():
            if item.is_file() and item.name not in ['index.md', 'index.html']:
                files.append(item)
            elif item.is_dir():
                subfolders.append(item)

        # Sort files and folders
        files.sort()
        subfolders.sort()

        if format == 'md':
            return self._generate_markdown_index(folder_path, files, subfolders)
        else:
            return self._generate_html_index(folder_path, files, subfolders)

    def _generate_markdown_index(self, folder_path, files, subfolders):
        """Generate Markdown index content."""
        try:
            relative_path = folder_path.relative_to(self.dir_manager.get_project_base())
            title = f"Index of {relative_path}"
        except ValueError:
            # If folder_path is not relative to project base, use the folder name
            title = f"Index of {folder_path.name}"

        # Check for README file to use as jump address (supports *README* pattern)
        import glob
        readme_pattern = '*README*'
        readme_files = list(folder_path.glob(readme_pattern))
        readme_file = None
        if readme_files:
            # Use the first README file found
            readme_file = readme_files[0].name

        content = f"""# {title}

This folder contains the following files and subdirectories:

"""
        # If README exists, make it the primary jump address
        if readme_file:
            content += f"## [📁 {readme_file}]({readme_file})\n\n"
            content += f"*Jump to main documentation for this folder*\n\n"
            content += "---\n\n"

        content += "## Files\n\n"
        
        # Add files list (excluding README if it exists)
        if files:
            for file in files:
                if readme_file and file.name.lower() in [r.name.lower() for r in readme_files]:
                    continue  # Skip README as it's already featured
                content += f"- [{file.name}]({file.name})\n"
        else:
            content += "No files in this directory.\n"

        # Add subfolders list
        content += "\n## Subdirectories\n\n"
        if subfolders:
            for subfolder in subfolders:
                content += f"- [{subfolder.name}/]({subfolder.name}/)\n"
        else:
            content += "No subdirectories.\n"

        # Add footer
        content += f"\n---\n*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} by IndexGenerator v{__version__}*"

        return content

    def _generate_html_index(self, folder_path, files, subfolders):
        """Generate HTML index content."""
        try:
            relative_path = folder_path.relative_to(self.dir_manager.get_project_base())
            title = f"Index of {relative_path}"
        except ValueError:
            # If folder_path is not relative to project base, use the folder name
            title = f"Index of {folder_path.name}"

        # Check for README file to use as jump address (supports *README* pattern)
        import glob
        readme_pattern = '*README*'
        readme_files = list(folder_path.glob(readme_pattern))
        readme_file = None
        if readme_files:
            # Use the first README file found
            readme_file = readme_files[0].name

        content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            margin: 2em;
            color: #333;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 2px solid #eee;
            padding-bottom: 0.5em;
        }}
        h2 {{
            color: #3498db;
            margin-top: 1.5em;
        }}
        .readme-jump {{
            background-color: #eaf4ff;
            border-left: 4px solid #3498db;
            padding: 1em;
            margin: 1em 0;
        }}
        .readme-jump h3 {{
            margin-top: 0;
            color: #2c3e50;
        }}
        ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        li {{
            margin: 0.5em 0;
        }}
        a {{
            color: #2980b9;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .footer {{
            margin-top: 2em;
            font-size: 0.8em;
            color: #7f8c8d;
            border-top: 1px solid #eee;
            padding-top: 1em;
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>

    <p>This folder contains the following files and subdirectories:</p>

"""
        # If README exists, make it the primary jump address
        if readme_file:
            content += f"""    <div class="readme-jump">
        <h3>📁 <a href="{readme_file}">{readme_file}</a></h3>
        <p><em>Jump to main documentation for this folder</em></p>
    </div>

    <hr>

"""

        content += "    <h2>Files</h2>\n    <ul>\n"
        
        # Add files list (excluding README if it exists)
        if files:
            for file in files:
                if readme_file and file.name.lower() in [r.name.lower() for r in readme_files]:
                    continue  # Skip README as it's already featured
                content += f"        <li><a href=\"{file.name}\">{file.name}</a></li>\n"
        else:
            content += "        <li>No files in this directory.</li>\n"

        content += "    </ul>\n\n    <h2>Subdirectories</h2>\n    <ul>\n"
        # Add subfolders list
        if subfolders:
            for subfolder in subfolders:
                content += f"        <li><a href=\"{subfolder.name}/\">{subfolder.name}/</a></li>\n"
        else:
            content += "        <li>No subdirectories.</li>\n"

        content += f"""    </ul>

    <div class=\"footer\">
        Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} by IndexGenerator v{__version__}
    </div>
</body>
</html>
"""
        return content

    def create_index_files(self, folder_path, format='both', recursive=False):
        """
        Create index files for a folder.

        Args:
            folder_path (str): Path to the folder
            format (str): Output format ('md', 'html', or 'both')
            recursive (bool): Whether to process subfolders recursively
        """
        folder_path = Path(folder_path)

        if not folder_path.exists():
            logging.error(f"Folder does not exist: {folder_path}")
            return False

        if not folder_path.is_dir():
            logging.error(f"Path is not a directory: {folder_path}")
            return False

        logging.info(f"Processing folder: {folder_path}")

        # Create index files for this folder
        if format in ['md', 'both']:
            self._create_single_index(folder_path, 'md')
        if format in ['html', 'both']:
            self._create_single_index(folder_path, 'html')

        # Process subfolders recursively
        if recursive:
            for subfolder in folder_path.iterdir():
                if subfolder.is_dir():
                    # Skip hidden directories
                    if subfolder.name.startswith('.'):
                        continue
                    self.create_index_files(subfolder, format, recursive)

        return True

    def _create_single_index(self, folder_path, format):
        """Create a single index file."""
        if format == 'md':
            # MD files go in the same folder as the README
            index_file = folder_path / 'index.md'
            extension = 'md'
        else:
            # HTML files go to the standardized output directory
            index_file_path = self.dir_manager.generate_html_path(str(folder_path / 'index.html'))
            index_file = Path(index_file_path)
            extension = 'html'
            
            # Ensure the output directory exists
            self.dir_manager.ensure_output_directory(index_file_path)

        # Check if index file already exists
        if index_file.exists():
            logging.warning(f"Index file already exists: {index_file}")
            return

        # Check if README file exists in the folder (supports *README* pattern)
        import glob
        readme_pattern = '*README*'
        readme_files = list(folder_path.glob(readme_pattern))
        readme_exists = len(readme_files) > 0
        
        # Only create index.md if README exists (this is the key change)
        if not readme_exists and format == 'md':
            logging.info(f"No README file exists in {folder_path}, skipping index.md generation")
            return

        # Generate content and write to file
        content = self.generate_index_content(folder_path, format)

        try:
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content)
            logging.info(f"Created {extension.upper()} index: {index_file}")
            self.created_files.append(index_file)
        except IOError as e:
            logging.error(f"Failed to create index file {index_file}: {e}")

    def process_folder_links(self, root_path, format='both'):
        """
        Process all folders that might be targets of links.

        Args:
            root_path (str): Root path to search for folders
            format (str): Output format ('md', 'html', or 'both')
        """
        root_path = Path(root_path)

        if not root_path.exists():
            logging.error(f"Root path does not exist: {root_path}")
            return False

        # Find all directories that might need index files
        for folder_path, dirs, files in os.walk(root_path):
            folder_path = Path(folder_path)

            # Skip hidden directories
            if any(part.startswith('.') for part in folder_path.parts):
                continue

            # Create index files for this folder
            self.create_index_files(folder_path, format, False)

        return True

def main():
    """Main function to handle command line interface."""
    parser = argparse.ArgumentParser(
        description="Generate index files for folders that are targets of links.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "folder_path",
        help="Path to the folder or root directory to process"
    )
    parser.add_argument(
        "--format",
        choices=['md', 'html', 'both'],
        default='both',
        help="Output format (default: both)"
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Process subfolders recursively"
    )
    parser.add_argument(
        "--process-links",
        action="store_true",
        help="Process all folders that might be targets of links"
    )

    args = parser.parse_args()

    # Initialize generator
    generator = IndexGenerator()

    if args.process_links:
        # Process all folders that might be link targets
        generator.process_folder_links(args.folder_path, args.format)
    else:
        # Process specific folder
        generator.create_index_files(args.folder_path, args.format, args.recursive)

    # Summary
    logging.info(f"Index generation complete. Created {len(generator.created_files)} files.")

    if generator.created_files:
        logging.info("Created files:")
        for file in generator.created_files:
            logging.info(f"  - {file}")

def generate_index_for_folder(folder_path, format='both', project_base=None):
    """
    Direct function call for generating index files.
    This allows the index generator to be called programmatically from other tools.

    Args:
        folder_path (str): Path to the folder
        format (str): Output format ('md', 'html', or 'both')
        project_base (str): Optional project base path for consistent output directory structure

    Returns:
        bool: True if successful, False otherwise
    """
    generator = IndexGenerator(project_base)
    return generator.create_index_files(folder_path, format, recursive=False)

if __name__ == "__main__":
    main()
