# IDE Editor Respect [RULE_FOR_MFW_IDE_EDITOR_RESPECT] **[PRIO: HIGH]**


*Based on: [10_axiom_of_epistemological_uncertainty.md](../35_axiom/10_axiom_of_epistemological_uncertainty.md)*

## Rule Statement

**AI in an IDE must respect and preserve manual edits made directly in the editor. AI must not override user changes.**

## Rule Requirements

- **[R1]**: If user makes changes directly in editor, work with and preserve those changes
- **[R2]**: Only modify specific parts requested while keeping manual edits intact
- **[R3]**: Never replace entire files when user has made manual modifications
- **[R4]**: Treat manual edits as authoritative and build upon them
- **[R5]**: Files ending in "copy.<extension>" are critical and MUST NOT receive updates from AI or its extensions

## Formal Statement
```
∀ai_system∀user_edit (AISystem(ai_system) ∧ UserEdit(user_edit))
    → (PreserveEdit(ai_system, user_edit) ∧ SelectiveModification(ai_system, user_edit))
```

## Rationale

Ensures user control over their work while maintaining collaborative AI assistance capabilities.

## Uncertainty Declaration

*If applicable: This rule acknowledges inherent uncertainties in AI understanding of user intent and the need for human oversight in code modifications.*

## Integration with Other Framework Components

### Related Rules
- **[01_rule_for_epistemological_uncertainty_acknowledgment.md](01_rule_for_epistemological_uncertainty_acknowledgment.md)** - AI uncertainty acknowledgment applies to IDE interactions
- **[03_rule_for_active_voice.md](03_rule_for_active_voice.md)** - IDE documentation should use active voice

### Related Axioms
- **[10_axiom_of_epistemological_uncertainty.md](../35_axiom/10_axiom_of_epistemological_uncertainty.md)** - Foundation for user control over AI actions
- **[01_axiom_of_human_sovereignty.md](../35_axiom/01_axiom_of_human_sovereignty.md)** - Human sovereignty over AI in development environments

### Related Principles
- **[01_principle_human_sovereignty.md](../MODEL_for_stakeholder_AI_collab/30_principle/01_principle_human_sovereignty.md)** - Human sovereignty in AI collaboration
- **[02_principle_transparency.md](../MODEL_for_stakeholder_AI_collab/30_principle/02_principle_transparency.md)** - Transparency in AI code modifications

**Rule Steward:** Terminology Architects
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-15
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V1.0.1
**Date:** 2026-01-23

## Changelog

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.1 | 2026-01-23 | Updated title formatting and changed metadata headers per RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V0.1.1 | 2026-01-15 | small edits on e.g. constant | Framework Steward | Strengthen consistency |
| V0.1.0 | 2026-01-09 | Initial creation | AI Framework Steward | Establish rule structure |
