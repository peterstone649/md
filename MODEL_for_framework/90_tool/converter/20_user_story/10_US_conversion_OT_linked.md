# User Story: Automatic Conversion of Linked Documents (US_MFW_CONVERSION_OT_LINKED) **[PRIO: MEDIUM]**

**As a** Framework Documenter,
**I want** the HTML conversion tool to automatically find and convert any linked Markdown documents that it references,
**so that** I can be confident all local links will work correctly in the final HTML output without having to convert each file manually.

---

## Acceptance Criteria

1.
    - **Given** I convert a single Markdown file (`A.md`),
    - **And** `A.md` contains a relative link to another Markdown file (`B.md`),
    - **When** the conversion process runs,
    - **Then** both `A.html` and `B.html` should be generated in the correct output directory.

2.
    - **Given** a linked document (`B.md`) has already been converted in the same process (e.g., it was also linked from another file),
    - **When** the converter encounters the link to `B.md` again,
    - **Then** it should not re-convert it, to avoid redundant processing.

3.
    - **Given** a file contains a link to a non-Markdown file (e.g., an image or a PDF),
    - **When** the conversion process runs,
    - **Then** the link should be preserved in the final HTML, but no conversion should be attempted on the linked file.

4.
    - **Given** a file contains a link to an external website (e.g., `https://...`),
    - **When** the conversion process runs,
    - **Then** the external link should be preserved without any processing.

5.
    - **Given** this feature is active,
    - **When** I use the existing `--recursive` flag on a directory,
    - **Then** both the recursive directory scan and the linked-document scan should work together, ensuring all documents are found and converted.

---

## Related Documents
- **Rule:** [Changelog Update Rule](../../12_rule/04_rule_for_version_changelog_update.md)
- **User Story:** [conversion_OT_recursive.md](./conversion_OT_recursive.md)

---

## Changelog

| Version | Date | Changes | Stakeholder | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | 2026-01-10 | Initial creation | AI Analyst | To capture the feature request for converting linked documents. |
