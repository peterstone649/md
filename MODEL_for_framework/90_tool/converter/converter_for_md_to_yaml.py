#!/usr/bin/env python3
"""
MD to YAML Converter
====================

A specialized tool to convert Markdown files to YAML format,
designed specifically for the MODEL_for_framework structured documentation.

This tool extracts structured data from Markdown files and converts them
to YAML format for use in configuration files, manifests, and structured data storage.
"""

import os
import sys
import argparse
import re
import yaml
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from manager_for_dir_OT_base import ManagerForDirOTBase

__version__ = "1.0.0"
__status__ = "ACTIVE"

"""
CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-01-13 | Initial release with full MD to YAML conversion functionality | Framework Steward | Provide comprehensive MD to YAML conversion for MODEL_for_framework structured documentation |
"""

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ConverterForMdToYaml:
    """Converts Markdown files to YAML format."""

    def __init__(self, input_path: str, project_base: str = None):
        self.input_path = os.path.abspath(input_path)
        # Use the shared base directory manager
        self.dir_manager = ManagerForDirOTBase(project_base)
        # Fixed output directory: <PROJECT_BASE_PATH>\out\yaml
        self.output_root = os.path.join(self.dir_manager.get_project_base(), "out", "yaml")
        self.stats = {
            'success': 0,
            'failed': 0,
            'processed_files': []
        }

    def _generate_yaml_path(self) -> str:
        """
        Generates the output YAML path using the shared directory manager.
        """
        # Use the shared directory manager to generate the path
        html_path = self.dir_manager.generate_html_path(self.input_path)
        # Replace .html extension with .yaml
        return html_path.replace('.html', '.yaml')

    def _parse_markdown_structure(self, content: str) -> Dict[str, Any]:
        """
        Parse Markdown content and extract structured data.
        """
        lines = content.split('\n')
        result = {
            'metadata': {},
            'title': '',
            'sections': [],
            'tables': [],
            'lists': [],
            'code_blocks': []
        }

        current_section = None
        in_code_block = False
        code_block_lang = ''
        code_block_content = []

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Handle code blocks
            if line.startswith('```'):
                if not in_code_block:
                    in_code_block = True
                    code_block_lang = line[3:].strip()
                    code_block_content = []
                else:
                    in_code_block = False
                    result['code_blocks'].append({
                        'language': code_block_lang,
                        'content': '\n'.join(code_block_content)
                    })
                i += 1
                continue

            if in_code_block:
                code_block_content.append(lines[i])
                i += 1
                continue

            # Parse title (first # heading)
            if not result['title'] and line.startswith('# '):
                result['title'] = line[2:].strip()
                i += 1
                continue

            # Parse sections (headings)
            if line.startswith('#'):
                level = len(line) - len(line.lstrip('#'))
                title = line[level:].strip()
                current_section = {
                    'level': level,
                    'title': title,
                    'content': []
                }
                result['sections'].append(current_section)
                i += 1
                continue

            # Parse tables
            if '|' in line and i + 1 < len(lines) and '|' in lines[i + 1] and re.match(r'^\s*\|[\s\-\|:]+\|\s*$', lines[i + 1]):
                table_data = self._parse_table(lines, i)
                if table_data:
                    result['tables'].append(table_data)
                    i = table_data['end_line'] + 1
                    continue

            # Parse lists
            if line.startswith(('- ', '* ', '+ ', '1. ', '2. ', '3. ')):
                list_data = self._parse_list(lines, i)
                if list_data:
                    result['lists'].append(list_data)
                    i = list_data['end_line'] + 1
                    continue

            # Add content to current section
            if current_section is not None and line:
                current_section['content'].append(line)

            i += 1

        return result

    def _parse_table(self, lines: List[str], start_idx: int) -> Optional[Dict[str, Any]]:
        """
        Parse a Markdown table starting from the given line index.
        """
        if start_idx + 2 >= len(lines):
            return None

        # Check if this looks like a table
        header_line = lines[start_idx].strip()
        separator_line = lines[start_idx + 1].strip()

        if not ('|' in header_line and '|' in separator_line):
            return None

        # Parse headers
        headers = [col.strip() for col in header_line.split('|')[1:-1]]

        # Parse rows
        rows = []
        i = start_idx + 2
        while i < len(lines) and '|' in lines[i]:
            row_data = [col.strip() for col in lines[i].strip().split('|')[1:-1]]
            if len(row_data) == len(headers):
                rows.append(row_data)
            i += 1

        return {
            'headers': headers,
            'rows': rows,
            'start_line': start_idx,
            'end_line': i - 1
        }

    def _parse_list(self, lines: List[str], start_idx: int) -> Optional[Dict[str, Any]]:
        """
        Parse a Markdown list starting from the given line index.
        """
        items = []
        i = start_idx

        while i < len(lines):
            line = lines[i].strip()
            if not line.startswith(('- ', '* ', '+ ', '1. ', '2. ', '3. ')):
                break

            # Remove the list marker
            if line.startswith(('- ', '* ', '+ ')):
                item_content = line[2:].strip()
            else:
                # Ordered list
                item_content = re.sub(r'^\d+\.\s+', '', line).strip()

            items.append(item_content)
            i += 1

        if not items:
            return None

        return {
            'items': items,
            'start_line': start_idx,
            'end_line': i - 1
        }

    def _convert_to_yaml_structure(self, parsed_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert parsed Markdown data to a structured YAML format.
        """
        yaml_data = {
            'document_info': {
                'title': parsed_data['title'],
                'source_file': os.path.basename(self.input_path),
                'conversion_date': datetime.now().isoformat(),
                'converter_version': __version__
            },
            'content': {}
        }

        # Add sections
        if parsed_data['sections']:
            yaml_data['content']['sections'] = []
            for section in parsed_data['sections']:
                yaml_data['content']['sections'].append({
                    'level': section['level'],
                    'title': section['title'],
                    'content': section['content']
                })

        # Add tables
        if parsed_data['tables']:
            yaml_data['content']['tables'] = []
            for table in parsed_data['tables']:
                yaml_data['content']['tables'].append({
                    'headers': table['headers'],
                    'rows': table['rows']
                })

        # Add lists
        if parsed_data['lists']:
            yaml_data['content']['lists'] = []
            for list_data in parsed_data['lists']:
                yaml_data['content']['lists'].append({
                    'items': list_data['items']
                })

        # Add code blocks
        if parsed_data['code_blocks']:
            yaml_data['content']['code_blocks'] = parsed_data['code_blocks']

        return yaml_data

    def convert(self) -> bool:
        """
        Executes the conversion from Markdown to YAML.
        """
        if not os.path.isfile(self.input_path):
            logging.error(f"Input file not found: {self.input_path}")
            return False

        if not self.input_path.endswith(('.md', '.markdown')):
            logging.error(f"Input file is not a Markdown file: {self.input_path}")
            return False

        yaml_path = self._generate_yaml_path()
        output_dir = os.path.dirname(yaml_path)

        try:
            # Read Markdown file
            with open(self.input_path, 'r', encoding='utf-8') as f:
                md_content = f.read()

            # Parse Markdown structure
            parsed_data = self._parse_markdown_structure(md_content)

            # Convert to YAML structure
            yaml_data = self._convert_to_yaml_structure(parsed_data)

            # Write YAML file
            os.makedirs(output_dir, exist_ok=True)
            with open(yaml_path, 'w', encoding='utf-8') as f:
                yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

            logging.info(f"Successfully converted '{self.input_path}' to '{yaml_path}'")
            self.stats['success'] += 1
            self.stats['processed_files'].append({
                'input': self.input_path,
                'output': yaml_path,
                'status': 'success'
            })
            return True

        except Exception as e:
            logging.error(f"Error processing {self.input_path}: {e}")
            self.stats['failed'] += 1
            self.stats['processed_files'].append({
                'input': self.input_path,
                'output': None,
                'status': 'failed',
                'error': str(e)
            })
            return False

def main():
    parser = argparse.ArgumentParser(
        description="Converts Markdown files to YAML format with fixed output directory for MODEL_for_framework.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("input_path", help="Path to a Markdown file or a directory containing Markdown files.")
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="If input_path is a directory, process all Markdown files recursively."
    )
    parser.add_argument(
        "--project-base",
        default=None,
        help="The project base path for calculating relative output paths. Defaults to PROJECT_BASE_PATH from .env file or 'E:\\2025_11\\_29'."
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Display a summary report after conversion."
    )

    args = parser.parse_args()

    converter = ConverterForMdToYaml(args.input_path, args.project_base)

    if os.path.isdir(args.input_path):
        if not args.recursive:
            print("Error: Input path is a directory, but --recursive flag was not provided.")
            sys.exit(1)

        logging.info(f"Starting recursive MD to YAML conversion in directory: {args.input_path}")

        md_files = []
        for root, _, files in os.walk(args.input_path):
            for file in files:
                if file.endswith(('.md', '.markdown')):
                    md_files.append(os.path.join(root, file))

        if not md_files:
            logging.warning(f"No Markdown files found in directory: {args.input_path}")
            return

        logging.info(f"Found {len(md_files)} Markdown file(s) to process")

        for md_file in md_files:
            converter.input_path = md_file
            converter.convert()

    elif os.path.isfile(args.input_path):
        if not args.input_path.endswith(('.md', '.markdown')):
            print("Error: Input file does not appear to be a Markdown file.")
            sys.exit(1)

        converter.convert()
    else:
        print(f"Error: Input path not found: {args.input_path}")
        sys.exit(1)

    # Display summary if requested
    if args.summary or converter.stats['failed'] > 0:
        print("\n" + "="*60)
        print("MD TO YAML CONVERSION SUMMARY")
        print("="*60)
        print(f"Files processed: {len(converter.stats['processed_files'])}")
        print(f"Successful: {converter.stats['success']}")
        print(f"Failed: {converter.stats['failed']}")

        if converter.stats['failed'] > 0:
            print("\nFailed files:")
            for file_info in converter.stats['processed_files']:
                if file_info['status'] == 'failed':
                    print(f"  - {file_info['input']}")
                    print(f"    Error: {file_info['error']}")

        print("="*60)

if __name__ == "__main__":
    main()
