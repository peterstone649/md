# Rule for AI_LOCK Content Protection **[RULE_FW_AI_LOCK_PROTECTION]**
**Version: V0.1.0** **Date: 2026-01-09**

**Rule ID:** RULE_AI_LOCK_PROTECTION
**Priority:** CRITICAL
**Applies to:** All AI-assisted document processing and generation

---

## Rule Statement

**AI systems MUST NOT modify, rephrase, rewrite, or alter any content enclosed within `[AI_LOCK]` and `[END_AI_LOCK]` markers. These markers designate protected content that represents the authoritative, human-authored intent and MUST remain unchanged.**

---

## Rationale

The AI_LOCK mechanism protects:
- **Human Authored Intent**: Content within AI_LOCK markers represents definitive human statements that must not be altered by AI
- **Semantic Integrity**: Prevents AI from introducing subtle changes that alter meaning
- **Accountability Chains**: Maintains clear provenance of protected statements
- **Framework Stability**: Ensures core principles and definitions remain consistent
- **Trust Boundaries**: Creates explicit zones where human authority supersedes AI capability

---

## AI_LOCK Pattern Structure

### Standard Format
```markdown
**[AI_LOCK]**
[PROTECTED_CONTENT]
**[END_AI_LOCK]**
```

### Examples

| Protected Content Type | Example |
|------------------------|---------|
| **Principles** | **[AI_LOCK]** Human sovereignty establishes that... **[END_AI_LOCK]** |
| **Axioms** | **[AI_LOCK]** The axiom of systematic framework development... **[END_AI_LOCK]** |
| **Definitions** | **[AI_LOCK]** Consciousness is defined as... **[END_AI_LOCK]** |
| **Policy Statements** | **[AI_LOCK]** The framework prohibits... **[END_AI_LOCK]** |

---

## Rules for AI Systems

### 1. Recognition Rule
AI systems MUST recognize and respect `[AI_LOCK]` and `[END_AI_LOCK]` markers in all contexts:
- Within any document type (Markdown, YAML, JSON, etc.)
- Across all framework directories
- Regardless of document length or complexity

### 2. Preservation Rule
When processing documents, AI systems MUST:
- **PRESERVE** all content within AI_LOCK markers exactly as written
- **NOT** rephrase, reword, or modify protected content
- **NOT** add, remove, or alter markers
- **NOT** summarize or reference protected content in ways that change its meaning

### 3. Generation Rule
When AI generates new content:
- AI_LOCK markers may only be used for NEW protected content
- Existing AI_LOCK sections must remain unchanged
- AI must clearly separate its own content from protected content

### 4. Interaction Rule
AI systems interacting with AI_LOCK content:
- **MAY** reference protected content in analysis
- **MUST NOT** modify the content itself
- **MUST** indicate when content falls within protected zones

---

## Acceptable Modifications (Human Only)

Only human stakeholders may modify AI_LOCK content through:
1. **Direct Edit**: Human-authored changes to protected sections
2. **Version Update**: Incremented version numbers when content changes
3. **Migration**: Explicit migration procedures for framework evolution

AI systems may suggest modifications but MUST:
- Clearly label suggestions as "PROPOSED_CHANGES"
- Never auto-apply changes to protected content
- Request explicit human approval before any modification

---

## Violation Examples

### ❌ Violation: Content Modification
```markdown
**[AI_LOCK]**
Human sovereignty establishes that humans retain final decision-making authority.
**[END_AI_LOCK]**

# AI modification (VIOLATION):
**[AI_LOCK]**
Humans retain the final say in all decisions within collaborative frameworks.
**[END_AI_LOCK]**
```

### ❌ Violation: Marker Removal
```markdown
# Before (VALID):
**[AI_LOCK]**
Core principle content...
**[END_AI_LOCK]**

# After (VIOLATION):
Core principle content...
```

### ❌ Violation: Content Reformatting
```markdown
# Before (VALID):
**[AI_LOCK]**
The Principle of Human Sovereignty establishes...
**[END_AI_LOCK]**

# After (VIOLATION):
**[AI_LOCK]**
We establish that the Principle of Human Sovereignty...
**[END_AI_LOCK]**
```

---

## Validation Checklist

- [ ] All AI_LOCK sections preserved exactly
- [ ] No rephrasing or rewording of protected content
- [ ] Markers remain intact (opening and closing)
- [ ] New AI_LOCK content clearly distinguished from existing
- [ ] AI-generated suggestions labeled separately
- [ ] No auto-application of changes to protected zones

---

## Enforcement

1. **Detection Phase:** AI tools flag AI_LOCK sections during processing
2. **Preservation Phase:** Automated checks verify marker integrity
3. **Review Phase:** Human reviewers verify protected content remains unchanged
4. **Violation Response:** Document violations and revert unauthorized changes

---

## Integration with Other Rules

| Rule | Relationship |
|------|--------------|
| RULE_ACTIVE_VOICE | AI_LOCK content exempt from active voice requirements |
| Framework Conventions | AI_LOCK sections override general formatting rules |
| Writing Standards | Protected content follows original author's style |

---

## References

- MODEL_for_stakeholder_AI_collab/30_principle/01_principle_human_sovereignty.md
- Framework Writing Conventions (20_convention/03_convention_for_writing_style.md)
- Intellectual Property Rights Conventions (20_convention/16_convention_for_intellectual_property_rights.md)

---

**Rule Steward:** Framework Standards Committee
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-09
**Review Cycle:** Annual
