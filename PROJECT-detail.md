# PROJECT-detail.md — Evaluation Framework Skill

## 1. Project Vision

Build a reusable Claude Skill that, given any project document or requirement description, automatically constructs a **comprehensive, multi-dimensional evaluation framework** grounded in globally recognized research and analysis methodologies. The output is a structured assessment report that stakeholders can immediately act on.

---

## 2. Problem Statement

When analysts, product managers, strategists, or researchers receive a new project or requirement, they face:

- **Framework selection paralysis**: dozens of methodologies exist; choosing the right ones takes expertise
- **Incomplete coverage**: single-framework analyses miss blind spots (e.g., doing only SWOT ignores macro forces that PESTLE captures)
- **Inconsistent quality**: assessments depend heavily on individual analyst skill
- **Time cost**: building a thorough evaluation from scratch takes 4–12 hours for a skilled analyst

This skill compresses that work to minutes while maintaining or exceeding the depth of an expert analyst.

---

## 3. Target Users

| User Type | Example Use Case |
|---|---|
| Product Manager | Evaluate a new feature requirement before committing to sprint |
| Business Analyst | Assess a client project for feasibility and risk |
| Startup Founder | Evaluate a business idea across strategic dimensions |
| Policy Researcher | Assess a government program proposal |
| Tech Lead | Evaluate a system architecture proposal or migration plan |
| Academic Researcher | Structure an evaluation framework for a research program |

---

## 4. Input Specifications

### 4.1 Input Mode A: Document Upload
- Accepts: `.pdf`, `.docx`, `.txt`, `.md`
- The skill reads the document and extracts: objectives, scope, constraints, stakeholders, timeline, success criteria
- Falls back to asking the user for missing elements

### 4.2 Input Mode B: Direct Requirement Description
- User describes the project/requirement in 1 paragraph to several pages
- Skill identifies domain, scale, and nature of the requirement
- Asks 2–3 clarifying questions if critical information is missing

### 4.3 Input Mode C: Hybrid
- User provides a document AND a specific evaluation question (e.g., "Is this product launch plan financially viable?")
- Skill focuses evaluation around the question while using the document as context

---

## 5. Domain Classification System

The skill first classifies the input into a primary domain to select appropriate frameworks:

| Domain | Signal Keywords / Patterns | Primary Frameworks |
|---|---|---|
| Business Strategy | market, revenue, competition, growth, M&A | SWOT, PESTLE, Porter's Five Forces, Ansoff |
| Product Development | feature, user story, MVP, sprint, product-market fit | Jobs-To-Be-Done, Design Thinking, Kano Model |
| Technology / Architecture | system, API, microservices, infrastructure, migration | TOGAF ADM, C4 Assessment, DevSecOps Maturity |
| Financial Investment | ROI, NPV, payback, budget, cost | NPV/ROI, Cost-Benefit, Payback, Sensitivity Analysis |
| Organizational Change | transformation, culture, restructuring, team | McKinsey 7S, Lewin Change Model, ADKAR |
| Research / Policy | program, intervention, theory, outcomes, evidence | Theory of Change, Logic Model, Kirkpatrick, REALIST |
| Risk Management | risk, compliance, security, audit, regulation | Risk Matrix, FMEA, Bow-Tie Analysis |
| Innovation | new idea, startup, disruptive, market creation | Blue Ocean, JTBD, Design Thinking, Lean Canvas |

Mixed signals → skill selects frameworks from multiple domains and notes the overlap.

---

## 6. Framework Catalog (Summary)

Full definitions and templates are in `references/frameworks-catalog.md`. Summary:

### Strategic Frameworks
- **SWOT**: Strengths, Weaknesses, Opportunities, Threats — internal vs. external, helpful vs. harmful
- **PESTLE**: Political, Economic, Social, Technological, Legal, Environmental macro-analysis
- **Porter's Five Forces**: Competitive intensity, supplier/buyer power, substitutes, new entrants
- **Ansoff Matrix**: Market penetration, development, product development, diversification

### Organizational Frameworks
- **McKinsey 7S**: Strategy, Structure, Systems, Shared Values, Skills, Style, Staff — alignment check
- **Balanced Scorecard**: Financial, Customer, Internal Process, Learning & Growth perspectives
- **OKR Alignment Audit**: Are objectives measurable, time-bound, outcome-focused?

### Risk Frameworks
- **Risk Matrix**: Likelihood × Impact grid with mitigation paths
- **FMEA**: Failure Mode and Effects Analysis — severity × occurrence × detectability
- **Bow-Tie Analysis**: Causes → hazard → consequences with barriers

### Innovation Frameworks
- **Design Thinking Assessment**: Empathize, Define, Ideate, Prototype, Test — maturity per phase
- **Blue Ocean Canvas**: Eliminate, Reduce, Raise, Create factors vs. competition
- **Lean Canvas**: Problem, Solution, UVP, Channels, Revenue, Costs, Key Metrics, Unfair Advantage

### Technical Frameworks
- **TOGAF ADM Phase Review**: Architecture vision, business, info systems, tech architecture, governance
- **DevSecOps Maturity Model**: Culture, CI/CD, Security, Monitoring, Feedback loops
- **C4 Architecture Assessment**: Context, Container, Component, Code clarity and risk

### Research / Evaluation Frameworks
- **Theory of Change**: Inputs → Activities → Outputs → Outcomes → Impact chain
- **Kirkpatrick Model**: Reaction, Learning, Behavior, Results — program effectiveness
- **Logic Model**: Resources, Activities, Outputs, Short/Long-term Outcomes

### Financial Frameworks
- **NPV / ROI Analysis**: Net Present Value calculation and Return on Investment
- **Cost-Benefit Analysis**: Quantified benefits vs. costs with benefit-cost ratio
- **Payback Period + Sensitivity**: Break-even timeline and scenario sensitivity

