# Active Voice [RULE_FOR_MFW_ACTIVE_VOICE] **[PRIO: HIGH]**


## Rule Statement

All framework documents SHOULD use active voice constructions. Avoid passive voice unless specifically required for emphasis or when the actor is genuinely unknown.

## Rule Requirements

- **[R1]**: Subject performs action in 90%+ of sentences
- **[R2]**: No "was/were + past participle" patterns without reason
- **[R3]**: Actor clearly identified and positioned first
- **[R4]**: "By" phrases used only when actor adds value

## Formal Statement
```
∀sentence (Sentence(sentence) ∧ FrameworkDocument(sentence))
    → (ActiveVoice(sentence) ∨ JustifiedPassive(sentence))
```

## Rationale

Active voice clarifies responsibility, improves readability, and aligns with framework principles of clarity and precision.

## Uncertainty Declaration

*If applicable: This rule acknowledges inherent uncertainties in language interpretation and the subjective nature of voice assessment.*

## Integration with Other Framework Components

### Related Rules
- **[01_rule_for_epistemological_uncertainty_acknowledgment.md](01_rule_for_epistemological_uncertainty_acknowledgment.md)** - Active voice supports uncertainty acknowledgment
- **[02_rule_for_ai_lock_protection.md](02_rule_for_ai_lock_protection.md)** - AI_LOCK content may use passive voice when appropriate

### Related Axioms
- **[02_axiom_of_framework_validation_integrity.md](../35_axiom/02_axiom_of_framework_validation_integrity.md)** - Validation includes language quality assessment
- **[03_axiom_of_clarity_and_precision.md](../35_axiom/03_axiom_of_clarity_and_precision.md)** - Foundation for active voice requirement

### Related Principles
- **[02_principle_transparency.md](../MODEL_for_stakeholder_AI_collab/30_principle/02_principle_transparency.md)** - Transparency requires clear language
- **[03_principle_proportionality.md](../MODEL_for_stakeholder_AI_collab/30_principle/03_principle_proportionality.md)** - Proportionality applies to language complexity

**Rule Steward:** Terminology Architects
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-08
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V1.0.1
**Date:** 2026-01-23

## Changelog

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.1 | 2026-01-23 | Updated title formatting and changed metadata headers per RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V0.1.0 | 2026-01-09 | Initial creation | AI Framework Admin | Establish file |
