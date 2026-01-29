#!/usr/bin/env python3
"""
ReaderForTrait - Python implementation for reading and understanding Traits.yaml

This tool provides functionality to parse and analyze the agent trait composition file.
"""

import yaml
import os
from typing import Dict, List, Optional, Union, Any
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Expertise:
    """Represents an expertise area"""
    name: str
    description: str
    keywords: List[str]

@dataclass
class Personality:
    """Represents a personality trait"""
    name: str
    description: str
    prompt_fragment: str

@dataclass
class Approach:
    """Represents an approach style"""
    name: str
    description: str
    prompt_fragment: str

@dataclass
class VoiceInfo:
    """Represents voice information"""
    voice_id: str
    characteristics: List[str]
    description: str
    stability: float
    similarity_boost: float

@dataclass
class TraitMapping:
    """Represents a trait to voice mapping"""
    traits: List[str]
    voice: str
    voice_id: str
    reason: str

@dataclass
class VoiceMappings:
    """Represents voice mapping configuration"""
    default: str
    default_voice_id: str
    voice_registry: Dict[str, VoiceInfo]
    mappings: List[TraitMapping]
    fallbacks: Dict[str, str]

@dataclass
class CompositionExample:
    """Represents a composition example"""
    description: str
    traits: List[str]

@dataclass
class TraitData:
    """Main data structure for traits"""
    expertise: Dict[str, Expertise]
    personality: Dict[str, Personality]
    approach: Dict[str, Approach]
    voice_mappings: VoiceMappings
    examples: Dict[str, CompositionExample]

