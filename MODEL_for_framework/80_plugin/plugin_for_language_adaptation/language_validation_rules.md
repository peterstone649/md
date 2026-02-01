# ⚖️ Language Validation Rules

**Rules for validating translation quality and consistency**

## 🎯 Core Validation Principles

### 1. **Accuracy Validation**
- **Semantic Accuracy**: Translations must accurately convey original meaning
- **Technical Accuracy**: Technical terms must be correctly translated
- **Context Preservation**: Original context and intent must be maintained
- **Completeness**: All content must be fully translated without omissions

### 2. **Consistency Validation**
- **Terminology Consistency**: Use consistent terminology across all translations
- **Style Consistency**: Follow established style guidelines
- **Formatting Consistency**: Maintain consistent formatting and structure
- **Voice Consistency**: Preserve original tone and voice

### 3. **Cultural Appropriateness**
- **Cultural Sensitivity**: Content must be culturally appropriate
- **Local Relevance**: Examples and references should be locally relevant
- **Religious Sensitivity**: Avoid content that may be religiously inappropriate
- **Social Context**: Consider local social norms and values

### 4. **Technical Quality**
- **Grammar and Syntax**: Proper grammar and sentence structure
- **Spelling and Punctuation**: Correct spelling and punctuation
- **Character Encoding**: Proper character encoding and display
- **Formatting**: Correct formatting and layout

## 📋 Validation Categories

### Content Validation Rules

#### **Text Completeness**
```yaml
validation_rules:
  text_completeness:
    check_type: "completeness"
    requirements:
      - "All source text must be translated"
      - "No untranslated segments allowed"
      - "All placeholders must be preserved"
      - "All HTML tags must be properly handled"
    severity: "critical"
    auto_check: true
```

#### **Terminology Consistency**
```yaml
validation_rules:
  terminology_consistency:
    check_type: "consistency"
    requirements:
      - "Use approved glossary terms"
      - "Maintain consistent terminology across documents"
      - "Follow established translation memory"
      - "Check against terminology database"
    severity: "high"
    auto_check: true
```

#### **Cultural Appropriateness**
```yaml
validation_rules:
  cultural_appropriateness:
    check_type: "cultural"
    requirements:
      - "Avoid culturally insensitive content"
      - "Use locally relevant examples"
      - "Consider religious and social norms"
      - "Adapt metaphors and idioms appropriately"
    severity: "medium"
    auto_check: false
    manual_review: true
```

### Technical Validation Rules

#### **Character Encoding**
```yaml
validation_rules:
  character_encoding:
    check_type: "technical"
    requirements:
      - "UTF-8 encoding required"
      - "Proper handling of special characters"
      - "Correct display of diacritical marks"
      - "RTL text properly formatted (for RTL languages)"
    severity: "high"
    auto_check: true
```

#### **Formatting Preservation**
```yaml
validation_rules:
  formatting_preservation:
    check_type: "formatting"
    requirements:
      - "Preserve original formatting structure"
      - "Maintain code block formatting"
      - "Keep table structures intact"
      - "Preserve heading hierarchy"
    severity: "medium"
    auto_check: true
```

#### **Link and Reference Integrity**
```yaml
validation_rules:
  link_integrity:
    check_type: "structural"
    requirements:
      - "All links must be functional"
      - "References must be updated for local context"
      - "File paths must be correct"
      - "Anchor links must work properly"
    severity: "medium"
    auto_check: true
```

## 🛠️ Validation Tools & Methods

### Automated Validation

#### **CAT Tool Integration**
```yaml
cat_tools:
  sdl_trados:
    validation_features:
      - "Terminology consistency checking"
      - "Quality assurance checks"
      - "Spell checking integration"
      - "Formatting validation"
  memoq:
    validation_features:
      - "Translation memory validation"
      - "Terminology database checking"
      - "Quality assurance rules"
      - "Context validation"
  free_alternatives:
    - "OmegaT"
    - "POEditor"
    - "Weblate"
    - "Crowdin"
```

#### **Quality Assurance Tools**
```yaml
qa_tools:
  validation_checks:
    - "Spell checking"
    - "Grammar checking"
    - "Terminology consistency"
    - "Number and date format validation"
    - "Placeholder preservation"
    - "Tag balance checking"
    - "Character encoding validation"
  automated_tools:
    - "Xbench"
    - "Verifika"
    - "QA Distiller"
    - "LanguageTool"
```

### Manual Validation

#### **Peer Review Process**
```yaml
peer_review:
  requirements:
    - "Review by second qualified translator"
    - "Focus on accuracy and completeness"
    - "Check for cultural appropriateness"
    - "Validate technical terminology"
  review_criteria:
    - "Semantic accuracy"
    - "Cultural sensitivity"
    - "Technical correctness"
    - "Readability and flow"
```

