# User Story: Bulk Conversion of Documentation (US_MSHCOL_CONVERSION_OT_RECURSIVE) **[PRIO: HIGH]**

**Version: V1.0** **Status: DRAFT** **Date: 2026-01-10**

**As a** Framework Documenter,
**I want to** run a single command to convert an entire directory of Markdown files into styled HTML documents,
**so that** I can efficiently publish the complete set of framework documentation without having to convert each file one by one.

---

## Acceptance Criteria

1.  **Given** I have a directory containing multiple Markdown files and subdirectories with more Markdown files,
    **When** I run the `html_converter.py` script with a `--recursive` flag, pointing to that directory,
    **Then** the script should find and convert every `.md` file within that directory tree.

2.  **Given** the script is run recursively,
    **When** the HTML files are generated,
    **Then** they should be placed in the specified output directory, maintaining the same subdirectory structure as the source.

3.  **Given** I run the script on a directory without the `--recursive` flag,
    **When** the script executes,
    **Then** it should show an error message and exit, preventing accidental misuse.

4.  **Given** I run the script on a single file,
    **When** the script executes,
    **Then** it should convert only that single file as it did before.

5.  **Given** any conversion is performed,
    **When** the HTML is generated,
    **Then** it should use the standard, colorful styling defined in the tool.

---

## Related Documents
- **Tool:** [converter_OT_html.py](../converter_OT_html.py)
- **Rule:** [RULE_FW_DOC_VERSION_CHANGELOG](../../12_rule/03_rule_for_version_changelog_update.md)

## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | 2026-01-24 | Initial creation | Framework Maintenance Team | Establish foundational structure |
