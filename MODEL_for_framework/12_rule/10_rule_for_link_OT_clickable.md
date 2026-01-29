# Clickable Links [RULE_FOR_MFW_LINK_OT_CLICKABLE] **[PRIO: HIGH]**


## Rule Statement

All cross-references to framework documents SHOULD use clickable markdown links. Plain text file paths are NOT acceptable for internal navigation.

## Rule Requirements

- **[R1]**: All internal document references use `[Text](path)` format
- **[R2]**: Link text describes the target document's purpose
- **[R3]**: Relative paths are correct and functional
- **[R4]**: No broken or dead links
- **[R5]**: Links work in markdown viewers and IDEs

## Formal Statement
```
∀document∀reference (Document(document) ∧ Reference(reference) ∧ InternalReference(reference))
    → (ClickableLink(reference) ∧ FunctionalPath(reference))
```

## Rationale

Clickable links enable direct navigation between related documents and reduce friction for readers exploring the framework.

## Uncertainty Declaration

*If applicable: This rule acknowledges inherent uncertainties in link functionality and the evolving nature of document locations.*

## Integration with Other Framework Components

### Related Rules
- **[07_rule_for_readme_clickable_links.md](07_rule_for_readme_clickable_links.md)** - README-specific clickable link requirements
- **[03_rule_for_active_voice.md](03_rule_for_active_voice.md)** - Link descriptions should use active voice

### Related Axioms
- **[02_axiom_of_framework_validation_integrity.md](../35_axiom/02_axiom_of_framework_validation_integrity.md)** - Validation includes link functionality
- **[03_axiom_of_clarity_and_precision.md](../35_axiom/03_axiom_of_clarity_and_precision.md)** - Clear navigation supports clarity requirements

### Related Principles
- **[02_principle_transparency.md](../MODEL_for_stakeholder_AI_collab/30_principle/02_principle_transparency.md)** - Transparency requires accessible navigation
- **[03_principle_proportionality.md](../MODEL_for_stakeholder_AI_collab/30_principle/03_principle_proportionality.md)** - Proportionality applies to navigation complexity

**Rule Steward:** Framework Standards Committee
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-09
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V1.0.0
**Date:** 2026-01-09

## Changelog

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.1 | 2026-01-23 | Updated title formatting and placeholders per RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V1.0.0 | 2026-01-09 | Initial creation | AI Framework Admin | Establish rule |
