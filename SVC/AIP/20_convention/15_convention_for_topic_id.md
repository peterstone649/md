# 15. Convention for Analysis Document IDs **[CONV_FOR_SVC_AIP_ANALYSIS_IDS]** **[PRIO: MEDIUM]**

**Purpose:** Standardize identification format for analysis documents in the SVC/AIP framework.

---

## Flexible ID Format for SVC/AIP Documents

### General Format Pattern
```
[DOCUMENT_TYPE]_[FRAMEWORK]_[TOPIC]_[SEQUENTIAL_NUMBER]
```

### Analysis-Specific Format
```
ANALYSIS_VMS_[TOPIC]_[SEQUENTIAL_NUMBER]
```

### Format Components

| Component | Description | Example | Flexibility |
|-----------|-------------|---------|-------------|
| **[DOCUMENT_TYPE]** | Document type identifier | `ANALYSIS`, `TASK`, `VALUE`, `PRIORITY` | Flexible - can be any document type |
| **[FRAMEWORK]** | Framework identifier | `VMS`, `SVC`, `AIP` | Flexible - can specify different frameworks |
| **[TOPIC]** | Subject matter (underscore-separated) | `THREE_PILLAR`, `COMPARATIVE`, `SAFE_PROGRESS` | Flexible - descriptive topic identifier |
| **[SEQUENTIAL_NUMBER]** | Unique identifier within topic | `001`, `002`, `003` | Sequential numbering per topic |

### Complete Examples

| Analysis Document | Analysis ID |
|-------------------|-------------|
| `analysis_vms_vs_general_layered_architectures.md` | `ANALYSIS_VMS_COMPARATIVE_001` |
| `analysis_3_pillar_flourishing_approach.md` | `ANALYSIS_VMS_THREE_PILLAR_001` |
| `analysis_substrate_rebellion_risks.md` | `ANALYSIS_VMS_SUBSTRATE_REBELLION_001` |

---

## Usage Guidelines

### When to Use
- All analysis documents in the VMS framework
- Comparative evaluations and assessments
- Research findings and recommendations
- Alternative approach explorations

### ID Assignment Rules
1. **ANALYSIS prefix**: Always starts with `ANALYSIS`
2. **VMS identifier**: Always includes `_VMS_` after ANALYSIS
3. **Topic description**: Use concise, descriptive terms separated by underscores
4. **Sequential numbering**: Start with `001` for each topic, increment as needed

### Topic Naming Conventions
- Use **descriptive nouns** that clearly identify the analysis subject
- **Avoid verbs** in topic names (use nouns like `COMPARATIVE`, `THREE_PILLAR`)
- **Keep concise** while being specific enough for identification
- **Use underscores** to separate multi-word concepts

---

## Implementation Examples

### Correct Usage
```markdown
**Analysis ID:** ANALYSIS_VMS_COMPARATIVE_001
**Title:** What Separates VMS from General Layered Value Architectures

**Analysis ID:** ANALYSIS_VMS_THREE_PILLAR_001
**Title:** Simplified Flourishing Framework with Three Core Pillars
```

### Incorrect Usage
```markdown
**Analysis ID:** VMS_THREE_PILLAR_ANALYSIS_001  # Wrong order
**Analysis ID:** ANALYSIS_COMPARATIVE_VMS_001   # VMS not in right position
**Analysis ID:** ANALYSIS_VMS_001               # Missing topic
```

---

## Integration with File Naming

### Consistent Naming Pattern
Analysis documents should follow this parallel structure:

| Component | ID Format | Filename Format |
|-----------|-----------|-----------------|
| Type | `ANALYSIS` | `analysis` |
| Framework | `_VMS_` | (implied in path) |
| Topic | `[TOPIC]` | `[topic]` |
| Number | `_[NUMBER]` | (sequential) |

### Complete Correspondence
```
ID: ANALYSIS_VMS_COMPARATIVE_001
File: analysis_vms_vs_general_layered_architectures.md

ID: ANALYSIS_VMS_THREE_PILLAR_001
File: analysis_3_pillar_flourishing_approach.md
```

---

## Validation Checklist

- [ ] ID starts with `ANALYSIS_VMS_`
- [ ] Topic uses descriptive nouns separated by underscores
- [ ] Sequential number follows `001` format
- [ ] No verbs in topic description
- [ ] Topic is concise yet specific
- [ ] ID matches filename pattern

---

## Related Conventions

| Convention | Relationship |
|------------|--------------|
| [14_convention_for_stati.md](./14_convention_for_stati.md) | Status values for analysis documents |
| [10_convention_for_file_naming.md](./10_convention_for_file_naming.md) | Filename patterns for analysis documents |
| [01_convention_for_version.md](./01_convention_for_version.md) | Versioning for analysis documents |

---

## Changelog

| Version | Date | Changes | Stakeholder | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | 2026-01-14 | Initial analysis ID convention | Framework Steward | Standardize identification format for VMS analysis documents |
