# Rule for Title Line Formatting [RULE_FOR_MFW_TITLE_FORMAT] **[PRIO: MEDIUM]**

## Rule Statement **[STATUS: ACTIVE]**

All framework document title lines MUST follow the standardized format:
- Ensure consistent document identification across the framework
- Provide clear priority indication for content organization
- Enable automated processing and categorization
- Support framework navigation and search functionality
- Maintain professional presentation standards

All framework document title lines therefore MUST follow the standardized format:
```
# [DOCUMENT_TITLE_DESCRIPTIVE] [TYPE_FRAMEWORK_TITLE_ABBREV] **[PRIO: XXX]**
```

### Title Line Format Specification

#### Required Structure
```
# [DOCUMENT_TITLE_DESCRIPTIVE] [TYPE_FRAMEWORK_TITLE_ABBREV] **[PRIO: XXX]**
```

#### Components Breakdown

| Component | Description | Example |
|-----------|-------------|---------|
| `#` | Markdown header level 1 | `#` |
| `[DOCUMENT_TITLE_DESCRIPTIVE]` | Descriptive title of the document in normal top down writing form | `Definition for Term in MFW` |
| `[TYPE_FRAMEWORK_TITLE_ABBREV]` | Combined type and framework abbreviation | `[DEF_FOR_MFW_TERM]` |
| `**[PRIO: XXX]**` | Priority level indicator | `**[PRIO: HIGHEST]**` |

#### Complete Format Example
```markdown
# Convention for Date [CONV_FOR_MFW_DATE] **[PRIO: HIGH]**
```

#### TYPE Component Examples

The TYPE component indicates the document category e.g. can be:

| TYPE Value | Meaning | Example Usage |
|------------|---------|---------------|
| **RULE** | Framework rules and guidelines | `[RULE_FOR_MFW_TITLE_FORMAT]` |
| **TERM** | Definitions and terminology | `[TERM_FOR_MFW_TERM]` |
| **VISION** | Vision and strategic documents | `[VISION_FOR_MFW]` |
| **PRINC** | Principles and core values | `[PRINC_FOR_MFW_ACCESSIBILITY]` |
| **AXIOM** | Fundamental axioms | `[AXIOM_FOR_MFW_VALIDATION]` |
| **CONV** | Conventions and standards | `[CONV_FOR_MFW_VERSION]` |
| **TPL** | Templates and patterns | `[TPL_FOR_MFW_DOCUMENT]` |

---

## Framework Abbreviations

### Core Framework Abbreviations

| Abbreviation | Full Term | Usage Context |
|-------------|-----------|---------------|
| **TERM_FOR_<FW>_** | Term for | Document definitions |
| **RULE_FOR_<FW>_** | Rule Framework | Framework rules |
| **PRINC_FOR_<FW>_** | Principle | Framework principles |
| **AXIOM_FOR_<FW>_** | Axiom | Framework axioms |
| **CONV_FOR_<FW>_** | Convention for | Framework conventions |
| **TPL_FOR_<FW>_** | Template for | Framework templates |

### Priority Levels

| Priority Code | Meaning | Color Coding |
|---------------|---------|--------------|
| **CRITICAL** | Critical framework components | 🔴 Red |
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
| Terms | `TERM_FOR_<FW>_` | `TERM_FOR_MFW_TERM` |
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
**Correction:** `# Title [ABBREV] **[PRIO: HIGH]**`

### Missing Priority
**Problem:** `# Title [ABBREV]`
**Correction:** `# Title [ABBREV] **[PRIO: MEDIUM]**`

### Wrong Header Level
**Problem:** `## Title [ABBREV] **[PRIO: HIGH]**`
**Correction:** `# Title [ABBREV] **[PRIO: HIGH]**`

### Invalid Priority Code
**Problem:** `# Title [ABBREV] **[PRIO: IMPORTANT]**`
**Correction:** `# Title [ABBREV] **[PRIO: HIGH]**`

## Enforcement

1. **Document Creation:** Apply correct format during initial drafting
2. **Template Validation:** Automated checks verify format compliance
3. **Review Process:** Manual verification during document reviews
4. **Bulk Updates:** Periodic audits ensure consistency across framework


## Automation Support

### Example Regex Pattern for Validation
```regex
^# .+\[.*\]\s+\*\*\[PRIO:\s+(CRITICAL|HIGH|MEDIUM|LOW)\]\*\*$
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

---

## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|------------|
| V1.0.3 | 2026-02-07 | Applied version and changelog update rule per RULE_FOR_MFW_VERSION_CHANGELOG_UPDATE; updated Rule Statement to use active voice and proper format | AI Framework Steward | Ensure compliance with framework version and changelog standards |
| V1.0.2 | 2026-01-23 | Updated metadata headers per RULE_FOR_MFW_TITLE_FORMAT; changed DEF to TERM in examples | Framework Admin | Ensure framework-wide consistency with terminology |
| V1.0.1 | 2026-01-23 | Updated placeholders to [DOCUMENT_TITLE_DESCRIPTIVE] and [TYPE_FRAMEWORK_TITLE_ABBREV] (with underscores) | Framework Admin | Improve clarity and hierarchy |
| V1.0.0 | 2026-01-09 | Initial creation | AI Framework Admin | Establish file |
