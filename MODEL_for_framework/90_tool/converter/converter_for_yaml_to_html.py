#!/usr/bin/env python3
"""
YAML to HTML Converter
A specialized tool to convert YAML files to styled HTML documents,
designed specifically for the MODEL_for_framework user stories and structured data.

This tool extends the existing HTML conversion capabilities to handle YAML files
with structured data including metadata, acceptance criteria, and related documents.
"""

import os
import sys
import argparse
import yaml
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from manager_for_dir_OT_base import ManagerForDirOTBase

__version__ = "1.2.0"
__status__ = "ACTIVE"

"""
CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.2.0  | 2026-01-13 | Renamed file from yaml_to_html_converter.py to converter_for_yaml_to_html.py and updated class name from YAMLToHTMLConverter to ConverterForYamlToHtml | Framework Steward | Align with framework naming conventions and improve consistency |
| V1.1.0  | 2026-01-13 | Adapted fixed output directory structure <PROJECT_BASE_PATH>\out\html | Framework Steward | Standardize HTML output location for consistent deployment and easier maintenance |
| V1.0.0  | 2026-01-10 | Initial release with full YAML to HTML conversion functionality | AI Coder | Provide comprehensive YAML to HTML conversion for MODEL_for_framework user stories |
| V0.1.1  | 2026-01-10 | Updated template metadata to include Framework Version and use list format | AI Coder | To provide more detailed and consistently formatted metadata in new documents |
"""

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ConverterForYamlToHtml:
    """Converts YAML files to styled HTML documents."""

    def __init__(self, input_path: str, project_base: str = None):
        self.input_path = os.path.abspath(input_path)
        # Use the shared base directory manager
        self.dir_manager = ManagerForDirOTBase(project_base)
        # Fixed output directory: <PROJECT_BASE_PATH>\out\html
        self.output_root = self.dir_manager.get_output_root()
        self.stats = {
            'success': 0,
            'failed': 0,
            'processed_files': []
        }

    def _generate_html_path(self) -> str:
        """
        Generates the output HTML path using the shared directory manager.
        """
        return self.dir_manager.generate_html_path(self.input_path)

    def _generate_yaml_html_template(self, yaml_data: Dict[str, Any], file_name: str) -> str:
        """
        Generates a styled HTML template specifically designed for YAML user stories.
        """
        title = yaml_data.get('title', file_name)
        story_id = yaml_data.get('id', 'Unknown')
        priority = yaml_data.get('priority', 'Not specified')

        # Generate metadata section
        metadata_html = self._generate_metadata_html(yaml_data.get('metadata', {}))

        # Generate story section
        story_html = self._generate_story_html(yaml_data.get('story', ''))

        # Generate acceptance criteria section
        acceptance_criteria_html = self._generate_acceptance_criteria_html(
            yaml_data.get('acceptance_criteria', [])
        )

        # Generate related documents section
        related_docs_html = self._generate_related_documents_html(
            yaml_data.get('related_documents', [])
        )

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {story_id}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
            font-size: 14px;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            background-color: #f8f9fa;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .header {{
            border-bottom: 2px solid #007bff;
            padding-bottom: 15px;
            margin-bottom: 25px;
        }}
        .header h1 {{
            color: #007bff;
            margin: 0;
            font-size: 1.8em;
        }}
        .header .subheader {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 10px;
        }}
        .story-id {{
            font-weight: bold;
            color: #6c757d;
        }}
        .priority-badge {{
            background-color: #ffc107;
            color: #212529;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 0.9em;
            font-weight: bold;
        }}
        .priority-high {{
            background-color: #dc3545;
            color: white;
        }}
        .priority-medium {{
            background-color: #ffc107;
            color: #212529;
        }}
        .priority-low {{
            background-color: #28a745;
            color: white;
        }}
        .section {{
            margin-bottom: 30px;
        }}
        .section h2 {{
            color: #007bff;
            border-bottom: 1px solid #dee2e6;
            padding-bottom: 8px;
            margin-top: 0;
        }}
        .metadata-table {{
            width: 100%;
            border-collapse: collapse;
        }}
        .metadata-table th, .metadata-table td {{
            text-align: left;
            padding: 8px;
            border-bottom: 1px solid #dee2e6;
        }}
        .metadata-table th {{
            background-color: #f8f9fa;
            width: 20%;
        }}
        .story-content {{
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            white-space: pre-wrap;
        }}
        .acceptance-criteria {{
            counter-reset: criterion-counter;
        }}
        .criterion {{
            counter-increment: criterion-counter;
            margin-bottom: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 5px;
        }}
        .criterion-title {{
            font-weight: bold;
            color: #007bff;
            margin-bottom: 8px;
        }}
        .criterion-steps {{
            margin-left: 20px;
        }}
        .criterion-steps li {{
            margin-bottom: 5px;
        }}
        .related-documents {{
            list-style: none;
            padding: 0;
        }}
        .related-documents li {{
            margin-bottom: 8px;
            padding-left: 1.2em;
        }}
        .related-documents li:before {{
            content: "📄";
            margin-right: 8px;
            color: #007bff;
        }}
        .related-documents a {{
            color: #007bff;
            text-decoration: none;
        }}
        .related-documents a:hover {{
            text-decoration: underline;
        }}
        footer {{
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #dee2e6;
            font-size: 0.9em;
            color: #6c757d;
            text-align: center;
        }}
        .success-badge {{
            background-color: #28a745;
            color: white;
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <div class="subheader">
                <span class="story-id">ID: {story_id}</span>
                <span class="priority-badge priority-{priority.lower()}">{priority}</span>
            </div>
        </div>

        {metadata_html}
        {story_html}
        {acceptance_criteria_html}
        {related_docs_html}

        <footer>
            <p>Generated from YAML on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} by ConverterForYamlToHtml v{__version__}</p>
        </footer>
    </div>
</body>
</html>"""

    def _generate_metadata_html(self, metadata: Dict[str, Any]) -> str:
        """Generates HTML for the metadata section."""
        if not metadata:
            return ""

        rows = ""
        for key, value in metadata.items():
            rows += f"<tr><th>{key.capitalize()}</th><td>{value}</td></tr>"

        return f"""
<div class="section">
    <h2>Metadata</h2>
    <table class="metadata-table">
        {rows}
    </table>
</div>
"""

    def _generate_story_html(self, story: str) -> str:
        """Generates HTML for the story section."""
        if not story:
            return ""

        return f"""
<div class="section">
    <h2>User Story</h2>
    <div class="story-content">
        {story}
    </div>
</div>
"""

    def _generate_acceptance_criteria_html(self, criteria: List[Dict[str, Any]]) -> str:
        """Generates HTML for acceptance criteria with nested steps."""
        if not criteria:
            return ""

        criteria_html = ""
        for criterion in criteria:
            criterion_id = criterion.get('id', '')
            steps = criterion.get('steps', [])

            steps_html = ""
            for step in steps:
                steps_html += f"<li>{step}</li>"

            criteria_html += f"""
<div class="criterion">
    <div class="criterion-title">Criterion {criterion_id}</div>
    <ul class="criterion-steps">
        {steps_html}
    </ul>
</div>
"""

        return f"""
<div class="section acceptance-criteria">
    <h2>Acceptance Criteria</h2>
    {criteria_html}
</div>
"""

    def _generate_related_documents_html(self, documents: List[Dict[str, Any]]) -> str:
        """Generates HTML for related documents section."""
        if not documents:
            return ""

        docs_html = ""
        for doc in documents:
            doc_type = doc.get('type', 'Document')
            path = doc.get('path', '#')
            # Make path relative and HTML-safe
            display_path = path.replace('_29/MODEL_for_framework/90_tool/20_user_story/', '')
            docs_html += f'<li><a href="{path}" target="_blank">{doc_type}: {display_path}</a></li>'

        return f"""
<div class="section">
    <h2>Related Documents</h2>
    <ul class="related-documents">
        {docs_html}
    </ul>
</div>
"""

    def convert(self) -> bool:
        """
        Executes the conversion from YAML to HTML.
        """
        if not os.path.isfile(self.input_path):
            logging.error(f"Input file not found: {self.input_path}")
            return False

        if not self.input_path.endswith(('.yaml', '.yml')):
            logging.error(f"Input file is not a YAML file: {self.input_path}")
            return False

        html_path = self._generate_html_path()
        output_dir = os.path.dirname(html_path)

        try:
            # Read YAML file
            with open(self.input_path, 'r', encoding='utf-8') as f:
                yaml_content = f.read()

            # Parse YAML
            yaml_data = yaml.safe_load(yaml_content)
            if yaml_data is None:
                yaml_data = {}

            # Generate HTML
            file_name = os.path.splitext(os.path.basename(self.input_path))[0]
            html_content = self._generate_yaml_html_template(yaml_data, file_name)

            # Write HTML file
            os.makedirs(output_dir, exist_ok=True)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)

            logging.info(f"Successfully converted '{self.input_path}' to '{html_path}'")
            self.stats['success'] += 1
            self.stats['processed_files'].append({
                'input': self.input_path,
                'output': html_path,
                'status': 'success'
            })
            return True

        except yaml.YAMLError as e:
            logging.error(f"YAML parsing error in {self.input_path}: {e}")
            self.stats['failed'] += 1
            self.stats['processed_files'].append({
                'input': self.input_path,
                'output': None,
                'status': 'failed',
                'error': str(e)
            })
            return False
        except IOError as e:
            logging.error(f"File I/O error processing {self.input_path}: {e}")
            self.stats['failed'] += 1
            self.stats['processed_files'].append({
                'input': self.input_path,
                'output': None,
                'status': 'failed',
                'error': str(e)
            })
            return False
        except Exception as e:
            logging.error(f"Unexpected error processing {self.input_path}: {e}")
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
        description="Converts YAML files to styled HTML documents with fixed output directory for MODEL_for_framework.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("input_path", help="Path to a YAML file or a directory containing YAML files.")
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="If input_path is a directory, process all YAML files recursively."
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

    converter = ConverterForYamlToHtml(args.input_path, args.project_base)

    if os.path.isdir(args.input_path):
        if not args.recursive:
            print("Error: Input path is a directory, but --recursive flag was not provided.")
            sys.exit(1)

        logging.info(f"Starting recursive YAML conversion in directory: {args.input_path}")

        yaml_files = []
        for root, _, files in os.walk(args.input_path):
            for file in files:
                if file.endswith(('.yaml', '.yml')):
                    yaml_files.append(os.path.join(root, file))

        if not yaml_files:
            logging.warning(f"No YAML files found in directory: {args.input_path}")
            return

        logging.info(f"Found {len(yaml_files)} YAML file(s) to process")

        for yaml_file in yaml_files:
            converter.input_path = yaml_file
            converter.convert()

    elif os.path.isfile(args.input_path):
        if not args.input_path.endswith(('.yaml', '.yml')):
            print("Error: Input file does not appear to be a YAML file.")
            sys.exit(1)

        converter.convert()
    else:
        print(f"Error: Input path not found: {args.input_path}")
        sys.exit(1)

    # Display summary if requested
    if args.summary or converter.stats['failed'] > 0:
        print("\n" + "="*60)
        print("YAML TO HTML CONVERSION SUMMARY")
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
