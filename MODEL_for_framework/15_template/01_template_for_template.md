# 1. Template for Template Minimal (TEMPLATE_FOR_MFW_TEMPLATE) **[PRIO: HIGH]**

**Template Version:** V1.0.0 **Template Status:** APPROVED **Date:** 2026-01-09
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
1. **Title with Reference**: `# [NUMBER]. [TITLE] ([CONSTANT_REFERENCE])`

**Version: V<Version>** **Status: <STATUS>** **Date: YYYY-MM-DD**

2. **Manifesto Statement**: `**[STATEMENT]**` or `**Manifesto Statement:** [STATEMENT]`
3. **Application Section**: `-`
4. **Bullet Points**: 4-6 specific application points
5. **Usage Instructions**: Clear guidance for template users

### Required Template Elements:
- **[CONSTANT_REFERENCE]**: UPPER_CASE_WITH_UNDERSCORES format
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
