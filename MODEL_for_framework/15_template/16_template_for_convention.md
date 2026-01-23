# [DOCUMENT_TITLE_DESCRIPTIVE] [TYPE_FRAMEWORK_TITLE_ABBREV] **[PRIO: XXX]**

**Version: V[VERSION]** **Status: [STATUS]** **Date: YYYY-MM-DD**

**We establish [CONVENTION_PURPOSE] that enable [CONVENTION_BENEFITS] across the framework ecosystems.**

**Rationale:**
[CONVENTION_RATIONALE - Explain why this convention exists and what problems it solves]

## Core Convention Principles

### **Standard Convention Format**
```
[NUMBER]_[TYPE_CONSTANT]_[DESCRIPTIVE_NAME].[EXTENSION]
```

### **Convention Component Definitions**
- **[NUMBER]**: Sequential identifier (01, 02, 10, etc.) for ordering and uniqueness
- **[TYPE_CONSTANT]**: Standardized convention type identifier (convention, rule, standard, etc.)
- **[DESCRIPTIVE_NAME]**: Clear, concise description using underscores
- **[EXTENSION]**: Standard file extension (.md, .yaml, etc.)

### **Convention Rules**
1. **Format**: All conventions follow the standard naming format
2. **Consistency**: Conventions must align with framework principles
3. **Documentation**: All conventions must be clearly documented
4. **Validation**: Conventions must support automated verification
5. **Evolution**: Conventions must allow for systematic updates

## Convention Usage Guidelines

### **Convention Application Rules**
1. **Scope Compliance**: Apply conventions only within their defined scope
2. **Consistency**: Follow conventions uniformly across all applicable contexts
3. **Documentation**: Reference conventions in relevant documentation
4. **Validation**: Use conventions to validate framework compliance
5. **Evolution**: Update conventions following established procedures

### **Convention Categories**
- **Core Conventions**: Fundamental framework standards (version, naming, etc.)
- **Domain Conventions**: Specific domain standards (technical, legal, etc.)
- **Special Conventions**: Specialized operational standards (quality, process, etc.)

## 1. Scope and Applicability

### 1.1 When to Apply
<Describe when this convention should be applied. What situations, document types, or contexts require following this convention?>

### 1.2 Target Audience
<Who should follow this convention? Developers, writers, architects, etc.>

## 2. Core Definitions

| Element | Definition | Example |
|---------|------------|---------|
| **<term1>** | <Definition of first key term> | `<example>` |
| **<term2>** | <Definition of second key term> | `<example>` |
| **<term3>** | <Definition of third key term> | `<example>` |

## 3. Version Requirements

### 3.1 Version Number
- **Version Number**: Every convention must include a version number (e.g., V0.1.0)
- **Version Format**: Use semantic versioning (MAJOR.MINOR.PATCH)
- **Version Location**: Place version information prominently at the top of the document
- **Version Tracking**: Document changes between versions with rationale
- **Compatibility**: Specify which framework versions the convention supports

### 3.2 Semantic Versioning Guidelines
| Version Type | Meaning | Description |
|--------------|---------|-------------|
| **MAJOR** | Breaking Changes | Changes that are not backward compatible |
| **MINOR** | New Features | New features that are backward compatible |
| **PATCH** | Bug Fixes | Minor improvements and fixes that are backward compatible |

### 3.3 Version Documentation
- Include version history in changelog format
- Document breaking changes and migration paths
- Specify minimum framework version requirements
- Track deprecation notices for older versions

## 4. Rules and Guidelines

### 4.1 <Rule Category 1>
<Describe the first category of rules. Include specific requirements and best practices.>

### 4.2 <Rule Category 2>
<Describe the second category of rules.>

### 4.3 <Rule Category 3>
<Describe the third category of rules if needed.>

## Quality Assurance Standards

### **Convention Validation Rules**
1. **Existence**: All referenced conventions must be documented
2. **Consistency**: Convention usage must follow established patterns
3. **Accuracy**: Conventions must correctly address their defined scope
4. **Completeness**: All applicable areas must have appropriate conventions
5. **Maintenance**: Convention list must be regularly reviewed and updated

### **Automated Validation**
- **Convention Checking**: Regular expression validation of convention usage
- **Scope Verification**: Automated checking of convention applicability
- **Consistency Auditing**: Regular audits of convention adherence
- **Usage Tracking**: Monitoring of convention adoption and effectiveness

