# Uncertainty Communication [CONV_FOR_MFW_UNCERTAINTY_COMMUNICATION] **[PRIO: HIGH]**

**Version: V0.1.1** **Status: APPROVED** **Date: 2026-01-23**
**Scope:** All framework statements, decisions, and outputs

## Convention Statement

**At least all critical or high impact statements, claims, and outputs within the MODEL_for_framework ecosystem MUST include explicit uncertainty declarations using the standardized communication format.**

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

## Uncertainty Declaration Requirements

### For Human Stakeholders
- [ ] State confidence level (0-100%) for all claims
- [ ] Identify what is unknown or uncertain
- [ ] Acknowledge potential blind spots or knowledge gaps
- [ ] Specify context and limitations of the statement
- [ ] Indicate time-sensitivity or temporal validity

### For AI Systems
- [ ] Provide confidence scores for all outputs
- [ ] Explicitly state known limitations
- [ ] Identify potential biases in training data affecting outputs
- [ ] Communicate uncertainty ranges for predictions
- [ ] Flag areas requiring human verification

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

## Compliance Checklist

- [ ] **U1**: All statements include a confidence assessment
- [ ] **U2**: Known limitations are explicitly documented
- [ ] **U3**: Potential biases are identified and declared
- [ ] **U4**: Context boundaries are clearly specified
- [ ] **U5**: Verification requirements are stated
- [ ] **U6**: High-stakes decisions require multiple confidence assessments
- [ ] **U7**: Low confidence statements are labeled as hypotheses
- [ ] **U8**: Regular reassessment of confidence levels as new information emerges

## Consequences of Non-Compliance

| Severity | Violation | Consequence |
|----------|-----------|-------------|
| **CRITICAL** | Omission of confidence in high-stakes decisions | Decision void until compliance |
| **HIGH** | Missing uncertainty declaration in formal outputs | Output marked as non-compliant |
| **MEDIUM** | Incomplete bias identification | Review required before proceeding |
| **LOW** | Vague confidence statements | Feedback and correction |

## Integration with Framework Components

### Related Rules
- **[01_rule_for_epistemological_uncertainty_acknowledgment.md](../12_rule/01_rule_for_epistemological_uncertainty_acknowledgment.md)** - Foundation for this convention
- **[04_rule_for_version_changelog_update.md](../12_rule/04_rule_for_version_changelog_update.md)** - Changelogs must document uncertainty

### Related Axioms
- **[10_axiom_of_epistemological_uncertainty.md](../35_axiom/10_axiom_of_epistemological_uncertainty.md)** - Foundation for uncertainty acknowledgment

### Related Principles (MODEL_for_stakeholder_AI_collab)
- **[02_principle_transparency.md](../../MODEL_for_stakeholder_AI_collab/30_principle/02_principle_transparency.md)** - Transparency requires uncertainty acknowledgment
- **[03_principle_proportionality.md](../../MODEL_for_stakeholder_AI_collab/30_principle/03_principle_proportionality.md)** - Proportionality depends on uncertainty recognition

**Rule Steward:** Framework Steward
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-15
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V0.1.1
**Date:** 2026-01-23

## Changelog

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.1 | 2026-01-23 | Updated title formatting and changed "Applies to" to "Scope" per RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V0.1.0 | 2026-01-15 | Initial convention extracted from uncertainty rule | Framework Steward | Standardize uncertainty communication across framework |
