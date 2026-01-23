# Active Voice [RULE_FOR_MFW_ACTIVE_VOICE] **[PRIO: HIGH]**

**Rule ID:** RULE_FOR_MFW_ACTIVE_VOICE
**Scope:** All framework documentation

## Rule Statement

All framework documents SHOULD use active voice constructions. Avoid passive voice unless specifically required for emphasis or when the actor is genuinely unknown.

## Rationale

Active voice:
- Clarifies who performs actions
- Creates more engaging and direct communication
- Reduces ambiguity in responsibility
- Aligns with framework principles of clarity and precision
- Makes sentences more concise

## Active Voice Pattern

### Structure
```
[ACTOR] + [ACTION] + [OBJECT]
```

### Examples

| Passive ❌ | Active ✅ |
|-----------|----------|
| The validation was performed by the framework | The framework validates |
| Decisions must be made by contributors | Contributors make decisions |
| Changes are required by the system | The system requires changes |
| Analysis is conducted by researchers | Researchers conduct analysis |

## Character-Action-Subject (CAS) Strategy

1. **Identify the Action** - What is actually happening?
2. **Name the Actor** - Who/what performs the action?
3. **Position Actor First** - Put subject at beginning of sentence

### Application
- **Step 1:** Find passive constructions (was/were + past participle)
- **Step 2:** Identify the actor and action
- **Step 3:** Restructure: Actor → Action → Object

## Acceptable Passive Voice Exceptions

Passive voice IS acceptable when:

1. **Unknown Actor**
   - "The file was corrupted during transmission" (actor unknown)

2. **Emphasis on Action/Object**
   - "The decision has been made" (focus on decision, not decision-maker)

3. **Scientific/Technical Neutrality**
   - "The sample was heated to 100°C" (standard scientific reporting)

4. **Deliberate De-emphasis**
   - "Mistakes were made" (when blaming is inappropriate)

## Validation Checklist

- [ ] Subject performs action in 90%+ of sentences
- [ ] No "was/were + past participle" patterns without reason
- [ ] Actor clearly identified and positioned first
- [ ] "By" phrases used only when actor adds value

## Enforcement

1. **Writing Phase:** Writers apply CAS strategy during drafting
2. **Review Phase:** Reviewers check for passive voice violations
3. **Automated Checks:** Tools flag passive constructions for review

## References

- Strunk & White, "The Elements of Style"
- Williams, "Style: Toward Clarity and Grace"
- Framework Writing Conventions (20_convention/03_convention_for_writing_style.md)

**Rule Steward:** Writing Standards Committee
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-08
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V0.1.0
**Date:** 2026-01-09

Changelog:
| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.1 | 2026-01-23 | Updated title formatting and placeholders per RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V0.1.0 | 2026-01-09 | Initial creation | AI Framework Admin | Establish file |