### **Maintenance Procedures**
- **Convention Addition**: Process for adding new conventions to the framework
- **Deprecation**: Procedures for phasing out obsolete conventions
- **Migration**: Guidelines for updating existing documents with new conventions
- **Documentation**: Regular updates to convention documentation

## Implementation Guidelines

### **Convention Adoption Process**
1. **Review Existing Usage**: Audit current convention usage patterns
2. **Standardization**: Align existing documents with convention standards
3. **Template Updates**: Modify document templates to use approved conventions
4. **Training**: Educate team members on convention standard usage
5. **Enforcement**: Apply convention standards to all new documents

### **Tools and Integration**
- **Validation Scripts**: Automated checking of convention compliance
- **Template Integration**: Document templates enforcing convention standards
- **IDE Support**: Editor plugins for convention standard enforcement
- **Documentation Tools**: Automated convention validation in documentation workflows

### **Monitoring and Compliance**
- **Regular Audits**: Periodic checking of convention standard compliance
- **Automated Alerts**: Notifications for convention standard violations
- **Usage Analytics**: Tracking of convention adoption and effectiveness
- **Exception Handling**: Defined procedures for convention standard exceptions

## Benefits and Impact

### **Operational Benefits**
- **Improved Standardization**: Conventions ensure consistent framework implementation
- **Automated Processing**: Scripts can reliably process convention-compliant documents
- **Quality Assurance**: Automated validation of framework standards
- **Maintenance Efficiency**: Easier framework management and organization

### **Development Benefits**
- **Consistency**: Uniform convention usage across all framework components
- **Scalability**: Convention standards scale with framework growth
- **Integration**: Easier integration with external tools and systems
- **Evolution**: Framework can evolve while maintaining convention consistency

### **Collaboration Benefits**
- **Team Coordination**: Clear expectations for convention usage
- **Knowledge Transfer**: Easy onboarding with standardized conventions
- **Review Efficiency**: Faster document reviews with consistent standards
- **Cross-Team Work**: Consistent convention usage across different teams and projects

## 5. Naming Conventions

| Pattern | Meaning | Example |
|---------|---------|---------|
| **<prefix>** | <Description> | `<example>` |
| **<prefix>** | <Description> | `<example>` |
| **<prefix>** | <Description> | `<example>` |

## 6. Status and States

| Status | Meaning | Transition |
|--------|---------|------------|
| **DRAFT** | Initial creation, pending review | → OPEN |
| **OPEN** | Ready for implementation | → IN PROGRESS |
| **IN PROGRESS** | Actively being implemented | → REVIEW or PAUSED |
| **PAUSED** | Temporarily halted | → IN PROGRESS or DONE |
| **REVIEW** | Pending validation | → DONE or IN PROGRESS |
| **DONE** | Complete and validated | → ARCHIVED |
| **ARCHIVED** | Historical reference | - |

## 7. Examples

### 7.1 Correct Usage
```
<example of correct implementation>
```

### 7.2 Incorrect Usage
```
<example of incorrect implementation - what to avoid>
```

### 7.3 Edge Cases
```
<examples of special cases and how to handle them>
```

## 8. Related Conventions and Documents

| Reference | Relationship |
|-----------|--------------|
| [CONV_FOR_<RELATED>] | <Description of relationship> |
| [CONV_FOR_<RELATED>] | <Description of relationship> |
| [<path/to/document>] | <Description of relationship> |

## 9. Implementation Notes

### 9.1 Migration Path
<If this convention replaces an older approach, describe how to migrate.>

### 9.2 Tooling Support
<List any tools, scripts, or automated checks that support this convention.>

### 9.3 Validation Checklist
- [ ] <First validation item>
- [ ] <Second validation item>
- [ ] <Third validation item>

**Rule Steward:** [STEWARD]
**Approval Status:** [STATUS]
**Effective Date:** YYYY-MM-DD
**Review Cycle:** [CYCLE]

**Framework:** MODEL_for_framework
**Framework Version:** V0.1.0
**Date:** 2026-01-23

## Changelog

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.1 | 2026-01-23 | Updated title formatting and placeholders per RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V0.1.0 | 2026-01-09 | Initial template creation | Framework Steward | Establish convention template standard |
