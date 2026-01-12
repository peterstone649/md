# 10. File Naming Convention (CONV_FOR_MODELFW_FILE_NAMING) **[PRIO: HIGH]**

**Version: V1.0** **Status: APPROVED** **Date: 2026-01-09**

**We establish consistent file naming standards that enable programmatic processing, improve discoverability, and maintain framework organization.**

**Benefits:**
- Consistent file naming enables automated framework validation and processing
- Standardized naming conventions support programmatic documentation generation
- Clear file naming improves framework navigation and maintenance
- Systematic naming enables automated cross-referencing and dependency tracking
- Framework evolution is supported through consistent naming patterns
- File naming standards enable automated quality assurance and compliance checking

---

## Referenced Standards

### Type Prefix Standards

**Prefix standards are defined in the dedicated convention: [`17_convention_for_prefix_standards.md`](../17_convention_for_prefix_standards.md)**

### **Integration with File Naming**
- File names use prefixes from the approved prefix standards
- Prefix selection must follow semantic accuracy guidelines
- All prefixes must be documented in the prefix standards convention
- Prefix usage enables automated categorization and processing
## Core File Naming Principles

### **Standard Format Structure**
```
[NUMBER]_[TYPE_CONSTANT]_[DESCRIPTIVE_NAME].[EXTENSION]
```

### **Component Definitions**
- **[NUMBER]**: Sequential identifier (01, 02, 10, etc.) for ordering and uniqueness
- **[TYPE]**: Content type identifier (term, axiom, theorem, template, convention, etc.)
- **[DESCRIPTIVE_NAME]**: Clear, concise description using underscores, structured top-down when possible (e.g., `convention_for_version`, `template_for_template_OT_flexible`)
- **[EXTENSION]**: Standard file extension (.md, .py, .json, etc.)

### **Naming Rules**
1. **Numbers**: normally 2 digits with leading zero (01, 02, ..., 10, 11, ...)
2. **Type Prefixes**: Use standardized type identifiers
3. **Descriptive Names**: Use lowercase with underscores, no spaces except for abbreviations
4. **Extensions**: Use appropriate file extensions consistently

---

## File Naming Examples

### **Terminology Files**
```
01_term_alignment.md
02_term_trust.md
10_term_system_health.md
59_term_defect.md
```

### **Axiom Files**
```
01_axiom_of_component_dual_nature.md
05_axiom_of_criticality_driven_resource_allocation.md
10_axiom_of_objective_achievement.md
```

### **Template Files**
```
01_template_for_template_OT_minimal.md
10_template_for_term_reference.md
05_template_for_template_OT_flexible.md
```

### **Convention Files**
```
01_convention_for_version.md
02_convention_for_file_naming.md
```

---

## Directory Structure Integration

### **Standard Directory Organization**
```
[PROJECT]/
├── [NUMBER]_[TYPE]_[CATEGORY]/
│   ├── [NUMBER]_[SUBTYPE]_[NAME].[EXT]
│   └── [NUMBER]_[SUBTYPE]_[NAME].[EXT]
```

### **Directory Naming Examples**
```
00_vision/
├── 01_vision_statement.md
└── 02_mission_objectives.md

30_terminology/
├── 01_term_alignment.md
├── 02_term_trust.md
└── 59_term_defect.md

15_template/
├── 01_template_for_template_OT_minimal.md
└── 10_template_for_term_reference.md
```

---

## Special Naming Cases

### **Reference Files**
- Use `_ref` suffix for reference documents
- Example: `59_term_defect_ref.md`

### **Versioned Files**
- Use `_v[VERSION]` suffix for versioned documents
- Example: `01_template_v2.1.md`

### **Draft Files**
- Use `_draft` suffix for draft documents
- Example: `02_convention_draft.md`

### **Archive Files**
- Use `_archive` suffix for archived documents
- Example: `01_term_archive.md`

---

## Quality Assurance Standards

### **Naming Validation Rules**
1. **Format Compliance**: All files must follow the standard format
2. **Uniqueness**: No duplicate file names within the same directory
3. **Consistency**: Type prefixes must be from approved list
4. **Clarity**: Descriptive names must be unambiguous and accurate
5. **Extensions**: File extensions must be appropriate for content type

### **Automated Validation**
- **Format Checking**: Regular expression validation of file names
- **Directory Scanning**: Automated inventory and compliance checking
- **Cross-Reference Validation**: Verification of file linkages and references
- **Consistency Auditing**: Regular audits of naming convention adherence

### **Maintenance Procedures**
- **Version Tracking**: Document changes to naming conventions
- **Migration Planning**: Procedures for renaming existing files
- **Documentation Updates**: Keep naming convention documentation current
- **Training Updates**: Update training materials when conventions change

---

## Implementation Guidelines

### **Adoption Process**
1. **Review Existing Files**: Audit current file naming patterns
2. **Plan Migration**: Develop strategy for renaming existing files
3. **Update Templates**: Modify document templates to use new conventions
4. **Training**: Educate team members on new naming standards
5. **Implementation**: Apply new conventions to new files immediately

### **Tools and Automation**
- **Validation Scripts**: Automated checking of file naming compliance
- **Renaming Tools**: Safe batch renaming with reference updating
- **Template Integration**: Document templates that enforce naming standards
- **IDE Integration**: Editor plugins for naming convention enforcement

### **Monitoring and Enforcement**
- **Regular Audits**: Periodic checking of naming convention compliance
- **Automated Alerts**: Notifications for naming convention violations
- **Documentation Links**: Clear references to naming standards
- **Exception Process**: Defined procedures for naming convention exceptions

---

## Benefits and Impact

### **Operational Benefits**
- **Improved Discoverability**: Files can be easily located and identified
- **Automated Processing**: Scripts can reliably process file collections
- **Quality Assurance**: Automated validation of documentation structure
- **Maintenance Efficiency**: Easier file management and organization

### **Development Benefits**
- **Consistency**: Uniform approach across all framework components
- **Scalability**: Naming conventions scale with framework growth
- **Integration**: Easier integration with external tools and systems
- **Evolution**: Framework can evolve while maintaining naming consistency

### **Collaboration Benefits**
- **Team Coordination**: Clear expectations for file naming
- **Knowledge Transfer**: Easy onboarding with standardized naming
- **Review Efficiency**: Faster code and documentation reviews
- **Cross-Team Work**: Consistent naming across different teams and projects

---

*This file naming convention establishes the foundation for consistent, maintainable, and programmatically accessible documentation across the entire framework.*

