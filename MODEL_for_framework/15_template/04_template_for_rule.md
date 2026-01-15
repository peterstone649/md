# Template for Rule [TEMPLATE_RULE] [PRIO: HIGH]

**Rule ID:** <RULE_TEMPLATE_ID_FROM_TITLE>
**Priority:** HIGH
**Applies to:** All framework rules

## Rule Statement

**Clear, concise statement of what this rule requires or prohibits.**

## Rule Requirements
/* can be more requirements if needed !*/
- **[R1]**: Description of requirement with ID for compliance tracking
- **[R2]**: Description of requirement with ID for compliance tracking
- **[R3]**: Description of requirement with ID for compliance tracking

**Formal Statement:**
```
e.g.
∀s∀a∀stakeholder (Statement(s) ∧ Actor(a) ∧ (Human(stakeholder) ∨ AI(a)))
    → MustAcknowledge(a, Uncertainty(s)) ∧ MustIdentify(a, Limitations(s))
    ∧ MustDeclare(a, BiasPotential(s)))
```

## Rationale

Brief explanation of why this rule exists and its benefits.

*Based on: [document.md](../path/to/document.md)*

## Uncertainty Declaration

*If applicable: This rule acknowledges inherent uncertainties in [specific domain/area]. Key limitations include: [list key uncertainties or limitations].*

## Integration with Other Framework Components

### Related Rules
- **[rule_name.md](path/to/rule.md)** - Description of relationship

### Related Axioms
- **[axiom_name.md](path/to/axiom.md)** - Foundation for this rule

### Related Principles
- **[principle_name.md](../path/to/principle.md)** - Description of relationship

## Changelog

| Version | Date | Changes | Stakeholder | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.1 | 2026-01-15 | Added extended footer section with Rule Owner, Enforcement Authority, Framework metadata | Framework Steward | Provide comprehensive rule documentation template |
| V0.1.0 | YYYY-MM-DD | Initial template creation | Framework Steward | Establish rule template standard |

**Rule Steward:** Framework Steward
**Approval Status:** Template
**Effective Date:** YYYY-MM-DD
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V[VERSION]
**Date:** YYYY-MM-DD
**Priority:** [PRIORITY]
**Compliance:** [Mandatory | Recommended]
