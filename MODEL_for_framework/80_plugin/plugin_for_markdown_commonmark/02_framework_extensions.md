# Markdown Extensions [CONVENTION_FOR_MFW_MARKDOWN_EXTENSIONS] **[PRIO: MEDIUM]**

**Version: V1.0.0** **Status: APPROVED** **Date: 2026-02-01**

## Overview

This document defines the framework-specific Markdown extensions that extend beyond the CommonMark specification. All extensions MUST maintain compatibility with CommonMark and provide clear documentation and fallback behavior.

## Extension Guidelines

### 1. Extension Principles
```markdown
Extension Requirements:
├── MUST not conflict with CommonMark core syntax
├── MUST provide clear documentation and examples
├── MUST include fallback behavior for non-supporting parsers
├── MUST maintain semantic equivalence with CommonMark
└── MUST be clearly marked as framework extensions
```

### 2. Extension Categories
```markdown
Extension Types:
├── Semantic Extensions → Enhanced meaning and structure
├── Presentation Extensions → Visual formatting and styling
├── Functional Extensions → Interactive and dynamic content
└── Metadata Extensions → Document and content metadata
```

## Semantic Extensions

### 1. Framework-Specific Headers
```markdown
Enhanced Headers:
# [RULE] Header Title
## [PRINCIPLE] Header Title
### [AXIOM] Header Title
#### [TEMPLATE] Header Title
##### [CONVENTION] Header Title
###### [GUIDELINE] Header Title

Usage:
- Use framework-specific prefixes for semantic meaning
- Maintain standard CommonMark header structure
- Provide clear semantic context for document purpose
```

### 2. Status and Priority Markers
```markdown
Status Indicators:
[STATUS: DRAFT] → Document in development
[STATUS: REVIEW] → Under review
[STATUS: APPROVED] → Approved for use
[STATUS: DEPRECATED] → No longer recommended

Priority Markers:
[PRIORITY: HIGH] → Critical importance
[PRIORITY: MEDIUM] → Moderate importance
[PRIORITY: LOW] → Lower priority
```

### 3. Framework References
```markdown
Reference Syntax:
[FRAMEWORK: MODEL_for_framework] → Reference to framework
[COMPONENT: 20_convention] → Reference to component
[FILE: 01_markdown_convention.md] → Reference to specific file
[SECTION: Core Requirements] → Reference to section

Example:
See [COMPONENT: 20_convention] for more details.
```

## Presentation Extensions

### 1. Enhanced Code Blocks
```markdown
Language-Specific Formatting:
```javascript [EXAMPLE]
// Framework-specific JavaScript example
const config = {
  commonmark: true,
  extensions: ['framework']
};
```

```python [VALIDATION]
# Validation example
def validate_commonmark_compliance(content):
    return commonmark_parser.validate(content)
```

```bash [COMMAND]
# Command example
npm run validate:commonmark
```

Usage:
- Include [EXAMPLE], [VALIDATION], or [COMMAND] tags
- Provide context-specific language examples
- Maintain standard code block structure
```

### 2. Enhanced Tables
```markdown
Extended Table Features:
| Feature | CommonMark | Framework Extension |
|---------|------------|-------------------|
| Basic Tables | ✅ | ✅ |
| Table Headers | ✅ | ✅ |
| Alignment | ✅ | ✅ |
| Row Span | ❌ | ✅ [EXTENSION] |
| Column Span | ❌ | ✅ [EXTENSION] |
| Nested Content | Limited | ✅ [EXTENSION] |

Extended Syntax:
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
| Cell 7   | Cell 8   | Cell 9   |
```

### 3. Enhanced Lists
```markdown
Task Lists with Metadata:
- [x] [CRITICAL] Complete CommonMark validation
- [ ] [HIGH] Implement extension testing
- [ ] [MEDIUM] Update documentation
- [ ] [LOW] Review compatibility

Nested Lists with Extensions:
1. Main Task
   - [ ] Subtask A
   - [ ] Subtask B
     - [ ] Nested subtask
   - [ ] Subtask C

2. Another Task
   - [x] Completed item
   - [ ] Pending item
```

## Functional Extensions

### 1. Interactive Elements
```markdown
Collapsible Sections:
<details>
<summary>Click to expand</summary>

Extended content here.

</details>

Accordion Content:
<details open>
<summary>Always open section</summary>

This content is visible by default.

</details>
```

### 2. Embedded Content
```markdown
Iframe Embedding:
<iframe src="https://example.com" width="100%" height="400"></iframe>

Video Embedding:
<video controls width="100%">
  <source src="video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
```

### 3. Mathematical Expressions
```markdown
LaTeX Math (Extension):
Inline: $E = mc^2$

Block:
$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$

Complex Formula:
$$
f(x) = \int_{-\infty}^{\infty} \hat{f}(\xi) e^{2\pi i \xi x} d\xi
$$
```

## Metadata Extensions

### 1. Document Metadata
```markdown
Front Matter (YAML):
---
title: "Document Title"
version: "1.0.0"
status: "DRAFT"
date: "2026-02-01"
author: "Framework Steward"
tags: ["markdown", "commonmark", "extensions"]
---

Document Properties:
**Framework**: MODEL_for_framework
**Component**: 20_convention
**Created**: 2026-02-01
**Modified**: 2026-02-01
**Version**: 1.0.0
```

### 2. Content Metadata
```markdown
Block Metadata:
> **Note**: This is an important note.
> 
> Additional information can be found in the documentation.

> **Warning**: This is a warning message.
> 
> Proceed with caution when implementing this feature.

> **Tip**: This is a helpful tip.
> 
> Consider this approach for better results.
```

