# evaluation-framework - Skill

Generate comprehensive, multi-dimensional evaluation frameworks for any project, requirement, business idea, or document - grounded in 20+ world-renowned analytical methodologies.

## What It Does

Given any input (a project document, a business idea, a requirement description), this skill:

1. **Classifies the domain** — business strategy, product, tech, financial, policy, innovation, etc.
2. **Selects the right frameworks** — from 20+ methodologies including SWOT, PESTLE, Porter's Five Forces, McKinsey 7S, Theory of Change, Risk Matrix, NPV/ROI, Design Thinking, and more
3. **Applies each framework** with scored dimensions and evidence-backed analysis
4. **Synthesizes findings** across frameworks to find convergent insights and contradictions
5. **Produces a structured report** with Executive Summary, Priority Matrix, and actionable Next Steps

## Quick Start

When installed, simply describe your project or upload a document and ask for an evaluation:

> "Evaluate my startup pitch — we're building X for Y market..."
> "Analyze this project brief" [upload PDF]
> "Give me a full assessment of this product requirement"
> "What are the risks of this system migration plan?"

## File Structure

```
skill/
├── SKILL.md                    Main skill — Claude reads this first
├── references/
│   ├── frameworks-catalog.md   20+ framework definitions
│   ├── domain-selector.md      Framework selection decision logic
│   ├── output-templates.md     Per-framework report templates
│   ├── scoring-rubrics.md      1–5 scale criteria per dimension
│   └── document-reader-guide.md  How to parse uploaded docs
├── scripts/
│   ├── detect_domain.py        Domain classification
│   ├── extract_doc_sections.py Document section extractor (PDF/DOCX/TXT)
│   └── score_aggregator.py     Score computation + markdown tables
└── assets/
    └── report_template.md      Final report skeleton
```

## Frameworks Covered

| Category | Frameworks |
|---|---|
| Strategic | SWOT, PESTLE, Porter's Five Forces, Ansoff Matrix |
| Organizational | McKinsey 7S, Balanced Scorecard, OKR Alignment |
| Risk | Risk Matrix, FMEA |
| Product | Design Thinking, Jobs-To-Be-Done, Kano Model, Lean Canvas |
| Innovation | Blue Ocean Canvas |
| Research/Policy | Theory of Change, Kirkpatrick Model |
| Financial | NPV/ROI, Cost-Benefit Analysis |
| Technology | DevSecOps Maturity, TOGAF ADM |

## Script Dependencies

```bash
pip install pypdf python-docx --break-system-packages
```

Scripts degrade gracefully if dependencies are missing — they will return a clear error message instead of crashing.

## Output Structure

Every evaluation produces:
1. **Executive Summary** (250 words)
2. **Input Overview** with assumptions declared
3. **Framework Selection Rationale**
4. **Per-Framework Analysis** (scored 1–5 per dimension)
5. **Cross-Framework Synthesis** (convergent findings, contradictions)
6. **Priority Matrix** (Strengths, Risks, Opportunities, Actions)
7. **Recommended Next Steps** (with owner + timeline)
8. **Appendix A**: Score Summary Table
9. **Appendix B**: Evidence References

## Version

v1.0.0 — Initial release
