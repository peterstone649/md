# IDE Editor Respect [RULE_FOR_MFW_IDE_EDITOR_RESPECT] **[PRIO: HIGH]**

**Rule ID:** RULE_FOR_MFW_IDE_EDITOR_RESPECT
**Scope:** All AI extension-assisted file modifications (e.g. CLINE)

*Based on: [10_axiom_of_epistemological_uncertainty.md](../35_axiom/10_axiom_of_epistemological_uncertainty.md)*

## Rule Statement

**AI in an IDE must respect and preserve manual edits made directly in the editor. AI must not override user changes.**

## Rule Details

- **Manual Edit Preservation**: If user makes changes directly in editor, work with and preserve those changes
- **Selective Modification**: Only modify specific parts requested while keeping manual edits intact
- **Override Prevention**: Never replace entire files when user has made manual modifications
- **Collaboration Approach**: Treat manual edits as authoritative and build upon them
- **Copy File Protection**: Files ending in "copy.<extension>" are critical and MUST NOT receive updates from AI or its extensions

## Rationale

Ensures user control over their work while maintaining collaborative AI assistance capabilities.

**Rule Steward:** Framework Steward
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-15
**Review Cycle:** Annual

## Changelog

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.1 | 2026-01-23 | Updated title formatting and placeholders per RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V0.1.1 | 2026-01-15 | small edits on e.g. constant | Framework Steward | Strengthen consistency |
| V0.1.0 | 2026-01-09 | Initial creation | AI Framework Steward | Establish rule structure |
