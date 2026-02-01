#!/usr/bin/env python3
"""
AI_LOCK Converter for special handling of [AI_LOCK] and [AI_UNLOCK] tags in HTML conversion.

This module provides specialized conversion for AI_LOCK/AI_UNLOCK tags that appear
on the same line, ensuring they are properly formatted with line breaks and visual
separation in the HTML output.
"""

import os
import sys
import argparse
import markdown
import logging
import re
import shutil
from datetime import datetime
from dotenv import load_dotenv
from handler_for_link import Handler_for_Link

# Import the index generator for folder link handling
from index_generator import generate_index_for_folder

__version__ = "1.0.0"
__status__ = "ACTIVE"

"""
CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.0.0  | 2026-02-01 | Initial creation of AI_LOCK converter with special line break handling | Framework Steward | Provide specialized handling for AI_LOCK tags to ensure proper visual separation with <br> tags |
"""


class AILockConverter:
    """
    A specialized converter for handling AI_LOCK and AI_UNLOCK tags with proper
    line break formatting and visual separation in HTML output.
    """
    def __init__(self, input_path, project_base=None):
        self.input_path = os.path.abspath(input_path)
        # Use environment variable if available, otherwise use default
        if project_base is None:
            project_base = os.getenv('PROJECT_BASE_PATH', r"E:\2025_11\_29")
        self.project_base = os.path.abspath(project_base)
        # Fixed output directory: <PROJECT_BASE_PATH>\out\html
        self.output_root = os.path.join(self.project_base, "out", "html")

    def generate_for_html_path(self):
        """
        Generates the output HTML path, mirroring the source directory structure
        relative to the project base within the fixed output directory.
        """
        try:
            relative_path = os.path.relpath(self.input_path, self.project_base)
            base, _ = os.path.splitext(relative_path)
            return os.path.join(self.output_root, f"{base}.html")
        except ValueError:
            # Handle case where paths are on different drives
            # Use just the filename in this case
            base = os.path.splitext(os.path.basename(self.input_path))[0]
            return os.path.join(self.output_root, f"{base}.html")

    def process_ai_lock_tags(self, md_content):
        """
        Process AI_LOCK and AI_UNLOCK tags to ensure proper line break formatting.
        Converts single-line AI_LOCK tags to separate lines with <br> tags.
        """
        # Pattern to match AI_LOCK and AI_UNLOCK tags on the same line
        ai_lock_pattern = r'\[AI_LOCK\](.*?)\[AI_UNLOCK\]'
        
        def replace_ai_lock(match):
            content = match.group(1).strip()
            # Return formatted content with line breaks
            return f"\n\n[AI_LOCK] {content} [AI_UNLOCK]\n\n"
        
        # Replace single-line AI_LOCK tags with properly formatted versions
        processed_content = re.sub(ai_lock_pattern, replace_ai_lock, md_content, flags=re.DOTALL)
        
        return processed_content

    def copy_for_images(self, md_content, input_dir, output_dir):
        """
        Copies image files referenced in markdown content to the output directory
        and updates the content with new relative paths.
        """
        # Find all image references in markdown: ![alt](path)
        image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        updated_content = md_content

        for match in re.finditer(image_pattern, md_content):
            alt_text = match.group(1)
            image_path = match.group(2)

            # Skip external URLs (http/https)
            if image_path.startswith(('http://', 'https://')):
                continue

            # Resolve relative path from markdown file location
            abs_image_path = os.path.abspath(os.path.join(input_dir, image_path))

            if os.path.isfile(abs_image_path):
                # Create relative path from output directory to image
                try:
                    rel_image_path = os.path.relpath(abs_image_path, output_dir)
                    # Copy image to output directory
                    output_image_path = os.path.join(output_dir, os.path.basename(image_path))
                    shutil.copy2(abs_image_path, output_image_path)
                    logging.info(f"Copied image '{abs_image_path}' to '{output_image_path}'")

                    # Update the markdown content with the new relative path
                    old_ref = f'![{alt_text}]({image_path})'
                    new_ref = f'![{alt_text}]({os.path.basename(image_path)})'
                    updated_content = updated_content.replace(old_ref, new_ref)
                except Exception as e:
                    logging.warning(f"Failed to copy image '{abs_image_path}': {e}")
            else:
                logging.warning(f"Image file not found: '{abs_image_path}'")

        return updated_content

    def generate_for_folder_indices(self, md_content, input_dir):
        """
        Detects folder links in markdown content and generates index files for them.
        
        Args:
            md_content (str): The markdown content to scan for folder links
            input_dir (str): The directory containing the markdown file
        
        Returns:
            str: Updated markdown content with folder links modified
        """
        # Pattern to match folder links (links ending with / or pointing to directories)
        folder_pattern = r'\[([^\]]*)\]\(([^)]*\/)\)'
        
        updated_content = md_content
        
        for match in re.finditer(folder_pattern, md_content):
            link_text = match.group(1)
            folder_path = match.group(2)
            
            # Skip external URLs
            if folder_path.startswith(('http://', 'https://')):
                continue
            
            # Resolve relative path from markdown file location
            abs_folder_path = os.path.abspath(os.path.join(input_dir, folder_path))
            
            # Check if it's actually a directory
            if os.path.isdir(abs_folder_path):
                logging.info(f"Detected folder link: {abs_folder_path}")
                
                # Determine the new href
                readme_md = os.path.join(abs_folder_path, 'README.md')
                new_href = None
                
                if os.path.isfile(readme_md):
                    # Check if README.html exists in output directory
                    try:
                        rel_folder = os.path.relpath(abs_folder_path, self.project_base)
                        output_folder = os.path.join(self.output_root, rel_folder)
                        readme_html = os.path.join(output_folder, 'README.html')
                        if os.path.isfile(readme_html):
                            new_href = folder_path.rstrip('/') + '/README.html'
                            logging.info(f"Using existing README.html for folder: {abs_folder_path}")
                        else:
                            # Generate index.html
                            success = generate_index_for_folder(abs_folder_path, format='html')
                            if success:
                                new_href = folder_path.rstrip('/') + '/index.html'
                                logging.info(f"Generated index.html for folder with README: {abs_folder_path}")
                            else:
                                logging.warning(f"Failed to generate index for folder: {abs_folder_path}")
                    except Exception as e:
                        logging.error(f"Error processing folder {abs_folder_path}: {e}")
                        # Fallback: generate index
                        success = generate_index_for_folder(abs_folder_path, format='html')
                        if success:
                            new_href = folder_path.rstrip('/') + '/index.html'
                else:
                    # No README.md, generate index.html
                    success = generate_index_for_folder(abs_folder_path, format='html')
                    if success:
                        new_href = folder_path.rstrip('/') + '/index.html'
                        logging.info(f"Generated index.html for folder: {abs_folder_path}")
                    else:
                        logging.warning(f"Failed to generate index for folder: {abs_folder_path}")
                
                # Update the link in content if new_href was determined
                if new_href:
                    old_link = f'[{link_text}]({folder_path})'
                    new_link = f'[{link_text}]({new_href})'
                    updated_content = updated_content.replace(old_link, new_link)
                    logging.info(f"Updated folder link: {old_link} -> {new_link}")
        
        return updated_content

    def convert(self):
        """
        Executes the conversion from Markdown to a styled HTML file with AI_LOCK handling.
        """
        if not os.path.isfile(self.input_path):
            logging.error(f"Input file not found: {self.input_path}")
            return False

        html_path = self.generate_for_html_path()
        output_dir = os.path.dirname(html_path)
        input_dir = os.path.dirname(self.input_path)

        try:
            os.makedirs(output_dir, exist_ok=True)
            with open(self.input_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
        except IOError as e:
            logging.error(f"Error reading input file {self.input_path}: {e}")
            return False

        # Process AI_LOCK tags first to ensure proper formatting
        md_content = self.process_ai_lock_tags(md_content)

        # Copy images and update content
        md_content = self.copy_for_images(md_content, input_dir, output_dir)

        # Generate index files for any folder links found in the content and update links
        md_content = self.generate_for_folder_indices(md_content, input_dir)

        # Use markdown extensions for better formatting
        html_content = markdown.markdown(
            md_content, extensions=['fenced_code', 'tables']
        )

        # Convert .md links to .html links using the LinkHandler
        html_content = Handler_for_Link.handle_for_link(html_content, ".md", ".html")

        title = os.path.splitext(os.path.basename(self.input_path))[0]
        html_template = self.get_for_html_template(title, html_content)

        try:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_template)
            logging.info(f"Successfully converted '{self.input_path}' to '{html_path}' with AI_LOCK formatting")
            return True
        except IOError as e:
            logging.error(f"Error writing HTML file {html_path}: {e}")
            return False

    @staticmethod
    def get_for_html_template(title, body):
        """
        Returns a styled HTML5 template with enhanced AI_LOCK styling.
        """
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
            font-size: 12px;
            line-height: 1.5;
            margin: 2em;
            color: #333;
        }}
        h1, h2, h3 {{
            color: #2c3e50; /* Dark Slate Blue */
        }}
        h1 {{ font-size: 1.5em; }}
        h2 {{ font-size: 1.2em; }}
        h3 {{ font-size: 1.1em; }}
        a {{
            color: #007bff; /* A nice, standard blue */
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        code {{
            background-color: #eef; /* Lighter than pre for inline */
            padding: 2px 4px;
            border-radius: 4px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
        }}
        pre {{
            background-color: #f8f9fa; /* A very light grey */
            padding: 1em;
            border-radius: 5px;
            overflow-x: auto;
            border: 1px solid #dee2e6; /* A light border */
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 1em;
        }}
        th, td {{
            border: 1px solid #ccc; /* Lighter grey border */
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #eaf4ff; /* Light Blue for table headers */
            color: #2c3e50; /* Darker text for contrast */
        }}
        /* Enhanced AI_LOCK styling with visual separation */
        .ai-lock {{
            background-color: #fff3cd;
            border: 2px solid #ffc107;
            border-radius: 8px;
            padding: 15px;
            margin: 15px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-left: 5px solid #ffc107;
        }}
        .ai-lock::before {{
            content: "🔒 AI_LOCK PROTECTED CONTENT";
            display: block;
            font-weight: bold;
            color: #856404;
            margin-bottom: 8px;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .ai-lock-content {{
            color: #856404;
            line-height: 1.6;
        }}
        footer {{
            margin-top: 2em;
            font-size: 0.8em;
            color: #777;
        }}
    </style>
</head>
<body>
    {body}
        <footer>
            <p><em>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} by AILockConverter v{__version__}</em></p>
        </footer>
</body>
</html>"""

def main():
    parser = argparse.ArgumentParser(
        description="Converts Markdown files to styled HTML with AI_LOCK special handling and line break formatting.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("input_path", help="Path to a Markdown file or a directory.")
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="If input_path is a directory, convert all Markdown files recursively."
    )
    parser.add_argument(
        "--project-base",
        default=None,
        help="The project base path for calculating relative output paths. Defaults to PROJECT_BASE_PATH from .env file or 'E:\\2025_11\\_29'."
    )
    args = parser.parse_args()

    if os.path.isdir(args.input_path):
        if not args.recursive:
            print("Error: Input path is a directory, but --recursive flag was not provided.")
            sys.exit(1)

        logging.info(f"Starting recursive conversion in directory: {args.input_path}")
        for root, _, files in os.walk(args.input_path):
            for file in files:
                if file.endswith((".md", ".markdown")):
                    input_file = os.path.join(root, file)
                    converter = AILockConverter(input_file, args.project_base)
                    converter.convert()
        logging.info("Recursive conversion complete.")

    elif os.path.isfile(args.input_path):
        if not args.input_path.endswith((".md", ".markdown")):
            print("Error: Input file does not appear to be a Markdown file.")
            sys.exit(1)

        converter = AILockConverter(args.input_path, args.project_base)
        converter.convert()
    else:
        print(f"Error: Input path not found: {args.input_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()