# Title Master Requirements

## Purpose
This document defines the requirements for comparing extracted title files against the title_master.md template to ensure consistency and completeness, including identification of additional titles found in extracted files.

## Requirements

### R1: Template Comparison
The system MUST be able to compare generated title files (.title.txt) against the title_master.md template to verify:
- All required sections are present
- Section order matches the template
- Section titles match exactly (case-sensitive)

### R2: Required Sections Validation
The comparison MUST verify that all required sections from title_master.md are present in extracted titles:
- Rule Statement
- Rule Requirements
- Formal Statement
- Rationale
- Uncertainty Declaration
- Integration with Other Framework Components
- Related Rules
- Related Axioms
- Related Principles
- Changelog

### R3: Section Order Validation
The comparison MUST ensure that sections appear in the correct order as defined in title_master.md.

### R4: Missing Sections Detection
The system MUST identify and report any missing sections from the extracted titles compared to the template.

### R5: Extra Sections Detection
The system MUST identify and report any sections present in extracted titles that are not in the template.

### R6: Additional Titles Analysis
The system MUST provide detailed analysis of additional titles found, including:
- Categorization of additional titles (metadata, implementation details, examples, etc.)
- Frequency analysis of common additional titles across files
- Impact assessment on template compliance

### R7: Comparison Output Format
The comparison results MUST be output in a structured format that includes:
- List of missing sections
- List of extra sections with categorization
- Overall compliance status (PASS/FAIL)
- Detailed comparison report
- Additional titles summary with categories

### R8: Integration with Test Suite
The comparison functionality MUST be integrated into the existing test suite (test_extract_titles.py) as a new test method.

### R9: Template Path Configuration
The system MUST allow configuration of the template file path (default: ../12_rule/title_master.md).

### R10: Requirements Generation
The system MUST generate a requirements file (title_master_requi.md) that documents:
- All additional titles found across all files
- Categories of additional content
- Recommendations for template updates or cleanup procedures

## Implementation Requirements

### File Structure
```
MODEL_for_framework/90_tool/titles/
├── title_master_requi.md          # This requirements document (UPDATED)
├── title_master.md               # Template file (in 12_rule directory)
├── extract_titles.py             # Main extraction tool
├── compare_titles.py             # Comparison tool (ENHANCED)
├── run_tests.py                  # Test runner
└── tests/
    └── test_extract_titles.py    # Test suite (add comparison tests here)
```

### Test Method Signature
```python
def test_title_template_compliance(self):
    """Test that extracted titles comply with title_master.md template"""
    # Implementation details
```

### Comparison Algorithm
1. Parse title_master.md to extract expected sections
2. Parse generated .title.txt files to extract actual sections
3. Compare section lists for completeness and order
4. Categorize additional titles found
5. Generate compliance report with additional titles analysis
6. Create requirements documentation

## Additional Titles Found Analysis

### Metadata Titles (Found in all files)
- "Generated on [date]" - Timestamp information
- "Extracted Titles from [filename]" - File identification headers
- "Source: [path]" - Source file paths

### Implementation Details (Found in specific files)
- "Components Breakdown"
- "Common Issues and Corrections"
- "Example Regex Pattern for Validation"
- "Validation Checklist"
- "Automation Support"
- "Implementation Guidelines"
- "Automated Processing"
- "Enforcement"

### Content Examples (Found in specific files)
- "TYPE Component Examples"
- "Complete Format Example"
- "Incorrect Abbreviation Format"
- "Missing Priority"
- "Invalid Priority Code"
- "Wrong Header Level"

### Framework References (Found in specific files)
- "Framework Abbreviations"
- "Document Type Mapping"
- "Core Framework Abbreviations"
- "Priority Levels"
- "Title Construction Process"
- "References"

### File-Specific Additional Content
- **04_rule_for_version_changelog_update.title.txt**: "Example", "Related Conventions"
- **12_rule_for_title_line_formatting.title.txt**: Extensive implementation details and validation content

## Success Criteria

- All required sections from template are detected in extracted titles
- Section order matches template exactly
- Missing and extra sections are clearly identified with categorization
- Additional titles are categorized and analyzed for impact
- Requirements file is automatically generated with comprehensive analysis
- Comparison runs as part of automated test suite
- Results are easily readable and actionable

## Dependencies

- Python 3.8+
- Existing extract_titles.py functionality
- Test framework (unittest)
- File parsing utilities
- Enhanced compare_titles.py with additional titles analysis