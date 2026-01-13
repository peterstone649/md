# 1. Convention for version (CONV_FOR_MODELFW_VERSION) [PRIO: HIGH]
>
**Version:** V1.0.0 **Status:** APPROVED **Date:** 2026-01-09
**Integration Field:** MODEL_for_framework_ecosystem

## Derivation Source

Based on `.\SWmeth\20_convention\convention_for_version.md`
Based on `..\20_convention\*.md'

## Core Inheritance

- Inherits fundamental versioning principles from SWmeth framework
- Adapts semantic versioning for framework methodology criticality
- Extends version tracking for methodology verification requirements
- Maintains compatibility with document methodology foundations

## Rationale

Standardized versioning practices are essential for maintaining consistency, safety, and maintainability across the framework. This convention establishes:
- Automated verification support through consistent version formats
- Audit trails via comprehensive version tracking
- Compatibility checking between framework components
- Incremental improvement management
- Clear migration paths for breaking changes

## General Reference

This convention applies to all documents within the frameworks including conventions, templates, axioms, strategies, and tasks. All documents must follow these versioning practices to ensure systematic evolution and traceability.

---

## Abstract

This convention establishes standardized versioning practices for the frameworks. It defines version number formats, semantic versioning guidelines, version documentation requirements, and change management procedures. The goal is to ensure consistency, traceability, and compatibility across all framework components throughout their lifecycle.

---

## 1. Scope and Applicability

### 1.1 When to Apply
This convention should be applied when:
- Creating new framework documents (conventions, templates, axioms, strategies, tasks)
- Updating existing documents with changes
- Tracking document evolution over time
- Managing compatibility between frameworks and framework components 
- Planning migration paths for breaking changes

### 1.2 Target Audience
- Framework developers and maintainers
- Document authors and contributors
- System architects managing component compatibility
- Quality assurance teams

---

## 2. Core Definitions

| Element | Definition | Example |
|---------|------------|---------|
| **Version Number** | Unique identifier for document state | `V0.1.2` |
| **MAJOR Version** | First number indicating breaking changes | `1.x.x` |
| **MINOR Version** | Second number indicating new features | `x.1.x` |
| **PATCH Version** | Third number indicating bug fixes | `x.x.2` |
| **Changelog** | Documented history of version changes | See Section 10 |
| **Compatibility** | Degree of interoperability between versions | Full/Partial/None |

---

## 3. Version Requirements

### 3.1 Version Number
- **Requirement**: Every document must include a version number
- **Format**: Semantic versioning (MAJOR.MINOR.PATCH) with V prefix
- **Examples**: `V0.1.0`, `V1.0.0`, `V2.3.1`
- **Location**: Prominently displayed at the top of the document header
- **Tracking**: Document all changes between versions with rationale
- **Compatibility**: Specify which framework versions the document supports

### 3.2 Semantic Versioning Guidelines
| Version Type | Meaning | Description | Impact |
|--------------|---------|-------------|--------|
| **MAJOR** | Breaking Changes | Changes not backward compatible | Requires migration |
| **MINOR** | New Features | Backward-compatible additions | Optional upgrade |
| **PATCH** | Bug Fixes | Backward-compatible corrections | Recommended upgrade |

### 3.3 Version Number Progression
| Current Version | Next MAJOR | Next MINOR | Next PATCH |
|-----------------|------------|------------|------------|
| V0.1.0 | V1.0.0 | V0.2.0 | V0.1.1 |
| V1.2.3 | V2.0.0 | V1.3.0 | V1.2.4 |

### 3.4 Version Format Variations
| Format | Usage | Example |
|--------|-------|---------|
| **V{major}.{minor}.{patch}** | Standard version | `V1.2.3` |
| **{major}.{minor}** | Abbreviated (stable only) | `1.2` |
| **v{major}.{minor}.{patch}** | Lowercase variant | `v1.2.3` |

---

## 4. Version Documentation

### 4.1 Changelog Requirements
All documents must include a changelog with the following columns:
| Column | Description |
|--------|-------------|
| **Version** | Version number of the change |
| **Date** | Date of the change (YYYY-MM-DD) |
| **Changes** | Description of what changed |
| **Stakeholder** | Person or role responsible for the change |
| **Rationale/Motivation** | Why the change was made |

### 4.2 Changelog Entry Guidelines
- Include version history in changelog format
- Document breaking changes and migration paths
- Specify minimum framework version requirements
- Track deprecation notices for older versions
- Reference related issues or discussions when applicable
- **Stakeholder**: Document the person or role responsible for the change (e.g., "AI Framework Steward", "Quality Review Team")
- **Rationale/Motivation**: Explain why the change was made (e.g., "Enhanced accountability tracking based on stakeholder feedback")
- **Traceability**: Each version entry should link to a documented decision or request when applicable

### 4.3 Breaking Changes Documentation
When documenting breaking changes, include:
1. Description of what changed
2. Reason for the change
3. Migration steps for affected users
4. Timeline for deprecation (if applicable)

### 4.4 Version Deprecation
| Status | Meaning | Action |
|--------|---------|--------|
| **ACTIVE** | Current version, fully supported | Use this version |
| **DEPRECATED** | Scheduled for removal | Plan migration |
| **OBSOLETE** | No longer supported | Upgrade required |

---

## 5. Naming Conventions

| Pattern | Meaning | Example |
|---------|---------|---------|
| **V{major}.{minor}.{patch}** | Full version | `V1.2.3` |
| **V{major}.{minor}** | Major.Minor only | `V1.2` |

## 6. Rules and Guidelines

### 6.1 Version Number Rules
- **Rule 1**: All documents must include a version number in the header
- **Rule 2**: Version numbers must follow semantic versioning (MAJOR.MINOR.PATCH)
- **Rule 3**: Version numbers must be prefixed with 'V' (e.g., V1.0.0)
- **Rule 4**: Version numbers must be incremented appropriately for changes
- **Rule 5**: Breaking changes require MAJOR version increment
- **Rule 6**: New features require MINOR version increment
- **Rule 7**: Bug fixes require PATCH version increment
- **Rule 8**: V0.1.0 can NEVER be in APPROVED status - documents must progress to V0.1.1+ (patch versions) or V0.2.0+ (minor versions) before approval

### 6.2 Documentation Guidelines
- **Guideline 1**: Document all version changes in changelog
- **Guideline 2**: Include migration paths for breaking changes
- **Guideline 3**: Specify compatibility requirements clearly
- **Guideline 4**: Reference related documents and their versions
- **Guideline 5**: Use consistent date format (YYYY-MM-DD) in changelogs

### 6.3 Status Transition Guidelines
- **Guideline 6**: Version status must align with document status
- **Guideline 7**: V0.x.x versions should not be used in production
- **Guideline 8**: V1.0.0+ versions indicate stable, released documents
- **Guideline 9**: Deprecation notices must include migration timelines
- **Guideline 10**: Archived documents must maintain version history

---

## 7. Status and States

Version status follows the document status convention defined in [CONV_FOR_STATUS_CONVENTION](./14_convention_for_stati.md):

| Status | Meaning | Version Implication |
|--------|---------|---------------------|
| **DRAFT** | Initial creation | V0.1.0 (or V0.0.1) |
| **OPEN** | Ready for review | V0.x.x |
| **IN PROGRESS** | Active development | V0.x.x |
| **PAUSED** | Temporarily halted | V0.x.x |
| **REVIEW** | Under evaluation | V0.x.x or V1.0.0-RC |
| **APPROVED** | Reviewed and approved | V1.0.0-RC |
| **DONE** | Released | V1.0.0+ |
| **ARCHIVED** | Historical | Any version |

---

## 7. Examples

### 7.1 Changelog Entry Examples
```
| Version | Date | Changes |
|---------|------|---------|
| V1.0.0 | 2026-01-08 | Initial release with full convention set |
| V0.2.0 | 2026-01-07 | Added new field type abbreviations |
| V0.1.1 | 2026-01-06 | Fixed typos in Core Definitions table |
| V0.1.0 | 2026-01-05 | Initial creation |
```

### 7.2 Version Number Progression
```markdown
Initial creation:     V0.1.0
Minor feature add:    V0.2.0
Bug fix:              V0.2.1
Major feature add:    V1.0.0
Bug fix after 1.0:    V1.0.1
Minor feature after:  V1.1.0
Breaking change:      V2.0.0
```

### 7.3 Breaking Change Documentation
```markdown
## Breaking Changes in V2.0.0

