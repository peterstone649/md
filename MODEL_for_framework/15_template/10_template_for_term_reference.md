# Term Reference [TPL_FOR_MFW_TERM_REF] **[PRIO: HIGH]**

**We create term reference files that establish inheritance relationships between terminology across different frameworks, ensuring consistent term usage and clear cross-references.**

## Scope

- Term reference templates ensure consistent referencing of terms.

## Term Reference Creation Guidelines

### Core Reference Structure:
1. **Title with Reference**: `# [DOCUMENT_TITLE_DESCRIPTIVE] [TYPE_FRAMEWORK_TITLE_ABBREV] **[PRIO: XXX]**`

**Version: <Version>** **Date: YYYY-MM-DD**

2. **Primary Source Declaration**: `**Primary Definition Source:** [SOURCE_PATH]`
3. **Context-Specific Application**: Framework-specific usage and adaptations
4. **Reference Relationship**: How the term inherits and extends from source
5. **Cross-Reference Links**: Links to related terms in both source and current contexts
6. **Usage Guidelines**: When to use source vs. adapted definitions

### Required Reference Elements:
- **[TYPE_FRAMEWORK_TITLE_ABBREV]**: e.g. [TERM_FOR_MFW_DEFECT_REF]
- **Primary Source Path**: Full relative path to source term definition
- **Framework Context**: How term applies in current framework layer
- **Inheritance Relationship**: What is inherited, adapted, extended
- **Cross-References**: Links to related terms in both frameworks
- **Usage Guidelines**: Clear guidance on when to reference each definition

### Term Reference Naming Convention:
- Use the format: `[NUMBER]_term_[TERM_NAME]_ref.md`
- Examples:
  - `59_term_defect_ref.md` (defect term reference)
  - `71_term_framework_ref.md` (framework term reference)
  - `34_term_validation_ref.md` (validation term reference)

### Reference File Structure:
```
# [DOCUMENT_TITLE_DESCRIPTIVE] [TYPE_FRAMEWORK_TITLE_ABBREV] **[PRIO: XXX]**

## Term Reference
**Primary Definition Source:** [SOURCE_PATH]

## [FRAMEWORK_NAME] Context
[Framework-specific applications and adaptations]

## Reference Relationship
[Inheritance, adaptation, extension details]

## Cross-Reference Links
[Links to related terms]

## Usage Guidelines
[When to use source vs. adapted definitions]

## [FRAMEWORK_NAME]-Specific [TOPIC]
[Framework-specific implementations and details]

## Quality Assurance Integration
[Framework-specific quality metrics]

## Conclusion
[Summary of reference relationship and usage]
```

### Quality Assurance for References:
1. **Source Validity**: Primary source file exists and is accessible
2. **Inheritance Clarity**: Clear explanation of what is inherited vs. adapted
3. **Cross-Reference Accuracy**: All linked files exist and are relevant
4. **Usage Clarity**: Guidelines are unambiguous and practical
5. **Context Appropriateness**: Framework-specific content is relevant and accurate

### Version Requirements:
- **Version Number**: Every reference must include a version number (e.g., v1.0, v2.1)
- **Version Format**: Use semantic versioning (MAJOR.MINOR.PATCH)
- **Version Location**: Place version information prominently at the top of the document
- **Version Tracking**: Document changes between versions with rationale
- **Compatibility**: Specify which framework versions the reference supports

## Example: Defect Term Reference

Based on the defect reference file (`_29/MODEL_for_framework/30_terminology/59_term_defect_ref.md`), here is how the template extracts and structures information:

### **Extracted Information Structure:**
1. **Primary Source**: `_29/SWmeth/30_terminology/59_term_defect.md`
2. **Framework Context**: FWmeth-specific defect applications (template defects, convention defects, integration defects)
3. **Reference Relationship**: Inherits core concepts, adapts for framework contexts, extends for methodology compliance
4. **Cross-References**: Links to Framework, Template, Convention, Validation terms
5. **Usage Guidelines**: When to reference SWmeth vs. apply FWmeth context
6. **Framework-Specific Management**: Template validation, convention auditing, integration testing
7. **Quality Assurance**: Template defect rates, convention compliance rates, integration success rates

### **Template Application Benefits:**
- **Consistency**: Standardized format across all term references
- **Clarity**: Clear separation between source and adapted definitions
- **Maintainability**: Easy to update when source terms change
- **Navigation**: Framework users can easily find appropriate term definitions
- **Evolution**: Framework can evolve while maintaining term relationships

*This template establishes the methodology for creating term reference files that extract and adapt terminology from source frameworks, ensuring clear inheritance relationships and consistent usage across framework layers.*

**Framework:** MODEL_for_framework
**Framework Version:** V0.1.0
**Date:** 2026-01-23

## Changelog

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.1 | 2026-01-23 | Updated title formatting and placeholders per RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V0.1.0 | 2026-01-09 | Initial template creation | Framework Steward | Establish term reference template standard |
