import os
import sys
import argparse
import markdown
import logging
import re
import shutil
from datetime import datetime
from dotenv import load_dotenv

__version__ = "1.6.1"
__status__ = "ACTIVE"

r"""
CHANGELOG

| Version | Date       | Changes | Stakeholder | Rationale/Motivation |
|---------|------------|---------|-------------|----------------------|
| V1.6.1  | 2026-01-15 | Fixed syntax warning by making docstring a raw string | Framework Steward | Resolve Python syntax warning for invalid escape sequences in docstring table formatting |
| V1.6.0  | 2026-01-14 | Added automatic image copying for SVG and other image files | Framework Steward | Ensure images are properly included in HTML output |
| V1.5.0  | 2026-01-13 | Renamed file from md_to_html_converter.py to converter_for_md_to_html.py | Framework Steward | Align with framework naming conventions and improve consistency |
| V1.4.0  | 2026-01-13 | Restructured tool directory from 90_tool to 90_tool\converter | Framework Steward | Improve code organization and separate converter tools into dedicated subdirectory |
| V1.3.0  | 2026-01-13 | Adapted fixed output directory structure <PROJECT_BASE_PATH>\out\html | Framework Steward | Standardize HTML output location for consistent deployment and easier maintenance |
| V1.2.0  | 2026-01-10 | Added .env support for PROJECT_BASE_PATH configuration | AI Coder | Enable environment-based configuration for different deployment scenarios |
| V1.1.0  | 2026-01-10 | Enhanced Markdown processing with fenced_code and tables extensions | AI Coder | Improve support for code blocks and tables in Markdown documents |
| V1.0.0  | 2026-01-10 | Initial release with basic Markdown to HTML conversion | AI Coder | Provide foundational Markdown conversion capabilities |
| V0.1.1  | 2026-01-10 | Updated template metadata to include Framework Version and use list format | AI Coder | To provide more detailed and consistently formatted metadata in new documents |

mfw_tool.svg pulled from https://game-icons.net/1x1/lorc/gear-hammer.html

"""

# Load environment variables from .env file
load_dotenv()

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class HTMLConverter:
    """
    A modernized tool to convert Markdown files to HTML, aligning with
    the standards of MODEL_for_framework.
    """
    def __init__(self, input_path, project_base=None):
        self.input_path = os.path.abspath(input_path)
        # Use environment variable if available, otherwise use default
        if project_base is None:
            project_base = os.getenv('PROJECT_BASE_PATH', r"E:\2025_11\_29")
        self.project_base = os.path.abspath(project_base)
        # Fixed output directory: <PROJECT_BASE_PATH>\out\html
        self.output_root = os.path.join(self.project_base, "out", "html")

    def _generate_html_path(self):
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

    def _copy_images(self, md_content, input_dir, output_dir):
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

    def convert(self):
        """
        Executes the conversion from Markdown to a styled HTML file.
        """
        if not os.path.isfile(self.input_path):
            logging.error(f"Input file not found: {self.input_path}")
            return False

        html_path = self._generate_html_path()
        output_dir = os.path.dirname(html_path)
        input_dir = os.path.dirname(self.input_path)

        try:
            os.makedirs(output_dir, exist_ok=True)
            with open(self.input_path, 'r', encoding='utf-8') as f:
                md_content = f.read()
        except IOError as e:
            logging.error(f"Error reading input file {self.input_path}: {e}")
            return False

        # Copy images and update content
        md_content = self._copy_images(md_content, input_dir, output_dir)

        # Use markdown extensions for better formatting
        html_content = markdown.markdown(
            md_content, extensions=['fenced_code', 'tables']
        )

        title = os.path.splitext(os.path.basename(self.input_path))[0]
        html_template = self._get_html_template(title, html_content)

        try:
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_template)
            logging.info(f"Successfully converted '{self.input_path}' to '{html_path}'")
            return True
        except IOError as e:
            logging.error(f"Error writing HTML file {html_path}: {e}")
            return False

    @staticmethod
    def _get_html_template(title, body):
        """
        Returns a styled HTML5 template.
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
            <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} by MDToHTMLConverter v{__version__}</p>
        </footer>
</body>
</html>"""

def main():
    parser = argparse.ArgumentParser(
        description="Converts Markdown files to styled HTML with fixed output directory.",
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
                    converter = HTMLConverter(input_file, args.project_base)
                    converter.convert()
        logging.info("Recursive conversion complete.")

    elif os.path.isfile(args.input_path):
        if not args.input_path.endswith((".md", ".markdown")):
            print("Error: Input file does not appear to be a Markdown file.")
            sys.exit(1)

        converter = HTMLConverter(args.input_path, args.project_base)
        converter.convert()
    else:
        print(f"Error: Input path not found: {args.input_path}")
        sys.exit(1)

if __name__ == "__main__":
    main()
