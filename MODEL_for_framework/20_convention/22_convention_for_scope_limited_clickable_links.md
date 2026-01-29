# Scope-Limited Clickable Links Convention [CONV_FOR_MFW_SCOPE_LIMITED_LINKS] **[PRIO: HIGH]**

**Version: V1.0.0** **Status: APPROVED** **Date: 2026-01-26**
**Scope:** All framework documentation with clickable links

## Overview

**Scope-Limited Clickable Links Convention** establishes the principle that clickable links within framework documentation should primarily reference documents within the same folder or logical scope, rather than pointing to external locations. This convention enhances documentation coherence, reduces dependency risks, and improves maintainability.

### Core Purpose
- **Scope Coherence** - Maintain logical boundaries between documentation components
- **Dependency Reduction** - Minimize external dependencies that could break
- **Maintainability** - Simplify documentation updates and refactoring
- **Navigation Clarity** - Provide clear scope boundaries for readers

### Convention Characteristics
- **Scope-Aware** - Links respect folder and logical boundaries
- **Framework-Specific** - Tailored for MODEL_for_framework structure
- **Practical Application** - Actionable guidelines for link creation
- **Quality Assurance** - Validation mechanisms for link scope

---

## Core Principles

### Principle 1: Folder-Scoped Links
**Framework Application:** Clickable links should primarily reference documents within the same directory

#### Scope Boundary Rules
1. **Same-Folder Preference** - Links should point to files in the current directory
2. **Logical Scope** - Links within a conceptual unit stay within that unit
3. **Minimal External References** - Avoid links outside the immediate scope

**Framework Example:**
- **Preferred:** `[Related Principle](./02_principle_transparency.md)` (same folder)
- **Avoid:** `[External Reference](../../other_folder/document.md)` (different scope)

#### Scope Definition
- **Folder Scope:** Files within the same directory
- **Logical Scope:** Conceptually related documents
- **Framework Rule:** 80% of links should be within immediate scope

### Principle 2: Relative Path Strategy
**Framework Application:** Use relative paths that maintain scope boundaries

#### Path Construction Rules
1. **Current Directory First** - `./filename.md` for same-folder links
2. **Parent Directory Caution** - `../` only when necessary for scope
3. **Scope Preservation** - Maintain logical grouping in paths

**Examples:**
- **Same Scope:** `[Template](./17_template_for_principle.md)`
- **Parent Scope:** `[Overview](../README.md)` (when truly needed)
- **Avoid:** `[Distant Reference../../../other/section/document.md)`

#### Path Validation
- **Scope Check:** Does the link stay within logical boundaries?
- **Necessity Test:** Is the external reference truly required?
- **Framework Rule:** External links require justification

### Principle 3: Scope Hierarchy
**Framework Application:** Organize links according to documentation hierarchy

#### Hierarchy Levels
1. **Immediate Scope** - Same directory (preferred)
2. **Parent Scope** - Direct parent directory (use sparingly)
3. **Extended Scope** - Grandparent or deeper (avoid when possible)

**Framework Structure:**
```
framework_root/
├── 30_principle/          # Principle scope
│   ├── 01_principle_human_sovereignty.md
│   ├── 02_principle_transparency.md  ← [Transparency](./02_principle_transparency.md)
│   └── README.md
└── 15_template/          # Template scope (different scope)
    ├── 16_template_for_convention.md
    └── 17_template_for_principle.md
```

### Principle 4: Scope Documentation
**Framework Application:** Document the scope boundaries for each section

#### Scope Definition Requirements
- **Scope Statement:** Define the logical boundaries
- **Link Policy:** Specify allowed link destinations
- **Exception Handling:** Document when external links are permitted

**Scope Example:**
```
30_principle/ (Scope: Core Principles)
- Allowed Links: Within 30_principle/ directory
- Parent Links: To 15_template/ only for template references
- External Links: Require approval and justification
```

---

## Framework-Specific Standards

### Documentation Scope Boundaries

#### Principle Documentation
- **Scope:** Within 30_principle/ directory
- **Allowed Links:** Other principles in same directory
- **Parent Links:** Template references only
- **External Links:** Framework overview with justification

