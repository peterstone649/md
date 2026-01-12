#!/usr/bin/env python3
"""
Template Validator Tool
========================

This script validates template documents against the YAML schema
and generates a task file for AI agents to work on.

Usage:
    python templ_validator.py <file_to_check> [--schema <schema_file>]

Example:
    python templ_validator.py ../15_convention_for_abbreviations.md
"""

import argparse
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple
import yaml


class TemplateValidator:
    """Validates template documents against the YAML schema."""
    
    def __init__(self, schema_file: str):
        """Initialize validator with schema file."""
        self.schema_file = Path(schema_file)
        self.schema = self._load_schema()
        self.validation_results = []
        self.missing_elements = []
        self.recommendations = []
        
    def _load_schema(self) -> Dict:
        """Load YAML schema from file."""
        try:
            with open(self.schema_file, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Error: Schema file not found: {self.schema_file}")
            sys.exit(1)
        except yaml.YAMLError as e:
            print(f"Error parsing schema file: {e}")
            sys.exit(1)
    
    def parse_markdown_template(self, content: str) -> Dict:
        """Parse a markdown template file into structured data."""
        parsed = {
            'header': {},
            'sections': {},
            'tables': [],
            'links': [],
        }
        
        lines = content.split('\n')
        current_section = None
        in_header = True
        header_buffer = []
        
        for i, line in enumerate(lines):
            if in_header:
                if line.startswith('---'):
                    continue
                elif line.startswith('## '):
                    in_header = False
                    parsed['header'] = self._parse_header('\n'.join(header_buffer))
                    current_section = line.replace('## ', '').strip()
                else:
                    header_buffer.append(line)
                continue
            
            if line.startswith('## '):
                current_section = line.replace('## ', '').strip()
            elif line.startswith('| ') and '|' in line:
                table_entry = {
                    'section': current_section,
                    'line': i + 1,
                    'content': line.strip()
                }
                parsed['tables'].append(table_entry)
            elif line.startswith('[') and ']' in line and '(' in line:
                link_match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', line)
                if link_match:
                    parsed['links'].append({
                        'text': link_match.group(1),
                        'url': link_match.group(2),
                        'line': i + 1
                    })
        
        parsed['header'] = self._parse_header('\n'.join(header_buffer))
        return parsed
    
    def _parse_header(self, header_content: str) -> Dict:
        """Parse the template header metadata."""
        header = {}
        
        version_match = re.search(r'\*\*Version:\*\*\s*(V\d+\.\d+\.\d+)', header_content)
        if version_match:
            header['version'] = version_match.group(1)
        
        status_match = re.search(r'\*\*Status:\*\*\s*(\w+(?:\s+\w+)*)', header_content)
        if status_match:
            header['status'] = status_match.group(1).strip()
        
        date_match = re.search(r'\*\*Date:\*\*\s*(\d{4}-\d{2}-\d{2})', header_content)
        if date_match:
            header['date'] = date_match.group(1)
        
        confidence_match = re.search(r'\*\*Confidence Score:\*\*\s*(\d)', header_content)
        if confidence_match:
            header['confidence_score'] = int(confidence_match.group(1))
        
        integration_match = re.search(r'\*\*Integration Field:\*\*\s*(\w+)', header_content)
        if integration_match:
            header['integration_field'] = integration_match.group(1)
        
        # Search for CONV_FOR_ pattern in header content
        # Pattern: **[CONV_FOR_xxx]** or (CONV_FOR_xxx) anywhere in header
        conv_for_match = re.search(r'\*\*\[CONV_FOR_[^\]]+\]\*\*', header_content)
        if conv_for_match:
            header['title'] = conv_for_match.group(0)
        else:
            # Also try pattern without escaping (markdown can use single or double asterisks)
            conv_for_match2 = re.search(r'\[CONV_FOR_[^\]]+\]', header_content)
            if conv_for_match2:
                header['title'] = '**' + conv_for_match2.group(0) + '**'
            else:
                # Also accept parentheses format: (CONV_FOR_xxx)
                conv_for_match3 = re.search(r'\(CONV_FOR_[^\)]+\)', header_content)
                if conv_for_match3:
                    header['title'] = '**' + conv_for_match3.group(0) + '**'
        
        return header
    
    def validate_header(self, header: Dict) -> List[str]:
        """Validate header section."""
        errors = []
        
        if not header.get('title'):
            errors.append("Missing template title (must start with [CONV_FOR_ or (CONV_FOR_)")
        else:
            # Remove markdown bold formatting for validation
            clean_title = header['title'].strip('*')
            if not (clean_title.startswith('[CONV_FOR_') or clean_title.startswith('(CONV_FOR_')):
                errors.append(f"Invalid title format: {header['title']}")
        
        if not header.get('version'):
            errors.append("Missing version number")
        elif not re.match(r'^V\d+\.\d+\.\d+$', header['version']):
            errors.append(f"Invalid version format: {header['version']} (expected V0.1.0)")
        
        valid_statuses = ['DRAFT', 'OPEN', 'IN PROGRESS', 'PAUSED', 'REVIEW', 'APPROVED', 'DONE', 'ARCHIVED']
        if not header.get('status'):
            errors.append("Missing status")
        elif header['status'] not in valid_statuses:
            errors.append(f"Invalid status: {header['status']}")
        
        if not header.get('date'):
            errors.append("Missing date")
        elif not re.match(r'^\d{4}-\d{2}-\d{2}$', header['date']):
            errors.append(f"Invalid date format: {header['date']} (expected YYYY-MM-DD)")
        
        if not header.get('confidence_score'):
            errors.append("Missing confidence score")
        elif not 1 <= header['confidence_score'] <= 5:
            errors.append(f"Invalid confidence score: {header['confidence_score']} (must be 1-5)")
        
        valid_fields = ['OT', 'MODEL_for_framework', 'FIELDC', 'FIELDM']
        if not header.get('integration_field'):
            errors.append("Missing integration field")
        elif header['integration_field'] not in valid_fields:
            errors.append(f"Invalid integration field: {header['integration_field']}")
        
        return errors
    
    def validate_sections(self, content: str, parsed: Dict) -> List[str]:
        """Validate required sections exist."""
        errors = []
        
        required_sections = [
            'Derivation Source', 'Core Inheritance', 'Rationale', 'Abstract',
            'Scope and Applicability', 'Core Definitions', 'Version Requirements',
            'Rules and Guidelines', 'Naming Conventions', 'Status and States',
            'Examples', 'Related Conventions', 'Implementation', 'Changelog'
        ]
        
        for section in required_sections:
            if section not in content:
                errors.append(f"Missing required section: {section}")
                self.missing_elements.append({
                    'type': 'section',
                    'name': section,
                    'priority': 'high'
                })
        
        return errors
    
    def validate_tables(self, tables: List[Dict]) -> List[str]:
        """Validate table structures."""
        errors = []
        
        status_table_found = False
        definition_table_found = False
        
        for table in tables:
            if 'Status' in table['content'] and 'Meaning' in table['content']:
                status_table_found = True
            if 'Element' in table['content'] and 'Definition' in table['content']:
                definition_table_found = True
        
        if not status_table_found:
            errors.append("Missing Status and States table")
            self.missing_elements.append({'type': 'table', 'name': 'Status and States', 'priority': 'high'})
        
        if not definition_table_found:
            errors.append("Missing Core Definitions table")
            self.missing_elements.append({'type': 'table', 'name': 'Core Definitions', 'priority': 'high'})
        
        return errors
    
    def validate_statuses(self, content: str) -> List[str]:
        """Validate all 8 status values are present."""
        errors = []

        required_statuses = ['DRAFT', 'OPEN', 'IN PROGRESS', 'PAUSED', 'REVIEW', 'APPROVED', 'DONE', 'ARCHIVED']
        missing = []
        
        for status in required_statuses:
            if status not in content:
                missing.append(status)
        
        if missing:
            errors.append(f"Missing status values: {', '.join(missing)}")
            for status in missing:
                self.missing_elements.append({'type': 'status', 'name': status, 'priority': 'high'})
        
        return errors
    
    def validate(self, content: str) -> Tuple[bool, List[str]]:
        """Run all validations on the template content."""
        self.validation_results = []
        self.missing_elements = []
        self.recommendations = []
        
        parsed = self.parse_markdown_template(content)
        
        self.validation_results.extend(self.validate_header(parsed['header']))
        self.validation_results.extend(self.validate_sections(content, parsed))
        self.validation_results.extend(self.validate_tables(parsed['tables']))
        self.validation_results.extend(self.validate_statuses(content))
        
        is_valid = len(self.validation_results) == 0
        return is_valid, self.validation_results
    
    def generate_task_file(self, file_path: str, validation_errors: List[str]) -> str:
        """Generate a task markdown file for AI agents."""
        file_path = Path(file_path)
        
        priority_order = {'high': 0, 'medium': 1, 'low': 2}
        sorted_elements = sorted(
            self.missing_elements,
            key=lambda x: (priority_order.get(x['priority'], 3), x['type'], x['name'])
        )
        
        task_content = f"""# Task File for Template Validation

> **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
> **File Validated:** {file_path.name}
> **Status:** {'✅ ALL VALIDATIONS PASSED' if not validation_errors else '❌ VALIDATION ISSUES FOUND'}

---

## Summary

| Metric | Value |
|--------|-------|
| Total Issues | {len(validation_errors)} |
| Missing Sections | {len([e for e in self.missing_elements if e['type'] == 'section'])} |
| Missing Tables | {len([e for e in self.missing_elements if e['type'] == 'table'])} |
| Missing Statuses | {len([e for e in self.missing_elements if e['type'] == 'status'])} |

---

## Validation Results

{'✅ No validation errors found!' if not validation_errors else '### ❌ Issues Found (' + str(len(validation_errors)) + ')'}

"""
        
        if validation_errors:
            task_content += "#### Critical Issues\n\n"
            for i, error in enumerate(validation_errors, 1):
                task_content += f"{i}. {error}\n"
            task_content += "\n"
        
        if sorted_elements:
            task_content += "### 📋 Missing Elements (Priority Order)\n\n"
            task_content += "| Priority | Type | Element |\n"
            task_content += "|----------|------|---------|\n"
            for elem in sorted_elements:
                emoji = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}.get(elem['priority'], '⚪')
                task_content += f"| {emoji} {elem['priority'].upper()} | {elem['type']} | {elem['name']} |\n"
            task_content += "\n"
        
        task_content += "## 🚀 Tasks to Complete\n\n"
        task_id = 1
        
        for elem in sorted_elements:
            task_content += f"### Task {task_id}: Fix {elem['type']} \"{elem['name']}\"\n\n"
            task_content += f"- **Type:** {elem['type']}\n"
            task_content += f"- **Priority:** {elem['priority'].upper()}\n"
            task_content += f"- **Action Required:** Add/fix the {elem['type']} \"{elem['name']}\"\n\n"
            task_id += 1
        
        task_content += f"""---

## Reference

The template is available at: `../../15_template/16_template_for_convention.md`
The YAML schema is available at: `../10_YAML/convention_validation_schema.yaml`

---

**End of Task File**
"""
        
        return task_content


