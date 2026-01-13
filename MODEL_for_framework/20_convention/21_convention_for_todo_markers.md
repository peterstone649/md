# Convention for Todo Markers [CONVENTION_MFW_TODO_MARKERS] [PRIO: MEDIUM]

**Convention ID:** CONVENTION_TODO_MARKERS
**Priority:** MEDIUM
**Applies to:** All task files and project documentation

---

## Convention Statement

**All task files and project documentation should use standardized todo markers for progress tracking and project management.**

---

## Rationale

Standardized todo markers provide:
- Consistent progress tracking across all framework components
- Clear visual indicators of completion status
- Systematic project management methodology
- Enhanced collaboration and accountability
- Measurable progress reporting capabilities

---

## Todo Marker Standards

### Basic Format
All task files consistently use:

- `- [ ]` for **incomplete tasks** (unchecked)
- `- [x]` for **completed tasks** (checked)
- Clear, actionable descriptions
- Organized by phases/sections
- Measurable outcomes where applicable

### Syntax Rules

#### Unchecked Tasks
```markdown
- [ ] Task description with clear, actionable language
- [ ] Implement user authentication system
- [ ] Create database schema for user management
```

#### Checked Tasks
```markdown
- [x] Task description (completed)
- [x] Implement user authentication system
- [x] Create database schema for user management
```

#### Nested Tasks
```markdown
- [ ] Main task category
  - [ ] Subtask 1
  - [x] Subtask 2 (completed)
  - [ ] Subtask 3
```

---

## Implementation Guidelines

### File Naming Convention
Task files MUST follow the naming pattern:
```
task_for_[description].md
```
Examples:
- `task_for_vms_implementation.md`
- `task_for_physical_preservation.md`
- `task_for_user_authentication.md`

### File Structure
Task files MUST include:

1. **Header Section**
   - Clear title describing the task scope
   - Overview of objectives and deliverables
   - Timeline and milestones (when applicable)

2. **Task Organization**
   - Logical grouping by phases, components, or priorities
   - Hierarchical structure for complex tasks
   - Dependencies clearly identified

3. **Progress Tracking**
   - Regular updates to completion status
   - Comments on blockers or challenges
   - Updated completion dates

4. **Metadata Section**
   - Responsible stakeholders
   - Success criteria
   - Resource requirements
   - Risk assessments

### Content Standards

#### Task Descriptions
- **Action-oriented**: Start with verbs (Implement, Create, Test, etc.)
- **Specific**: Clearly define what needs to be done
- **Measurable**: Include criteria for completion where possible
- **Realistic**: Achievable within defined scope and resources

#### Examples of Good Task Descriptions
```markdown
- [ ] Implement OAuth 2.0 authentication flow with JWT tokens
- [ ] Create REST API endpoints for user profile management
- [ ] Write unit tests with >90% code coverage for authentication module
- [ ] Conduct security audit and penetration testing
```

#### Examples of Poor Task Descriptions
```markdown
- [ ] Work on authentication (too vague)
- [ ] Fix bugs (not specific enough)
- [ ] Make it better (subjective, not measurable)
```

---

## Task Organization Patterns

### Phase-Based Organization
```markdown
## Phase 1: Foundation (Weeks 1-4)
- [ ] Complete requirement analysis
- [ ] Design system architecture
- [ ] Set up development environment

## Phase 2: Implementation (Weeks 5-8)
- [ ] Develop core functionality
- [ ] Implement user interface
- [ ] Create database schema
```

### Component-Based Organization
```markdown
## Authentication Module
- [ ] Implement login/logout functionality
- [ ] Add password reset feature
- [ ] Integrate social login providers

## User Management Module
- [ ] Create user profile system
- [ ] Implement role-based permissions
- [ ] Add user administration interface
```

### Priority-Based Organization
```markdown
## High Priority (Must Complete)
- [ ] Critical security fixes
- [ ] Core functionality implementation

## Medium Priority (Should Complete)
- [ ] Performance optimizations
- [ ] Additional features

## Low Priority (Nice to Have)
- [ ] UI enhancements
- [ ] Advanced reporting features
```

---

## Progress Tracking Guidelines

### Update Frequency
- **Daily**: For active development tasks
- **Weekly**: For long-term planning tasks
- **Immediate**: When blockers are identified or resolved

### Status Updates
When updating task status:
1. Change `- [ ]` to `- [x]` for completed tasks
2. Add completion date in parentheses when applicable
3. Note any deviations from original plan
4. Update dependent tasks as needed

### Example Progress Update
```markdown
## Before
- [ ] Implement user authentication system
- [ ] Create database schema for user management

## After
- [x] Implement user authentication system (2026-01-13)
- [ ] Create database schema for user management
```

---

## Quality Assurance

### Validation Checklist
- [ ] All tasks use correct marker syntax (`- [ ]` or `- [x]`)
- [ ] Task descriptions are clear and actionable
- [ ] Tasks are organized logically by category/phase
- [ ] Completion criteria are defined where applicable
- [ ] File follows naming convention (`task_for_*.md`)

### Review Process
- **Self-Review**: Author validates task file before sharing
- **Peer Review**: Team member reviews for clarity and completeness
- **Stakeholder Review**: Relevant stakeholders approve task scope
- **Regular Audits**: Periodic review of task file maintenance

---

## Integration with Framework Tools

### Git Integration
Task files should be committed with meaningful messages:
```bash
git commit -m "Update VMS implementation tasks

- [x] Complete definition layer implementation
- [ ] Begin priority framework development
- [ ] Update timeline for Phase 2"
```

### Progress Reporting
Task completion status feeds into:
- Sprint planning and retrospectives
- Stakeholder communications
- Project dashboards and metrics
- Risk assessment and mitigation planning

---

## Exceptions and Special Cases

### Conditional Tasks
For tasks that depend on external factors:
```markdown
- [ ] Deploy to production (pending security audit completion)
- [ ] Implement advanced features (requires stakeholder approval)
```

### Blocked Tasks
For tasks waiting on dependencies:
```markdown
- [ ] Integrate with external API (BLOCKED: waiting for API documentation)
- [ ] Performance testing (BLOCKED: development environment setup)
```

### Deferred Tasks
For tasks moved to future scope:
```markdown
- [ ] Implement advanced analytics (DEFERRED: Phase 2)
- [ ] Mobile app development (DEFERRED: Post-MVP)
```

---

## Training and Adoption

### New Team Member Onboarding
- Review this convention during onboarding
- Provide examples of well-structured task files
- Demonstrate progress tracking workflows

### Continuous Improvement
- Regular review of task file effectiveness
- Updates to convention based on team feedback
- Sharing of best practices across projects

---

## References

- [CONVENTION_FILE_NAMING](../20_convention/10_convention_for_file_naming.md)
- [CONVENTION_WRITING_STYLE](../20_convention/03_convention_for_writing_style.md)
- [RULE_VERSION_CHANGELOG](../12_rule/04_rule_for_version_changelog_update.md)

---

## Changelog

| Version | Date | Changes | Stakeholder | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.0 | 2026-01-13 | Initial convention for standardized todo markers | Framework Steward | Establish consistent task tracking methodology across all framework projects |

---

**Convention Steward:** Framework Management Committee
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-13
**Review Cycle:** Annual
