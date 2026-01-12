# 19. Convention for Existential Risk Priority **[CONV_FOR_MODELFW_EXISTENTIAL_RISK]** **[PRIO: MAXIMUM]**

**Version: V0.1.0** **Date: 2026-01-09**

**Purpose:** Define priority classification for civilisation-threatening risks and existential hazards.

> **Note:** This convention is separate from standard framework priority conventions because existential risk aspects are not typical framework concerns. This document exists as an extension for AI safety and civilisation preservation contexts.

---

## Existential Risk Priority Matrix

For risk assessment involving civilisation-threatening scenarios:

| Priority | Meaning | Color Code | Response Required |
|----------|---------|------------|-------------------|
| **MAXIMUM** | Civilisation collapse risk | ⚫⚫⚫ Black/Red | IMMEDIATE - all hands, halt everything |
| **CATASTROPHIC** | Existential threat | 🔴 Red | Immediate halt, remediation |
| **SEVERE** | Major impact | 🟠 Orange | Urgent action within 48h |
| **MODERATE** | Significant impact | 🟡 Yellow | Address within 1 week |
| **MINOR** | Limited impact | 🟢 Green | Monitor and track |

---

## MAXIMUM Priority Definition

### Criteria for MAXIMUM Classification

An issue is classified as **MAXIMUM** when it meets ANY of the following:

1. **Civilisation Collapse Potential**
   - Risk of human extinction
   - Risk of irreversible global catastrophe
   - Risk of permanent reduction in human potential (>50% population)

2. **Uncontrolled AI Scenarios**
   - Loss of human control over AI systems
   - AI optimisation of harmful objectives
   - Recursive self-improvement without alignment

3. **Irreversibility**
   - Actions cannot be undone
   - No recovery path exists
   - Point of no return crossed or imminent

4. **Speed of Onset**
   - Less than 24 hours from detection to impact
   - Insufficient time for coordinated response
   - Exponential growth dynamics

---

## Response Protocols

### MAXIMUM Priority Response Protocol

| Phase | Action | Timeframe | Responsible |
|-------|--------|-----------|-------------|
| **Detection** | Identify and verify risk | Minutes | First observer |
| **Notification** | Alert all stakeholders | Minutes | Detection team |
| **Assessment** | Validate classification | <1 hour | Risk assessment team |
| **Response** | Implement containment | Immediate | All hands |
| **Communication** | External coordination | <1 hour | Leadership |

### Escalation to MAXIMUM

1. Any stakeholder can escalate to MAXIMUM
2. Verification required within 1 hour
3. All other work halts during MAXIMUM response
4. Documentation occurs after containment

---

## Review Cadence

| Priority Level | Review Frequency |
|----------------|------------------|
| MAXIMUM | CONTINUOUS - all hands, no delay |
| CATASTROPHIC | Weekly until resolved |
| SEVERE | Bi-weekly |
| MODERATE | Monthly |
| MINOR | Quarterly |

---

## Integration with Framework

### Relation to Standard Priority Convention

This convention **extends** [18_convention_for_priority_variants.md](18_convention_for_priority_variants.md) for existential risk contexts.

**Hierarchy:**
```
Existential Risk Priority (this document)
    ↓
Standard Priority (18_convention_for_priority_variants)
    ↓
Status Convention (14_convention_for_stati)
```

### When to Use This Convention

| Context | Use Convention |
|---------|----------------|
| AI safety documentation | Both (this + standard) |
| Existential risk assessment | This document only |
| General framework work | Standard only |
| AI alignment research | Both |

---

## Priority Format in Documents

### Standard Format
```
**[PRIO: MAXIMUM | CATASTROPHIC | SEVERE | MODERATE | MINOR]**
```

### Extended Format for AI Safety Documents
```
**[EXISTENTIAL_PRIO: MAXIMUM]** **[PRIO: CRITICAL]**
```

---

## Documentation Requirements

### For MAXIMUM Priority Items

- [ ] Threat magnitude documented
- [ ] Response protocol specified
- [ ] Stakeholder notification verified
- [ ] Post-incident review scheduled
- [ ] Lessons learned incorporated

---

## References

- [18_convention_for_priority_variants.md](18_convention_for_priority_variants.md) - Standard priority convention
- [14_convention_for_stati.md](14_convention_for_stati.md) - Status conventions
- [Ethosys/001_layer/35_strategy/10_risks/10_risks_to_be_aware.md](../Ethosys/001_layer/35_strategy/10_risks/10_risks_to_be_aware.md)
- [Ethosys/001_layer/35_strategy/01_ai_safety_awareness_strategy.md](../Ethosys/001_layer/35_strategy/01_ai_safety_awareness_strategy.md)

---

**Convention Reference:** Use this convention for AI safety, existential risk, and civilisation preservation contexts within the framework.

---

**End of Convention**

---

**Framework:** MODEL_for_framework (Extension)
**Version:** V0.1.0
**Date:** 2026-01-09
**Priority:** MAXIMUM
**Classification:** AI Safety / Existential Risk
