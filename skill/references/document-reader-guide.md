# Document Reader Guide

_Load during Phase 0–3 when the user has uploaded a file. Guides extraction of key information from project documents._

---

## Step 1: Identify File Type and Reading Strategy

| File Type | Reading Approach |
|---|---|
| `.pdf` | Run `scripts/extract_doc_sections.py --file path.pdf` — extracts text by section |
| `.docx` | Run `scripts/extract_doc_sections.py --file path.docx` — extracts headings + body |
| `.txt` / `.md` | Read directly; parse headings and bullet lists as section boundaries |
| Very long (> 20 pages) | Extract first 2 pages + table of contents + all section headers + last 1 page |

---

## Step 2: Map Document to Information Targets

For any project document, attempt to extract the following. Mark each as **Found / Partial / Not Found**:

| Information Target | What to Look For |
|---|---|
| **Project Name / Title** | Document title, header, cover page |
| **Objective / Goal** | "Purpose", "Objective", "Goal", "Mission", "Aim", "We seek to..." |
| **Scope** | "In scope", "Out of scope", "Boundaries", "Coverage", "Included / Excluded" |
| **Stakeholders** | "Stakeholders", "Sponsors", "Users", "Clients", "Partners", "Key contacts" |
| **Timeline / Milestones** | Dates, phases, "by Q[X]", "launch date", Gantt charts, milestone tables |
| **Budget / Financial** | "$", "budget", "cost", "investment", "funding", "allocation" |
| **Success Criteria / KPIs** | "Success criteria", "KPIs", "metrics", "targets", "acceptance criteria" |
| **Known Risks** | "Risks", "assumptions", "dependencies", "concerns", "constraints" |
| **Methodology / Approach** | "How we will...", "approach", "methodology", "process", "phases" |
| **Team / Resources** | Team structure, headcount, roles, skills |
| **Technical Specs** | Architecture diagrams, system requirements, technical constraints |
| **Market / Context** | Market size, competitors, customer research, context setting |

---

## Step 3: Section Header Patterns to Recognize

Documents use many different labels for the same content. Map these to the correct target:

| Common Header Variations | Maps To |
|---|---|
| "Executive Summary", "Overview", "Introduction", "Abstract" | Objective |
| "Deliverables", "In Scope", "Project Scope", "Coverage" | Scope |
| "Project Team", "Governance", "Accountability", "RACI" | Stakeholders |
| "Timeline", "Schedule", "Gantt", "Roadmap", "Phases", "Milestones" | Timeline |
| "Budget", "Cost Estimate", "Financial Plan", "Resource Allocation" | Financial |
| "KPIs", "Metrics", "Goals", "OKRs", "Success Factors", "Acceptance" | Success Criteria |
| "Risk Register", "Risk Assessment", "Issues & Risks", "Assumptions" | Risks |
| "Approach", "Methodology", "How We Work", "Process" | Methodology |
| "Technical Architecture", "System Design", "Tech Stack" | Technical Specs |
| "Background", "Context", "Business Case", "Problem Statement" | Context/Objective |

---

## Step 4: Extraction Quality Checklist

After extracting, verify:

- [ ] At least 3 of the 12 information targets are Found or Partial
- [ ] The project name/title is identified (or ask user)
- [ ] The primary objective is at least partially clear
- [ ] If fewer than 3 targets found → enter Clarification Mode (Phase 1) immediately

---

## Step 5: Evidence Tagging

When you extract a piece of text to use as evidence in a framework score, tag it like this:

```
[Doc: Section "Risks", Page 4] "The primary risk is regulatory approval timelines which may delay launch by 3–6 months."
```

Use these tags in:
- Phase 3: Document Deep Analysis
- Phase 4: Framework scoring evidence citations
- Appendix B of the final report

---

## Step 6: Gap Analysis After Extraction

For each information target that is "Not Found", note it as a gap. In the report, under **Section 1: Input Overview**, list:

```
Information Gaps (not present in document):
- Budget / financial data: [ASSUMED] Based on project scope, estimated at $[X]
- Success criteria: [ASSUMED] Standard KPIs for [domain] applied
- Timeline: Not specified — recommend defining within 30 days of project kickoff
```

Never silently fill gaps without flagging them. Assumptions are acceptable when labeled.

---

## Special Document Types

### Business Plan / Pitch Deck
- Prioritize: Problem, Solution, Market Size, Revenue Model, Team, Traction
- Automatically trigger: Lean Canvas, SWOT, NPV/ROI frameworks
- Watch for: Overclaiming market size, underestimating competition

### Technical Architecture Document
- Prioritize: System diagram, component list, non-functional requirements, integration points
- Automatically trigger: TOGAF ADM, DevSecOps Maturity, Risk Matrix
- Watch for: Missing security architecture, undocumented external dependencies

### Program / Project Brief (Policy)
- Prioritize: Problem statement, target beneficiaries, intervention logic, evaluation plan
- Automatically trigger: Theory of Change, Risk Matrix, Cost-Benefit Analysis
- Watch for: Unvalidated assumptions in the intervention logic

### Product Requirements Document (PRD)
- Prioritize: User stories, acceptance criteria, functional/non-functional requirements, personas
- Automatically trigger: JTBD, Design Thinking, Kano Model, OKR Alignment
- Watch for: Solution-first framing with no user research cited

### Investment Memo / Business Case
- Prioritize: Financial projections, market analysis, competitive landscape, return expectations
- Automatically trigger: NPV/ROI, Porter's Five Forces, PESTLE, Risk Matrix
- Watch for: Overly optimistic projections, missing sensitivity analysis
