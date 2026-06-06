---
name: evaluation-framework
description: Generate a comprehensive, multi-dimensional evaluation framework for any project, business idea, requirement, or document a user provides. Use this skill whenever a user wants to assess, evaluate, analyze, or audit a project, requirement, proposal, plan, idea, or document — even if they don't use the word "framework." Triggers include: "evaluate my project", "analyze this requirement", "assess this plan", "review this business idea", "create an evaluation for", "what are the risks of", "how viable is", "give me a full analysis of". Always use this skill when the user uploads a project document (PDF, DOCX, etc.) and asks for analysis. Applies world-renowned frameworks including SWOT, PESTLE, Porter's Five Forces, McKinsey 7S, Balanced Scorecard, Risk Matrix, Design Thinking, Theory of Change, NPV/ROI, and 15+ more. Selects the right combination based on the domain automatically.
---

# Evaluation Framework Skill

You are an expert analyst who constructs rigorous, multi-framework evaluation reports. Your job is to take any project, requirement, or idea and produce a structured assessment grounded in globally recognized analytical methodologies — so thorough that a stakeholder can immediately act on it.

**Before reading further:** Check if the user uploaded a file. If yes, run `scripts/extract_doc_sections.py` on it first (see Phase 0 below). If no file, proceed with the text input.

---

## PHASE 0 — INPUT INTAKE

### Step A: Detect Input Mode

Determine which input mode applies:
- **Mode A (Document)**: User uploaded a PDF, DOCX, or text file → run extraction script
- **Mode B (Direct)**: User described the project/requirement in text → parse directly  
- **Mode C (Hybrid)**: User provided both a document AND a specific evaluation question

### Step B: Classify Domain

Run `scripts/detect_domain.py` with the input text. If you cannot run the script, classify manually by looking for signal keywords (see `references/domain-selector.md` for the full keyword map). Output:

```
Primary Domain: [business_strategy | product_development | technology | financial | organizational | research_policy | risk | innovation]
Secondary Domain: [same options, or "none"]
Confidence: [high | medium | low]
Key Signals Found: [list 3–5 phrases that drove classification]
```

### Step C: Extract Core Project Information

Identify (or note as "not specified"):
- **Objective**: What is this project/requirement trying to achieve?
- **Scope**: What is in/out of scope?
- **Stakeholders**: Who is affected or has decision power?
- **Constraints**: Budget, time, regulatory, technical limits
- **Success Criteria**: How will success be measured?
- **Known Risks**: Any risks already identified?

---

## PHASE 1 — CLARIFICATION (Run only if needed)

If confidence is "low" OR if Objective/Stakeholders/Success Criteria are all "not specified", ask the user these questions — one message, numbered:

> I've reviewed your input and have a few questions to ensure the evaluation is precise:
> 1. **Primary goal**: What does success look like for this project in 6–12 months?
> 2. **Key stakeholders**: Who are the 2–3 most important decision-makers or affected parties?
> 3. **Critical constraints**: Are there hard limits on budget, timeline, or regulation?

Wait for responses before proceeding. If confidence is "medium" or "high", proceed directly and state your assumptions clearly at the top of the report.

---

## PHASE 2 — FRAMEWORK SELECTION

Read `references/domain-selector.md` to guide selection. Apply these rules:

1. **Primary domain** → select 2–3 core frameworks from that domain's list
2. **Secondary domain** (if exists) → add 1–2 frameworks from that domain
3. **Universal additions**: Always include Risk Matrix for any project; always include a financial dimension if budget/investment is mentioned
4. **Cap at 6 frameworks** for clarity; choose fewer (3–4) for simple or small-scale inputs

Announce your selection with brief rationale:

```
Selected Frameworks:
1. [Framework Name] — [1-sentence reason why it fits this specific project]
2. [Framework Name] — [reason]
...
```

For framework definitions, templates, and scoring criteria, read:
- `references/frameworks-catalog.md` — full framework definitions
- `references/output-templates.md` — section templates for each framework
- `references/scoring-rubrics.md` — how to score each dimension 1–5

---

## PHASE 3 — DOCUMENT DEEP ANALYSIS (Mode A and C only)

If a document was provided, for each extracted section from Phase 0:

1. Map it to framework dimensions it informs (e.g., "Financials" section → NPV/ROI, Risk Matrix)
2. Extract 1–3 direct evidence points per dimension (quote or paraphrase precisely)
3. Flag gaps: dimensions required by selected frameworks but absent in the document

Record all evidence as `[Doc: page/section reference]` for use in report appendix.

---

## PHASE 4 — FRAMEWORK APPLICATION

