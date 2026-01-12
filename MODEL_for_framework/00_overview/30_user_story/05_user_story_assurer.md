# User Story: Assurer **[US_MFW_ASSURER]** **[PRIO: HIGH]**

**Version: V1.0.0** **Date: 2026-01-09**

**Story ID:** US_MFW_ASSURER
**Stakeholder:** Assurer

---

## User Story

**As an** Assurer responsible for quality and compliance,

**I want to** validate that all framework documents and tools meet standards, conventions, and quality criteria,

**So that** I can ensure framework integrity, consistency, and trustworthiness.

---

## Description

Assurers are quality guardians who verify compliance with all framework standards. They review documents for active voice, clickable links, template compliance, AI_LOCK protection, and overall quality. Assurers maintain the framework's integrity by catching issues before they propagate.

---

## Goals

1. **Validate** document compliance with framework standards
2. **Verify** active voice usage throughout documents
3. **Check** clickable links function correctly
4. **Ensure** template & convention compliance and proper structure
5. **Confirm** relevant rules are correctly applied
6. **Document** compliance status and issues found

---

## Acceptance Criteria

- [ ] Assurer can validate document compliance with framework standards
- [ ] Assurer can verify active voice usage throughout documents
- [ ] Assurer can check clickable links function correctly
- [ ] Assurer can ensure template & convention compliance and proper structure
- [ ] Assurer can confirm relevant rules are correctly applied
- [ ] Assurer can document compliance status and issues found

---

## Assurance Workflow

```
1. SELECTION
   └── Identify document for review
   └── Determine applicable standards
   └── Review type (new, modified, periodic)
   
2. INSPECTION
   └── Check active voice compliance
   └── Verify clickable links work
   └── Validate template structure
   └── Confirm AI_LOCK markers
   └── Review terminology consistency
   
3. EVALUATION
   └── Score compliance by dimension
   └── Identify specific issues
   └── Prioritize findings by severity
   └── Document evidence
   
4. REPORTING
   └── Create compliance report
   └── Provide specific feedback
   └── Suggest remediation steps
   └── Track issue resolution
   
5. FOLLOW-UP
   └── Verify remediation
   └── Re-score if needed
   └── Update compliance status
   └── Archive review record
```

---

## Quality Dimensions

| Dimension | Standard | Validation Method |
|-----------|----------|-------------------|
| **Active Voice** | RULE_ACTIVE_VOICE | Manual review + automated checks |
| **Clickable Links** | RULE_CLICKABLE_LINKS | Link traversal verification |
| **Template Compliance** | 15_template/ | Structure comparison |
| **AI_LOCK Protection** | Framework standard | Marker verification |
| **Terminology** | 30_terminology/ | Consistency check |
| **Naming** | 20_convention/ | Pattern matching |

---

## Compliance Checklist

### General Compliance
- [ ] Document follows approved template
- [ ] File naming follows conventions
- [ ] Version and date correctly formatted
- [ ] Changelog present and complete

### Writing Standards
- [ ] Active voice used throughout
- [ ] No passive voice without justification
- [ ] Clear, concise language
- [ ] Proper terminology usage

### Navigation
- [ ] All internal links clickable
- [ ] Links point to correct documents
- [ ] Relative paths correct
- [ ] No broken or dead links

### Content Protection
- [ ] AI_LOCK markers present where needed
- [ ] Protected content not modified
- [ ] AI_LOCK syntax correct

### Documentation
- [ ] Abstract present and clear
- [ ] Scope well-defined
- [ ] Examples provided where needed
- [ ] Cross-references complete

---

## Review Levels

### Level 1: Quick Review
- File naming check
- Template structure check
- AI_LOCK marker check
- **Time:** ~5 minutes

### Level 2: Standard Review
- All Level 1 checks
- Active voice spot-check
- Link verification
- **Time:** ~15 minutes

### Level 3: Full Review
- All Level 2 checks
- Complete active voice review
- Full terminology check
- Compliance scoring
- **Time:** ~30 minutes

---

## Reporting Format

### Compliance Report Template

```markdown
## Review Summary
- **Document:** [path/to/document.md]
- **Reviewer:** [Assurer name]
- **Date:** [YYYY-MM-DD]
- **Review Level:** [1/2/3]
- **Overall Score:** [X/100]

### Issues Found
| Severity | Issue | Location | Remediation |
|----------|-------|----------|-------------|
| HIGH | Active voice violation | Section 2 | Rewrite sentence |
| MEDIUM | Broken link | Section 4 | Fix path |

### Recommendations
1. Rewrite passive constructions in Section 2
2. Update link to point to correct file
```

---

## Success Metrics

- 100% of new documents receive Level 2+ review
- Compliance score average ≥ 85%
- Critical issues resolved within 48 hours
- Review turnaround time ≤ 24 hours for standard reviews

---

## Tools and Resources

| Tool | Purpose | Location |
|------|---------|----------|
| Review Checklist | Standard criteria | This document |
| Active Voice Rule | Writing standard | `12_rule/01_rule_for_active_voice.md` |
| Clickable Links Rule | Navigation standard | `12_rule/02_rule_for_clickable_links.md` |
| Templates | Structure reference | `15_template/` |

---

**Story Status:** Ready
**Estimation:** 5 story points
**Sprint:** TBD
