#!/usr/bin/env python3
"""
Checker for Word in Language - Check word availability in language stem dictionaries
"""

import sys
import os
import argparse

# Add current directory to path
sys.path.insert(0, os.getcwd())

def check_word_in_language(word, lang_code, lang_name):
    """Check if a word exists in a specific language's stem dictionaries"""

    print(f'🔍 Checking word "{word}" in {lang_name} ({lang_code}) stem dictionaries...')
    print('=' * 60)

    results = {
        'wordnet_available': False,
        'wordnet_synsets': 0,
        'snowball_available': False,
        'stem_result': None,
        'porter_available': False,
        'porter_stem': None
    }

    try:
        import nltk
        from nltk.corpus import wordnet as wn

        # Check WordNet for the language
        try:
            lang_synsets = wn.synsets(word, lang=lang_code)
            results['wordnet_available'] = True
            results['wordnet_synsets'] = len(lang_synsets)

            print(f'✅ WordNet ({lang_name}): Found {len(lang_synsets)} synsets')

            if lang_synsets:
                for i, synset in enumerate(lang_synsets[:3]):  # Show up to 3 synsets
                    print(f'   {i+1}. {synset.name()}: {synset.definition()[:80]}...')
                    lemmas = [lemma.name() for lemma in synset.lemmas(lang=lang_code)]
                    if lemmas:
                        print(f'      Lemmas: {lemmas[:5]}')  # Show up to 5 lemmas

        except Exception as e:
            print(f'❌ WordNet ({lang_name}) error: {e}')

        # Check Snowball stemmer for the language
        snowball_languages = {
            'en': 'english', 'de': 'german', 'fr': 'french', 'es': 'spanish',
            'pt': 'portuguese', 'it': 'italian', 'ru': 'russian', 'da': 'danish',
            'nl': 'dutch', 'no': 'norwegian', 'sv': 'swedish', 'fi': 'finnish'
        }

        # Check CLTK for classical languages
        cltk_languages = {
            'la': 'latin', 'grc': 'greek', 'san': 'sanskrit', 'ara': 'arabic',
            'chi': 'chinese', 'cop': 'coptic', 'got': 'gothic', 'heb': 'hebrew',
            'pli': 'pali', 'xno': 'old_norse'
        }

        if lang_code in snowball_languages:
            try:
                from nltk.stem.snowball import SnowballStemmer
                stemmer = SnowballStemmer(snowball_languages[lang_code])
                stem_result = stemmer.stem(word)
                results['snowball_available'] = True
                results['stem_result'] = stem_result

                print(f'✅ Snowball Stemmer ({lang_name}): "{word}" -> "{stem_result}"')

            except Exception as e:
                print(f'❌ Snowball Stemmer ({lang_name}) error: {e}')

        elif lang_code in cltk_languages:
            # Debug CLTK API
            try:
                import cltk
                print(f"CLTK version: {cltk.__version__}")
                print(f"CLTK top-level modules: {[x for x in dir(cltk) if not x.startswith('_')]}")
                if hasattr(cltk, 'stem'):
                    print(f"CLTK stem module: {dir(cltk.stem)}")
                    if hasattr(cltk.stem, 'latin'):
                        print(f"CLTK latin module: {dir(cltk.stem.latin)}")
                else:
                    print("CLTK has no 'stem' attribute - checking alternatives...")
                    if hasattr(cltk, 'lemmatize'):
                        print(f"CLTK lemmatize module: {dir(cltk.lemmatize)}")
                        if hasattr(cltk.lemmatize, 'latin'):
                            print(f"CLTK lemmatize.latin: {dir(cltk.lemmatize.latin)}")
                    if hasattr(cltk, 'morphology'):
                        print(f"CLTK morphology module: {dir(cltk.morphology)}")
                        if hasattr(cltk.morphology, 'latin'):
                            print(f"CLTK morphology.latin: {dir(cltk.morphology.latin)}")
                    if hasattr(cltk, 'nlp'):
                        print(f"CLTK nlp module has LatinPipeline: {'LatinPipeline' in dir(cltk.nlp)}")
            except Exception as e:
                print(f"CLTK debug error: {e}")

            try:
                # Try different CLTK import patterns
                stem_result = None

                if lang_code == 'la':
                    try:
                        # CLTK 1.x style (version 1.5.0 detected) - use lemmatizer
                        from cltk.lemmatize.lat import LatinBackoffLemmatizer
                        lemmatizer = LatinBackoffLemmatizer()
                        # Lemmatizer returns a list of possible lemmas
                        lemmas = lemmatizer.lemmatize([word])
                        stem_result = lemmas[0] if lemmas and lemmas[0] else word
                    except Exception as e:
                        error_msg = str(e)
                        if 'latin_models_cltk' in error_msg:
                            print(f"⚠️  CLTK Latin models not downloaded. Error: {error_msg}")
                            print("   To download: python -c \"from cltk.corpus.utils.importer import CorpusImporter; ci = CorpusImporter('latin'); ci.import_corpus()\"")
                            stem_result = None
                        else:
                            try:
                                # Alternative CLTK 1.x lemmatizer
                                from cltk.lemmatize.latin import BackoffLemmatizer
                                lemmatizer = BackoffLemmatizer()
                                lemmas = lemmatizer.lemmatize([word])
                                stem_result = lemmas[0] if lemmas and lemmas[0] else word
                            except (ImportError, AttributeError):
                                try:
                                    # CLTK 1.x style (version 1.5.0 detected)
                                    from cltk.stem.latin import Stemmer
                                    stemmer = Stemmer()
                                    stem_result = stemmer.stem(word)
                                except (ImportError, AttributeError):
                                    try:
                                        # CLTK 2.x style
                                        from cltk.stem.latin import LatinStems
                                        stemmer = LatinStems()
                                        stems = stemmer.get_stems(word)
                                        stem_result = stems[0] if stems else word
                                    except:
                                        stem_result = None

                elif lang_code == 'grc':
                    try:
                        from cltk.stem.greek import GreekStemmer
                        stemmer = GreekStemmer()
                        stem_result = stemmer.stem(word)
                    except ImportError:
                        try:
                            from cltk.stem import Stemmer
                            stemmer = Stemmer(language='greek')
                            stem_result = stemmer.stem(word)
                        except:
                            # Try CLTK 1.x style
                            import cltk
                            stem_result = cltk.stem.greek.stem(word)
                else:
                    # Fallback for other CLTK languages
                    try:
                        from cltk.stem import Stemmer
                        stemmer = Stemmer(language=cltk_languages[lang_code])
                        stem_result = stemmer.stem(word)
                    except:
                        print(f'❌ CLTK Stemmer ({lang_name}): Unsupported language')

                if stem_result:
                    results['cltk_available'] = True
                    results['stem_result'] = stem_result
                    print(f'✅ CLTK Stemmer ({lang_name}): "{word}" -> "{stem_result}"')
                else:
                    print(f'❌ CLTK Stemmer ({lang_name}): No result')

            except ImportError as e:
                print(f'❌ CLTK not available for {lang_name}: {e}')
            except Exception as e:
                print(f'❌ CLTK Stemmer ({lang_name}) error: {e}')

        # Check Porter stemmer (English only, but show for comparison)
        if lang_code == 'en':
            try:
                from nltk.stem import PorterStemmer
                porter = PorterStemmer()
                porter_stem = porter.stem(word)
                results['porter_available'] = True
                results['porter_stem'] = porter_stem

                print(f'✅ Porter Stemmer (English): "{word}" -> "{porter_stem}"')

            except Exception as e:
                print(f'❌ Porter Stemmer error: {e}')

    except ImportError as e:
        print(f'❌ NLTK not available: {e}')
        print('Please install NLTK: pip install nltk')
        return results

    print('\\n📊 Summary:')
    print(f'   Word: {word}')
    print(f'   Language: {lang_name} ({lang_code})')
    print(f'   WordNet synsets: {results["wordnet_synsets"]}')
    if results['stem_result']:
        print(f'   Snowball stem: {results["stem_result"]}')
    if results['porter_stem']:
        print(f'   Porter stem: {results["porter_stem"]}')

    return results

