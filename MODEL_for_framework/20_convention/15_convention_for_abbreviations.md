# Abbreviation Convention [CONV_FOR_MFW_ABBREVIATIONS] **[PRIO: HIGH]**

**Scope:** All documents within the framework (conventions, templates, axioms, strategies, and tasks)

## Rationale

This convention establishes standardized abbreviations and acronyms for consistent use throughout the framework. It ensures clarity, maintainability, and interoperability across all framework components by providing a systematic approach to creating, documenting, and applying abbreviations.

---

## 1. Scope and Applicability

### 1.1 When to Apply
- Creating new framework documents (conventions, templates, axioms, strategies, tasks)
- Defining variable names and identifiers
- Naming files and folders
- Writing technical documentation
- Creating cross-references between documents

### 1.2 Target Audience
- Framework developers and maintainers
- Document authors and contributors
- e.g., Technical writers, System architects

---

## 2. Core Definitions

| Element | Definition | Example |
|---------|------------|---------|
| **Prefix** | Short code representing a full term, used at the beginning of identifiers | `fw`, `model`, `tpl` |
| **Abbreviation** | Shortened form of a word or phrase | `DRAFT`, `IN_PROGRESS` |
| **Acronym** | Word formed from initial letters |  `SAFe`, `FIELDC` |
| **Convention Constant** | Standardized constant prefix for framework references | `CONV_FOR_`, `CONV_VERSION` |

---

## 3. Version Requirements

Version management follows [CONV_FOR_MFW_VERSION](./01_convention_for_version.md).

| Version Type | Meaning | Description |
|--------------|---------|-------------|
| **MAJOR** | Breaking Changes | Not backward compatible |
| **MINOR** | New Features | Backward compatible |
| **PATCH** | Bug Fixes | Backward compatible |

---

## 4. Rules and Guidelines

### 4.1 Prefix-Based Abbreviations
Prefixes are defined in [CONV_FOR_MFW_FORMAL_NOTATION](./12_convention_for_formal_notation.md).

| Prefix | Full Term | Usage | Example |
|--------|-----------|-------|---------|
| **fra** | Framework | Framework-level references | `fra_id`, `fra_version` |
| **model** | Model | Model definitions | `mod_name`, `mod_type` |
| **tpl** | Template | Template components | `tpl_id`, `tpl_category` |
| **conv** | Convention | Convention references | `con_id`, `con_status` |
| **val** | Validation | Validation logic | `val_score`, `val_result` |
| **sys** | System/Systematic | System-level elements | `sys_name`, `sys_version` |
| **evo** | Evolution/Extension | Evolution tracking | `evo_phase`, `evo_status` |
| **axiom** | Axiom/Applicability | Axiom references | `axi_id`, `axi_type` |
| **integ** | Integration/Integrity | Integration points | `integ_type`, `integ_status` |
| **prop** | Property/Principle | Properties and principles | `prop_name`, `prop_value` |
| **term** | Term | Terminology entries | `term_id`, `term_name` |
| **def** | Definition | Definitions | `def_id`, `def_text` |

### 4.2 Status Abbreviations

| Abbreviation | Full Status | Meaning |
|--------------|-------------|---------|
| **DRAFT** | Draft | Initial creation, pending review |
| **OPEN** | Open | Task/work item identified, not started |
| **IN_PROGRESS** | In Progress | Active work being conducted |
| **PAUSED** | Paused | Work temporarily halted |
| **REVIEW** | Review | Pending validation/approval |
| **DONE** | Done | All work complete and validated |
| **ARCHIVED** | Archived | Historical reference, no longer active |

### 4.3 Document Type Abbreviations

| Abbreviation | Full Term | File Pattern |
|--------------|-----------|--------------|
| **axiom** | Axiom | `##_axiom_*.md` |
| **convention** | Convention | `##_convention_*.md` |
| **template** | Template | `##_template_*.md` |
| **strategy** | Strategy | `##_strategy_*.md` |
| **thesis** | Thesis | `##_thesis_*.md` |
| **term** | Term | `##_term_*.md` |
| **rule** | Rule | `##_rule_*.md` |
| **task** | Task | `task_*.md` |

### 4.4 Field/Category Abbreviations

