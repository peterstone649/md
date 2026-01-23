# Template for Template Minimal [TPL_FOR_MFW_TPL_OT_MIN] **[PRIO: HIGH]**

**Version: V1.0.2** **Status: ACTIVE** **Date: 2026-01-23**

**Template Scope:** MODEL_for_framework_ecosystem
**We create templates that standardize documentation and ensure consistency across all framework components.**

**Benefits:**
- Templates ensure consistent formatting across all documentation types
- Standardized structure improves readability and maintainability
- Template-based creation reduces errors and saves time
- Consistent naming conventions enable programmatic processing
- Templates support automated validation and quality checks
- Framework evolution is supported through template updates

---

## Template Creation Guidelines

### Core Template Structure:
1. **Title with Reference**: `# [DOCUMENT_TITLE_DESCRIPTIVE] [TYPE_FRAMEWORK_TITLE_ABBREV] **[PRIO: XXX]**`

2. **Manifesto Statement**: `**[STATEMENT]**` or `**Manifesto Statement:** [STATEMENT]`
3. **Application Section**: `-`
4. **Bullet Points**: 4-6 specific application points
5. **Usage Instructions**: Clear guidance for template users

### Required Template Elements:
- **[TYPE_FRAMEWORK_TITLE_ABBREV]**: UPPER_CASE_WITH_UNDERSCORES format emphasizing hierarchy (e.g., [TPL_FOR_MFW_DOCUMENT])
- **[PLACEHOLDER_FIELDS]**: Clearly marked with `[BRACKETS]`
- **Alternative Formats**: Provide both subtitle and section formats
- **Usage Examples**: Concrete examples of template application
- **Guidelines**: Best practices for template usage

### Template Naming Convention:
- Use the format: `[NUMBER]_template_for_[PURPOSE].md`
- Follow the file naming convention: [`02_convention_for_file_naming.md`](../20_convention/02_convention_for_file_naming.md)
- Examples:
  - `00_template_for_template.md` (meta-template)
  - `01_template_for_principle.md` (principle template)
  - `02_template_for_guideline.md` (guideline template)

#### Principle File Naming Convention:
- Use the format: `[NUMBER]_principle_[DESCRIPTIVE_NAME].md`
- Example: `13_principle_emergent_safety_architectures.md`
- Numbering should be sequential and reflect the principle's position in the framework
- Descriptive names should be concise but clearly indicate the principle's focus
- Use underscores to separate words in the descriptive name

### Quality Assurance:
1. **Consistency Check**: All templates follow the same structure
2. **Completeness**: All required fields are documented
3. **Clarity**: Instructions are unambiguous
4. **Examples**: Real usage examples provided
5. **Validation**: Templates support automated checking

### Version Requirements:
- Follow the version convention: [`01_convention_for_version.md`](../20_convention/01_convention_for_version.md)

---

*This meta-template establishes the methodology for creating all templates in the AI safety framework, ensuring consistency, quality, and maintainability across all documentation components.*

**Rule Steward:** Framework Admin
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-09
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V1.0.2
**Date:** 2026-01-23

## Changelog
| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.2 | 2026-01-23 | Synchronized terminology ([TYPE_FRAMEWORK_TITLE_ABBREV]) with RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V1.0.1 | 2026-01-23 | Synchronized placeholder terminology with RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V1.0.0 | 2026-01-09 | Initial creation | AI Framework Admin | Establish file |

