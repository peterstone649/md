#!/usr/bin/env python3
"""
Converter for Timestamp
=======================

A utility module for handling date and timestamp operations.
Provides conversion between different timestamp formats, validation,
and generation of standardized timestamps.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import re
from datetime import datetime, timezone, timedelta
from typing import Optional, Union, Tuple, Dict, Any
import logging

__version__ = "1.0.0"
__status__ = "ACTIVE"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TimestampConverter:
    """
    Converter for handling various timestamp formats and operations.
    """

    # Common timestamp formats
    FORMATS = {
        'iso': '%Y-%m-%dT%H:%M:%S.%fZ',  # ISO 8601 with microseconds
        'iso_simple': '%Y-%m-%dT%H:%M:%SZ',  # ISO 8601 without microseconds
        'compact': '%Y-%m-%d_%H-%M-%S_%f',  # Compact format for filenames
        'readable': '%Y-%m-%d %H:%M:%S.%f',  # Human readable
        'date_only': '%Y-%m-%d',  # Date only
        'time_only': '%H:%M:%S.%f',  # Time only
        'log_format': '%Y-%m-%d %H:%M:%S',  # For log timestamps
    }

    def __init__(self, timezone_offset: Optional[int] = None):
        """
        Initialize the timestamp converter.

        Args:
            timezone_offset: Hours offset from UTC (optional)
        """
        self.timezone_offset = timezone_offset
        if timezone_offset is not None:
            self.timezone = timezone(timedelta(hours=timezone_offset))
        else:
            self.timezone = timezone.utc

    def now(self, format_name: str = 'iso') -> str:
        """
        Get current timestamp in specified format.

        Args:
            format_name: Format name from FORMATS dict

        Returns:
            Formatted timestamp string
        """
        dt = datetime.now(self.timezone)
        format_str = self.FORMATS.get(format_name, format_name)
        return dt.strftime(format_str)

    def generate_filename_timestamp(self, original_filename: str) -> str:
        """
        Generate a timestamp-based filename.

        Args:
            original_filename: Original filename

        Returns:
            Timestamped filename
        """
        timestamp = self.now('compact')
        name_part, ext_part = self._split_filename(original_filename)
        return f"{timestamp}_{name_part}{ext_part}"

    def _split_filename(self, filename: str) -> Tuple[str, str]:
        """
        Split filename into name and extension parts.

        Args:
            filename: Filename to split

        Returns:
            Tuple of (name, extension)
        """
        import os
        return os.path.splitext(filename)

    def parse_timestamp(self, timestamp_str: str,
                       formats_to_try: Optional[list] = None) -> Optional[datetime]:
        """
        Parse a timestamp string using multiple formats.

        Args:
            timestamp_str: Timestamp string to parse
            formats_to_try: List of format names to try (optional)

        Returns:
            Parsed datetime object or None if parsing fails
        """
        if formats_to_try is None:
            formats_to_try = ['iso', 'iso_simple', 'readable', 'compact', 'log_format']

        for format_name in formats_to_try:
            format_str = self.FORMATS.get(format_name, format_name)
            try:
                # Handle compact format specially (may have variable microsecond length)
                if format_name == 'compact':
                    dt = self._parse_compact_format(timestamp_str)
                    if dt:
                        return dt
                else:
                    dt = datetime.strptime(timestamp_str, format_str)
                    # Apply timezone if parsed as naive
                    if dt.tzinfo is None:
                        dt = dt.replace(tzinfo=self.timezone)
                    return dt
            except ValueError:
                continue

        logger.warning(f"Could not parse timestamp: {timestamp_str}")
        return None

    def _parse_compact_format(self, timestamp_str: str) -> Optional[datetime]:
        """
        Parse compact timestamp format (YYYY-MM-DD_HH-MM-SS_microseconds).

        Args:
            timestamp_str: Timestamp string

        Returns:
            Parsed datetime or None
        """
        # Pattern: YYYY-MM-DD_HH-MM-SS_microseconds
        pattern = r'^(\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-(\d{2})_(\d{6})'
        match = re.match(pattern, timestamp_str)

        if match:
            y, m, d, h, mi, s, micro_str = match.groups()
            dt_str = f"{y}-{m}-{d} {h}:{mi}:{s}.{micro_str}"
            try:
                dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S.%f')
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=self.timezone)
                return dt
            except ValueError:
                pass

        return None

    def convert_format(self, timestamp_str: str, target_format: str,
                      source_format: Optional[str] = None) -> Optional[str]:
        """
        Convert timestamp from one format to another.

        Args:
            timestamp_str: Source timestamp string
            target_format: Target format name
            source_format: Source format name (optional, will auto-detect)

        Returns:
            Converted timestamp string or None if conversion fails
        """
        dt = self.parse_timestamp(timestamp_str, [source_format] if source_format else None)
        if dt is None:
            return None

        target_format_str = self.FORMATS.get(target_format, target_format)
        return dt.strftime(target_format_str)

    def validate_timestamp(self, timestamp_str: str,
                          format_name: Optional[str] = None) -> bool:
        """
        Validate if a timestamp string matches the expected format.

        Args:
            timestamp_str: Timestamp string to validate
            format_name: Expected format name (optional)

        Returns:
            True if valid, False otherwise
        """
        if format_name:
            formats_to_try = [format_name]
        else:
            formats_to_try = list(self.FORMATS.keys())

        return self.parse_timestamp(timestamp_str, formats_to_try) is not None

    def get_timestamp_info(self, timestamp_str: str) -> Optional[Dict[str, Any]]:
        """
        Extract detailed information from a timestamp string.

        Args:
            timestamp_str: Timestamp string

        Returns:
            Dict with timestamp information or None if parsing fails
        """
        dt = self.parse_timestamp(timestamp_str)
        if dt is None:
            return None

        return {
            'datetime': dt,
            'iso_format': dt.isoformat(),
            'year': dt.year,
            'month': dt.month,
            'day': dt.day,
            'hour': dt.hour,
            'minute': dt.minute,
            'second': dt.second,
            'microsecond': dt.microsecond,
            'weekday': dt.weekday(),
            'timestamp': dt.timestamp(),
            'timezone': str(dt.tzinfo) if dt.tzinfo else None
        }

    def calculate_time_difference(self, timestamp1: str, timestamp2: str,
                                unit: str = 'seconds') -> Optional[float]:
        """
        Calculate time difference between two timestamps.

        Args:
            timestamp1: First timestamp
            timestamp2: Second timestamp
            unit: Unit for difference ('seconds', 'minutes', 'hours', 'days')

        Returns:
            Time difference in specified unit or None if parsing fails
        """
        dt1 = self.parse_timestamp(timestamp1)
        dt2 = self.parse_timestamp(timestamp2)

        if dt1 is None or dt2 is None:
            return None

        delta = dt2 - dt1
        total_seconds = delta.total_seconds()

        unit_multipliers = {
            'seconds': 1,
            'minutes': 60,
            'hours': 3600,
            'days': 86400
        }

        multiplier = unit_multipliers.get(unit, 1)
        return total_seconds / multiplier

    def is_timestamped_filename(self, filename: str) -> bool:
        """
        Check if a filename appears to be timestamped.

        Args:
            filename: Filename to check

        Returns:
            True if filename appears timestamped, False otherwise
        """
        # Check if filename starts with compact timestamp pattern
        compact_pattern = r'^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}_\d{6}_'
        return bool(re.match(compact_pattern, filename))

    def extract_timestamp_from_filename(self, filename: str) -> Optional[str]:
        """
        Extract timestamp from a timestamped filename.

        Args:
            filename: Timestamped filename

        Returns:
            Timestamp string or None if not found
        """
        compact_pattern = r'^(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}_\d{6})'
        match = re.match(compact_pattern, filename)
        return match.group(1) if match else None

    def add_time_offset(self, timestamp_str: str, offset_seconds: int) -> Optional[str]:
        """
        Add time offset to a timestamp.

        Args:
            timestamp_str: Base timestamp
            offset_seconds: Seconds to add (can be negative)

        Returns:
            New timestamp string or None if parsing fails
        """
        dt = self.parse_timestamp(timestamp_str)
        if dt is None:
            return None

        new_dt = dt + timedelta(seconds=offset_seconds)
        return new_dt.strftime(self.FORMATS['iso'])

def create_timestamp_converter(timezone_offset: Optional[int] = None) -> TimestampConverter:
    """
    Factory function to create a TimestampConverter instance.

    Args:
        timezone_offset: Hours offset from UTC

    Returns:
        TimestampConverter instance
    """
    return TimestampConverter(timezone_offset)

# Convenience functions
def now(format_name: str = 'iso') -> str:
    """Get current timestamp."""
    converter = TimestampConverter()
    return converter.now(format_name)

def generate_filename_timestamp(original_filename: str) -> str:
    """Generate timestamped filename."""
    converter = TimestampConverter()
    return converter.generate_filename_timestamp(original_filename)

def parse_timestamp(timestamp_str: str) -> Optional[datetime]:
    """Parse timestamp string."""
    converter = TimestampConverter()
    return converter.parse_timestamp(timestamp_str)

if __name__ == "__main__":
    # Example usage
    converter = TimestampConverter()

    print("Current timestamp (ISO):", converter.now('iso'))
    print("Current timestamp (compact):", converter.now('compact'))

    # Test filename generation
    test_filename = "test_file.txt"
    timestamped = converter.generate_filename_timestamp(test_filename)
    print(f"Timestamped filename: {timestamped}")

    # Test parsing
    timestamp_part = timestamped.split('_' + test_filename)[0]
    parsed = converter.parse_timestamp(timestamp_part)
    print(f"Parsed timestamp: {parsed}")

    # Test validation
    print(f"Is valid timestamp: {converter.validate_timestamp(converter.now('iso'))}")

## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | 2026-01-24 | Initial creation | Framework Maintenance Team | Establish foundational structure |
