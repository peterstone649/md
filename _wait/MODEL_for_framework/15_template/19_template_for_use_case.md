# Template for Use Case [TPL_FOR_MFW_USE_CASE] **[PRIO: HIGH]**

**Version: V[VERSION]** **Status: [STATUS]** **Date: YYYY-MM-DD**

## Use Case Overview

**Use Case Name:** [USE_CASE_NAME]
**Use Case ID:** [UC-XXX]
**Primary Actor:** [PRIMARY_ACTOR]
**Secondary Actors:** [SECONDARY_ACTORS]
**Preconditions:** [PRECONDITIONS]
**Postconditions:** [POSTCONDITIONS]
**Priority:** [PRIORITY_LEVEL]
**Complexity:** [COMPLEXITY_LEVEL]

## Description

**Brief Description:**
[Provide a concise description of what this use case accomplishes and its business value]

**Detailed Description:**
[Provide a detailed explanation of the use case, including the business context and objectives]

## Flow of Events

### Main Success Scenario (Basic Flow)

1. **[Actor Action 1]** - [Description of first actor action]
2. **[System Response 1]** - [Description of system response]
3. **[Actor Action 2]** - [Description of second actor action]
4. **[System Response 2]** - [Description of system response]
5. **[Actor Action 3]** - [Description of third actor action]
6. **[System Response 3]** - [Description of system response]
7. **[Actor Action 4]** - [Description of fourth actor action]
8. **[System Response 4]** - [Description of system response]
9. **[Actor Action 5]** - [Description of fifth actor action]
10. **[System Response 5]** - [Description of system response]

### Alternative Flows

#### Alternative Flow A: [DESCRIPTION_OF_ALTERNATIVE_A]
- **Trigger:** [When this alternative flow is triggered]
- **Steps:**
  1. [Alternative step 1]
  2. [Alternative step 2]
  3. [Return to main flow at step X]

#### Alternative Flow B: [DESCRIPTION_OF_ALTERNATIVE_B]
- **Trigger:** [When this alternative flow is triggered]
- **Steps:**
  1. [Alternative step 1]
  2. [Alternative step 2]
  3. [Alternative step 3]
  4. [Return to main flow at step X]

### Exception Flows

#### Exception Flow E1: [DESCRIPTION_OF_EXCEPTION_1]
- **Trigger:** [When this exception occurs]
- **Steps:**
  1. [Exception handling step 1]
  2. [Exception handling step 2]
  3. [Recovery or termination action]

#### Exception Flow E2: [DESCRIPTION_OF_EXCEPTION_2]
- **Trigger:** [When this exception occurs]
- **Steps:**
  1. [Exception handling step 1]
  2. [Exception handling step 2]
  3. [Recovery or termination action]

## Business Rules

### Preconditions
- [Business rule 1]
- [Business rule 2]
- [Business rule 3]

### Postconditions
- [Business rule 1]
- [Business rule 2]
- [Business rule 3]

### Invariants
- [Invariant 1]
- [Invariant 2]
- [Invariant 3]

## Requirements Traceability

### Functional Requirements
- **FR-XXX:** [Description of functional requirement]
- **FR-XXX:** [Description of functional requirement]
- **FR-XXX:** [Description of functional requirement]

### Non-Functional Requirements
- **NFR-XXX:** [Description of non-functional requirement]
- **NFR-XXX:** [Description of non-functional requirement]
- **NFR-XXX:** [Description of non-functional requirement]

## Use Case Relationships

### Includes
- [Use case that this use case includes]

### Extends
- [Use case that extends this use case]

### Generalizations
- [Parent use case if this is a specialization]

### Dependencies
- [Related use cases that must be completed first]

## Data Requirements

### Input Data
- **[Field Name 1]:** [Description and validation rules]
- **[Field Name 2]:** [Description and validation rules]
- **[Field Name 3]:** [Description and validation rules]

### Output Data
- **[Output Name 1]:** [Description and format]
- **[Output Name 2]:** [Description and format]
- **[Output Name 3]:** [Description and format]

## User Interface Requirements

### Screen Mockups
[Include references to or descriptions of required user interface elements]

### Navigation Flow
[Describe how users navigate through the use case]

## Performance Requirements

- **Response Time:** [Maximum acceptable response time]
- **Throughput:** [Expected number of transactions per time period]
- **Concurrency:** [Number of users that can perform this use case simultaneously]

## Security Requirements

- **Authentication:** [Authentication requirements]
- **Authorization:** [Authorization requirements]
- **Data Protection:** [Data protection and privacy requirements]
- **Audit Trail:** [Audit requirements]

## Testing Requirements

### Test Scenarios
1. **[Test Scenario 1]** - [Description of test scenario]
2. **[Test Scenario 2]** - [Description of test scenario]
3. **[Test Scenario 3]** - [Description of test scenario]

### Success Criteria
- [Success criterion 1]
- [Success criterion 2]
- [Success criterion 3]

## Assumptions

- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Open Issues

- [Issue 1]
- [Issue 2]
- [Issue 3]

## Related Documents
- **Rule:** [Changelog Update Rule](../../12_rule/04_rule_for_version_changelog_update.md)
- **Principle:** [PRIN_...](./path/to/principle.md)
- **Tool:** [tool_name.py](../path/to/tool.py)
- **Requirements:** [Requirements document reference]
- **Design:** [Design document reference]

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
| V1.0.0 | YYYY-MM-DD | Initial creation | [Stakeholder] | [Initial rationale] |