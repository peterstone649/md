# Markdown Validation Rules [CONVENTION_FOR_MFW_MARKDOWN_VALIDATION] **[PRIO: HIGH]**

**Version: V1.0.0** **Status: APPROVED** **Date: 2026-02-01**

## Overview

This document defines the validation rules and requirements for ensuring CommonMark compliance and framework extension compatibility. All Markdown files within this framework MUST pass these validation rules.

## Validation Framework

### 1. Validation Levels
```markdown
Validation Categories:
├── L1: CommonMark Core Compliance
├── L2: Framework Extension Compliance
├── L3: Cross-Parser Compatibility
├── L4: Semantic Correctness
└── L5: Performance and Scalability
```

### 2. Validation Requirements
```markdown
Mandatory Validation:
├── All files MUST pass L1 validation
├── Framework-specific files MUST pass L2 validation
├── Public documentation MUST pass L3 validation
├── Critical documentation MUST pass L4 validation
└── Large files MUST pass L5 validation
```

## Level 1: CommonMark Core Compliance

### 1.1 Syntax Validation
```markdown
Core Syntax Rules:
├── Headers MUST follow CommonMark specification
├── Lists MUST use proper indentation and markers
├── Links MUST have valid URL syntax
├── Images MUST have valid alt text and URLs
├── Code blocks MUST use proper fencing
└── Emphasis MUST use consistent markers
```

### 1.2 Structure Validation
```markdown
Document Structure:
├── MUST have proper heading hierarchy
├── Lists MUST be properly nested
├── Tables MUST have consistent column alignment
├── Blockquotes MUST use proper syntax
├── Horizontal rules MUST use valid syntax
└── HTML blocks MUST be properly formatted
```

### 1.3 Content Validation
```markdown
Content Requirements:
├── Text MUST be properly escaped
├── Special characters MUST be handled correctly
├── Unicode characters MUST be supported
├── Line endings MUST be consistent
├── Whitespace MUST follow CommonMark rules
└── Comments MUST use proper syntax
```

## Level 2: Framework Extension Compliance

### 2.1 Extension Syntax Validation
```markdown
Extension Rules:
├── Framework headers MUST use proper prefixes
├── Status indicators MUST follow format
├── Priority markers MUST be valid
├── Framework references MUST be resolvable
├── Enhanced code blocks MUST have valid tags
└── Metadata MUST use proper format
```

### 2.2 Extension Compatibility
```markdown
Compatibility Requirements:
├── Extensions MUST not conflict with CommonMark
├── Fallback behavior MUST be documented
├── Extension syntax MUST be consistent
├── Extension usage MUST be justified
├── Extension documentation MUST be complete
└── Extension testing MUST be comprehensive
```

### 2.3 Extension Quality
```markdown
Quality Standards:
├── Extensions MUST enhance document clarity
├── Extensions MUST follow framework conventions
├── Extensions MUST be consistently applied
├── Extensions MUST have clear purpose
├── Extensions MUST be maintainable
└── Extensions MUST be documented
```

## Level 3: Cross-Parser Compatibility

### 3.1 Parser Testing
```markdown
Parser Compatibility:
├── MUST render correctly in CommonMark parser
├── MUST render correctly in GitHub Flavored Markdown
├── MUST render correctly in GitLab Flavored Markdown
├── MUST render correctly in Bitbucket Markdown
├── MUST render correctly in VS Code Markdown preview
└── MUST render correctly in major documentation tools
```

### 3.2 Platform Testing
```markdown
Platform Compatibility:
├── MUST work in GitHub repositories
├── MUST work in GitLab repositories
├── MUST work in documentation generators
├── MUST work in static site generators
├── MUST work in markdown editors
└── MUST work in CI/CD pipelines
```

### 3.3 Tool Integration
```markdown
Tool Compatibility:
├── MUST work with markdownlint
├── MUST work with prettier
├── MUST work with markdown-it
├── MUST work with pandoc
├── MUST work with commonmark.js
└── MUST work with markdown parsers
```

## Level 4: Semantic Correctness

### 4.1 Document Semantics
```markdown
Semantic Requirements:
├── Document structure MUST be logical
├── Heading hierarchy MUST be correct
├── Content organization MUST be clear
├── Cross-references MUST be valid
├── Link targets MUST exist
└── Image sources MUST be accessible
```

