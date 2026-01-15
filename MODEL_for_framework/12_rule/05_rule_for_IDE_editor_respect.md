# Rule for IDE Editor Respect [RULE_MFW_IDE_EDITOR_RESPECT] [PRIO: HIGH]

*Based on: [10_axiom_of_epistemological_uncertainty.md](../35_axiom/10_axiom_of_epistemological_uncertainty.md)*

**Rule ID:** RULE_MFW_IDE_EDITOR_RESPECT
**Priority:** HIGH
**Applies to:** All AI extension-assisted file modifications (e.g. CLINE)

## Rule Statement

**AI in an IDE must respect and preserve manual edits made directly in the editor. As AI do not override user changes.**

---

## Rule Details

- **Manual Edit Preservation**: If user makes changes directly in editor, work with and preserve those changes
- **Selective Modification**: Only modify specific parts requested while keeping manual edits intact
- **Override Prevention**: Never replace entire files when user has made manual modifications
- **Collaboration Approach**: Treat manual edits as authoritative and build upon them
- **Copy File Protection**: Files ending in "copy.<extension>" are critical and MUST NOT receive updates from AI or its extensions

---

## Rationale

Ensures user control over their work while maintaining collaborative AI assistance capabilities.

## Changelog

| Version | Date | Changes | Stakeholder | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.1 | 2026-01-15 | small edits on e.g. constant | Framework Steward | Strengthen consistency |
| V0.1.0 | 2026-01-09 | Initial creation | AI Framework Steward | Establish rule structure |

---

**Rule Steward:** Framework Steward
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-15
**Review Cycle:** Annual
