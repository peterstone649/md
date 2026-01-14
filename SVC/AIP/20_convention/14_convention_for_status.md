# 14. Convention for Status Stati **[CONV_FOR_SVC_AIP_STATUS_CONVENTION]** **[PRIO: HIGH]**

**Version:** V0.1.0 **Status:** ACTIVE **Date:** 2026-01-14

**Purpose:** Standardize status terminology across all SVC/AIP documents and tasks.

---

## Standard Status Stati

| Status | Meaning | Usage |
|--------|---------|-------|
| **OPEN** | Task/work item has been identified, not yet started | Ready to be picked up, initial state for new tasks |
| **IN PROGRESS** | Active work is being conducted | Currently being worked on, has recent activity |
| **PAUSED** | Work temporarily halted, may resume | Blocked by dependency or waiting for external input |
| **REVIEW** | Work complete, pending validation/approval | Awaiting feedback or quality assurance |
| **APPROVED** | Work reviewed and approved, ready for completion | Passed validation, ready for final implementation |
| **DONE** | All work complete and validated | Final state - fully completed and deployed |
| **ACTIVE** | Document/component is currently in use | Operational state for conventions, templates, principles |
| **ARCHIVED** | Historical reference, no longer active | Old completed items retained for reference |

---

## Status Workflow

```
OPEN → IN PROGRESS → REVIEW → APPROVED → DONE
                    ↘ PAUSED ↗
                    ↘ ARCHIVED
```

---

## Usage Guidelines

### When to Use Each Status:

**OPEN:**
- Task just created or identified
- Not yet assigned or started
- Waiting for resources or prioritization
- Planning phase for new initiatives

**IN PROGRESS:**
- Actively being worked on
- Has recent commits, updates, or activity
- Development, implementation, or execution underway
- Regular progress updates expected

**PAUSED:**
- Temporarily halted due to dependencies
- Waiting for external input or decisions
- Resource constraints or reprioritization
- Can be resumed when conditions are met

**REVIEW:**
- Work complete from implementer's perspective
- Awaiting validation, testing, or approval
- Quality assurance or stakeholder feedback pending
- Ready for evaluation but not yet approved

**APPROVED:**
- Work reviewed and approved by stakeholders
- Passed all validation and quality checks
- Ready for final implementation or deployment
- Authorized for production use

**DONE:**
- All requirements met and validated
- Successfully implemented and operational
- No remaining action items or follow-up needed
- Ready for monitoring and maintenance

**ACTIVE:**
- Document or component currently in active use
- Referenced and applied in current work
- Maintained and updated as needed
- Primary version for new implementations

**ARCHIVED:**
- Historical record retained for reference
- No longer the active or current version
- Completed work from previous phases
- Maintained for audit trails and lessons learned

---

## Status Format in Documents

### For Task Files:
```
**Task ID:** TASK_[ID]
**Title:** [Task Title]
**Priority:** [Priority Level]
**Status:** [STATUS]
**Assignee:** [Person/Role]
**Due Date:** YYYY-MM-DD
```

### For Template Files:
```
**Template Version:** V[major].[minor].[patch] **Template Status:** [STATUS] **Date:** YYYY-MM-DD
```

### For Convention Files:
```
**Version:** V[major].[minor].[patch] **Status:** [STATUS] **Date:** YYYY-MM-DD
```

### For Project Management:
```
| Component | Status | Owner | Due Date |
|-----------|--------|-------|----------|
| [Name] | OPEN | [Person] | YYYY-MM-DD |
```

---

## Status Transition Rules

1. **OPEN → IN PROGRESS**: When work begins and active development starts
2. **IN PROGRESS → PAUSED**: When work halts due to external factors
3. **IN PROGRESS → REVIEW**: When implementation work is complete
4. **PAUSED → IN PROGRESS**: When blocking factors are resolved
5. **PAUSED → ARCHIVED**: When work is abandoned or deprioritized indefinitely
6. **REVIEW → APPROVED**: When validation and approval are complete
7. **REVIEW → IN PROGRESS**: When feedback requires additional work
8. **APPROVED → DONE**: When approved work is successfully deployed
9. **APPROVED → IN PROGRESS**: When approved work needs further refinement
10. **DONE → ARCHIVED**: After 30 days of stable operation (for tasks)
11. **ACTIVE → ARCHIVED**: When document/component is superseded

---

## Document Type Status Guidelines

### Task Documents
- Start as **OPEN** when created
- Move to **IN PROGRESS** when work begins
- **REVIEW** when implementation complete
- **APPROVED** when validated
- **DONE** when deployed and operational
- **ARCHIVED** after 30 days of completion

### Template Documents
- Use **ACTIVE** for current templates in use
- **APPROVED** for reviewed templates ready for use
- **ARCHIVED** for superseded template versions

### Convention Documents
- **ACTIVE** for current conventions being followed
- **APPROVED** for reviewed conventions ready for adoption
- **ARCHIVED** for superseded convention versions

### Implementation Documents
- **OPEN** for planned implementations
- **IN PROGRESS** during development
- **REVIEW** when implementation complete
- **APPROVED** when tested and validated
- **DONE** when successfully deployed
- **ACTIVE** for operational systems

---

## Status Validation Checklist

- [ ] Status matches current state of work/document
- [ ] Status transitions follow defined workflow rules
- [ ] Status is appropriate for document type (task/template/convention)
- [ ] Status is updated when state changes occur
- [ ] Status is clearly visible in document header
- [ ] Status changes are documented in changelog when applicable

---

## Common Status Mistakes to Avoid

### Incorrect Transitions
- Skipping **REVIEW** phase for critical work
- Moving directly from **OPEN** to **DONE**
- Using **PAUSED** for work that should be **ARCHIVED**

### Status Misuse
- Using **IN PROGRESS** for work not actively being done
- Keeping items in **REVIEW** indefinitely
- Using **DONE** before validation is complete

### Documentation Issues
- Not updating status when work state changes
- Inconsistent status format across similar documents
- Missing status in document headers

---

## Integration with Other Conventions

| Related Convention | Relationship |
|-------------------|--------------|
| [Version Convention](./01_convention_for_version.md) | Status often aligns with version progression |
| [File Naming Convention](./10_convention_for_file_naming.md) | Status may influence naming conventions |
| [Task Management Convention](./15_convention_for_task_management.md) | Defines task status workflow |

---

## Changelog

| Version | Date | Changes | Stakeholder | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.0 | 2026-01-14 | Initial status convention for SVC/AIP framework | Framework Steward | Establish standardized status terminology across all SVC/AIP documents and tasks |