#### Template Documentation
- **Scope:** Within 15_template/ directory
- **Allowed Links:** Other templates in same directory
- **Parent Links:** Principle references for examples
- **External Links:** Implementation guides with approval

### Quality Assurance Guidelines

#### Scope Compliance Checklist
- [ ] Links primarily reference same-directory files
- [ ] Relative paths maintain logical scope
- [ ] External links are minimized and justified
- [ ] Scope boundaries are documented

#### Link Validation Process
- [ ] Scope boundary verification
- [ ] Path correctness validation
- [ ] Dependency risk assessment
- [ ] Maintenance impact analysis

---

## Implementation Guidelines

### Application Phases

#### Phase 1: Foundation (Immediate)
- Apply scope-limited links to all new documentation
- Document scope boundaries for each directory
- Establish scope compliance checklist

#### Phase 2: Integration (Week 1-2)
- Review existing links for scope compliance
- Refactor external links to scope-limited alternatives
- Train contributors on scope boundaries

#### Phase 3: Mastery (Month 1-2)
- Scope-limited links become automatic
- Quality assurance integrated into workflow
- Framework-wide scope coherence achieved

### Tools and Resources

#### Link Validation Tools
- **Scope Checker:** Automated verification of link scope
- **Path Analyzer:** Relative path correctness validation
- **Dependency Mapper:** Visualization of link relationships

#### Documentation Templates
- **Scope Definition Template:** Standard format for scope boundaries
- **Link Policy Template:** Framework for link guidelines
- **Exception Justification:** Template for external link approval

---

## Validation and Quality Assurance

### Scope Compliance Metrics
- **Scope Adherence:** Percentage of links within immediate scope
- **Dependency Risk:** Number of external link dependencies
- **Maintainability Score:** Ease of documentation updates
- **Navigation Clarity:** Reader comprehension of scope boundaries

### Review Process
- **Self-Review:** Author verifies scope compliance
- **Peer Review:** Colleague validates link scope
- **Architecture Review:** Framework steward approves scope boundaries
- **Final Validation:** Quality assurance team confirms compliance

### Continuous Monitoring
- **Scope Tracking:** Regular assessment of link compliance
- **Dependency Analysis:** Periodic review of external links
- **Standards Evolution:** Update conventions based on effectiveness

---

## Integration with Framework Components

### Cross-Reference Integration
- **12_rule/:** Scope-limited links complement clickable link rules
- **20_convention/:** Link conventions integrate with writing standards
- **30_terminology/:** Scope terms added to framework terminology
- **15_template/:** Scope templates included in template library

### Field-Specific Applications
- **MODEL_for_framework:** Core framework documentation scope
- **MODEL_for_STKHLD_AI_COLLAB:** Stakeholder-AI collaboration scope
- **FIELDC* directories:** Domain-specific scope boundaries
- **All Components:** Consistent scope-limited linking

---

## Conclusion

**Scope-Limited Clickable Links Convention** transforms framework documentation linking from potentially fragile external dependencies into robust, maintainable, scope-coherent references. By establishing clear scope boundaries and link policies, this convention ensures that framework documentation remains navigable, maintainable, and logically organized.

**Scope-Limited Clickable Links Convention** provides the structural foundation that enables framework documentation to scale effectively while maintaining clarity, coherence, and long-term maintainability.

---

## Key Principles Summary

1. **Scope Coherence:** Links respect folder and logical boundaries
2. **Dependency Reduction:** Minimize external references that could break
3. **Maintainability:** Simplify documentation updates and refactoring
4. **Navigation Clarity:** Provide clear scope boundaries for readers
5. **Framework Integration:** Align with existing documentation standards

---

**"Effective documentation linking begins with clear scope boundaries and ends with maintainable, coherent references."**

**Rule Steward:** Documentation Architecture Team
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-26
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V1.0.0
**Date:** 2026-01-26

## Changelog

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.0 | 2026-01-26 | Initial creation | Framework Documentation Team | Establish scope-limited linking standards |