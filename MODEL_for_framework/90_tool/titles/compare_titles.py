#!/usr/bin/env python3
"""
Title Comparator Module

This module provides functionality to compare extracted title files (.title.txt)
against the title_master.md template to ensure consistency and completeness.

Author: AI Framework Steward
Created: 2026-02-07
"""

import os
import re
import logging
from typing import List, Dict, Tuple, Optional, Set
from pathlib import Path

# Import the placeholder checker
from check_for_var_name import check_name

# Version variable
__version__ = "1.1.1"


class TitleTemplateComparator:
    """Comparator for validating extracted titles against template requirements."""
    
    def __init__(self, template_path: str = "../../12_rule/title_master.md"):
        """
        Initialize the comparator with template path.
        
        Args:
            template_path (str): Path to the title_master.md template file
        """
        self.template_path = template_path
        self.expected_sections = []
        self.additional_titles_analysis = {}
        self.logger = logging.getLogger(__name__)
        
    def parse_template(self) -> List[str]:
        """
        Parse the template file to extract expected sections.
        
        Returns:
            List[str]: List of expected section titles
        """
        if not os.path.exists(self.template_path):
            raise FileNotFoundError(f"Template file not found: {self.template_path}")
            
        with open(self.template_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract section titles using regex for markdown headers
        # Matches #, ##, ### followed by text
        section_pattern = r'^#{1,3}\s+(.+)$'
        matches = re.findall(section_pattern, content, re.MULTILINE)
        
        self.expected_sections = matches
        self.logger.info(f"Extracted {len(self.expected_sections)} sections from template")
        
        return self.expected_sections
    
    def parse_extracted_titles(self, title_file_path: str) -> List[str]:
        """
        Parse an extracted title file to get actual sections.
        
        Args:
            title_file_path (str): Path to the .title.txt file
            
        Returns:
            List[str]: List of extracted section titles
        """
        if not os.path.exists(title_file_path):
            raise FileNotFoundError(f"Title file not found: {title_file_path}")
            
        with open(title_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract section titles, skipping comment lines that start with #
        # Title files have format: # Section Title or ## Section Title
        lines = content.strip().split('\n')
        extracted_sections = []
        
        for line in lines:
            line = line.strip()
            # Skip comment lines (starting with # but not section headers)
            if line.startswith('# ') or line.startswith('## ') or line.startswith('### '):
                # Remove markdown header markers and strip whitespace
                section_title = re.sub(r'^#{1,3}\s+', '', line).strip()
                if section_title:
                    extracted_sections.append(section_title)
                    
        self.logger.info(f"Extracted {len(extracted_sections)} sections from {title_file_path}")
        return extracted_sections
    
    def compare_sections(self, extracted_sections: List[str]) -> Dict:
        """
        Compare extracted sections against expected template sections.
        
        Args:
            extracted_sections (List[str]): List of extracted section titles
            
        Returns:
            Dict: Comparison results with missing, extra, and compliance status
        """
        expected_set = set(self.expected_sections)
        extracted_set = set(extracted_sections)
        
        # Find missing sections
        missing_sections = expected_set - extracted_set
        
        # Find extra sections (not in template)
        extra_sections = extracted_set - expected_set
        
        # Check section order
        order_compliant = self._check_section_order(extracted_sections)
        
        # Overall compliance
        has_all_required = len(missing_sections) == 0
        has_no_extras = len(extra_sections) == 0
        overall_compliant = has_all_required and has_no_extras and order_compliant
        
        result = {
            'overall_compliant': overall_compliant,
            'has_all_required': has_all_required,
            'has_no_extras': has_no_extras,
            'order_compliant': order_compliant,
            'missing_sections': list(missing_sections),
            'extra_sections': list(extra_sections),
            'expected_sections': self.expected_sections.copy(),
            'extracted_sections': extracted_sections.copy(),
            'total_expected': len(self.expected_sections),
            'total_extracted': len(extracted_sections),
            'missing_count': len(missing_sections),
            'extra_count': len(extra_sections)
        }
        
        return result
    
    def _check_section_order(self, extracted_sections: List[str]) -> bool:
        """
        Check if extracted sections appear in the correct order.
        
        Args:
            extracted_sections (List[str]): List of extracted section titles
            
        Returns:
            bool: True if order is compliant, False otherwise
        """
        if not self.expected_sections:
            return True
            
        # Create a mapping of expected section to its index
        expected_order = {section: i for i, section in enumerate(self.expected_sections)}
        
        # Filter extracted sections to only those that are in the template
        relevant_extracted = [s for s in extracted_sections if s in expected_order]
        
        # Check if the order matches
        last_index = -1
        for section in relevant_extracted:
            current_index = expected_order[section]
            if current_index < last_index:
                return False
            last_index = current_index
            
        return True
    
    def compare_file(self, title_file_path: str) -> Dict:
        """
        Compare a single title file against the template.
        
        Args:
            title_file_path (str): Path to the .title.txt file
            
        Returns:
            Dict: Comparison results
        """
        if not self.expected_sections:
            self.parse_template()
            
        extracted_sections = self.parse_extracted_titles(title_file_path)
        result = self.compare_sections(extracted_sections)
        
        result['file_path'] = title_file_path
        result['template_path'] = self.template_path
        
        return result
    
    def compare_directory(self, directory_path: str) -> Dict[str, Dict]:
        """
        Compare all title files in a directory against the template.
        
        Args:
            directory_path (str): Path to directory containing .title.txt files
            
        Returns:
            Dict[str, Dict]: Results for each file
        """
        if not self.expected_sections:
            self.parse_template()
            
        results = {}
        
        # Find all .title.txt files in directory
        title_files = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.title.txt'):
                    title_files.append(os.path.join(root, file))
        
        self.logger.info(f"Found {len(title_files)} title files to compare")
        
        # Compare each file
        for title_file in title_files:
            try:
                result = self.compare_file(title_file)
                results[title_file] = result
            except Exception as e:
                self.logger.error(f"Error comparing {title_file}: {e}")
                results[title_file] = {
                    'error': str(e),
                    'file_path': title_file,
                    'template_path': self.template_path
                }
        
        # Analyze additional titles across all files
        self.analyze_additional_titles(results)
        
        return results
    
    def analyze_additional_titles(self, results: Dict[str, Dict]) -> Dict:
        """
        Analyze additional titles found across all files and categorize them.
        
        Args:
            results (Dict[str, Dict]): Comparison results from all files
            
        Returns:
            Dict: Analysis of additional titles with categorization
        """
        all_extra_sections = []
        file_specific_extras = {}
        
        # Collect all extra sections from all files
        for file_path, result in results.items():
            if 'extra_sections' in result and not result.get('error'):
                all_extra_sections.extend(result['extra_sections'])
                file_specific_extras[os.path.basename(file_path)] = result['extra_sections']
        
        # Categorize additional titles
        categories = self.categorize_additional_titles(all_extra_sections)
        
        # Count frequency of additional titles
        frequency = {}
        for title in all_extra_sections:
            frequency[title] = frequency.get(title, 0) + 1
        
        self.additional_titles_analysis = {
            'total_additional_titles': len(all_extra_sections),
            'unique_additional_titles': len(set(all_extra_sections)),
            'all_additional_titles': all_extra_sections,
            'file_specific_extras': file_specific_extras,
            'categories': categories,
            'frequency': frequency,
            'total_files_analyzed': len(results)
        }
        
        self.logger.info(f"Analyzed {len(all_extra_sections)} additional titles across {len(results)} files")
        return self.additional_titles_analysis
    
    def categorize_additional_titles(self, additional_titles: List[str]) -> Dict[str, List[str]]:
        """
        Categorize additional titles based on their content.
        
        Args:
            additional_titles (List[str]): List of additional titles found
            
        Returns:
            Dict[str, List[str]]: Categorized additional titles
        """
        categories = {
            'metadata': [],
            'implementation_details': [],
            'examples': [],
            'framework_references': [],
            'validation': [],
            'other': []
        }
        
        # Define keywords for categorization
        metadata_keywords = ['generated', 'extracted', 'source', 'on', 'date']
        implementation_keywords = ['components', 'breakdown', 'implementation', 'guidelines', 'automation', 'enforcement']
        example_keywords = ['example', 'format', 'pattern', 'validation']
        framework_keywords = ['framework', 'abbreviation', 'priority', 'reference', 'mapping']
        validation_keywords = ['validation', 'checklist', 'compliance', 'test']
        
        for title in additional_titles:
            title_lower = title.lower()
            
            # Check for metadata
            if any(keyword in title_lower for keyword in metadata_keywords):
                categories['metadata'].append(title)
            # Check for implementation details
            elif any(keyword in title_lower for keyword in implementation_keywords):
                categories['implementation_details'].append(title)
            # Check for examples
            elif any(keyword in title_lower for keyword in example_keywords):
                categories['examples'].append(title)
            # Check for framework references
            elif any(keyword in title_lower for keyword in framework_keywords):
                categories['framework_references'].append(title)
            # Check for validation
            elif any(keyword in title_lower for keyword in validation_keywords):
                categories['validation'].append(title)
            else:
                categories['other'].append(title)
        
        return categories
    
    def generate_report(self, results: Dict[str, Dict]) -> str:
        """
        Generate a human-readable report from comparison results.
        
        Args:
            results (Dict[str, Dict]): Comparison results
            
        Returns:
            str: Formatted report
        """
        report_lines = []
        report_lines.append("=" * 80)
        report_lines.append("TITLE TEMPLATE COMPLIANCE REPORT")
        report_lines.append("=" * 80)
        report_lines.append("")
        
        # Summary
        total_files = len(results)
        compliant_files = sum(1 for r in results.values() if r.get('overall_compliant', False))
        error_files = sum(1 for r in results.values() if 'error' in r)
        
        report_lines.append(f"SUMMARY:")
        report_lines.append(f"  Total files: {total_files}")
        report_lines.append(f"  Compliant: {compliant_files}")
        report_lines.append(f"  Errors: {error_files}")
        report_lines.append(f"  Success rate: {(compliant_files/total_files*100):.1f}%" if total_files > 0 else "  Success rate: N/A")
        report_lines.append("")
        
        # Additional Titles Analysis
        if self.additional_titles_analysis:
            analysis = self.additional_titles_analysis
            report_lines.append("ADDITIONAL TITLES ANALYSIS:")
            report_lines.append(f"  Total additional titles found: {analysis['total_additional_titles']}")
            report_lines.append(f"  Unique additional titles: {analysis['unique_additional_titles']}")
            report_lines.append(f"  Files analyzed: {analysis['total_files_analyzed']}")
            report_lines.append("")
            
            # Categorized additional titles
            for category, titles in analysis['categories'].items():
                if titles:  # Only include categories with content
                    report_lines.append(f"  {category.replace('_', ' ').title()} Titles ({len(titles)} instances):")
                    for title in sorted(set(titles)):
                        frequency = analysis['frequency'].get(title, 0)
                        report_lines.append(f"    - {title} (found {frequency} times)")
                    report_lines.append("")
        
        # File-by-file results
        for file_path, result in results.items():
            report_lines.append("-" * 60)
            report_lines.append(f"FILE: {file_path}")
            report_lines.append("-" * 60)
            
            if 'error' in result:
                report_lines.append(f"  ERROR: {result['error']}")
                continue
                
            # Compliance status
            status = "PASS" if result['overall_compliant'] else "FAIL"
            report_lines.append(f"  STATUS: {status}")
            
            # Section counts
            report_lines.append(f"  Expected sections: {result['total_expected']}")
            report_lines.append(f"  Extracted sections: {result['total_extracted']}")
            
            # Missing sections
            if result['missing_sections']:
                report_lines.append(f"  MISSING SECTIONS ({len(result['missing_sections'])}):")
                for section in result['missing_sections']:
                    report_lines.append(f"    - {section}")
            else:
                report_lines.append("  MISSING SECTIONS: None")
            
            # Extra sections
            if result['extra_sections']:
                report_lines.append(f"  EXTRA SECTIONS ({len(result['extra_sections'])}):")
                for section in result['extra_sections']:
                    report_lines.append(f"    - {section}")
            else:
                report_lines.append("  EXTRA SECTIONS: None")
            
            # Order compliance
            order_status = "PASS" if result['order_compliant'] else "FAIL"
            report_lines.append(f"  ORDER COMPLIANCE: {order_status}")
            
            report_lines.append("")
        
        return "\n".join(report_lines)
    
    def generate_compare_md(self, results: Dict[str, Dict]) -> str:
        """
        Generate a compare.md file in the same folder as the title_master file.
        
        Args:
            results (Dict[str, Dict]): Comparison results
            
        Returns:
            str: Path to the generated compare.md file
        """
        # Determine the directory for compare.md (same as title_master.md)
        template_dir = os.path.dirname(os.path.abspath(self.template_path))
        compare_file_path = os.path.join(template_dir, "compare.md")
        
        # Generate the content for compare.md
        content_lines = []
        content_lines.append("# Title Template Comparison Results")
        content_lines.append("")
        content_lines.append("This file contains the comparison results between extracted title files and the title_master.md template.")
        content_lines.append("")
        
        # Summary section
        total_files = len(results)
        compliant_files = sum(1 for r in results.values() if r.get('overall_compliant', False))
        error_files = sum(1 for r in results.values() if 'error' in r)
        
        content_lines.append("## Summary")
        content_lines.append(f"- **Total files analyzed:** {total_files}")
        content_lines.append(f"- **Compliant files:** {compliant_files}")
        content_lines.append(f"- **Files with errors:** {error_files}")
        content_lines.append(f"- **Success rate:** {(compliant_files/total_files*100):.1f}%" if total_files > 0 else "- **Success rate:** N/A")
        content_lines.append("")
        
        # Missing sections section
        content_lines.append("## Missing Sections")
        content_lines.append("List of sections that are missing from extracted titles compared to the template:")
        content_lines.append("")
        
        missing_sections_found = False
        for file_path, result in results.items():
            if 'error' in result:
                continue
            if result['missing_sections']:
                missing_sections_found = True
                relative_path = os.path.relpath(file_path, template_dir)
                content_lines.append(f"### {relative_path}")
                for section in result['missing_sections']:
                    content_lines.append(f"- {section}")
                content_lines.append("")
        
        if not missing_sections_found:
            content_lines.append("No missing sections found across all files.")
            content_lines.append("")
        
        # Extra sections section
        content_lines.append("## Extra Sections")
        content_lines.append("List of sections found in extracted titles that are not in the template:")
        content_lines.append("")
        
        extra_sections_found = False
        for file_path, result in results.items():
            if 'error' in result:
                continue
            if result['extra_sections']:
                extra_sections_found = True
                relative_path = os.path.relpath(file_path, template_dir)
                content_lines.append(f"### {relative_path}")
                for section in result['extra_sections']:
                    content_lines.append(f"- {section}")
                content_lines.append("")
        
        if not extra_sections_found:
            content_lines.append("No extra sections found across all files.")
            content_lines.append("")
        
        # Compliance status section
        content_lines.append("## Compliance Status")
        content_lines.append("Overall compliance status for each file:")
        content_lines.append("")
        
        for file_path, result in results.items():
            if 'error' in result:
                relative_path = os.path.relpath(file_path, template_dir)
                content_lines.append(f"- **{relative_path}:** ERROR - {result['error']}")
                continue
                
            status = "✅ PASS" if result['overall_compliant'] else "❌ FAIL"
            relative_path = os.path.relpath(file_path, template_dir)
            content_lines.append(f"- **{relative_path}:** {status}")
        content_lines.append("")
        
        # Additional titles analysis section
        if self.additional_titles_analysis:
            analysis = self.additional_titles_analysis
            content_lines.append("## Additional Titles Analysis")
            content_lines.append("")
            content_lines.append(f"**Total additional titles found:** {analysis['total_additional_titles']}")
            content_lines.append(f"**Unique additional titles:** {analysis['unique_additional_titles']}")
            content_lines.append(f"**Files analyzed:** {analysis['total_files_analyzed']}")
            content_lines.append("")
            
            # Categorized additional titles
            for category, titles in analysis['categories'].items():
                if titles:  # Only include categories with content
                    content_lines.append(f"### {category.replace('_', ' ').title()} Titles")
                    content_lines.append(f"({len(titles)} instances found)")
                    content_lines.append("")
                    for title in sorted(set(titles)):
                        frequency = analysis['frequency'].get(title, 0)
                        content_lines.append(f"- **{title}** (found {frequency} times)")
                    content_lines.append("")
        
        # Recommendations section
        content_lines.append("## Recommendations")
        content_lines.append("")
        
        # Generate recommendations based on analysis
        recommendations = []
        
        if missing_sections_found:
            recommendations.append("- Review missing sections and ensure all required sections are present in extracted titles")
        
        if extra_sections_found:
            recommendations.append("- Evaluate extra sections to determine if they should be added to the template or removed from extracted titles")
        
        if self.additional_titles_analysis and self.additional_titles_analysis['unique_additional_titles'] > 0:
            recommendations.append("- Consider updating the template to include commonly found additional titles")
        
        if not recommendations:
            recommendations.append("- No specific recommendations - all files are compliant with the template")
        
        for rec in recommendations:
            content_lines.append(rec)
        content_lines.append("")
        
        # Footer
        content_lines.append("---")
        content_lines.append(f"*Generated on {self._get_current_timestamp()}*")
        content_lines.append(f"*Template used: {os.path.basename(self.template_path)}*")
        
        # Write the compare.md file
        content = "\n".join(content_lines)
        with open(compare_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        self.logger.info(f"Generated compare.md file at: {compare_file_path}")
        return compare_file_path
    
    def _get_current_timestamp(self) -> str:
        """Get current timestamp in readable format."""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main():
    """Main function for command-line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Compare title files against template')
    parser.add_argument('path', help='Path to title file or directory')
    parser.add_argument('--template', default='../12_rule/title_master.md', 
                       help='Path to template file (default: ../12_rule/title_master.md)')
    parser.add_argument('--output', help='Output file for report')
    
    args = parser.parse_args()
    
    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Create comparator
    comparator = TitleTemplateComparator(args.template)
    
    # Compare files
    if os.path.isfile(args.path):
        result = comparator.compare_file(args.path)
        results = {args.path: result}
    else:
        results = comparator.compare_directory(args.path)
    
    # Generate compare.md file
    compare_md_path = comparator.generate_compare_md(results)
    print(f"Generated compare.md file at: {compare_md_path}")
    
    # Generate report
    report = comparator.generate_report(results)
    
    # Output report
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report written to {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()


"""
## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|------------|
| V1.1.1 | 2026-02-07 | Applied version and changelog update rule per RULE_FOR_MFW_VERSION_CHANGELOG_UPDATE, updated version number and enhanced changelog format | AI Framework Steward | Ensure compliance with framework version and changelog standards |
| V1.1.0 | 2026-02-07 | Added generate_compare_md method to create compare.md file in the same folder as title_master.md, including summary, missing sections, extra sections, compliance status, additional titles analysis, and recommendations | AI Framework Steward | Implement requirement R11 from title_master_requi.md to generate comprehensive comparison results in markdown format |
| V1.0.0 | 2026-02-07 | Initial creation of compare_titles.py with TitleTemplateComparator class and integration of check_for_var_name import | AI Framework Steward | Establish foundational title comparison functionality with placeholder detection |
"""
