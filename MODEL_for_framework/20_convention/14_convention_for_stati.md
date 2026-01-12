# 14. Convention for Status Statti **[CONV_FOR_MODELFW_STATUS_CONVENTION]** **[PRIO: HIGH]**

**Version: V0.1.0** **Date: 2026-01-08**

**Purpose:** Standardize status terminology across all framework documents and tasks.

---

## Standard Status Statti

| Status | Meaning | Usage |
|--------|---------|-------|
| **DRAFT** | Initial creation, pending review | Task just created, not yet started |
| **OPEN** | Task/work item has been identified, not yet started | Ready to be picked up |
| **IN PROGRESS** | Active work is being conducted | Currently being worked on |
| **PAUSED** | Work temporarily halted, may resume | Blocked by dependency or waiting |
| **REVIEW** | Work complete, pending validation/approval | Awaiting feedback or approval |
| **APPROVED** | Work reviewed and approved, ready for completion | Passed validation, awaiting finalization |
| **DONE** | All work complete and validated | Final state - fully completed |
| **ARCHIVED** | Historical reference, no longer active | Old completed items |


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
- Task just created
- Not yet assigned
- Waiting for resources
- Planning phase

**IN PROGRESS:**
- Actively being worked on
- Has active development
- Has recent commits/changes

**PAUSED:**
- Blocked by dependency
- Waiting for external input
- Temporarily deprioritized
- Resource constraints

**REVIEW:**
- Work complete
- Awaiting validation
- Pending peer feedback
- Quality check pending

**APPROVED:**
- Work reviewed and approved
- Passed all validation checks
- Ready for final implementation
- Awaiting completion/finalization

**DONE:**
- All requirements met
- Validation passed
- No remaining action items
- Ready for production/use

**ARCHIVED:**
- Historical record
- Reference purposes only
- No further changes expected
- Completed more than 30 days ago

---

## Status Format in Documents

### For Task Files:
```
## Status: [STATUS]
Started: YYYY-MM-DD [TIME]h
Completed: YYYY-MM-DD [TIME]h OR -
```

### For Issue Tracking:
```
**Status:** [STATUS] - [Brief note]
```

### For Project Management:
```
| Component | Status | Owner |
|-----------|--------|-------|
| [Name] | OPEN | [Person] |
```

---

## Status Transition Rules

1. **OPEN → IN PROGRESS**: When work begins
2. **IN PROGRESS → PAUSED**: When work halts temporarily
3. **IN PROGRESS → REVIEW**: When work is complete
4. **PAUSED → IN PROGRESS**: When work resumes
5. **PAUSED → ARCHIVED**: When work is abandoned
6. **REVIEW → APPROVED**: When validation passes and work is approved
7. **REVIEW → IN PROGRESS**: When feedback requires changes
8. **APPROVED → DONE**: When approved work is finalized/completed
9. **APPROVED → IN PROGRESS**: When approved work needs further changes
10. **DONE → ARCHIVED**: After 30 days of stability

---

## Emoji Indicators (Optional)

| Status | Emoji |
|--------|-------|
| OPEN | 📋 |
| IN PROGRESS | 🔄 |
| PAUSED | ⏸️ |
| REVIEW | 👀 |
| APPROVED | 👍 |
| DONE | ✅ |
| ARCHIVED | 📦 |

---

**Convention Reference:** Apply to all task files, issue tracking, and project management documents in MODEL_for_framework.
