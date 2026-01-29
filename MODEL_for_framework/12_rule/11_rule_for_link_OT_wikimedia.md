# Wikimedia Links [RULE_FOR_MFW_WIKIMEDIA_LINKS] **[PRIO: MEDIUM]**


**Version: V1.0.1** **Status: APPROVED** **Date: 2026-01-23**
**Scope:** All framework documents containing Wikimedia references

## Rule Statement

**All references to Wikimedia Commons and Wikipedia resources MUST include proper attribution, licensing information, and direct links to source materials.**

## Rule Requirements

- **[R1]**: All Wikimedia links include direct URLs to specific pages
- **[R2]**: Attribution information is complete and accurate (creator name when available)
- **[R3]**: License information is specified and correct (CC BY, CC BY-SA, CC0, etc.)
- **[R4]**: Access dates are included and current (ISO format YYYY-MM-DD)
- **[R5]**: Links are functional and accessible
- **[R6]**: Alt text is provided for images
- **[R7]**: Attribution format follows established patterns

## Formal Statement
```
∀wikimedia_ref (WikimediaReference(wikimedia_ref) ∧ FrameworkDocument(wikimedia_ref))
    → (HasAttribution(wikimedia_ref) ∧ HasLicense(wikimedia_ref) ∧ HasAccessDate(wikimedia_ref))
```

## Rationale

Proper Wikimedia linking ensures compliance with Creative Commons licensing requirements and supports academic and research integrity.

## Uncertainty Declaration

*If applicable: This rule acknowledges inherent uncertainties in external resource availability and licensing changes over time.*

## Integration with Other Framework Components

### Related Rules
- **[10_rule_for_link_OT_clickable.md](10_rule_for_link_OT_clickable.md)** - General clickable link requirements
- **[03_rule_for_active_voice.md](03_rule_for_active_voice.md)** - Attribution text should use active voice

### Related Axioms
- **[02_axiom_of_framework_validation_integrity.md](../35_axiom/02_axiom_of_framework_validation_integrity.md)** - Validation includes external resource compliance
- **[03_axiom_of_clarity_and_precision.md](../35_axiom/03_axiom_of_clarity_and_precision.md)** - Clear attribution supports transparency

### Related Principles
- **[02_principle_transparency.md](../MODEL_for_stakeholder_AI_collab/30_principle/02_principle_transparency.md)** - Transparency requires proper attribution
- **[03_principle_proportionality.md](../MODEL_for_stakeholder_AI_collab/30_principle/03_principle_proportionality.md)** - Proportionality applies to attribution complexity

**Rule Steward:** Terminology Architects
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-13
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V1.0.1
**Date:** 2026-01-23

## Changelog

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.1 | 2026-01-23 | Updated title formatting and changed metadata headers per RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V0.1.0 | 2026-01-13 | Initial creation | AI Framework Admin | Establish file |