def main():
    """Main entry point for the validator."""
    parser = argparse.ArgumentParser(
        description='Validate template documents and generate task files.'
    )
    parser.add_argument(
        'file_to_check',
        help='Path to the template file to validate'
    )
    parser.add_argument(
        '--schema',
        default='../10_YAML/convention_validation_schema.yaml',
        help='Path to the YAML schema file'
    )
    parser.add_argument(
        '--output',
        '-o',
        help='Output file path for the task file'
    )
    
    args = parser.parse_args()
    
    schema_path = Path(args.schema)
    if not schema_path.is_absolute():
        schema_path = Path.cwd() / schema_path
    
    file_path = Path(args.file_to_check)
    if not file_path.is_absolute():
        file_path = Path.cwd() / file_path
    
    validator = TemplateValidator(str(schema_path))
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    is_valid, errors = validator.validate(content)
    task_content = validator.generate_task_file(str(file_path), errors)
    
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = file_path.parent / f"task_{file_path.name}"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(task_content)
    
    print(f"\n{'='*60}")
    print(f"Template Validator Results")
    print(f"{'='*60}")
    print(f"File: {file_path.name}")
    print(f"Status: {'✅ VALID' if is_valid else '❌ INVALID'}")
    print(f"Issues Found: {len(errors)}")
    print(f"Task File: {output_path}")
    print(f"{'='*60}\n")
    
    return 0 if is_valid else 1


if __name__ == '__main__':
    sys.exit(main())
