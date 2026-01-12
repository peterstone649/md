# 12. Principle of Accessibility (PRINC_MFR_ACCESSIBILITY) **[PRIO: CRITICAL]**

**Version: V0.1.1** **Status: ACTIVE** **Date: 2026-01-12**

**We establish Accessibility as a foundational principle requiring that all products, documents, and tools be designed, developed, and documented to be usable by people with the widest possible range of abilities.**

**Objectives:**
1. **Perceivable**: Ensure users can perceive all presented information through their available senses.
2. **Operable**: Ensure user interface components and navigation are fully operable by all users.
3. **Understandable**: Ensure information and the operation of the user interface are clear and understandable.
4. **Robust**: Ensure content is robust enough to be interpreted reliably by a wide variety of user agents, including assistive technologies.

---

## Abstract

**[AI_LOCK]**
The Principle of Accessibility mandates that the framework and its outputs are inclusive by design. It moves beyond a "one-size-fits-all" approach to ensure that users with visual, auditory, motor, or cognitive disabilities can access and interact with content and tools on an equal basis. Adherence to this principle is not just a matter of compliance but a core tenet of creating high-quality, user-centric products. This principle adopts the internationally recognized Web Content Accessibility Guidelines (WCAG) as its primary standard.
**[END_AI_LOCK]**

---

## 1. Scope and Applicability

This principle applies to all aspects of the framework, including but not limited to:
- All generated HTML documents.
- All user-facing tools and interfaces.
- All official documentation, both in Markdown and its rendered forms.

---

## 2. Core Definitions

| Element | Definition |
|---------|------------|
| **Accessibility (a11y)** | The practice of making websites, tools, and documents usable by as many people as possible, including those with disabilities. |
| **WCAG** | Web Content Accessibility Guidelines. An international standard providing a wide range of recommendations for making web content more accessible. |
| **Assistive Technology** | Hardware and/or software that acts as a user agent to provide functionality to meet the requirements of users with disabilities (e.g., screen readers, screen magnifiers). |

---

## 4. Rules and Guidelines

### 4.1 HTML Content Requirements (based on WCAG 2.1 AA)
1. **Alt Text**: All non-decorative images (`<img>`) MUST have descriptive alternative text (`alt` attribute).
2. **Semantic HTML**: Use appropriate HTML5 semantic elements (`<main>`, `<nav>`, `<article>`, etc.) to define the structure of the page.
3. **Color Contrast**: Text and interactive elements MUST have a color contrast ratio of at least 4.5:1 against the background.
4. **Keyboard Navigation**: All interactive elements (links, buttons, form fields) MUST be fully accessible and operable using only a keyboard.

### 4.2 Documentation Requirements
1. **Descriptive Links**: Link text MUST clearly describe the destination of the link. Avoid generic phrases like "click here".
2. **Structured Content**: Use headings, lists, and other structural elements correctly to create a logical document outline.

---

## 8. Related Principles and Documents

| Reference | Relationship |
|-----------|--------------|
| [WCAG 2.1 Guidelines](https://www.w3.org/TR/WCAG21/) | The primary technical standard for this principle. |

---

## 10. Changelog

| Version | Date | Changes | Stakeholder | Rationale/Motivation |
|---------|------|---------|-------------|----------------------|
| V0.1.1 | 2026-01-10 | Initial creation | Framework Steward | mini review changes|
| V0.1.0 | 2026-01-10 | Initial creation | AI Framework Steward | To formally establish accessibility as a core principle of the framework. |