def main():
    """Main function for the word checker"""
    parser = argparse.ArgumentParser(
        description="Checker for Word in Language - Check word availability in language stem dictionaries"
    )
    parser.add_argument(
        'lang',
        help='Language code (e.g., en, de, fr, es)'
    )
    parser.add_argument(
        'word',
        help='Word to check in the language dictionaries'
    )

    args = parser.parse_args()

    # Language name mapping
    lang_names = {
        'en': 'English', 'de': 'German', 'fr': 'French', 'es': 'Spanish',
        'pt': 'Portuguese', 'it': 'Italian', 'ru': 'Russian', 'da': 'Danish',
        'nl': 'Dutch', 'no': 'Norwegian', 'sv': 'Swedish', 'fi': 'Finnish',
        'la': 'Latin', 'grc': 'Ancient Greek', 'san': 'Sanskrit', 'ara': 'Arabic',
        'chi': 'Chinese', 'cop': 'Coptic', 'got': 'Gothic', 'heb': 'Hebrew',
        'pli': 'Pali', 'xno': 'Old Norse'
    }

    lang_name = lang_names.get(args.lang, f'Language-{args.lang.upper()}')

    # Check the word
    results = check_word_in_language(args.word, args.lang, lang_name)

    print('\\n✨ Word check complete!')

if __name__ == "__main__":
    main()
