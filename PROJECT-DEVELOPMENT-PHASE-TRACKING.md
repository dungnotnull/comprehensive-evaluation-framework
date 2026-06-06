# PROJECT-DEVELOPMENT-PHASE-TRACKING.md

_Last Updated: 2026-06-04_

---

## Project: Evaluation Framework Skill
**Version:** 1.0.0  
**Status:** ✅ Phase 1–4 Complete | 🔄 Phase 5 In Progress

---

## Phase Overview

| Phase | Name | Status | Deliverables |
|---|---|---|---|
| 1 | Architecture & Design | ✅ Done | CLAUDE.md, PROJECT-detail.md, this file |
| 2 | Core Skill File | ✅ Done | skill/SKILL.md |
| 3 | Reference Library | ✅ Done | frameworks-catalog.md, domain-selector.md, output-templates.md, scoring-rubrics.md |
| 4 | Supporting Scripts | ✅ Done | detect_domain.py, extract_doc_sections.py, score_aggregator.py |
| 5 | Report Template & Assets | ✅ Done | report_template.md |
| 6 | Evaluation & Testing | 🔲 Planned | evals.json, test runs, iteration |
| 7 | Description Optimization | 🔲 Planned | Optimized SKILL.md frontmatter |
| 8 | Packaging | 🔲 Planned | .skill bundle |

---

## Phase 1: Architecture & Design ✅

**Goal:** Define scope, design the harness flow, document all specifications.

**Completed:**
- [x] Problem statement and user personas defined
- [x] Input mode classification (Document / Direct Requirement / Hybrid)
- [x] Domain taxonomy with 8 domains mapped
- [x] Framework catalog planned (20+ frameworks)
- [x] 6-phase harness flow designed
- [x] Output specification finalized
- [x] Script specifications written
- [x] CLAUDE.md created
- [x] PROJECT-detail.md created
- [x] This tracking file created

---

## Phase 2: Core Skill File ✅

**Goal:** Write the main SKILL.md that agents will follow.

**Completed:**
- [x] YAML frontmatter (name, description)
- [x] Phase 0–6 harness instructions
- [x] Clarification question templates
- [x] Framework selection decision logic
- [x] Pointers to all reference files
- [x] Error/edge case handling instructions

---

## Phase 3: Reference Library ✅

**Goal:** Build the detailed reference documents agents load as needed.

**Completed:**
- [x] `frameworks-catalog.md` — Full definitions for 20+ frameworks
- [x] `domain-selector.md` — Decision logic for framework selection
- [x] `output-templates.md` — Per-framework section templates
- [x] `scoring-rubrics.md` — 1–5 scale definitions for each framework dimension
- [x] `document-reader-guide.md` — How to parse uploaded documents

---

## Phase 4: Supporting Scripts ✅

**Goal:** Write Python scripts that make the skill deterministic and efficient.

**Completed:**
- [x] `detect_domain.py` — Domain classification from text
- [x] `extract_doc_sections.py` — Document section extractor
- [x] `score_aggregator.py` — Score computation and markdown table generator

---

## Phase 5: Report Template ✅

**Goal:** Create the final report skeleton agents populate.

**Completed:**
- [x] `assets/report_template.md` — Full report skeleton with placeholders

---

## Phase 6: Evaluation & Testing 🔲

**Goal:** Run test cases, evaluate quality, iterate on skill.

**Planned Test Cases:**
1. Business strategy input: startup pitch document (PDF)
2. Tech architecture input: system migration requirement description
3. Policy/research input: government program brief
4. Ambiguous/vague input: minimal single-paragraph requirement
5. Hybrid input: product requirement doc + specific evaluation question

**Success Criteria:**
- [ ] Framework selection matches domain correctly (> 90% of cases)
- [ ] All 6 report sections present and populated
- [ ] At least one non-obvious insight per report
- [ ] Scores grounded in evidence (not generic)
- [ ] Report completable in one session

---

## Phase 7: Description Optimization 🔲

**Goal:** Maximize trigger accuracy for the skill.

**Planned:**
- [ ] Generate 20 trigger eval queries (10 should-trigger, 10 should-not)
- [ ] Run `run_loop.py` optimization
- [ ] Apply best description to SKILL.md frontmatter
- [ ] Target: > 85% trigger accuracy

---

## Phase 8: Packaging 🔲

**Goal:** Bundle the skill for distribution.

**Planned:**
- [ ] Run `package_skill.py`
- [ ] Generate `.skill` file
- [ ] Document installation instructions
- [ ] README.md finalized

---

## Known Issues & Decisions

| Date | Issue | Decision |
|---|---|---|
| 2026-06-04 | Very long documents (> 20 pages) may exceed context | extract_doc_sections.py reads first 8000 tokens + key section headers |
| 2026-06-04 | Mixed-domain inputs need multi-framework coverage | Skill selects up to 6 frameworks max; always notes primary vs. secondary |
| 2026-06-04 | Scoring subjectivity | Each 1–5 dimension has explicit rubric criteria in scoring-rubrics.md |

---

## Iteration Log

| Iteration | Date | Changes | Outcome |
|---|---|---|---|
| v0.1 | 2026-06-04 | Initial design + all core files | Baseline created |

---

## Contributor Notes

- All reference files should stay under 400 lines each (use sub-files if needed)
- Scripts must handle missing inputs gracefully with clear error messages
- Every framework in the catalog must have: definition, dimensions, template, scoring criteria
- Do not add frameworks without adding corresponding output template and scoring rubric
