#!/usr/bin/env python3
"""
WordNet Lemmatizer
==================

Module for lemmatizing words using NLTK's WordNet lemmatizer.
Provides proper linguistic lemmatization with part-of-speech tagging.

Version: 1.0.0
Status: ACTIVE
Author: Framework Steward
License: EUPL v1.2
"""

import os
import sys
import logging
from typing import Set, List, Optional

# Import NLTK components
try:
    from nltk.stem import WordNetLemmatizer
    from nltk.corpus import wordnet
    from nltk import pos_tag, download
    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False
    WordNetLemmatizer = None
    wordnet = None
    pos_tag = None
    download = None

__version__ = "1.0.0"
__status__ = "ACTIVE"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WordNetLemmatizerHandler:
    """
    Handler for WordNet-based lemmatization using NLTK.
    """

    def __init__(self):
        """
        Initialize the WordNet lemmatizer handler.
        """
        if not NLTK_AVAILABLE:
            raise ImportError(
                "NLTK is required for WordNet lemmatization. "
                "Install with: pip install nltk"
            )

        # Ensure required NLTK data is available
        self._ensure_nltk_data()

        # Initialize lemmatizer
        self.lemmatizer = WordNetLemmatizer()
        logger.info("WordNet lemmatizer initialized successfully")

    def _ensure_nltk_data(self):
        """
        Ensure required NLTK data packages are downloaded.
        """
        required_packages = ['wordnet', 'omw-1.4', 'averaged_perceptron_tagger']

        for package in required_packages:
            try:
                # Try to access the package to see if it's available
                if package == 'wordnet':
                    wordnet.ensure_loaded()
                elif package == 'omw-1.4':
                    # This will raise LookupError if not available
                    wordnet.langs()
                elif package == 'averaged_perceptron_tagger':
                    # Try POS tagging
                    pos_tag(['test'])
                logger.debug(f"NLTK package '{package}' is available")
            except (LookupError, OSError):
                logger.info(f"Downloading NLTK package: {package}")
                try:
                    download(package, quiet=True)
                except Exception as e:
                    logger.warning(f"Failed to download NLTK package '{package}': {e}")

    def get_wordnet_pos(self, word: str) -> str:
        """
        Get WordNet part-of-speech tag for a word.

        Args:
            word: Word to analyze

        Returns:
            WordNet POS tag (n, v, a, r) or 'n' as default
        """
        if not pos_tag:
            return wordnet.NOUN

        try:
            # Get POS tag from NLTK
            pos_tag_result = pos_tag([word])
            if pos_tag_result:
                tag = pos_tag_result[0][1]

                # Map Penn Treebank tags to WordNet tags
                tag_dict = {
                    "J": wordnet.ADJ,    # Adjective
                    "N": wordnet.NOUN,   # Noun
                    "V": wordnet.VERB,   # Verb
                    "R": wordnet.ADV     # Adverb
                }

                # Return first character uppercased, or default to NOUN
                first_char = tag[0].upper()
                return tag_dict.get(first_char, wordnet.NOUN)
        except Exception as e:
            logger.debug(f"POS tagging failed for '{word}': {e}")

        return wordnet.NOUN  # Default to noun

    def lemmatize_word(self, word: str) -> str:
        """
        Lemmatize a single word using WordNet.

        Args:
            word: Word to lemmatize

        Returns:
            Lemmatized word
        """
        try:
            # Get POS tag
            pos = self.get_wordnet_pos(word)

            # Lemmatize with POS tag
            lemma = self.lemmatizer.lemmatize(word, pos)

            return lemma
        except Exception as e:
            logger.warning(f"Lemmatization failed for '{word}': {e}")
            return word  # Return original word on failure

    def lemmatize_words(self, words: Set[str]) -> Set[str]:
        """
        Lemmatize a set of words.

        Args:
            words: Set of words to lemmatize

        Returns:
            Set of lemmatized words
        """
        lemmatized_words = set()

        for word in words:
            lemma = self.lemmatize_word(word)
            lemmatized_words.add(lemma)

        return lemmatized_words

    def get_info(self) -> dict:
        """
        Get information about the lemmatizer.

        Returns:
            Dictionary with lemmatizer information
        """
        return {
            'lemmatizer_type': 'wordnet',
            'library': 'nltk',
            'nltk_available': NLTK_AVAILABLE,
            'wordnet_available': wordnet is not None,
            'pos_tagger_available': pos_tag is not None
        }

def create_wordnet_lemmatizer() -> WordNetLemmatizerHandler:
    """
    Factory function to create a WordNet lemmatizer instance.

    Returns:
        WordNetLemmatizerHandler instance

    Raises:
        ImportError: If NLTK is not available
    """
    return WordNetLemmatizerHandler()

# Convenience functions
def lemmatize(word: str) -> str:
    """
    Convenience function to lemmatize a single word.

    Args:
        word: Word to lemmatize

    Returns:
        Lemmatized word
    """
    handler = WordNetLemmatizerHandler()
    return handler.lemmatize_word(word)

def lemmatize_set(words: Set[str]) -> Set[str]:
    """
    Convenience function to lemmatize a set of words.

    Args:
        words: Set of words to lemmatize

    Returns:
        Set of lemmatized words
    """
    handler = WordNetLemmatizerHandler()
    return handler.lemmatize_words(words)

if __name__ == "__main__":
    # Example usage
    try:
        lemmatizer = WordNetLemmatizerHandler()

        test_words = ["contributions", "contributing", "contributors", "running", "jumped"]
        print("WordNet Lemmatization Examples:")
        print("-" * 40)

        for word in test_words:
            lemma = lemmatizer.lemmatize_word(word)
            print(f"{word:15} → {lemma}")

    except ImportError as e:
        print(f"Error: {e}")
        print("Install NLTK with: pip install nltk")
        print("Download data with: python -c \"import nltk; nltk.download('wordnet'); nltk.download('omw-1.4'); nltk.download('averaged_perceptron_tagger')\"")

    # Changelog
    print("\nChangelog:")
    print("V0.1.0 - 2026-01-24 - Initial creation - Framework Maintenance Team - Establish foundational structure")
