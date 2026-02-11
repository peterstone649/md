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

### R7: Simplified Comparison Output Format
The comparison results MUST be output in a simplified format that includes:
- File-by-file comparison results
- For each file: show OK if title fits template, show missing template title if gap exists
- Process sequentially: compare title_master.md titles against extracted titles one by one
- Continue until no titles remain in either the master template or the extracted titles
- Clear indication of compliance status per file

### R8: File-by-File Processing
The system MUST process files individually with the following logic:
1. Start with first title from title_master.md
2. Check if matching title exists in extracted .title.txt file
3. If match found: mark as OK and proceed to next template title
4. If no match found: display the missing template title
5. Continue until all template titles are processed
6. Report any remaining titles in extracted file as extra

### R9: Template Path Configuration
The system MUST allow configuration of the template file path (default: ../12_rule/title_master.md).

### R10: Compare File Generation
The system MUST create a compare.md file in the same folder as the input title_master file that contains:
- Simple file-by-file comparison results
- For each file: sequential comparison showing OK or missing template titles
- No complex categorization or analysis
- Clear pass/fail status per file
- File path: [same directory as title_master.md]/compare.md

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

### Simplified Comparison Algorithm
1. Parse title_master.md to extract expected sections in order
2. Parse generated .title.txt files to extract actual sections
3. For each file, process template titles sequentially:
   - Compare first template title against extracted titles
   - If match found: mark as OK, remove from both lists, continue
   - If no match found: display missing template title, continue with next template title
4. Continue until no titles remain in either template or extracted list
5. Report any remaining titles as extra
6. Generate simple compare.md file with file-by-file results

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

- File-by-file comparison shows clear OK/missing status for each template title
- Sequential processing continues until no titles remain in either template or extracted file
- Simple compare.md output without complex categorization or analysis
- Clear pass/fail status per file
- Results are easily readable and actionable
- No complex additional titles analysis or categorization required

## Dependencies

- Python 3.8+
- Existing extract_titles.py functionality
- Test framework (unittest)
- File parsing utilities
- Enhanced compare_titles.py with additional titles analysis