### 4.2 Content Semantics
```markdown
Content Meaning:
├── Text MUST convey intended meaning
├── Code examples MUST be accurate
├── Tables MUST present data clearly
├── Lists MUST be logically ordered
├── Blockquotes MUST be properly attributed
└── Metadata MUST be accurate and complete
```

### 4.3 Accessibility Semantics
```markdown
Accessibility Requirements:
├── Alt text MUST be descriptive
├── Headings MUST form logical hierarchy
├── Links MUST have meaningful text
├── Tables MUST have proper headers
├── Images MUST have appropriate descriptions
└── Code blocks MUST be readable
```

## Level 5: Performance and Scalability

### 5.1 File Size Limits
```markdown
Size Requirements:
├── Individual files MUST be under 1MB
├── Large files MUST be split appropriately
├── Images MUST be optimized
├── Code blocks MUST be reasonably sized
├── Tables MUST not exceed reasonable complexity
└── Documents MUST load quickly
```

### 5.2 Processing Performance
```markdown
Performance Standards:
├── Parsing MUST complete in reasonable time
├── Rendering MUST be efficient
├── Validation MUST be fast
├── Processing MUST scale with file size
├── Memory usage MUST be reasonable
└── CPU usage MUST be optimized
```

### 5.3 Scalability Considerations
```markdown
Scalability Rules:
├── Large documents MUST be manageable
├── Complex documents MUST render correctly
├── Many files MUST process efficiently
├── Validation MUST scale with project size
├── Tools MUST handle large repositories
└── Performance MUST not degrade with growth
```

## Validation Tools and Processes

### 1. Automated Validation
```markdown
Validation Pipeline:
├── Pre-commit hooks MUST validate Markdown
├── CI/CD MUST include Markdown validation
├── Automated testing MUST run validation
├── Documentation builds MUST validate
├── Release processes MUST validate
└── Code reviews MUST check validation
```

### 2. Manual Validation
```markdown
Manual Review Process:
├── Critical documents MUST be manually reviewed
├── New extensions MUST be manually validated
├── Complex documents MUST be manually checked
├── Cross-platform testing MUST be manual
├── Accessibility MUST be manually verified
└── Semantic correctness MUST be manually reviewed
```

### 3. Validation Tools
```markdown
Tool Requirements:
├── CommonMark validator MUST be used
├── Framework extension validator MUST be used
├── Cross-parser validator MUST be used
├── Accessibility validator MUST be used
├── Performance validator MUST be used
└── Custom validators MUST be developed as needed
```

## Validation Implementation

### 1. Pre-commit Hooks
```markdown
Hook Configuration:
#!/bin/bash
# Markdown validation pre-commit hook

echo "Validating Markdown files..."

# Check for CommonMark compliance
for file in $(git diff --cached --name-only --diff-filter=ACM | grep -E '\.md$'); do
  echo "Validating $file..."
  
  # Run CommonMark validation
  if ! commonmark-validator "$file"; then
    echo "ERROR: $file failed CommonMark validation"
    exit 1
  fi
  
  # Run framework extension validation
  if ! framework-markdown-validator "$file"; then
    echo "ERROR: $file failed framework extension validation"
    exit 1
  fi
  
  # Run cross-parser compatibility check
  if ! cross-parser-validator "$file"; then
    echo "ERROR: $file failed cross-parser validation"
    exit 1
  fi
done

echo "All Markdown files validated successfully!"
```

### 2. CI/CD Integration
```yaml
# GitHub Actions workflow example
name: Markdown Validation
on: [push, pull_request]

jobs:
  markdown-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Install validation tools
        run: |
          npm install -g commonmark-validator
          npm install -g framework-markdown-validator
          
      - name: Validate CommonMark compliance
        run: find . -name "*.md" -exec commonmark-validator {} \;
        
      - name: Validate framework extensions
        run: find . -name "*.md" -exec framework-markdown-validator {} \;
        
      - name: Validate cross-parser compatibility
        run: find . -name "*.md" -exec cross-parser-validator {} \;
```

