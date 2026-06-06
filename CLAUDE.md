# Evaluation Framework Skill — Project Overview

## What This Project Does

This project builds a **Claude Skill** that enables AI agents to generate comprehensive, standards-based evaluation frameworks for any project or requirement a user provides. The skill applies world-renowned research and analysis methodologies — SWOT, PESTLE, Balanced Scorecard, OKR alignment, Risk Matrices, McKinsey 7S, Porter's Five Forces, Design Thinking, and more — to produce structured, actionable assessment reports.

The skill handles two primary input modes:
1. **Project Documents** — reads uploaded docs, specs, or briefings and derives evaluation criteria from them
2. **Direct Requirements** — user describes a requirement or goal in natural language; the skill interprets and frames it

## Core Design Principles

- **Harness-first**: every step in the workflow is guided by explicit instructions; the AI agent never guesses
- **Framework plurality**: no single methodology is applied alone — frameworks are selected and combined based on the input type (business, tech, product, policy, research, etc.)
- **Iterative refinement**: the skill prompts the agent to ask clarifying questions before locking in the framework
- **Progressive disclosure**: sub-skills are loaded only when needed, keeping context lean
- **Output fidelity**: every output section maps to a named framework with clear rationale

## Repository Structure

```
evaluation-framework-skill/
├── CLAUDE.md                            ← You are here
├── PROJECT-detail.md                    ← Full project specification
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md ← Live development tracker
├── skill/
│   ├── SKILL.md                         ← Main skill entrypoint (Claude reads this)
│   ├── references/
│   │   ├── frameworks-catalog.md        ← Full catalog of 20+ evaluation frameworks
│   │   ├── domain-selector.md           ← How to choose frameworks by domain
│   │   ├── document-reader-guide.md     ← How to parse uploaded project documents
│   │   ├── output-templates.md          ← Standardized report section templates
│   │   └── scoring-rubrics.md           ← Quantitative scoring guidance
│   ├── scripts/
│   │   ├── detect_domain.py             ← Heuristic: classify input as biz/tech/product/policy/research
│   │   ├── extract_doc_sections.py      ← Extract key sections from uploaded documents
│   │   └── score_aggregator.py          ← Aggregate scores across framework dimensions
│   └── assets/
│       └── report_template.md           ← Final report skeleton
├── evals/
│   └── evals.json                       ← Test cases for skill validation
└── README.md
```

## Key Frameworks Covered

| Category | Frameworks |
|---|---|
| Strategic | SWOT, PESTLE, Porter's Five Forces, Ansoff Matrix |
| Organizational | McKinsey 7S, Balanced Scorecard, OKR Alignment |
| Risk | Risk Matrix (Likelihood × Impact), FMEA, Monte Carlo framing |
| Innovation | Design Thinking, Jobs-To-Be-Done, Blue Ocean |
| Technical | TOGAF ADM, C4 Architecture Assessment, DevSecOps Maturity |
| Research | Theory of Change, Logic Model, Program Evaluation |
| Financial | NPV/ROI Framework, Cost-Benefit Analysis, Payback Period |

## How the Skill Workflow Flows

```
User Input
    │
    ▼
[INTAKE] Classify input type + domain
    │
    ▼
[CLARIFY] Ask 2-3 targeted questions if ambiguous
    │
    ▼
[SELECT] Choose 3-5 best-fit frameworks from catalog
    │
    ▼
[ANALYZE] Apply each framework section by section
    │
    ▼
[SCORE] Generate quantitative + qualitative scores
    │
    ▼
[SYNTHESIZE] Cross-framework findings + priority matrix
    │
    ▼
[REPORT] Render structured output with Executive Summary
```

## Development Environment

- Language: Python 3.10+
- Dependencies: `pypdf`, `python-docx`, `tabulate`, `rich`
- No external API calls required (fully self-contained)
- Skill runs inside Claude Code or Claude.ai with computer use

## Quick Start for Developers

1. Read `PROJECT-detail.md` for the full specification
2. Check `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` for current phase
3. The main skill logic lives in `skill/SKILL.md`
4. Framework definitions are in `skill/references/frameworks-catalog.md`
5. Test cases are in `evals/evals.json`