### 3. Code Metadata
```markdown
Code Annotations:
```javascript
// @author Framework Steward
// @version 1.0.0
// @since 2026-02-01
// @description CommonMark validation function
function validateCommonMark(content) {
  // Implementation here
}
```

```python
"""
@file: commonmark_validator.py
@author: Framework Steward
@version: 1.0.0
@since: 2026-02-01
@description: CommonMark validation utilities
"""
```

## Extension Validation

### 1. Compatibility Testing
```markdown
Validation Requirements:
├── CommonMark core syntax MUST remain unchanged
├── Extensions MUST not break existing CommonMark content
├── Fallback behavior MUST be documented
├── Cross-parser compatibility MUST be verified
└── Semantic correctness MUST be maintained
```

### 2. Testing Framework
```markdown
Test Categories:
├── Core CommonMark compliance tests
├── Extension functionality tests
├── Fallback behavior tests
├── Cross-parser compatibility tests
└── Semantic correctness tests
```

### 3. Documentation Requirements
```markdown
Documentation Standards:
├── Each extension MUST have clear usage examples
├── Fallback behavior MUST be documented
├── Compatibility notes MUST be included
├── Migration guides MUST be provided when needed
└── Best practices MUST be documented
```

## Implementation Guidelines

### 1. Parser Configuration
```markdown
Parser Settings:
{
  "commonmark": true,
  "extensions": {
    "framework-specific": true,
    "enhanced-tables": true,
    "task-lists": true,
    "metadata": true
  },
  "fallback": {
    "strip-extensions": true,
    "preserve-content": true
  }
}
```

### 2. Processing Pipeline
```markdown
Processing Order:
1. CommonMark parsing
2. Extension processing
3. Fallback handling
4. Validation and verification
5. Output generation
```

### 3. Error Handling
```markdown
Error Management:
├── Extension errors MUST not break CommonMark parsing
├── Fallback content MUST be provided for failed extensions
├── Error messages MUST be clear and actionable
├── Logging MUST include extension-specific information
└── Recovery strategies MUST be documented
```

## Examples and Use Cases

### 1. Framework Documentation
```markdown
# [RULE] Framework Naming Convention

[STATUS: APPROVED] [PRIORITY: HIGH]

## Overview

This rule defines the naming convention for framework components.

## Requirements

- All component names MUST follow PascalCase
- File names MUST use kebab-case
- Directory names MUST be descriptive and lowercase

## Examples

```javascript [EXAMPLE]
// Correct naming
const FrameworkComponent = () => {
  // Implementation
};
```

```bash [COMMAND]
# File naming example
framework-component.md
```

## References

- [COMPONENT: 20_convention]
- [FILE: 01_markdown_convention.md]
```

### 2. Technical Documentation
```markdown
# API Documentation

## Endpoint: /api/v1/users

**Method**: GET
**Authentication**: Required
**Rate Limit**: 1000/hour

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | integer | No | Page number |
| limit | integer | No | Items per page |
| filter | string | No | Filter criteria |

### Response

```json [EXAMPLE]
{
  "data": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 100
  }
}
```

### Error Handling

> **Warning**: Rate limit exceeded
> 
> The API rate limit has been exceeded. Please wait before making additional requests.

> **Note**: Authentication required
> 
> All API endpoints require valid authentication tokens.
```

### 3. Validation Scripts
```markdown
# CommonMark Validation

## Overview

This script validates CommonMark compliance for framework documents.

```bash [VALIDATION]
#!/bin/bash
# CommonMark validation script

for file in *.md; do
  echo "Validating $file..."
  commonmark-validator "$file" || echo "FAILED: $file"
done
```

## Usage

1. Install CommonMark validator
2. Run validation script
3. Review any failures
4. Fix compliance issues

## Requirements

- CommonMark parser installed
- Framework extensions documented
- Fallback behavior implemented
```

## Maintenance and Updates

### 1. Extension Lifecycle
```markdown
Extension Management:
├── New extensions MUST be documented and tested
├── Deprecated extensions MUST have migration paths
├── Removed extensions MUST have clear deprecation notices
├── Extension updates MUST maintain backward compatibility
└── Extension removal MUST be planned and communicated
```

### 2. Version Management
```markdown
Version Control:
├── Extension versions MUST be tracked
├── Breaking changes MUST be clearly marked
├── Migration guides MUST be provided for major changes
├── Deprecation notices MUST be included in advance
└── Compatibility matrices MUST be maintained
```

### 3. Quality Assurance
```markdown
QA Process:
├── Regular extension functionality testing
├── CommonMark compliance verification
├── Cross-parser compatibility testing
├── Performance impact assessment
└── Documentation accuracy verification
```

## References and Resources

### CommonMark Resources
- [CommonMark Specification](https://spec.commonmark.org/)
- [CommonMark Test Suite](https://spec.commonmark.org/dingus/)
- [CommonMark Implementations](https://github.com/commonmark/commonmark-spec/wiki/Markdown-Implementations)

### Framework Integration
- [01_commonmark_standard.md](01_commonmark_standard.md) - CommonMark compliance requirements
- [03_validation_framework.md](03_validation_framework.md) - Validation requirements
- [04_toolchain_integration.md](04_toolchain_integration.md) - Tools and processors

### Extension Development
- [Markdown-it Extensions](https://github.com/markdown-it/markdown-it) - Extension development guide
- [CommonMark Extensions](https://talk.commonmark.org/c/extensions) - Community extension discussions
- [Markdown Linting](https://github.com/DavidAnson/markdownlint) - Linting rules and extensions

---

**Framework**: MODEL_for_framework  
**Framework Version**: V1.0.0  
**Date**: 2026-02-01  

## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.0 | 2026-02-01 | Initial creation | Framework Steward | Define framework-specific extensions |