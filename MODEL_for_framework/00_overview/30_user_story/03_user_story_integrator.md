# User Story: Integrator **[US_MFW_INTEGRATOR]** **[PRIO: HIGH]**

**Version: V1.0.0** **Date: 2026-01-09**

**Story ID:** US_MFW_INTEGRATOR
**Stakeholder:** Integrator

---

## User Story

**As an** Integrator working with AI tools,

**I want to** create and enhance framework content using AI assistance while respecting AI_LOCK protection,

**So that** I can leverage AI capabilities to produce high-quality framework documents efficiently.

---

## Description

Integrators use AI tools (LLMs, AI assistants) to create and improve framework content. They combine human oversight with AI capabilities. Key responsibilities include: generating drafts, enhancing existing content, maintaining AI_LOCK boundaries, and ensuring human validation of all AI-assisted work.

---

## Goals

1. **Generate** high-quality first drafts using AI tools
2. **Enhance** existing documents with AI-assisted improvements
3. **Protect** AI_LOCK sections from AI modification
4. **Validate** all AI-generated content through human review
5. **Maintain** transparency about AI involvement

---

## Acceptance Criteria

- [ ] Integrator can generate framework content using AI
- [ ] AI_LOCK markers protect core content from modification
- [ ] All AI-generated content undergoes human review
- [ ] Changelog documents AI involvement
- [ ] Quality standards are met for AI-assisted content
- [ ] Transparency about AI tools used

---

## Integrator Workflow

```
1. PREPARATION
   └── Identify content need
   └── Mark AI_LOCK sections if creating new document
   └── Define clear prompts for AI
   
2. AI GENERATION
   └── Use AI tools to generate content
   └── Apply framework conventions to prompts
   └── Request active voice and proper structure
   
3. HUMAN REVIEW
   └── Verify AI_LOCK sections intact
   └── Check active voice compliance
   └── Validate clickable links
   └── Assess content quality
   
4. REFINEMENT
   └── Edit AI-generated content
   └── Add cross-references
   └── Apply final polish
   
5. DOCUMENTATION
   └── Note AI assistance in methodology
   └── Update changelog with Stakeholder="AI_Assistant"
   └── Document Rationale/Motivation
```

---

## AI Integration Principles

| Principle | Application |
|-----------|-------------|
| **Human Sovereignty** | Human makes final decisions on AI content |
| **Transparency** | Disclose AI tools and methods used |
| **Iterative Validation** | Review AI output at multiple checkpoints |
| **Context Preservation** | Maintain framework context in AI prompts |
| **Reversibility** | Keep human-authored backup of AI content |

---

## AI_LOCK Protection

**[AI_LOCK]**
Core framework abstracts and fundamental principles MUST NOT be modified by AI.
**[END_AI_LOCK]**

Integrators MUST:
- Identify content requiring AI_LOCK protection
- Ensure AI tools do not modify protected sections
- Verify AI_LOCK integrity after AI assistance

---

## Quality Standards for AI Content

| Criterion | Standard |
|-----------|----------|
| **Active Voice** | 100% compliance (RULE_ACTIVE_VOICE) |
| **Clickable Links** | All cross-references functional (RULE_CLICKABLE_LINKS) |
| **Template Compliance** | Follows standardized structures |
| **Human Review** | All AI content reviewed by human |
| **Transparency** | AI involvement documented |

---

## Example Use Cases

1. **AI Draft Generation**
   > "I need a new principle document. I'll use an LLM to generate a first draft, then carefully review it for active voice, add cross-references, and ensure AI_LOCK sections are protected."

2. **Content Enhancement**
   > "This principle document needs improvement. I'll use AI to suggest enhancements while keeping the AI_LOCK abstract intact."

3. **Bulk Template Population**
   > "We need consistent metadata across documents. I'll use AI to help, but verify each result manually."

---

## Tools and Resources

| Tool | Purpose | Documentation |
|------|---------|---------------|
| AI Assistants | Content generation | `MODEL_for_STKHLD_AI_COLLAB/00_overview/01_legal/02_methodology_ai_assistance.md` |
| Principle Template | Structure AI output | `15_template/17_template_for_principle.md` |
| Active Voice Rule | Quality standard | `12_rule/01_rule_for_active_voice.md` |
| Clickable Links Rule | Navigation standard | `12_rule/02_rule_for_clickable_links.md` |

---

## Success Metrics

- AI-assisted content meets same quality standards as human-written
- Zero AI_LOCK violations
- Human review covers 100% of AI-generated content
- AI involvement transparently documented

---

**Story Status:** Ready
**Estimation:** 5 story points
**Sprint:** TBD