class ReaderForTrait:
    """
    A tool to read and understand the Traits.yaml file for agent composition.
    """

    def __init__(self, file_path: str = 'PAI/Packs/pai-agents-skill/src/skills/Agents/Data/Traits.yaml'):
        """
        Initialize the ReaderForTrait with the path to Traits.yaml

        Args:
            file_path: Path to the Traits.yaml file
        """
        self.file_path = self._resolve_path(file_path)
        self.trait_data = self.parse_yaml()

    def _resolve_path(self, file_path: str) -> str:
        """Resolve the file path relative to current working directory"""
        if not os.path.isabs(file_path):
            # Resolve relative to current working directory
            return str(Path(os.getcwd()) / file_path)
        return file_path

    def parse_yaml(self) -> TraitData:
        """
        Parse the YAML file and return structured trait data

        Returns:
            TraitData object containing all parsed data

        Raises:
            FileNotFoundError: If the file doesn't exist
            yaml.YAMLError: If there's an error parsing the YAML
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                raw_data = yaml.safe_load(file)

            # Convert raw YAML data to structured objects
            expertise = {
                key: Expertise(
                    name=item['name'],
                    description=item['description'],
                    keywords=item['keywords']
                )
                for key, item in raw_data['expertise'].items()
            }

            personality = {
                key: Personality(
                    name=item['name'],
                    description=item['description'],
                    prompt_fragment=item['prompt_fragment']
                )
                for key, item in raw_data['personality'].items()
            }

            approach = {
                key: Approach(
                    name=item['name'],
                    description=item['description'],
                    prompt_fragment=item['prompt_fragment']
                )
                for key, item in raw_data['approach'].items()
            }

            # Parse voice mappings
            voice_mappings_data = raw_data['voice_mappings']
            voice_registry = {
                name: VoiceInfo(
                    voice_id=info['voice_id'],
                    characteristics=info['characteristics'],
                    description=info['description'],
                    stability=info['stability'],
                    similarity_boost=info['similarity_boost']
                )
                for name, info in voice_mappings_data['voice_registry'].items()
            }

            mappings = [
                TraitMapping(
                    traits=mapping['traits'],
                    voice=mapping['voice'],
                    voice_id=mapping['voice_id'],
                    reason=mapping['reason']
                )
                for mapping in voice_mappings_data['mappings']
            ]

            voice_mappings = VoiceMappings(
                default=voice_mappings_data['default'],
                default_voice_id=voice_mappings_data['default_voice_id'],
                voice_registry=voice_registry,
                mappings=mappings,
                fallbacks=voice_mappings_data['fallbacks']
            )

            examples = {
                key: CompositionExample(
                    description=example['description'],
                    traits=example['traits']
                )
                for key, example in raw_data['examples'].items()
            }

            return TraitData(
                expertise=expertise,
                personality=personality,
                approach=approach,
                voice_mappings=voice_mappings,
                examples=examples
            )

        except FileNotFoundError:
            raise FileNotFoundError(f"Traits.yaml file not found at: {self.file_path}")
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML file: {e}")
        except Exception as e:
            raise Exception(f"Failed to parse Traits.yaml: {e}")

    def get_expertise_details(self, expertise_key: str) -> Optional[Expertise]:
        """
        Get details for a specific expertise area

        Args:
            expertise_key: The expertise key (e.g., "security", "technical")

        Returns:
            Expertise object or None if not found
        """
        return self.trait_data.expertise.get(expertise_key)

    def get_personality_details(self, personality_key: str) -> Optional[Personality]:
        """
        Get details for a specific personality trait

        Args:
            personality_key: The personality key (e.g., "skeptical", "analytical")

        Returns:
            Personality object or None if not found
        """
        return self.trait_data.personality.get(personality_key)

    def get_approach_details(self, approach_key: str) -> Optional[Approach]:
        """
        Get details for a specific approach style

        Args:
            approach_key: The approach key (e.g., "thorough", "systematic")

        Returns:
            Approach object or None if not found
        """
        return self.trait_data.approach.get(approach_key)

    def find_voice_for_traits(self, traits: List[str]) -> Dict[str, Union[str, None]]:
        """
        Find the optimal voice for a combination of traits

        Args:
            traits: List of trait strings

        Returns:
            Dictionary with voice, voice_id, and optional reason
        """
        # Sort traits for consistent matching
        sorted_traits = sorted(traits)

        # First, try to find exact trait combination matches
        for mapping in self.trait_data.voice_mappings.mappings:
            mapping_traits = sorted(mapping.traits)
            if sorted_traits == mapping_traits:
                return {
                    'voice': mapping.voice,
                    'voice_id': mapping.voice_id,
                    'reason': mapping.reason
                }

        # If no exact match, try to find the best partial match
        best_match = None
        best_match_score = 0

        for mapping in self.trait_data.voice_mappings.mappings:
            intersection = [trait for trait in mapping.traits if trait in traits]
            score = len(intersection)

            if score > best_match_score:
                best_match_score = score
                best_match = mapping

        if best_match and best_match_score > 0:
            return {
                'voice': best_match.voice,
                'voice_id': best_match.voice_id,
                'reason': f"{best_match.reason} (partial match)"
            }

        # If no partial match, use fallback for the first trait
        if traits:
            first_trait = traits[0]
            voice_name = self.trait_data.voice_mappings.fallbacks.get(first_trait)
            if voice_name:
                voice_info = self.trait_data.voice_mappings.voice_registry.get(voice_name)
                if voice_info:
                    return {
                        'voice': voice_name,
                        'voice_id': voice_info.voice_id
                    }

        # Final fallback to default voice
        return {
            'voice': self.trait_data.voice_mappings.default,
            'voice_id': self.trait_data.voice_mappings.default_voice_id
        }

    def generate_agent_composition(self, task_description: str) -> List[List[str]]:
        """
        Generate recommended traits for a specific task

        Args:
            task_description: Description of the task

        Returns:
            List of recommended trait combinations
        """
        recommendations = []
        lower_task = task_description.lower()

        # Check for predefined examples first
        for example_key, example in self.trait_data.examples.items():
            if (example_key.lower() in lower_task or
                any(trait.lower() in lower_task for trait in example.traits)):
                recommendations.append(example.traits)

        # Add some intelligent recommendations based on keywords
        keyword_recommendations = self._generate_keyword_based_recommendations(lower_task)
        if keyword_recommendations:
            recommendations.extend(keyword_recommendations)

        # Remove duplicates while preserving order
        seen = set()
        unique_recommendations = []
        for trait_combo in recommendations:
            # Convert list to tuple for hashability
            trait_tuple = tuple(trait_combo)
            if trait_tuple not in seen:
                seen.add(trait_tuple)
                unique_recommendations.append(trait_combo)

        return unique_recommendations

    def _generate_keyword_based_recommendations(self, task_description: str) -> List[List[str]]:
        """
        Generate trait recommendations based on keywords in task description

        Args:
            task_description: Lowercase task description

        Returns:
            List of recommended trait combinations
        """
        recommendations = []

        # Security-related tasks
        if any(keyword in task_description for keyword in ['security', 'audit', 'vulnerability', 'threat']):
            recommendations.append(['security', 'skeptical', 'thorough', 'adversarial'])

        # Legal/Contract tasks
        if any(keyword in task_description for keyword in ['contract', 'legal', 'agreement', 'terms']):
            recommendations.append(['legal', 'cautious', 'meticulous', 'systematic'])

        # Technical/Code tasks
        if any(keyword in task_description for keyword in ['code', 'technical', 'implementation', 'debug']):
            recommendations.append(['technical', 'meticulous', 'systematic'])

        # Research tasks
        if any(keyword in task_description for keyword in ['research', 'study', 'analysis']):
            recommendations.append(['research', 'analytical', 'thorough'])

        # Creative tasks
        if any(keyword in task_description for keyword in ['creative', 'design', 'content']):
            recommendations.append(['creative', 'enthusiastic', 'exploratory'])

        # Business tasks
        if any(keyword in task_description for keyword in ['business', 'market', 'strategy']):
            recommendations.append(['business', 'analytical', 'comparative', 'thorough'])

        return recommendations

    def analyze_compatibility(self, traits: List[str]) -> Dict[str, Any]:
        """
        Analyze the compatibility and effectiveness of trait combinations

        Args:
            traits: List of traits to analyze

        Returns:
            Dictionary with compatibility analysis
        """
        analysis = {
            'traits': traits,
            'expertise_count': 0,
            'personality_count': 0,
            'approach_count': 0,
            'potential_conflicts': [],
            'recommendations': []
        }

        # Categorize traits
        for trait in traits:
            if trait in self.trait_data.expertise:
                analysis['expertise_count'] += 1
            elif trait in self.trait_data.personality:
                analysis['personality_count'] += 1
            elif trait in self.trait_data.approach:
                analysis['approach_count'] += 1

        # Check for potential conflicts
        if 'skeptical' in traits and 'enthusiastic' in traits:
            analysis['potential_conflicts'].append(
                "Skeptical and enthusiastic traits may conflict - skeptical questions assumptions while enthusiastic embraces discoveries"
            )

        if 'thorough' in traits and 'rapid' in traits:
            analysis['potential_conflicts'].append(
                "Thorough and rapid approaches may conflict - thorough requires comprehensive analysis while rapid focuses on speed"
            )

        if 'bold' in traits and 'cautious' in traits:
            analysis['potential_conflicts'].append(
                "Bold and cautious traits may conflict - bold takes risks while cautious considers failure modes"
            )

        # Add recommendations
        if analysis['expertise_count'] == 0:
            analysis['recommendations'].append(
                "Consider adding an expertise trait to define the agent's domain knowledge"
            )

        if analysis['personality_count'] == 0:
            analysis['recommendations'].append(
                "Consider adding a personality trait to define how the agent thinks and behaves"
            )

        if analysis['approach_count'] == 0:
            analysis['recommendations'].append(
                "Consider adding an approach trait to define how the agent works on tasks"
            )

        return analysis

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the reader
        reader = ReaderForTrait()

        # Example: Get expertise details
        security_expertise = reader.get_expertise_details("security")
        print(f"Security Expertise: {security_expertise.name}")
        print(f"Description: {security_expertise.description[:100]}...")

        # Example: Find voice for traits
        voice_result = reader.find_voice_for_traits(["security", "skeptical", "thorough"])
        print(f"\nRecommended Voice: {voice_result['voice']} ({voice_result['voice_id']})")
        print(f"Reason: {voice_result.get('reason', 'Default fallback')}")

        # Example: Generate composition
        compositions = reader.generate_agent_composition("security architecture review")
        print(f"\nRecommended compositions for security review:")
        for i, comp in enumerate(compositions, 1):
            print(f"{i}. {comp}")

        # Example: Analyze compatibility
        compatibility = reader.analyze_compatibility(["security", "skeptical", "thorough", "adversarial"])
        print(f"\nCompatibility analysis:")
        print(f"Expertise: {compatibility['expertise_count']}, Personality: {compatibility['personality_count']}, Approach: {compatibility['approach_count']}")
        if compatibility['potential_conflicts']:
            print("Potential conflicts:")
            for conflict in compatibility['potential_conflicts']:
                print(f" - {conflict}")

    except Exception as e:
        print(f"Error: {e}")