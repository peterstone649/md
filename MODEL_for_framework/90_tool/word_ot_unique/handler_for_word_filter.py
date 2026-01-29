#!/usr/bin/env python3
"""
Handle Word Filter
==================

Module for loading and applying word filtering rules from YAML configuration.
Provides configurable filtering of words based on patterns, length, and exclusion lists.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import os
import re
import yaml
import logging
from typing import Set, List, Dict, Any, Optional
from pathlib import Path

# Import local lemmatizer
try:
    from lemmatizer_wordnet import WordNetLemmatizerHandler
    LEMMATIZER_AVAILABLE = True
except ImportError:
    LEMMATIZER_AVAILABLE = False
    WordNetLemmatizerHandler = None

__version__ = "1.0.0"
__status__ = "ACTIVE"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WordFilter:
    """
    Handles word filtering based on YAML configuration.
    """

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the word filter with configuration.

        Args:
            config_path: Path to the YAML configuration file (optional)
        """
        if config_path is None:
            # Default path relative to this module
            module_dir = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(module_dir, "word_filter.yaml")

        self.config_path = config_path
        self.config = self._load_config()
        self._compile_patterns()
        self._initialize_lemmatizer()

        if self.config.get('logging', {}).get('filter_decisions', False):
            logger.info("Word filter initialized with decision logging enabled")
        else:
            logger.info("Word filter initialized")

    def _load_config(self) -> Dict[str, Any]:
        """
        Load configuration from YAML file.

        Returns:
            Configuration dictionary
        """
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            logger.info(f"Loaded word filter configuration from {self.config_path}")
            return config
        except FileNotFoundError:
            logger.warning(f"Configuration file not found: {self.config_path}")
            return self._get_default_config()
        except yaml.YAMLError as e:
            logger.error(f"Error parsing YAML configuration: {e}")
            return self._get_default_config()

    def _get_default_config(self) -> Dict[str, Any]:
        """
        Get default configuration when file loading fails.

        Returns:
            Default configuration dictionary
        """
        return {
            'version': '1.0.0',
            'filters': {
                'length_filters': [],
                'pattern_filters': [],
                'exclude_lists': {
                    'abbreviations': [],
                    'common_excludes': []
                }
            },
            'processing': {
                'case_sensitive': False,
                'normalize_unicode': True,
                'strip_punctuation': True
            },
            'logging': {
                'filter_decisions': False,
                'performance_stats': False
            }
        }

    def _compile_patterns(self):
        """
        Compile regex patterns for efficient matching.
        """
        self.compiled_patterns = []
        pattern_filters = self.config.get('filters', {}).get('pattern_filters', [])

        for filter_rule in pattern_filters:
            if filter_rule.get('enabled', True):
                try:
                    pattern = re.compile(filter_rule['pattern'])
                    self.compiled_patterns.append({
                        'pattern': pattern,
                        'description': filter_rule.get('description', ''),
                        'rule': filter_rule
                    })
                except re.error as e:
                    logger.warning(f"Invalid regex pattern '{filter_rule['pattern']}': {e}")

    def _initialize_lemmatizer(self):
        """
        Initialize the lemmatizer/stemmer if configured and available.
        """
        self.lemmatizer = None
        processing_config = self.config.get('processing', {})

        if processing_config.get('enable_lemmatization', False):
            lemmatization_method = processing_config.get('lemmatization_method', 'none')

            if lemmatization_method == 'wordnet' and LEMMATIZER_AVAILABLE:
                try:
                    self.lemmatizer = WordNetLemmatizerHandler()
                    logger.info("WordNet lemmatizer enabled")
                except Exception as e:
                    logger.warning(f"Failed to initialize WordNet lemmatizer: {e}")
                    self.lemmatizer = None
            elif lemmatization_method == 'porter':
                try:
                    # Import PorterStemmer from NLTK
                    from nltk.stem import PorterStemmer
                    self.lemmatizer = PorterStemmer()
                    logger.info("Porter stemmer enabled")
                except ImportError:
                    logger.warning("Porter stemmer requires NLTK. Install with: pip install nltk")
                    self.lemmatizer = None
            else:
                logger.info(f"Lemmatization method '{lemmatization_method}' not available or disabled")

    def should_filter_word(self, word: str) -> tuple[bool, str]:
        """
        Check if a word should be filtered based on all configured rules.

        Args:
            word: Word to check

        Returns:
            Tuple of (should_filter, reason)
        """
        # Apply length filters
        length_filters = self.config.get('filters', {}).get('length_filters', [])
        for length_filter in length_filters:
            if length_filter.get('enabled', True):
                min_len = length_filter.get('min_length', 0)
                max_len = length_filter.get('max_length', float('inf'))
                if min_len <= len(word) <= max_len:
                    reason = length_filter.get('description', f'Length filter: {min_len}-{max_len} chars')
                    if self.config.get('logging', {}).get('filter_decisions', False):
                        logger.debug(f"Filtered '{word}': {reason}")
                    return True, reason

        # Apply pattern filters
        for compiled_pattern in self.compiled_patterns:
            if compiled_pattern['pattern'].match(word):
                reason = compiled_pattern['rule'].get('description', 'Pattern match')
                if self.config.get('logging', {}).get('filter_decisions', False):
                    logger.debug(f"Filtered '{word}': {reason}")
                return True, reason

        # Apply exclusion lists
        exclude_lists = self.config.get('filters', {}).get('exclude_lists', {})
        processing_config = self.config.get('processing', {})

        # Check case sensitivity
        check_word = word
        if not processing_config.get('case_sensitive', False):
            check_word = word.lower()

        # Check abbreviations
        abbreviations = exclude_lists.get('abbreviations', [])
        if check_word in abbreviations:
            reason = f"In abbreviations exclusion list"
            if self.config.get('logging', {}).get('filter_decisions', False):
                logger.debug(f"Filtered '{word}': {reason}")
            return True, reason

        # Check OS commands
        os_commands = exclude_lists.get('os_commands', [])
        if check_word in os_commands:
            reason = f"In OS commands exclusion list"
            if self.config.get('logging', {}).get('filter_decisions', False):
                logger.debug(f"Filtered '{word}': {reason}")
            return True, reason

        # Check country codes
        country_codes = exclude_lists.get('country_codes', [])
        if check_word in country_codes:
            reason = f"In country codes exclusion list"
            if self.config.get('logging', {}).get('filter_decisions', False):
                logger.debug(f"Filtered '{word}': {reason}")
            return True, reason

        # Check common excludes
        common_excludes = exclude_lists.get('common_excludes', [])
        if check_word in common_excludes:
            reason = f"In common exclusion list"
            if self.config.get('logging', {}).get('filter_decisions', False):
                logger.debug(f"Filtered '{word}': {reason}")
            return True, reason

        return False, ""

    def filter_words(self, words: Set[str]) -> Set[str]:
        """
        Filter a set of words based on configuration rules.

        Args:
            words: Set of words to filter

        Returns:
            Filtered set of words
        """
        filtered_words = set()
        stats = {'total': len(words), 'filtered': 0, 'kept': 0}

        for word in words:
            should_filter, reason = self.should_filter_word(word)
            if should_filter:
                stats['filtered'] += 1
                if self.config.get('logging', {}).get('filter_decisions', False):
                    logger.debug(f"Filtered: {word} - {reason}")
            else:
                filtered_words.add(word)
                stats['kept'] += 1

        if self.config.get('logging', {}).get('performance_stats', False):
            logger.info(f"Filtering stats: {stats}")

        return filtered_words

    def lemmatize_words(self, words: Set[str]) -> Set[str]:
        """
        Lemmatize/stem a set of words if lemmatization is enabled and available.

        Args:
            words: Set of words to lemmatize/stem

        Returns:
            Set of lemmatized/stemmed words (or original words if unavailable)
        """
        if self.lemmatizer is None:
            # Return original words if no lemmatizer available
            return words

        try:
            lemmatized_words = set()

            # Handle different lemmatizer types
            if hasattr(self.lemmatizer, 'lemmatize_words'):
                # WordNetLemmatizerHandler
                lemmatized_words = self.lemmatizer.lemmatize_words(words)
            elif hasattr(self.lemmatizer, 'stem'):
                # PorterStemmer or similar stemmer
                for word in words:
                    stemmed = self.lemmatizer.stem(word)
                    lemmatized_words.add(stemmed)
            else:
                # Unknown lemmatizer type
                logger.warning(f"Unknown lemmatizer type: {type(self.lemmatizer)}")
                return words

            if self.config.get('logging', {}).get('performance_stats', False):
                logger.info(f"Processed {len(words)} words")

            return lemmatized_words
        except Exception as e:
            logger.warning(f"Lemmatization/stemming failed: {e}")
            return words  # Return original words on failure

    def get_config_info(self) -> Dict[str, Any]:
        """
        Get information about the current configuration.

        Returns:
            Configuration information dictionary
        """
        return {
            'config_path': self.config_path,
            'version': self.config.get('version', 'unknown'),
            'enabled_filters': {
                'length_filters': len([f for f in self.config.get('filters', {}).get('length_filters', []) if f.get('enabled', True)]),
                'pattern_filters': len(self.compiled_patterns),
                'abbreviations': len(self.config.get('filters', {}).get('exclude_lists', {}).get('abbreviations', [])),
                'os_commands': len(self.config.get('filters', {}).get('exclude_lists', {}).get('os_commands', [])),
                'country_codes': len(self.config.get('filters', {}).get('exclude_lists', {}).get('country_codes', [])),
                'common_excludes': len(self.config.get('filters', {}).get('exclude_lists', {}).get('common_excludes', []))
            },
            'processing_options': self.config.get('processing', {}),
            'logging_enabled': self.config.get('logging', {})
        }

def create_word_filter(config_path: Optional[str] = None) -> WordFilter:
    """
    Factory function to create a WordFilter instance.

    Args:
        config_path: Optional path to configuration file

    Returns:
        WordFilter instance
    """
    return WordFilter(config_path)

# Convenience functions
def should_filter(word: str, config_path: Optional[str] = None) -> bool:
    """
    Convenience function to check if a word should be filtered.

    Args:
        word: Word to check
        config_path: Optional configuration file path

    Returns:
        True if word should be filtered
    """
    filter_instance = WordFilter(config_path)
    should_filter, _ = filter_instance.should_filter_word(word)
    return should_filter

def filter_word_set(words: Set[str], config_path: Optional[str] = None) -> Set[str]:
    """
    Convenience function to filter a set of words.

    Args:
        words: Set of words to filter
        config_path: Optional configuration file path

    Returns:
        Filtered set of words
    """
    filter_instance = WordFilter(config_path)
    return filter_instance.filter_words(words)

# Changelog
# V1.0.0 - 2026-01-29 - Initial creation - Framework Steward - Establish word filtering functionality
