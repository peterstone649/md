# 04. Rule of Epistemological Uncertainty Acknowledgment **[RULE_MFW_EPISTEMOLOGICAL_ACKNOWLEDGMENT]** **[PRIO: CRITICAL]**

*Based on: [10_axiom_of_epistemological_uncertainty.md](../35_axiom/10_axiom_of_epistemological_uncertainty.md)*

---

## Rule Statement

All stakeholders and AI systems MUST acknowledge the inherent uncertainty in all statements, claims, and outputs. No statement shall be treated as absolute, complete, or bias-free.

**Formal Statement:**
```
∀s∀a∀stakeholder (Statement(s) ∧ Actor(a) ∧ (Human(stakeholder) ∨ AI(a))) 
    → MustAcknowledge(a, Uncertainty(s)) ∧ MustIdentify(a, Limitations(s)) 
    ∧ MustDeclare(a, BiasPotential(s)))
```

---

## Core Requirements

### 1. Uncertainty Declaration

**For Human Stakeholders:**
- [ ] State confidence level (0-100%) for all claims
- [ ] Identify what is unknown or uncertain
- [ ] Acknowledge potential blind spots or knowledge gaps
- [ ] Specify context and limitations of the statement
- [ ] Indicate time-sensitivity or temporal validity

**For AI Systems:**
- [ ] Provide confidence scores for all outputs
- [ ] Explicitly state known limitations
- [ ] Identify potential biases in training data affecting outputs
- [ ] Communicate uncertainty ranges for predictions
- [ ] Flag areas requiring human verification

---

## Uncertainty Communication Format

### Standard Declaration Template

```
[STATEMENT]: <claim or observation>
[CONFIDENCE]: <0-100%>
[KNOWN_LIMITATIONS]: <what we don't know>
[POTENTIAL_BIASES]: <possible sources of distortion>
[CONTEXT_BOUNDARY]: <where this applies/doesn't apply>
[REQUIRES_VERIFICATION]: <yes/no>
```

### Example Usage

**Human Stakeholder:**
```
[STATEMENT]: The project will complete by Q2 2026
[CONFIDENCE]: 65%
[KNOWN_LIMITATIONS]: Resource availability uncertain, dependency on stakeholder approval
[POTENTIAL_BIASES]: Optimism bias in timeline estimation, limited visibility into stakeholder decisions
[CONTEXT_BOUNDARY]: Assumes current team size and no major obstacles
[REQUIRES_VERIFICATION]: Yes - monthly review needed
```

**AI System:**
```
[STATEMENT]: Recommended approach is X
[CONFIDENCE]: 78%
[KNOWN_LIMITATIONS]: Limited access to organizational culture context, unknown stakeholder preferences
[POTENTIAL_BIASES]: Training data may over-represent certain industries
[CONTEXT_BOUNDARY]: Based on general best practices, may not fit specific context
[REQUIRES_VERIFICATION]: Yes - human stakeholder approval required
```

---

## Verification Protocol

### Before Finalizing Any Output

| Step | Action | Responsible |
|------|--------|-------------|
| 1 | Uncertainty declaration completed | Actor (human/AI) |
| 2 | Confidence level assigned | Actor (human/AI) |
| 3 | Alternative perspectives considered | Human stakeholder |
| 4 | Bias check performed | Human stakeholder |
| 5 | Limitations documented | Actor (human/AI) |

### Confidence Threshold Matrix

| Confidence Level | Action Required |
|-----------------|-----------------|
| **90-100%** | Standard review |
| **70-89%** | Enhanced review by additional stakeholder |
| **50-69%** | Multiple stakeholder review + documentation of uncertainty |
| **Below 50%** | Treat as hypothesis, not conclusion; explicit labeling required |

---

## Compliance Checklist

- [ ] **U1**: All statements include a confidence assessment
- [ ] **U2**: Known limitations are explicitly documented
- [ ] **U3**: Potential biases are identified and declared
- [ ] **U4**: Context boundaries are clearly specified
- [ ] **U5**: Verification requirements are stated
- [ ] **U6**: High-stakes decisions require multiple confidence assessments
- [ ] **U7**: Low confidence statements are labeled as hypotheses
- [ ] **U8**: Regular reassessment of confidence levels as new information emerges

---

## Consequences of Non-Compliance

| Severity | Violation | Consequence |
|----------|-----------|-------------|
| **CRITICAL** | Omission of confidence in high-stakes decisions | Decision void until compliance |
| **HIGH** | Missing uncertainty declaration in formal outputs | Output marked as non-compliant |
| **MEDIUM** | Incomplete bias identification | Review required before proceeding |
| **LOW** | Vague confidence statements | Feedback and correction |

---

## Integration with Other Framework Components

### Related Rules
- **[RULE_VERSION_CHANGELOG_UPDATE.md](03_rule_for_version_changelog_update.md)** - Changelogs must document uncertainty
- **[RULE_AI_LOCK_PROTECTION.md](02_rule_for_ai_lock_protection.md)** - Protected content must acknowledge uncertainty

### Related Axioms
- **[10]_axiom_[epistemological_uncertainty].md** - Foundation for this rule
- **[02]_axiom_[framework_validation_integrity].md** - Validation must consider uncertainty

### Related Principles (MODEL_for_stakeholder_AI_collab)
- [02_principle_transparency.md](../MODEL_for_stakeholder_AI_collab/30_principle/02_principle_transparency.md) - Transparency requires uncertainty acknowledgment
- [03_principle_proportionality.md](../MODEL_for_stakeholder_AI_collab/30_principle/03_principle_proportionality.md) - Proportionality depends on uncertainty recognition

---

## Scientific Foundation

Based on:
- **Gödel's Incompleteness Theorems** - No system can prove all truths about itself
- **Heisenberg's Uncertainty Principle** - Complementary uncertainties in measurement
- **Cognitive Bias Research** - Systematic errors in human judgment
- **Bayesian Epistemology** - Probabilistic approach to knowledge

---

## References

- [10 Axiom of Epistemological Uncertainty](../35_axiom/10 axiom_of_epistemological_uncertainty.md)
- [01 Rule for Active Voice](01_rule_for_active_voice.md)
- [02 Rule for AI Lock Protection](02_rule_for_ai_lock_protection.md)
- [03 Rule for Version Changelog Update](03_rule_for_version_changelog_update.md)

---

**Rule Owner:** Framework Development Team
**Enforcement Authority:** All stakeholders in MODEL_for_framework and MODEL_for_stakeholder_AI_collab
**Review Cycle:** Quarterly or when significant uncertainty research emerges

---

**End of Rule**

---

**Framework:** MODEL_for_framework
**Framework Version:** V0.1.0
**Date:** 2026-01-09
**Priority:** CRITICAL
**Compliance:** Mandatory for all stakeholders and AI systems
