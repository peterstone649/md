# AI_LOCK Content Protection [RULE_FOR_MFW_AI_LOCK_PROTECTION] **[PRIO: HIGHEST]**


## Rule Statement

AI systems MUST NOT modify, rephrase, rewrite, or alter any content enclosed within `[AI_LOCK]` and `[AI_UNLOCK]` markers. These markers designate protected content that represents the authoritative, human-authored intent and MUST remain unchanged.

## Rule Requirements

- **[R1]**: AI systems MUST recognize and respect `[AI_LOCK]` and `[AI_UNLOCK]` markers in all contexts
- **[R2]**: AI systems MUST preserve all content within AI_LOCK markers exactly as written
- **[R3]**: AI systems MUST NOT rephrase, reword, or modify protected content
- **[R4]**: AI systems MUST NOT add, remove, or alter markers
- **[R5]**: AI systems MUST NOT summarize or reference protected content in ways that change its meaning

## Formal Statement
```
∀document∀ai_system (Document(document) ∧ AISystem(ai_system) ∧ ContainsAilock(document))
    → (PreserveContent(ai_system, document) ∧ RespectMarkers(ai_system, document))
```

## Rationale

The AI_LOCK mechanism protects human-authored intent and ensures semantic integrity in collaborative AI environments.

## Uncertainty Declaration

*If applicable: This rule acknowledges inherent uncertainties in AI content generation and the need for human oversight in critical content areas.*

## Integration with Other Framework Components

### Related Rules
- **[03_rule_for_version_changelog_update.md](03_rule_for_version_changelog_update.md)** - Version updates must preserve AI_LOCK content
- **[01_rule_for_epistemological_uncertainty_acknowledgment.md](01_rule_for_epistemological_uncertainty_acknowledgment.md)** - AI_LOCK content represents human certainty

### Related Axioms
- **[01_axiom_of_human_sovereignty.md](../35_axiom/01_axiom_of_human_sovereignty.md)** - Foundation for human authority over AI
- **[02_axiom_of_framework_validation_integrity.md](../35_axiom/02_axiom_of_framework_validation_integrity.md)** - Validation must respect protected content

### Related Principles
- **[01_principle_human_sovereignty.md](../MODEL_for_stakeholder_AI_collab/30_principle/01_principle_human_sovereignty.md)** - Human sovereignty over AI decisions
- **[02_principle_transparency.md](../MODEL_for_stakeholder_AI_collab/30_principle/02_principle_transparency.md)** - Transparency in AI-human collaboration

**Rule Steward:** Terminology Architects
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-25
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V1.1.0
**Date:** 2026-01-25

## Changelog

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.1.0 | 2026-01-25 | Changed closing tag to [AI_UNLOCK]; Updated standard example | Framework Admin | User request for new standard |
| V1.0.1 | 2026-01-23 | Updated title formatting and changed metadata headers per RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V0.1.0 | 2026-01-09 | Initial creation | AI Framework Admin | Establish file |
