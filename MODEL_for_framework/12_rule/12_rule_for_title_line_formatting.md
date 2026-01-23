# Rule for Title Line Formatting [RULE_FOR_MFW_TITLE_FORMAT] **[PRIO: MEDIUM]**

**Rule ID:** RULE_FOR_MFW_TITLE_FORMAT
**Scope:** All framework document title lines

## Rule Statement

**All framework document title lines should follow the standardized format: # [DOCUMENT_TITLE_DESCRIPTIVE] [TYPE_FRAMEWORK_TITLE_ABBREV] **[PRIO: XXX]****

## Rationale

Standardized title formatting:
- Ensures consistent document identification across the framework
- Provides clear priority indication for content organization
- Enables automated processing and categorization
- Supports framework navigation and search functionality
- Maintains professional presentation standards

## Title Line Format Specification

### Required Structure
```
# [DOCUMENT_TITLE_DESCRIPTIVE] [TYPE_FRAMEWORK_TITLE_ABBREV] **[PRIO: XXX]**
```

### Components Breakdown

| Component | Description | Example |
|-----------|-------------|---------|
| `#` | Markdown header level 1 | `#` |
| `[DOCUMENT_TITLE_DESCRIPTIVE]` | Descriptive title of the document in normal top down writing form | `Definition for Term in MFW` |
| `[TYPE_FRAMEWORK_TITLE_ABBREV]` | Combined type and framework abbreviation | `[DEF_FOR_MFW_TERM]` |
| `**[PRIO: XXX]**` | Priority level indicator | `**[PRIO: HIGHEST]**` |

### Complete Format Example
```markdown
# Term [DEF_FOR_MFW_TERM] **[PRIO: HIGHEST]**
```

### TYPE Component Examples

The TYPE component indicates the document category e.g. can be:

| TYPE Value | Meaning | Example Usage |
|------------|---------|---------------|
| **RULE** | Framework rules and guidelines | `[RULE_FOR_MFW_TITLE_FORMAT]` |
| **DEF_FOR** | Definitions and terminology | `[DEF_FOR_MFW_TERM]` |
| **VISION** | Vision and strategic documents | `[VISION_FOR_MFW]` |
| **PRINC** | Principles and core values | `[PRINC_FOR_MFW_ACCESSIBILITY]` |
| **AXIOM** | Fundamental axioms | `[AXIOM_FOR_MFW_VALIDATION]` |
| **CONV_FOR** | Conventions and standards | `[CONV_FOR_MFW_VERSION]` |
| **TPL_FOR** | Templates and patterns | `[TPL_FOR_MFW_DOCUMENT]` |

---

## Framework Abbreviations

### Core Framework Abbreviations

| Abbreviation | Full Term | Usage Context |
|-------------|-----------|---------------|
| **DEF_FOR_<FW>_** | Definition for | Document definitions |
| **RULE_FOR_<FW>_** | Rule Framework | Framework rules |
| **PRINC_FOR_<FW>_** | Principle | Framework principles |
| **AXIOM_FOR_<FW>_** | Axiom | Framework axioms |
| **CONV_FOR_<FW>_** | Convention for | Framework conventions |
| **TPL_FOR_<FW>_** | Template for | Framework templates |

### Priority Levels

| Priority Code | Meaning | Color Coding |
|---------------|---------|--------------|
| **HIGHEST** | Critical framework components | 🔴 Red |
| **HIGH** | Important operational elements | 🟠 Orange |
| **MEDIUM** | Standard framework elements | 🟡 Yellow |
| **LOW** | Supplementary materials | 🟢 Green |

## Implementation Guidelines

### Title Construction Process

1. **Identify Document Type** - Determine the primary category
2. **Select Appropriate Abbreviation** - Use standard framework abbreviations
3. **Determine Priority Level** - Assess document importance
4. **Format Complete Title** - Combine all elements in specified order

### Document Type Mapping

| Document Type | Abbreviation Pattern | Example |
|---------------|---------------------|---------|
| Rules | `RULE_FOR_<FW>_` | `RULE_FOR_MFW_TITLE_FORMAT` |
| Principles | `PRINC_FOR_<FW>_` | `PRINC_FOR_MFW_ACCESSIBILITY` |
| Definitions | `DEF_FOR_<FW>_` | `DEF_FOR_MFW_TERM` |
| Conventions | `CONV_FOR_<FW>_` | `CONV_FOR_MFW_VERSION` |
| Templates | `TPL_FOR_<FW>_` | `TPL_FOR_MFW_DOCUMENT` |

## Validation Checklist

- [ ] Title starts with single `#` for level 1 header
- [ ] Document title is descriptive and clear
- [ ] Framework abbreviation uses correct format `[ABBREV]`
- [ ] Priority level uses valid code (HIGHEST/HIGH/MEDIUM/LOW)
- [ ] Priority format follows `**[PRIO: XXX]**` exactly (must be bolded)
- [ ] No extra spaces or formatting variations
- [ ] Abbreviation corresponds to document content

## Common Issues and Corrections

### Incorrect Abbreviation Format
**Problem:** `# Title ABBREV [PRIO: HIGH]`
**Correction:** `# Title [ABBREV] [PRIO: HIGH]`

### Missing Priority
**Problem:** `# Title [ABBREV]`
**Correction:** `# Title [ABBREV] [PRIO: MEDIUM]`

### Wrong Header Level
**Problem:** `## Title [ABBREV] [PRIO: HIGH]`
**Correction:** `# Title [ABBREV] [PRIO: HIGH]`

### Invalid Priority Code
**Problem:** `# Title [ABBREV] [PRIO: IMPORTANT]`
**Correction:** `# Title [ABBREV] [PRIO: HIGH]`

## Enforcement

1. **Document Creation:** Apply correct format during initial drafting
2. **Template Validation:** Automated checks verify format compliance
3. **Review Process:** Manual verification during document reviews
4. **Bulk Updates:** Periodic audits ensure consistency across framework


## Automation Support

### Example Regex Pattern for Validation
```regex
^# .+\[.*\]\s+\*\*\[PRIO:\s+(HIGHEST|HIGH|MEDIUM|LOW)\]\*\*$
```

### Automated Processing
- **Search/Indexing:** Standardized format enables reliable document discovery
- **Priority Filtering:** Automated sorting by priority level
- **Cross-References:** Consistent abbreviations support linking systems

## References

- Framework Writing Conventions (20_convention/03_convention_for_writing_style.md)
- Document Naming Convention (20_convention/10_convention_for_file_naming.md)
- Abbreviation Reference (99_appendix/abbreviation_reference.md)
- Active Voice Rule (12_rule/03_rule_for_active_voice.md)

**Rule Steward:** Documentation Standards Committee
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-13
**Review Cycle:** Annual

Changelog:
| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.1 | 2026-01-23 | Updated placeholders to [DOCUMENT_TITLE_DESCRIPTIVE] and [TYPE_FRAMEWORK_TITLE_ABBREV] (with underscores) | Framework Admin | Improve clarity and hierarchy |
| V1.0.0 | 2026-01-09 | Initial creation | AI Framework Admin | Establish file |