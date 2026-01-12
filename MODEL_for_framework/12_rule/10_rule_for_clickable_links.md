# Rule for Clickable Links **[RULE_FW_CLICKABLE_LINKS]** **[PRIO: HIGH]**

**Version: V1.0.0** **Status: ACTIVE** **Date: 2026-01-09**

**Rule ID:** RULE_CLICKABLE_LINKS
**Applies to:** All framework documentation

---

## Rule Statement

**All cross-references to framework documents SHOULD use clickable markdown links. Plain text file paths are NOT acceptable for internal navigation.**

---

## Rationale

Clickable links:
- Enable direct navigation between related documents
- Reduce friction for readers exploring the framework
- Ensure links remain functional when file locations change
- Support markdown viewers and IDE navigation
- Align with framework principles of clarity and accessibility
- Make framework exploration intuitive and efficient

---

## Clickable Link Pattern

### Structure
```markdown
[Link Text](relative/path/to/file.md)
```

### Examples

| Unacceptable ❌ | Acceptable ✅ |
|----------------|---------------|
| See `30_principle/01_principle_human_sovereignty.md` | See [Human Sovereignty](../30_principle/01_principle_human_sovereignty.md) |
| Templates are in `15_template/17_template_for_principle.md` | Templates are in [17_template_for_principle.md](../../15_template/17_template_for_principle.md) |
| Legal info in 01_copyright_notice.md | Legal info in [01_copyright_notice.md](../01_legal/01_copyright_notice.md) |

---

## Link Construction Strategy

1. **Identify Target File** - Determine the document you want to reference
2. **Calculate Relative Path** - Navigate from current file to target
3. **Write Descriptive Link Text** - Use meaningful, concise text
4. **Wrap in Markdown Syntax** - `[Text](path)`

### Path Navigation Rules
- `../` = Move up one directory level
- `../../` = Move up two directory levels
- No leading slash = Relative to current directory

### Application Examples

**From subdirectory to parent:**
```markdown
[Principle Document](../30_principle/01_principle_human_sovereignty.md)
[Template File](../../15_template/17_template_for_principle.md)
[Legal Document](../01_legal/01_copyright_notice.md)
```

**From principle to overview:**
```markdown
[Getting Started Guide](../../00_overview/20_stakeholder/01_getting_started.md)
[Principle Template](../../15_template/17_template_for_principle.md)
```

---

## Acceptable Plain Text Exceptions

Plain text file paths ARE acceptable when:

1. **Table Columns**
   - Document location is a column value requiring visual clarity
   
2. **Directory Structure Listings**
   - File tree diagrams where links would be visually overwhelming

3. **Code Examples**
   - Demonstrating path format in documentation about paths

4. **Quick Reference Tables**
   - When both link text and path need visible separation

---

## Validation Checklist

- [ ] All internal document references use `[Text](path)` format
- [ ] Link text describes the target document's purpose
- [ ] Relative paths are correct and functional
- [ ] No broken or dead links
- [ ] Links work in markdown viewers and IDEs

---

## Enforcement

1. **Writing Phase:** Writers apply link pattern during drafting
2. **Review Phase:** Reviewers verify all cross-references are clickable
3. **Automated Checks:** Tools can verify markdown link syntax

---

## Cross-Framework Application

This rule applies universally across all framework directories:
- **MODEL_for_framework** - Core methodology documentation
- **MODEL_for_STKHLD_AI_COLLAB** - Stakeholder-AI collaboration principles
- **FIELDC*** directories - Domain-specific implementations
- **Ethosys** - Ethics and safety framework

---

## References

- Framework Writing Conventions (20_convention/03_convention_for_writing_style.md)
- Markdown Specification (CommonMark)
- Active Voice Rule (12_rule/01_rule_for_active_voice.md)

---

**Rule Steward:** Framework Standards Committee
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-09
**Review Cycle:** Annual