| Abbreviation | Full Field | Usage |
|--------------|------------|-------|
| **OT** | Orthogonal Theory / "of type" | Philosophical/theoretical framework, type indicator |
| **FIELDC** | Field of Consciousness / Field of type core | Domain classification, core field type |
| **FIELDM** | Field of type major | Major field classification |
| **Ethosys** | Ethical System | Ethics and safety framework |
| **SAFe** | Scaled Agile Framework | Implementation methodology |
| **PROGL** | Programming Language | Programming language references |
| **meth** | Methodology | Methodology references |
| **SYST** | System of Type | System classification by type |

### 4.5 Naming Convention Constants

| Abbreviation | Full Constant | Value |
|--------------|---------------|-------|
| **CONV_FOR_** | Convention Prefix | Standard prefix for convention constants |
| **CONV_VERSION** | Convention Version | Current convention version |
| **CONV_STATUS** | Convention Status | Current convention status |
| **CONV_DATE** | Convention Date | Date of last update |

### 4.6 Validation Abbreviations

| Abbreviation | Full Term | Range |
|--------------|-----------|-------|
| **CONF** | Confidence Score | 0-100 or 1-5 scale |
| **VAL** | Validation Status | PASS/FAIL/PENDING |
| **QC** | Quality Check | Numeric or categorical |

---

## 5. Naming Conventions

| Pattern | Meaning | Example |
|---------|---------|---------|
| **Lowercase prefixes** | Variable/identifier naming | `fra_id`, `mod_type` |
| **UPPERCASE status** | Document/work status | `DRAFT`, `IN_PROGRESS` |
| **CONV_FOR_* constant** | Convention reference constants | `CONV_FOR_MFW_ABBREVIATIONS` |

---

## 6. Status Workflow

| Status | Meaning | Transition |
|--------|---------|------------|
| **DRAFT** | Initial creation, pending review | → OPEN |
| **OPEN** | Ready for implementation | → IN PROGRESS |
| **IN PROGRESS** | Actively being implemented | → REVIEW or PAUSED |
| **PAUSED** | Temporarily halted | → IN PROGRESS or DONE |
| **REVIEW** | Pending validation | → DONE or IN PROGRESS |
| **DONE** | Complete and validated | → ARCHIVED |
| **ARCHIVED** | Historical reference | - |

---

## 7. Examples

### 7.1 Correct Usage
```
fra_id = "model-framework-001"
tpl_category = "axiom"
con_status = "DRAFT"
val_score = 85
```

### 7.2 Incorrect Usage
```
Fra_id = "model-framework-001"  // Wrong: mixed case prefix
tpl-category = "axiom"          // Wrong: hyphen instead of underscore
status = "draft"                 // Wrong: lowercase status
```

---

## 8. Related Conventions

| Reference | Relationship |
|-----------|--------------|
| [CONV_FOR_MFW_VERSION](./01_convention_for_version.md) | Version management standards |
| [CONV_FOR_MFW_FORMAL_NOTATION](./12_convention_for_formal_notation.md) | Defines variable prefix standards |
| [CONV_FOR_MFW_STATUS](./14_convention_for_stati.md) | Defines status workflow |
| [CONV_FOR_MFW_FILE_NAMING](./10_convention_for_file_naming.md) | File naming conventions |
| [../99_appendix/abbreviations.md](../99_appendix/abbreviations.md) | Quick reference guide |

---

## 9. Implementation

### 9.1 Migration Path
1. Identify all abbreviations in the document
2. Cross-reference with this convention's tables
3. Update incorrect abbreviations to match standards
4. Add missing abbreviations to the quick reference

### 9.2 Validation Checklist
- [ ] All prefixes follow lowercase convention
- [ ] All status abbreviations use UPPERCASE
- [ ] All convention constants use CONV_FOR_ prefix
- [ ] New abbreviations are documented in both files

---

**Rule Steward:** Abbreviation Standards Committee
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-08
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V1.0.1
**Date:** 2026-01-23

## Changelog

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.1 | 2026-01-23 | Updated title formatting, metadata headers, and consolidated header structure per RULE_FOR_MFW_TITLE_FORMAT. Standardized tag to MFW. | Framework Admin | Ensure framework-wide consistency |
| V0.1.2 | 2026-01-08 | Added FIELDC (Field of type core), FIELDM (Field of type major) | Framework Steward | Expansion |
| V0.1.1 | 2026-01-08 | Added PROGL, meth, SYST abbreviations; OT updated with "of type" | Framework Steward | Refinement |
| V0.1.0 | 2026-01-08 | Initial creation | AI Framework Steward | Establish foundation |
