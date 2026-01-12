# [NUMBER]. Template for Task **[TASK_TEMPLATE]** **[PRIO: [LEVEL]]**

**Version: V0.1** **Date: 2026-01-08**

---

## Task Template Structure

### Core Template Elements:
1. **Title with Reference**: `# Task: [TASK_NAME]` **[TASK_REFERENCE]** **[PRIO: [LEVEL]]**
2. **Version Block**: `**Version: V<Version>**` `**Date: YYYY-MM-DD**`
3. **Focus Statement**: Brief description of task focus
4. **Problems/Issues Section**: Numbered list of problems found
5. **Fix Plan Section**: Checkbox list of action items
6. **Status Section**: Task status tracking
7. **Metadata**: AI model used, timestamps

---

## Task Template Fields:
- **Version Format**: Use semantic versioning (MAJOR.MINOR.PATCH)
| Field | Format | Example |
|-------|--------|---------|
| **Task Reference** | UPPER_CASE_WITH_UNDERSCORES | TASK_FIX_PROBLEMS |
| **Priority Level** | HIGHEST/HIGH/MEDIUM/LOW | HIGH |
| **Version** | V<MAJOR>.<MINOR>.<PATCH> | V0.1.0 |
| **Focus** | Brief description | "Fix structural problems in MODEL_for_framework" |

---

## Template Structure:

```markdown
# Task: [TASK_NAME] **[TASK_REFERENCE]** **[PRIO: PRIORITY_LEVEL]**

**Version: V<Version>** **Date: YYYY-MM-DD**

**Focus:** [BRIEF_DESCRIPTION_OF_TASK_FOCUS]

---

## [PROBLEMS_FOUND/ISSUES/AREAS_COVERED]:

### [NUMBER]. **[PROBLEM_TITLE]**
- **File:** [FILE_PATH]
- **Issue:** [DESCRIPTION_OF_ISSUE]
- **Impact:** [EFFECT_ON_FRAMEWORK]
- **Line/Location:** [OPTIONAL_SPECIFIC_LOCATION]

### [NUMBER]. **[PROBLEM_TITLE]**
- **File:** [FILE_PATH]
- **Issue:** [DESCRIPTION_OF_ISSUE]
- **Impact:** [EFFECT_ON_FRAMEWORK]
- **Line/Location:** [OPTIONAL_SPECIFIC_LOCATION]

---

## [FIX_PLAN/ACTION_ITEMS/SOLUTION]:

- [ ] **[TASK_ITEM_1]** - [DESCRIPTION]
- [ ] **[TASK_ITEM_2]** - [DESCRIPTION]
- [ ] **[TASK_ITEM_3]** - [DESCRIPTION]
- [ ] **[TASK_ITEM_N]** - [DESCRIPTION]

---

## Status: [STATUS]
**Started:** YYYY-MM-DD [TIME]h
**Completed:** YYYY-MM-DD [TIME]h OR -

**AI Model used**: [MODEL_NAME]

---

## Additional Sections (Optional):

### **Validation Criteria**
- [ ] [CRITERION_1]
- [ ] [CRITERION_2]

### **Dependencies**
- [RELATED_TASK_FILE_1]
- [RELATED_DOCUMENT_2]

### **Notes**
- [NOTE_1]
- [NOTE_2]

### **Related Files**
- [FILE_1]
- [FILE_2]
```

---

## Task Naming Convention:
- Use format: `task_for_[ACTION]_[TARGET].md`
- Examples:
  - `task_for_fixing_problems_V0.1.0.md`
  - `task_for_validation_of_theorem.md`
  - `task_for_refactoring_documents.md`
  - `task_for_quality_assessment.md`

---

## Version Requirements:
- Follow version convention: [`01_convention_for_version.md`](../20_convention/01_convention_for_version.md)

## Priority Levels:
- **CRITICAL**: Immediate action required, blocks other work
- **HIGH**: Important issues affecting framework integrity
- **MEDIUM**: Improvement opportunities, moderate impact
- **LOW**: Minor enhancements, nice-to-have improvements

---

## Task Status Workflow:
Follow status convention: [`14_convention_for_stati.md`](../20_convention/14_convention_for_stati.md)

1. **DRAFT** - Initial creation, pending review
2. **OPEN** - Ready to be picked up
3. **IN PROGRESS** - Currently being worked on
4. **PAUSED** - Temporarily halted
5. **REVIEW** - Pending validation
6. **DONE** - All action items completed
7. **ARCHIVED** - Historical reference

---

## Common Task Categories:

### **Problem Fixing Tasks**
```
Focus: Identify and resolve issues in framework
Sections: Problems Found → Fix Plan → Status
```

### **Validation Tasks**
```
Focus: Verify framework components meet standards
Sections: Validation Criteria → Findings → Recommendations
```

### **Improvement Tasks**
```
Focus: Enhance existing framework components
Sections: Current State → Desired State → Implementation Plan
```

### **Creation Tasks**
```
Focus: Develop new framework components
Sections: Requirements → Design → Implementation Steps
```

---

*This task template ensures consistent documentation of work items, problems, and improvements across the MODEL_for_framework.*