### 3. Validation Scripts
```bash
#!/bin/bash
# Comprehensive Markdown validation script

echo "=== Markdown Validation Report ==="
echo "Date: $(date)"
echo "Files: $(find . -name "*.md" | wc -l)"
echo ""

# Count validation results
total=0
passed=0
failed=0

for file in $(find . -name "*.md"); do
  total=$((total + 1))
  echo "Validating: $file"
  
  # CommonMark validation
  if commonmark-validator "$file" >/dev/null 2>&1; then
    echo "  ✓ CommonMark compliance"
  else
    echo "  ✗ CommonMark compliance FAILED"
    failed=$((failed + 1))
    continue
  fi
  
  # Framework extension validation
  if framework-markdown-validator "$file" >/dev/null 2>&1; then
    echo "  ✓ Framework extensions"
  else
    echo "  ✗ Framework extensions FAILED"
    failed=$((failed + 1))
    continue
  fi
  
  # Cross-parser validation
  if cross-parser-validator "$file" >/dev/null 2>&1; then
    echo "  ✓ Cross-parser compatibility"
  else
    echo "  ✗ Cross-parser compatibility FAILED"
    failed=$((failed + 1))
    continue
  fi
  
  passed=$((passed + 1))
  echo "  ✓ All validations passed"
  echo ""
done

echo "=== Validation Summary ==="
echo "Total files: $total"
echo "Passed: $passed"
echo "Failed: $failed"
echo "Success rate: $(( passed * 100 / total ))%"

if [ $failed -gt 0 ]; then
  echo ""
  echo "❌ Validation failed! Please fix the issues above."
  exit 1
else
  echo ""
  echo "✅ All validations passed!"
  exit 0
fi
```

## Validation Reporting

### 1. Validation Reports
```markdown
Report Format:
# Markdown Validation Report

**Date**: 2026-02-01
**Files Checked**: 150
**Passed**: 148
**Failed**: 2
**Success Rate**: 98.7%

## Failed Files

### file1.md
- ✗ CommonMark compliance: Line 45, invalid link syntax
- ✗ Framework extensions: Line 12, invalid status indicator

### file2.md
- ✗ Cross-parser compatibility: Line 89, unsupported extension

## Recommendations

1. Fix link syntax in file1.md
2. Update status indicator format in file1.md
3. Review extension usage in file2.md
```

### 2. Continuous Monitoring
```markdown
Monitoring Dashboard:
├── Daily validation reports
├── Weekly trend analysis
├── Monthly compliance summaries
├── Quarterly framework extension reviews
├── Annual CommonMark specification updates
└── Real-time validation alerts
```

### 3. Quality Metrics
```markdown
Quality Indicators:
├── CommonMark compliance rate
├── Framework extension compliance rate
├── Cross-parser compatibility rate
├── Validation performance metrics
├── Error frequency and types
└── Resolution time for issues
```

## Maintenance and Updates

### 1. Validation Rule Updates
```markdown
Update Process:
├── Monitor CommonMark specification changes
├── Review framework extension requirements
├── Update validation rules as needed
├── Test updated rules thoroughly
├── Deploy updated validation tools
└── Communicate changes to team
```

### 2. Tool Maintenance
```markdown
Tool Management:
├── Regular updates to validation tools
├── Performance optimization of validators
├── Bug fixes and issue resolution
├── New feature implementation
├── Documentation updates
└── User support and training
```

### 3. Process Improvement
```markdown
Continuous Improvement:
├── Analyze validation failure patterns
├── Identify common issues and solutions
├── Improve validation tool accuracy
├── Enhance validation speed and efficiency
├── Update validation guidelines
└── Share best practices and lessons learned
```

## References and Resources

### CommonMark Validation Tools
- [CommonMark Validator](https://github.com/commonmark/commonmark.js)
- [Markdownlint](https://github.com/DavidAnson/markdownlint)
- [Prettier Markdown](https://prettier.io/)
- [Vale Linter](https://vale.sh/)

### Framework Validation Tools
- [Framework Markdown Validator](https://github.com/framework/markdown-validator)
- [Extension Compatibility Checker](https://github.com/framework/extension-checker)
- [Cross-Parser Validator](https://github.com/framework/cross-parser-validator)

### Validation Best Practices
- [CommonMark Test Suite](https://spec.commonmark.org/dingus/)
- [Markdown Style Guide](https://www.markdownguide.org/)
- [Accessibility Guidelines](https://www.w3.org/WAI/)

---

**Framework**: MODEL_for_framework  
**Framework Version**: V1.0.0  
**Date**: 2026-02-01  

## Changelog

| Version | Date | Change Content | Stakeholders | Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.0 | 2026-02-01 | Initial creation | Framework Steward | Establish validation framework |