# 📝 Translation Templates

**Templates for consistent and high-quality translations**

## 🎯 Basic Translation Template

### Content Translation Template
```markdown
# [Original Title in English]

**[Translated Title]**

## Overview

[Original content paragraph 1]

[Original content paragraph 2]

## Key Points

- [Original bullet point 1]
- [Original bullet point 2]
- [Original bullet point 3]

## Examples

### Example 1
```[language]
[Original code example]
```

**Explanation:** [Original explanation]

### Example 2
```[language]
[Original code example]
```

**Explanation:** [Original explanation]

## Best Practices

[Original best practices content]

## Additional Resources

- [Original resource 1]
- [Original resource 2]
- [Original resource 3]
```

### Template Usage Notes
- **Preserve structure**: Keep original formatting and organization
- **Translate content**: Translate all text content while preserving meaning
- **Maintain code**: Keep code examples in original language
- **Adapt examples**: Modify examples to be culturally relevant when appropriate
- **Update resources**: Include local or regional resources when available

## 📋 Technical Documentation Template

### API Documentation Template
```markdown
# API Reference

## [API Name] (English)

**[Translated API Name]**

### Endpoint: [Endpoint Name]

**Method:** [HTTP Method]
**URL:** [API Endpoint URL]

#### Parameters

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| [param1] | [type] | [description] | [yes/no] |
| [param2] | [type] | [description] | [yes/no] |

#### Request Example

```json
{
  "param1": "value1",
  "param2": "value2"
}
```

#### Response Example

```json
{
  "status": "success",
  "data": {
    "result": "value"
  }
}
```

#### Error Codes

| Code | Description |
|------|-------------|
| 400 | [Error description] |
| 401 | [Error description] |
| 500 | [Error description] |

**Notes:** [Additional technical notes]
```

### Template Guidelines
- **Keep technical terms**: Use established technical translations
- **Preserve code**: Maintain original code examples and syntax
- **Translate descriptions**: Translate all explanatory text
- **Maintain structure**: Keep API documentation format consistent
- **Update examples**: Adapt examples for local context when appropriate

## 🖥️ User Interface Text Template

### UI String Translation Template
```json
{
  "en": {
    "welcome_message": "Welcome to our application!",
    "login_button": "Login",
    "logout_button": "Logout",
    "save_changes": "Save Changes",
    "cancel": "Cancel",
    "error_occurred": "An error occurred. Please try again.",
    "loading": "Loading...",
    "success": "Operation completed successfully!"
  },
  "[language_code]": {
    "welcome_message": "[Translated welcome message]",
    "login_button": "[Translated login button text]",
    "logout_button": "[Translated logout button text]",
    "save_changes": "[Translated save changes text]",
    "cancel": "[Translated cancel text]",
    "error_occurred": "[Translated error message]",
    "loading": "[Translated loading text]",
    "success": "[Translated success message]"
  }
}
```

### UI Translation Guidelines
- **Keep variables**: Preserve placeholder variables like {name}, {count}
- **Maintain context**: Ensure translations make sense in UI context
- **Consider length**: Account for text expansion/contraction in different languages
- **Preserve formatting**: Keep HTML tags, line breaks, and special characters
- **Test in context**: Verify translations work properly in actual UI

## 📚 User Guide Template

### User Guide Translation Template
```markdown
# User Guide: [Product/Feature Name]

## Introduction

This guide will help you get started with [product/feature] in [language].

## Getting Started

### Prerequisites

Before you begin, ensure you have:

- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

### Installation

1. [Step 1 description]
2. [Step 2 description]
3. [Step 3 description]

### Configuration

After installation, configure your settings:

```[configuration_format]
[configuration_example]
```

## Basic Usage

### First Steps

1. **Launch the application**
   [Description of how to start using the application]

2. **Create your first project**
   [Step-by-step instructions]

3. **Configure basic settings**
   [Configuration instructions]

### Common Tasks

#### Task 1: [Task Name]
[Description of the task and how to perform it]

#### Task 2: [Task Name]
[Description of the task and how to perform it]

#### Task 3: [Task Name]
[Description of the task and how to perform it]

## Advanced Features

### Feature 1: [Feature Name]
[Detailed explanation of advanced feature]

### Feature 2: [Feature Name]
[Detailed explanation of advanced feature]

## Troubleshooting

### Common Issues

**Problem:** [Description of problem]
**Solution:** [Solution description]

**Problem:** [Description of problem]
**Solution:** [Solution description]

### Getting Help

If you need additional assistance:

- **Documentation:** [Link to documentation]
- **Community Forum:** [Link to community]
- **Support:** [Contact information]
```

### User Guide Guidelines
- **Adapt examples**: Use locally relevant examples and scenarios
- **Consider cultural context**: Ensure examples are culturally appropriate
- **Maintain structure**: Keep original organization and flow
- **Translate terminology**: Use consistent technical translations
- **Update contact info**: Include local support information

## 📋 Translation Quality Checklist

### Pre-Translation
- [ ] Review source content for complexity and terminology
- [ ] Check glossary for approved translations
- [ ] Understand target audience and context
- [ ] Identify any cultural adaptation needs

### During Translation
- [ ] Maintain original meaning and intent
- [ ] Use approved terminology consistently
- [ ] Adapt examples for cultural relevance
- [ ] Preserve technical accuracy
- [ ] Ensure readability and natural flow

### Post-Translation
- [ ] Review for completeness and accuracy
- [ ] Check for cultural appropriateness
- [ ] Verify technical terms and concepts
- [ ] Test in context if possible
- [ ] Proofread for grammar and style

### Quality Assurance
- [ ] Peer review by another translator
- [ ] Subject matter expert review (if technical content)
- [ ] Cultural review for appropriateness
- [ ] Final quality validation

## 🔄 Template Customization

### For Different Content Types

#### Marketing Content
- Focus on tone and messaging adaptation
- Emphasize cultural relevance
- Adapt examples and references
- Maintain brand voice consistency

#### Technical Documentation
- Prioritize accuracy and precision
- Use established technical terminology
- Maintain logical structure
- Preserve code examples unchanged

#### User Interface
- Consider space limitations
- Maintain consistency across interface
- Test translations in actual UI
- Ensure accessibility compliance

#### Legal Content
- Use certified translators
- Maintain legal accuracy
- Follow regulatory requirements
- Include appropriate disclaimers

### For Different Languages

#### RTL Languages (Arabic, Hebrew)
- Adapt layout for right-to-left reading
- Ensure proper Unicode handling
- Consider cultural and religious sensitivity
- Test with native speakers

#### Asian Languages (Chinese, Japanese, Korean)
- Handle character encoding properly
- Consider formality levels
- Adapt for cultural context
- Test with appropriate fonts

#### European Languages
- Handle diacritical marks correctly
- Consider regional variations
- Maintain grammatical accuracy
- Adapt for local conventions

## 📞 Template Support

### Getting Help with Templates
- **Template Questions**: Review template guidelines and examples
- **Translation Issues**: Consult with translation experts
- **Technical Problems**: Check template formatting and structure
- **Cultural Concerns**: Seek cultural consultation

### Template Updates
- Templates are regularly updated based on feedback
- New templates added for emerging content types
- Best practices incorporated from real-world usage
- Community contributions welcome

--- 

**Next Steps**: Use these templates as a starting point for your translations. Always review [language_standards.md](language_standards.md) for specific language requirements!