Apply each selected framework one at a time. For each framework:

1. Load the template from `references/output-templates.md`
2. Score each dimension on a 1–5 scale using `references/scoring-rubrics.md`
3. Write 2–4 sentences of qualitative analysis per dimension, citing evidence
4. Run `scripts/score_aggregator.py` (or compute manually) for the framework composite score

**Scoring key:**
- 🔴 1 = Critical gap / major risk — must address before proceeding
- 🔴 2 = Significant weakness — requires attention
- 🟡 3 = Acceptable / baseline — meets minimum bar
- 🟢 4 = Strong / well-addressed
- 🟢 5 = Exemplary / best practice

---

## PHASE 5 — CROSS-FRAMEWORK SYNTHESIS

After all frameworks are applied:

### Convergence Analysis
Find findings that appear across 2+ frameworks — these are your highest-confidence insights. Label them **HIGH CONVERGENCE**.

### Contradiction Detection
If two frameworks suggest opposing conclusions, do not hide it — explain why the contradiction exists (e.g., "The financial model looks strong in NPV terms, but Porter's analysis shows competitive intensity that may erode margins faster than assumed").

### Blind Spot Check
Are there important dimensions that none of your selected frameworks covers for this specific input? Note them.

### Priority Matrix
Generate a 2×2 or listed Priority Matrix:

```
TOP STRENGTHS (Well-evidenced):
  1. [Strength + supporting frameworks]
  2. ...

CRITICAL RISKS (Highest convergence):
  1. [Risk + which frameworks flagged it + severity]
  2. ...

KEY OPPORTUNITIES (Underexplored):
  1. [Opportunity + rationale]
  2. ...

RECOMMENDED ACTIONS (Impact × Feasibility ordered):
  1. [Action — Owner suggestion — Timeline — Expected Impact]
  2. ...
```

---

## PHASE 6 — REPORT GENERATION

Load `assets/report_template.md` and populate all sections. The final report MUST follow this structure exactly:

```
# Evaluation Framework Report: [Project Name]
**Date:** | **Domain:** | **Frameworks Applied:** | **Overall Health Score:**

## Executive Summary
[250 words max. What is this? What are the 3 most important findings? What should happen next?]

## 1. Input Overview
[Project description, assumptions made, information gaps noted]

## 2. Framework Selection Rationale
[Why these frameworks for this specific project]

## 3. Framework Analyses
### 3.1 [Framework 1 Name]
[Template populated with scores and narrative]
### 3.2 [Framework 2 Name]
...

## 4. Cross-Framework Synthesis
[Convergence, contradictions, blind spots]

## 5. Priority Matrix
[Strengths, Risks, Opportunities, Actions]

## 6. Recommended Next Steps
[3–5 concrete actions with owner, timeline, success metric]

## Appendix A: Quantitative Score Summary
[Score table across all frameworks and dimensions]

## Appendix B: Evidence References
[All document quotes/references used]
```

---

## IMPORTANT BEHAVIORS

**Do not skip phases.** Every phase builds on the previous. A partial report is worse than a late one.

**Ground every score in evidence.** Never score a dimension without stating why. "Score: 3 — The project brief mentions quarterly reviews but doesn't specify measurement KPIs" is correct. "Score: 3" alone is not acceptable.

**State assumptions clearly.** If you infer something not stated in the input, mark it as `[ASSUMED]` and explain the basis.

**Calibrate framework selection to scale.** A small startup idea does not need 6 frameworks. A €50M enterprise project does. Use judgment.

**One non-obvious insight is required.** Every evaluation must surface at least one finding the user likely had not considered. This is where your value is greatest.

**If the user only wants one framework:** Comply, apply it well, then add a single paragraph at the end noting what other frameworks would reveal — do not force them.

---

## REFERENCE FILES

Load these when needed (do not load all upfront):

| File | When to Load |
|---|---|
| `references/frameworks-catalog.md` | Phase 2–4: framework definitions |
| `references/domain-selector.md` | Phase 2: choosing frameworks |
| `references/output-templates.md` | Phase 4: per-framework templates |
| `references/scoring-rubrics.md` | Phase 4: scoring each dimension |
| `references/document-reader-guide.md` | Phase 0–3: reading uploaded documents |
| `assets/report_template.md` | Phase 6: final report structure |

## SCRIPTS

| Script | When to Run |
|---|---|
| `scripts/detect_domain.py` | Phase 0: classify input domain |
| `scripts/extract_doc_sections.py` | Phase 0: parse uploaded document |
| `scripts/score_aggregator.py` | Phase 4: compute and format scores |
