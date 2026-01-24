# Wikimedia Links [RULE_FOR_MFW_WIKIMEDIA_LINKS] **[PRIO: MEDIUM]**

**Version: V1.0.1** **Status: APPROVED** **Date: 2026-01-23**
**Scope:** All framework documents containing Wikimedia references

## Rule Statement

**All references to Wikimedia Commons and Wikipedia resources MUST include proper attribution, licensing information, and direct links to source materials.**

## Rationale

Proper Wikimedia linking:
- Ensures compliance with Creative Commons licensing requirements
- Provides transparency about source materials
- Enables proper attribution to original creators
- Supports academic and research integrity
- Facilitates verification of referenced information
- Aligns with framework principles of transparency and accountability

## Wikimedia Link Requirements

### Required Elements

Every Wikimedia reference MUST include:

1. **Direct Link** - Functional URL to the specific Wikimedia page
2. **Attribution** - Creator/artist name when available
3. **License Information** - Specific Creative Commons license
4. **Access Date** - When the resource was accessed

### Link Format Pattern

```markdown
[![Alt Text](link-to-image)](link-to-wikimedia-page)
*Image by [Creator Name](link-to-creator-profile) / [License Name](link-to-license) via Wikimedia Commons*
```

### Complete Attribution Examples

**For Images:**
```markdown
[![Game Hammer Icon](https://game-icons.net/icons/ffffff/000000/gear-hammer/000000/64.png)](https://game-icons.net/1x1/lorc/gear-hammer.html)
*Icon by [Lorc](https://game-icons.net/about.html#lorc) / [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) via Game-Icons.net*
```

**For Wikipedia Articles:**
```markdown
[Artificial Intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence) (WP)
```

**For Wikimedia Commons Files:**
```markdown
[Framework Architecture Diagram](https://commons.wikimedia.org/wiki/File:Example_diagram.svg)(WM)
*Diagram by [Creator Name](https://commons.wikimedia.org/wiki/User:Username) / [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) via Wikimedia Commons*
```

## Attribution Standards

### License Identification

| License Code | Full Name | Attribution Required |
|-------------|-----------|---------------------|
| CC BY 3.0 | Creative Commons Attribution 3.0 | Yes |
| CC BY-SA 4.0 | Creative Commons Attribution-ShareAlike 4.0 | Yes |
| CC0 | Creative Commons Zero (Public Domain) | Recommended |
| Public Domain | Public Domain | Recommended |

### Creator Attribution

- Include creator name when available from Wikimedia metadata
- Link to creator's profile page when possible
- Use "Anonymous" or "Unknown" if creator information is not available
- Preserve original attribution chains for derivative works

### Access Documentation

- Include access date in ISO format (YYYY-MM-DD)
- Place access date in parentheses after the link
- Update access date when content is verified or refreshed

## Implementation Guidelines

### Image Usage
1. **Select Appropriate License** - Prefer CC BY-SA or CC0 for maximum compatibility
2. **Download Original Resolution** - Use highest quality available
3. **Preserve Metadata** - Keep EXIF data for attribution tracking
4. **Create Alt Text** - Descriptive text for accessibility

### Content References
1. **Cite Specific Sections** - Link to relevant article sections when possible
2. **Include Context** - Explain why the reference supports the framework content
3. **Regular Verification** - Check links periodically for continued availability

### Framework Integration
1. **Consistent Placement** - Place attributions immediately after referenced content
2. **Visual Separation** - Use italics or smaller text for attribution blocks
3. **Grouping** - Group multiple attributions from same source when appropriate

## Validation Checklist

- [ ] All Wikimedia links include direct URLs
- [ ] Attribution information is complete and accurate
- [ ] License information is specified and correct
- [ ] Access dates are included and current
- [ ] Links are functional and accessible
- [ ] Alt text is provided for images
- [ ] Attribution format follows established patterns

## Enforcement

1. **Content Creation:** Include complete attribution during initial drafting
2. **Review Process:** Verify all Wikimedia references meet attribution requirements
3. **Automated Checks:** Tools can validate link syntax and presence of attribution elements
4. **Regular Audits:** Periodic review of all Wikimedia references for accuracy

## References

- [Creative Commons License Chooser](https://creativecommons.org/choose/)
- [Wikimedia Commons Licensing](https://commons.wikimedia.org/wiki/Commons:Licensing)
- [Wikipedia Citation Guidelines](https://en.wikipedia.org/wiki/Wikipedia:Citing_Wikipedia)
- Framework Writing Conventions (20_convention/03_convention_for_writing_style.md)
- Clickable Links Rule (12_rule/10_rule_for_clickable_links.md)

**Rule Steward:** Terminology Architects
**Approval Status:** Framework Approved
**Effective Date:** 2026-01-13
**Review Cycle:** Annual

**Framework:** MODEL_for_framework
**Framework Version:** V1.0.1
**Date:** 2026-01-23

## Changelog

| Version | Date | Change Content | Stakeholders | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V1.0.1 | 2026-01-23 | Updated title formatting and changed metadata headers per RULE_FOR_MFW_TITLE_FORMAT | Framework Admin | Ensure framework-wide consistency |
| V0.1.0 | 2026-01-13 | Initial creation | AI Framework Admin | Establish file |
