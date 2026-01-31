# Plugin Convention [CONV_FOR_MFW_PLUGIN] **[PRIO: HIGH]**

**We establish plugin conventions as a core convention that defines standardized patterns for creating, organizing, and integrating plugins within the MODEL_for_framework ecosystem.**

**Objectives:**
1. **Standardization**: Define consistent plugin structure and naming
2. **Integration**: Ensure seamless plugin integration with core framework

---

## Abstract

**[AI_LOCK]**
The Plugin Conventions establish standardized patterns for creating, organizing, and integrating plugins within the MODEL_for_framework ecosystem. These conventions ensure that all plugins follow consistent structural patterns, naming conventions, and integration protocols.
**[END_AI_LOCK]**

---

## 1. Scope and Applicability

### 1.1 When to Apply
- Creating new plugins for the framework
- Modifying existing plugin structure

### 1.2 Target Audience
- Plugin developers
- Framework maintainers

---

## 2. Core Definitions

| Element | Definition | Example |
|---------|------------|---------|
| **Plugin** | Self-contained extension that restricts/modifies/adds functionality | Feedback processing plugin |
| **Convention** | Standardized pattern or practice | Naming, structure, integration |

---

## 3. Plugin Structure

### 3.1 Directory Structure

```
plugin_name/
├── README.md                    # Plugin documentation entry
├── 10_templates/               # Plugin templates
├── 20_rules/                   # Plugin-specific rules
├── 30_principles/              # Plugin principles
├── 40_use_cases/               # Plugin use cases
├── 50_examples/                # Plugin examples
├── 60_tests/                   # Plugin tests
└── 99_appendix/                # Plugin appendix
```

### 3.2 File Naming

| File Type | Pattern | Example |
|-----------|---------|---------|
| **Plugin Directory** | `plugin_name/` | `plugin_for_feedback/` |
| **Main Documentation** | `README.md` | `README.md` |
| **Plugin Entry** | `index.md` | `index.md` |
| **Templates** | `10_template_*.md` | `10_template_feedback_for_template.md` |
| **Rules** | `20_rule_*.md` | `20_rule_naming.md` |
| **Principles** | `30_principle_*.md` | `30_principle_integration.md` |
| **Use Cases** | `40_use_case_*.md` | `40_use_case_feedback.md` |
| **Examples** | `50_example_*.md` | `50_example_simple.md` |
| **Tests** | `60_test_*.md` | `60_test_functionality.md` |
| **Glossary** | `99_appendix/10_glossary.md` | `99_appendix/10_glossary.md` |

---

## 4. Plugin Integration

### 4.1 Plugin Registration

1. **Plugin Directory**: Create plugin in `MODEL_for_framework/00_overview/40_plugin/`
2. **Index Entry**: Add plugin to main plugin index
3. **Cross-References**: Link to related framework components
4. **Documentation**: Provide comprehensive plugin documentation

### 4.2 Plugin Dependencies

1. **Framework Dependencies**: Specify required framework components
2. **Plugin Dependencies**: Document dependencies on other plugins
3. **External Dependencies**: List any external tool requirements
4. **Version Compatibility**: Specify compatible framework versions

---

## 5. Related Documents

| Reference | Relationship |
|-----------|--------------|
| [16_template_for_convention.md](../15_template/16_template_for_convention.md) | Template for plugin conventions |
| [10_convention_for_file_naming.md](../20_convention/10_convention_for_file_naming.md) | File naming standards |
| [17_convention_for_prefix_standards.md](../20_convention/17_convention_for_prefix_standards.md) | Prefix standards |

---

## 6. Changelog

| Version | Date | Changes | Stakeholder | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | 2026-01-31 | Initial creation | Framework Steward | Establish plugin conventions for framework ecosystem |

**Version History Guidelines:**
- **Stakeholder**: Document the person or role responsible for the change
- **Rationale/Motivation**: Explain why the change was made
- **Traceability**: Each version entry links to a documented decision or request

---

**End of Plugin Convention**

---

**Template Version:** V1.0
**Template Reference:** [16_template_for_convention.md](../15_template/16_template_for_convention.md)
**Date:** 2026-01-31
**Framework:** MODEL_for_framework