---

## 7. Skill Workflow — Detailed Harness Flow

### Phase 0: INPUT INTAKE
```
AGENT ACTION:
1. Detect if user has uploaded a file → if yes, run extract_doc_sections.py
2. If no file: parse user text for domain signals
3. Run detect_domain.py to classify primary + secondary domains
4. Output: domain_classification.json (domain, confidence, signals_found)
```

### Phase 1: CLARIFICATION (conditional)
```
IF confidence < 0.7 OR critical fields missing:
  Ask user maximum 3 questions (one at a time if conversational):
  - What is the primary goal / desired outcome?
  - Who are the key stakeholders?
  - What constraints exist (budget, time, regulation)?
ELSE:
  Proceed with extracted information, state assumptions clearly
```

### Phase 2: FRAMEWORK SELECTION
```
Read references/domain-selector.md
Select 3–6 frameworks based on:
  - Primary domain (2–3 core frameworks)
  - Secondary domain if exists (1–2 frameworks)
  - Complexity of project (simple → fewer; enterprise → more)
  - User's stated focus (risk, innovation, strategy, etc.)
Output: selected_frameworks list with rationale for each
```

### Phase 3: DOCUMENT DEEP ANALYSIS
```
IF document was provided:
  For each extracted section:
    - Identify which framework dimensions it informs
    - Extract evidence quotes for scoring
    - Flag gaps (sections present in framework but missing in doc)
```

### Phase 4: FRAMEWORK APPLICATION
```
For each selected framework:
  Load template from references/output-templates.md
  Apply framework section by section:
    - Use document evidence where available
    - Use domain knowledge to infer where evidence gaps exist
    - Generate quantitative scores (1–5 scale) per dimension
    - Generate qualitative narrative per dimension
  Run score_aggregator.py to compute framework-level scores
```

### Phase 5: CROSS-FRAMEWORK SYNTHESIS
```
Identify:
  - Convergent findings (multiple frameworks flag same issue → high priority)
  - Contradictions (frameworks suggest opposing conclusions → note and explain)
  - Blind spots (dimensions no framework covers → flag as risk)
Generate Priority Matrix:
  - Top 3 Strengths (well-evidenced)
  - Top 3 Critical Risks (highest convergence)
  - Top 3 Opportunities (underexplored but high-potential)
  - Top 3 Recommended Actions (sequenced by impact × feasibility)
```

### Phase 6: REPORT GENERATION
```
Load report_template.md from assets/
Populate all sections:
  1. Executive Summary (250 words max)
  2. Input Overview + Assumptions
  3. Framework Selection Rationale
  4. Per-Framework Analysis (one section per framework)
  5. Cross-Framework Synthesis
  6. Priority Matrix
  7. Recommended Next Steps (with ownership + timeline suggestions)
  8. Appendix: Scoring Tables + Evidence References
```

---

## 8. Output Specification

### 8.1 Report Structure (Always Produced)
```
# Evaluation Framework Report: [Project/Requirement Name]
## Executive Summary
## 1. Input Overview
## 2. Framework Selection & Rationale
## 3. Framework Analyses
   ### 3.1 [Framework Name]
   ### 3.2 [Framework Name]
   ...
## 4. Cross-Framework Synthesis
## 5. Priority Matrix
## 6. Recommended Next Steps
## Appendix A: Quantitative Score Summary
## Appendix B: Evidence References
```

### 8.2 Scoring System
- Each framework dimension scored 1–5:
  - 1 = Critical gap / major risk
  - 2 = Significant weakness / concern
  - 3 = Acceptable / baseline
  - 4 = Strong / well-addressed
  - 5 = Exemplary / best practice
- Scores aggregated to framework-level composite
- Color coding in output: 🔴 1–2, 🟡 3, 🟢 4–5

### 8.3 Output Formats
- Primary: Structured Markdown (inline in conversation)
- Optional: `.docx` if user requests downloadable report
- Optional: JSON scoring summary for integration with other tools

---

## 9. Supporting Scripts

### `detect_domain.py`
- Input: raw text string
- Output: JSON `{domain, confidence, secondary_domain, signals}`
- Method: keyword frequency + co-occurrence pattern matching

### `extract_doc_sections.py`
- Input: file path (pdf/docx/txt)
- Output: JSON with extracted sections: `{objectives, scope, constraints, stakeholders, timeline, success_criteria, risks_mentioned, financials}`
- Libraries: `pypdf`, `python-docx`

### `score_aggregator.py`
- Input: list of `{dimension, score, evidence}` objects
- Output: `{framework_score, dimension_breakdown, weakest_area, strongest_area}`
- Produces both numeric summary and markdown table

---

## 10. Quality Criteria

A high-quality output from this skill must:
1. Select frameworks appropriate to the domain (not generic defaults every time)
2. Ground every score in specific evidence from the input (not generic statements)
3. Identify at least one insight the user likely had not considered
4. Produce actionable recommendations (not vague "improve X")
5. Be internally consistent (no contradicting conclusions across sections)
6. Be completable in a single Claude session (no orphaned partial reports)

---

## 11. Limitations & Edge Cases

| Situation | Handling |
|---|---|
| Input too vague (< 50 words) | Enter clarification mode; do not proceed to frameworks |
| Domain is ambiguous | Apply 2 frameworks from each plausible domain; note ambiguity |
| Document is very long (> 20 pages) | Extract key sections only; flag what was not read |
| User wants only one specific framework | Comply, but note what other frameworks would add |
| Non-English document | Note limitation; proceed if English content is sufficient |
| Highly technical / niche domain | Apply general frameworks; flag need for domain expert review |