### Change: Renamed "FIELDC" to "FIELD_CORE"

**Migration Steps:**
1. Search for all occurrences of "FIELDC"
2. Replace with "FIELDC" (no change) or "FIELDM" for major fields
3. Update any references in code and documentation
4. Run validation scripts to verify compliance

**Timeline:** Effective immediately, V1.x.x supported until 2026-07-01
```

---

## 8. Related Conventions and Documents

| Reference | Relationship |
|-----------|--------------|
| [CONV_FOR_ABBREVIATIONS](./15_convention_for_abbreviations.md) | Uses version conventions |
| [CONV_FOR_STATUS_CONVENTION](./14_convention_for_stati.md) | Document status workflow |
| [CONV_FOR_FILE_NAMING](./10_convention_for_file_naming.md) | File naming with versions |
| [CONV_FOR_FORMAL_NOTATION](./12_convention_for_formal_notation.md) | Version prefix notation |

---

## 9. Implementation Notes

### 9.1 Migration Path
When updating to follow this convention:
1. Assign initial version number (V0.1.0 for new documents)
2. Create changelog section with initial entry
3. Document all existing changes in changelog
4. Update document header with version info
5. Review compatibility with related documents

### 9.2 Tooling Support
- **VS Code**: Search and replace for version updates
- **Git**: Track version changes via commit history
- **Linting**: Validate version format compliance
- **Scripts**: Automated version bump scripts

### 9.3 Validation Checklist
- [ ] Version number follows V{major}.{minor}.{patch} format
- [ ] Changelog exists with at least one entry
- [ ] Changelog columns match required format
- [ ] Breaking changes documented with migration path
- [ ] Document status matches version progression
- [ ] Related documents referenced where applicable

---

## 10. Changelog

| Version | Date | Changes |
|---------|------|---------|
| V0.2.0 | 2026-01-08 | Enhanced with full template structure; added examples and implementation notes |
| V0.1.0 | 2026-01-08 | Initial creation from SWmeth conventions |

---

## 11. Appendices

### Appendix A: Version Format Reference
| Format | Example | Usage |
|--------|---------|-------|
| V{major}.{minor}.{patch} | V1.2.3 | Standard document version |
| v{major}.{minor}.{patch} | v1.2.3 | Alternative case format |
| V{major}.{minor} | V1.2 | Stable major versions only |

### Appendix B: Semantic Versioning Summary
- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Appendix C: Compatibility Matrix
| From \ To | V0.x.x | V1.0.0 | V2.0.0 |
|-----------|--------|--------|--------|
| V0.x.x | Compatible | Review | Migrate |
| V1.0.0 | Review | Compatible | Migrate |
| V2.0.0 | Migrate | Migrate | Compatible |

---

**End of Convention**