#### **Subject Matter Review**
```yaml
subject_matter_review:
  requirements:
    - "Review by domain expert"
    - "Validate technical accuracy"
    - "Check industry terminology"
    - "Ensure content correctness"
  review_scope:
    - "Technical concepts"
    - "Industry-specific terms"
    - "Complex explanations"
    - "Specialized content"
```

#### **Cultural Review**
```yaml
cultural_review:
  requirements:
    - "Review by cultural expert"
    - "Validate cultural appropriateness"
    - "Check local relevance"
    - "Ensure social sensitivity"
  review_focus:
    - "Cultural references"
    - "Examples and metaphors"
    - "Social norms and values"
    - "Religious considerations"
```

## 📊 Validation Levels

### **Level 1: Basic Validation**
- **Scope**: Essential quality checks
- **Tools**: Automated tools only
- **Time**: 5-10 minutes per document
- **Coverage**: 80% of common issues

**Checks Included:**
- Spell checking
- Grammar checking
- Basic terminology consistency
- Formatting preservation
- Link integrity

### **Level 2: Standard Validation**
- **Scope**: Comprehensive quality assurance
- **Tools**: Automated + manual review
- **Time**: 15-30 minutes per document
- **Coverage**: 95% of quality issues

**Checks Included:**
- All Level 1 checks
- Terminology database validation
- Context validation
- Cultural appropriateness review
- Technical accuracy verification

### **Level 3: Premium Validation**
- **Scope**: Maximum quality assurance
- **Tools**: Full manual + automated review
- **Time**: 30-60 minutes per document
- **Coverage**: 99% of quality issues

**Checks Included:**
- All Level 2 checks
- Subject matter expert review
- Cultural expert review
- Comprehensive peer review
- Final quality validation

## 🔄 Validation Workflow

### Pre-Translation Validation
```yaml
pre_translation_validation:
  steps:
    - "Content analysis and complexity assessment"
    - "Terminology extraction and glossary preparation"
    - "Translation memory preparation"
    - "Quality requirements definition"
  tools:
    - "Content analysis tools"
    - "Terminology management systems"
    - "Translation memory databases"
    - "Quality requirement templates"
```

### During Translation Validation
```yaml
during_translation_validation:
  steps:
    - "Real-time quality checking"
    - "Terminology consistency monitoring"
    - "Context preservation validation"
    - "Formatting integrity checks"
  tools:
    - "CAT tool validation features"
    - "Real-time QA tools"
    - "Terminology databases"
    - "Style guide enforcement"
```

### Post-Translation Validation
```yaml
post_translation_validation:
  steps:
    - "Comprehensive quality review"
    - "Peer review process"
    - "Subject matter validation"
    - "Cultural appropriateness review"
    - "Final approval process"
  tools:
    - "Quality assurance tools"
    - "Peer review templates"
    - "Expert review checklists"
    - "Final approval workflows"
```

## 📈 Validation Metrics

### Quality Metrics
- **Accuracy Rate**: Percentage of accurate translations
- **Consistency Score**: Terminology and style consistency
- **Cultural Appropriateness**: Cultural relevance and sensitivity
- **Technical Accuracy**: Technical term correctness

### Process Metrics
- **Validation Time**: Time spent on validation
- **Issue Detection Rate**: Percentage of issues found
- **Review Cycle Time**: Time for review completion
- **Rejection Rate**: Percentage of translations rejected

### Automation Metrics
- **Automated Check Coverage**: Percentage of checks automated
- **Tool Accuracy**: Accuracy of automated validation tools
- **False Positive Rate**: Rate of incorrect validation failures
- **Tool Performance**: Speed and efficiency of validation tools

## 🚨 Validation Failure Handling

### Critical Failures
- **Definition**: Issues that prevent publication
- **Examples**: Inaccurate technical terms, missing content
- **Action**: Immediate correction required
- **Review**: Manual review by senior translator

### High Priority Failures
- **Definition**: Significant quality issues
- **Examples**: Terminology inconsistency, cultural issues
- **Action**: Correction before final approval
- **Review**: Review by subject matter expert

### Medium Priority Failures
- **Definition**: Quality improvements needed
- **Examples**: Style inconsistencies, minor formatting issues
- **Action**: Correction in next revision cycle
- **Review**: Review during regular quality review

### Low Priority Failures
- **Definition**: Minor improvements
- **Examples**: Suggested wording improvements
- **Action**: Consider for future updates
- **Review**: Track for continuous improvement

## 📞 Validation Support

### Getting Help with Validation
- **Tool Issues**: Contact validation tool support
- **Process Questions**: Consult validation guidelines
- **Quality Concerns**: Escalate to quality assurance team
- **Technical Problems**: Contact technical support

### Validation Training
- **Tool Training**: Training on validation tools and features
- **Process Training**: Training on validation procedures
- **Quality Standards**: Training on quality requirements
- **Best Practices**: Training on validation best practices

--- 

**Next Steps**: Use these validation rules to ensure translation quality. Always review [translation_workflow.md](translation_workflow.md) for implementation details!