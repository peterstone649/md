#!/usr/bin/env python3
"""
Link Filter Module
==================

Filters out broken markdown links that point to non-existent files.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import os
import re
import logging
from typing import Optional
from urllib.parse import urlparse

__version__ = "1.0.0"
__status__ = "ACTIVE"

# Setup logging
logger = logging.getLogger(__name__)

class FilterForLinks:
    """
    Filters out broken markdown links from text.
    """

    def __init__(self):
        """
        Initialize the link filter.
        """
        pass

    def filter_broken_links(self, line: str, base_dir: str) -> str:
        """
        Filter out markdown links that point to non-existent files.

        Args:
            line: Line of text containing potential markdown links
            base_dir: Base directory to resolve relative paths

        Returns:
            str: Line with broken links filtered out
        """
        # Regex to find markdown links: [text](url)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

        def replace_link(match):
            text = match.group(1)
            url = match.group(2)

            # Skip external URLs (http, https, etc.)
            parsed = urlparse(url)
            if parsed.scheme in ('http', 'https', 'mailto', 'ftp'):
                return match.group(0)  # Keep external links

            # Check if it's a relative file path
            if not url.startswith('/') and '://' not in url:
                # Resolve relative path from the base directory
                full_path = os.path.join(base_dir, url)

                # Remove fragment and query if present
                path_only = parsed.path
                if path_only:
                    full_path = os.path.join(base_dir, path_only)

                # Check if file exists
                if os.path.exists(full_path):
                    return match.group(0)  # Keep working links
                else:
                    logger.debug(f"Filtering broken link: {url} (resolved to {full_path})")
                    return text  # Remove link, keep text only

            return match.group(0)  # Keep other types of links

        return re.sub(link_pattern, replace_link, line)

def create_filter_for_links() -> FilterForLinks:
    """
    Factory function to create a FilterForLinks instance.

    Returns:
        FilterForLinks instance
    """
    return FilterForLinks()

## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | 2026-01-24 | Initial creation | Framework Maintenance Team | Establish foundational structure |
