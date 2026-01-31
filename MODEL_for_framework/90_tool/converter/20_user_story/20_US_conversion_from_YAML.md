# User Story: Generate HTML from YAML Files (US_MFW_CONVERSION_FROM_YAML) **[PRIO: HIGH]**

**As a** Framework Maintainer,
**I want to** automatically generate styled HTML documents from all YAML files in the framework,
**so that** I can ensure consistent formatting and automate the publication of structured documentation from YAML sources.

---

## Acceptance Criteria

1.
    - **Given** I have one or more YAML files in a directory,
    - **When** I run the conversion script with the path to the directory or specific YAML file,
    - **Then** styled HTML documents should be created in the specified output directory for each YAML file.

2.
    - **Given** a YAML file is converted,
    - **When** the HTML is generated,
    - **Then** it should correctly display all structured fields including `title`, `id`, `priority`, `metadata`, `story`, `acceptance_criteria`, and `related_documents` in a readable format.

3.
    - **Given** the YAML file has `acceptance_criteria` with nested steps,
    - **When** the HTML is generated,
    - **Then** the criteria should be rendered as a styled, numbered list with nested bullets, preserving the hierarchical structure.

4.
    - **Given** the YAML file has `related_documents` with paths,
    - **When** the HTML is generated,
    - **Then** these should be rendered as a list of clickable HTML links with proper relative paths.

5.
    - **Given** I run the conversion script with recursive flag,
    - **When** I specify a directory containing YAML files,
    - **Then** it should process all YAML files recursively through subdirectories.

6.
    - **Given** I run the conversion script,
    - **When** I provide no arguments or invalid arguments,
    - **Then** it should display a comprehensive help message explaining usage, required parameters, and available options.

7.
    - **Given** the conversion process,
    - **When** generating HTML from YAML,
    - **Then** the output should include proper CSS styling, semantic HTML structure, and metadata preservation.

8.
    - **Given** multiple YAML files are processed,
    - **When** the conversion completes,
    - **Then** a summary report should be generated showing success/failure status for each file processed.

---

## Related Documents
- **Template:** [18_template_for_user_story.md](../../15_template/18_template_for_user_story.md)
- **Example YAML:** [10_US_conversion_OT_linked.yaml](./10_YAML/10_US_conversion_OT_linked.yaml)
- **Converter Tool:** [converter_OT_html.py](../converter_OT_html.py)
- **HTML Generator:** [../../../80_utility/html_generator/html_generator.py](../../../80_utility/html_generator/html_generator.py)

---

## Implementation Notes

- The solution should leverage the existing `converter_OT_html.py` tool and extend it to handle YAML file parsing
- YAML parsing should use PyYAML or similar library for robust YAML handling
- HTML templates should be designed to properly render YAML structured data
- Error handling should be comprehensive for malformed YAML files
- The tool should maintain consistency with existing HTML generation patterns in the framework

---

## Changelog

| Version | Date | Changes | Stakeholder | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V0.2.0 | 2026-01-10 | Enhanced to handle multiple YAML files, added recursive processing, improved acceptance criteria | AI Framework Steward | To enable comprehensive YAML to HTML conversion across the entire framework |
| V0.1.0 | 2026-01-10 | Initial creation | AI Framework Steward | To capture the feature request for generating HTML from YAML. |
