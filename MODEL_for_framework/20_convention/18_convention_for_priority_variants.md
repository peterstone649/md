# 18. Convention for Priority Variants **[CONV_FOR_MODELFW_PRIORITY_VARIANTS]** **[PRIO: HIGH]**

**Version: V0.1.0** **Date: 2026-01-09**

**Purpose:** Define priority classification systems for different document types in the framework.

---

## Standard Priority Levels (General)

For most framework documents:

| Priority | Meaning | Color Code | Response Time |
|----------|---------|------------|---------------|
| **CRITICAL** | Immediate action required | 🔴 Red | Within 24 hours |
| **HIGH** | Important, address soon | 🟠 Orange | Within 1 week |
| **MEDIUM** | Standard priority | 🟡 Yellow | Within 1 month |
| **LOW** | Nice to have, when time permits | 🟢 Green | When resources available |

---

## Rule-Specific Priority Levels **[RULE_PRIO]**

Rules use a modified priority system reflecting enforcement severity:

| Priority | Meaning | Enforcement | Examples |
|----------|---------|-------------|----------|
| **MANDATORY** | Must comply, no exceptions | Blocking | Security rules, ethical protections |
| **REQUIRED** | Compliance expected | Non-blocking with escalation | Quality standards, documentation |
| **RECOMMENDED** | Best practice, encouraged | Advisory | Style guidelines, efficiency tips |
| **OPTIONAL** | Available for use | No enforcement | Experimental features, templates |

### Rule Priority Format
```
**[RULE_PRIO: MANDATORY | REQUIRED | RECOMMENDED | OPTIONAL]**
```

### Examples

**Mandatory Rule:**
```
# 01. Rule for AI Lock Protection **[RULE_AI_LOCK]** **[RULE_PRIO: MANDATORY]**
```

**Recommended Rule:**
```
# XX. Rule for Documentation Style **[RULE_DOC_STYLE]** **[RULE_PRIO: RECOMMENDED]**
```

---

## Axiom Priority Levels **[AXIOM_PRIO]**

Axioms use an importance-based priority system:

| Priority | Meaning | Impact Scope |
|----------|---------|--------------|
| **FOUNDATIONAL** | Core to framework existence | All documents |
| **ESSENTIAL** | Critical to framework function | All active documents |
| **IMPORTANT** | Significant to framework quality | Relevant documents |
| **SUPPORTING** | Enhances framework capability | Optional documents |

### Axiom Priority Format
```
**[AXIOM_PRIO: FOUNDATIONAL | ESSENTIAL | IMPORTANT | SUPPORTING]**
```

---

## Principle Priority Levels **[PRIO]**

For stakeholder-AI collaboration principles:

| Priority | Meaning | Stakeholder Impact |
|----------|---------|-------------------|
| **CRITICAL** | Non-negotiable, essential | Immediate adoption required |
| **HIGH** | Very important | Strong recommendation |
| **MEDIUM** | Standard importance | Suggested adoption |
| **LOW** | Optional enhancement | When applicable |

### Principle Priority Format
```
**[PRIO: CRITICAL | HIGH | MEDIUM | LOW]**
```

---

## Task Priority Levels

For task and work item tracking:

| Priority | Meaning |排序 | Example |
|----------|---------|-----|---------|
| **P0** | Critical path, blocker | 1 | Framework blocker |
| **P1** | High priority | 2 | Important feature |
| **P2** | Medium priority | 3 | Standard work |
| **P3** | Low priority | 4 | Backlog item |

### Task Priority Format
```
**Priority:** P0 | P1 | P2 | P3
```

---

## Risk Priority Matrix

For risk assessment and hazard identification:

| Priority | Meaning | Response Required |
|----------|---------|-------------------|
| **CATASTROPHIC** | Existential threat | Immediate halt, remediation |
| **SEVERE** | Major impact | Urgent action within 48h |
| **MODERATE** | Significant impact | Address within 1 week |
| **MINOR** | Limited impact | Monitor and track |

> **Note:** For civilisation collapse risks (MAXIMUM), use [19_convention_for_existential_risk_priority.md](19_convention_for_existential_risk_priority.md) instead.

---

## Priority Usage Guidelines

### Document Type to Priority Mapping

| Document Type | Priority Type | Format |
|---------------|---------------|--------|
| Rule | RULE_PRIO | **[RULE_PRIO: X]** |
| Axiom | AXIOM_PRIO | **[AXIOM_PRIO: X]** |
| Principle | PRIO | **[PRIO: X]** |
| Task | Task Priority | **Priority: PX** |
| Convention | Standard | **[PRIO: X]** |
| Template | Standard | **[PRIO: X]** |

### Priority Placement in Documents

Place priority marker in the document header:
```
# Document Title **[PRIO_TYPE: VALUE]**

**Version:** V0.1.0 **Date:** YYYY-MM-DD **[PRIO_TYPE: VALUE]**
```

---

## Priority Transition Rules

### Escalation (Increasing Priority)
- New information reveals higher impact
- Deadlines approach with incomplete work
- Stakeholder feedback indicates importance

### De-escalation (Decreasing Priority)
- Issue resolved or mitigated
- Circumstances change reducing impact
- Alternative solution implemented

### Transition Documentation
When priority changes, document in changelog:
```
| Version | Date | Stakeholder | Priority Change | Rationale |
|---------|------|-------------|-----------------|-----------|
| V0.2.0 | 2026-01-10 | Author | MEDIUM → HIGH | Stakeholder feedback |
```

---

## Priority Review Cadence

| Priority Level | Review Frequency |
|----------------|------------------|
| CRITICAL/FOUNDATIONAL/CATASTROPHIC | Weekly until resolved |
| HIGH/P0/SEVERE | Bi-weekly |
| MEDIUM/P1 | Monthly |
| LOW/P2/P3 | Quarterly |

> **Note:** For MAXIMUM priority (civilisation risks), see [19_convention_for_existential_risk_priority.md](19_convention_for_existential_risk_priority.md).

---

## Priority Override Protocol

### When Standard Rules Don't Apply

1. **Emergency Declaration**: CRITICAL → CATASTROPHIC for immediate threats
2. **Strategic Priority**: Stakeholder alignment for framework-wide changes
3. **Deprecation Path**: Phased reduction from HIGH → LOW

### Override Documentation
```
**Priority Override:** [Standard Priority] → [Override Priority]
**Rationale:** [Explanation]
**Approved By:** [Authority]
**Valid Until:** [Date or Condition]
```

---

## References

- [14_convention_for_stati.md](14_convention_for_stati.md) - Status conventions
- [17_convention_for_prefix_standards.md](17_convention_for_prefix_standards.md) - Prefix standards
- [11_convention_for_confidence_scoring.md](11_convention_for_confidence_scoring.md) - Related scoring

---

**Convention Reference:** Apply to all documents in MODEL_for_framework and derived frameworks.

---

**End of Convention**

---

**Framework:** MODEL_for_framework
**Version:** V0.1.0
**Date:** 2026-01-09
**Priority:** HIGH
