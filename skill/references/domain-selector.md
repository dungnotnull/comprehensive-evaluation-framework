# Domain Selector — Framework Selection Guide

_Load during Phase 2 of the evaluation-framework skill._

---

## How to Use This File

1. You already have `domain_classification` from Phase 0 (primary domain, secondary domain, confidence)
2. Find the primary domain section below → get your core framework list
3. Find the secondary domain section (if any) → add 1–2 more frameworks
4. Apply the modifiers at the bottom for special contexts
5. Cap total at 6 frameworks; prioritize depth over breadth

---

## Domain → Framework Mapping

### BUSINESS_STRATEGY

**Core Frameworks (always pick 2–3):**
- SWOT Analysis — universal baseline; always include
- PESTLE Analysis — if market entry, expansion, or macro sensitivity is relevant
- Porter's Five Forces — if competitive landscape matters
- Ansoff Matrix — if growth direction is the key decision
- Balanced Scorecard — if execution and performance tracking is the focus

**Secondary Add-ons:**
- Risk Matrix — add if the strategy involves significant uncertainty or investment
- Blue Ocean Canvas — add if the strategy claims to be differentiated or disruptive

**Avoid:** Kirkpatrick (training-specific), TOGAF (tech-specific), FMEA (engineering-specific)

**Example signals:** "market strategy", "business plan", "competitive advantage", "market entry", "growth plan", "expansion", "go-to-market", "revenue model", "customer acquisition"

---

### PRODUCT_DEVELOPMENT

**Core Frameworks (always pick 2–3):**
- Jobs-To-Be-Done — if the product is solving a user problem
- Design Thinking Assessment — if UX/human-centered approach is important
- Kano Model — if feature prioritization is the key decision
- Lean Canvas — if this is an early-stage product or startup
- OKR Alignment Audit — if the team has defined objectives for this product

**Secondary Add-ons:**
- Risk Matrix — always add for product launches
- SWOT — add if competitive positioning matters

**Avoid:** PESTLE (unless regulatory environment is a key constraint), Kirkpatrick

**Example signals:** "product", "feature", "user story", "MVP", "sprint", "roadmap", "user experience", "prototype", "product-market fit", "requirements"

---

### TECHNOLOGY

**Core Frameworks (always pick 2–3):**
- DevSecOps Maturity Model — if the project involves software development or engineering
- TOGAF ADM Review — if the project involves enterprise architecture or large system design
- Risk Matrix — always include for technology projects; security and technical debt are key risks
- FMEA — if the system is mission-critical or has safety implications

**Secondary Add-ons:**
- Balanced Scorecard — add if the tech initiative has business performance goals
- McKinsey 7S — add if organizational change accompanies the tech change

**Avoid:** Kirkpatrick (unless training component), Blue Ocean (unless tech strategy)

**Example signals:** "system", "API", "architecture", "microservices", "cloud", "migration", "infrastructure", "DevOps", "CI/CD", "software", "database", "integration", "platform"

---

### FINANCIAL

**Core Frameworks (always pick 2–3):**
- NPV / ROI Framework — always include when investment decision is being made
- Cost-Benefit Analysis — include for public sector, policy, or large capital projects
- Risk Matrix — financial risk deserves explicit risk scoring

**Secondary Add-ons:**
- Balanced Scorecard — add if financial performance is being tracked alongside non-financial metrics
- SWOT — add if the financial viability depends on strategic positioning

**Avoid:** Design Thinking, JTBD, Kirkpatrick, TOGAF

**Example signals:** "budget", "investment", "ROI", "revenue", "cost", "financial model", "funding", "valuation", "profit", "payback", "NPV", "IRR", "capital"

---

### ORGANIZATIONAL

**Core Frameworks (always pick 2–3):**
- McKinsey 7S — always include for organizational change; identifies alignment gaps
- Balanced Scorecard — if performance measurement is part of the initiative
- OKR Alignment Audit — if the org is setting or reviewing goals

**Secondary Add-ons:**
- Risk Matrix — change management always carries people/culture risk
- SWOT — add if the organizational change is strategic

**Avoid:** FMEA, TOGAF, Blue Ocean (unless org is pursuing market disruption)

**Example signals:** "restructuring", "transformation", "culture change", "team", "leadership", "people", "organization", "change management", "talent", "capability", "operating model"

---

### RESEARCH_POLICY

**Core Frameworks (always pick 2–3):**
- Theory of Change — always include; it is the gold standard for program logic
- Kirkpatrick Model — include if there is a training, learning, or capacity-building component
- Risk Matrix — policy initiatives carry implementation and political risk

**Secondary Add-ons:**
- Cost-Benefit Analysis — add if program involves public funding or resource allocation
- Balanced Scorecard — add if program has multiple stakeholder performance dimensions
- Logic Model — alternative to or complement of Theory of Change for output-focused programs

**Avoid:** Porter's Five Forces, FMEA, DevSecOps, TOGAF

**Example signals:** "program", "intervention", "policy", "government", "evaluation", "impact", "outcome", "social", "grant", "research project", "nonprofit", "community", "evidence-based"

---

### RISK

**Core Frameworks (always pick 2–3):**
- Risk Matrix — primary tool; always include
- FMEA — include if this is engineering, product, or process risk
- Bow-Tie Analysis (see Note below) — include if the risk scenario is clearly defined with known causes and consequences

**Secondary Add-ons:**
- Balanced Scorecard — to link risk to performance dimensions
- PESTLE — if risks are macro/external in nature

**Note on Bow-Tie:** This framework is described in this file as it is simpler than the others. Bow-Tie maps: Threats/Causes → [Hazard Event] → Consequences, with Prevention Barriers on the left and Recovery Barriers on the right. Score each barrier's effectiveness 1–5.

**Example signals:** "risk assessment", "compliance", "audit", "security", "regulatory", "disaster", "failure", "vulnerability", "mitigation", "contingency"

---

### INNOVATION

**Core Frameworks (always pick 2–3):**
- Blue Ocean Canvas — if the innovation claims to create a new market or differentiate radically
- Lean Canvas — if this is a startup or new venture
- Jobs-To-Be-Done — always; innovation must solve a real job
- Design Thinking Assessment — if human-centered design process is involved

**Secondary Add-ons:**
- Ansoff Matrix — to position where in the product/market grid this innovation sits
- Risk Matrix — innovation carries high uncertainty

**Avoid:** Kirkpatrick, TOGAF, McKinsey 7S (unless scaling an innovation)

**Example signals:** "startup", "new idea", "disruptive", "innovation", "venture", "new market", "first mover", "novel", "breakthrough", "ideation"

---

## Contextual Modifiers

Apply these additional rules regardless of domain:

### Always Add Risk Matrix If:
- Budget > $100K is mentioned
- Timeline > 12 months
- Regulatory or compliance context is mentioned
- Multiple stakeholders with conflicting interests
- The user explicitly mentions uncertainty, risks, or failure scenarios

### Add Financial Framework If:
- Any mention of budget, revenue, cost, investment, or funding
- Even for non-financial projects: "what will this cost?" → add NPV/ROI

### Add Balanced Scorecard If:
- The project has multiple success dimensions (not just one KPI)
- Multiple stakeholder groups with different interests
- Long-term strategic initiative (not a one-time task)

### Reduce to 3 Frameworks If:
- Input is fewer than 200 words
- The project is small-scale (team of < 5, budget < $50K, timeline < 3 months)
- User explicitly requests a quick or focused assessment

### Use 5–6 Frameworks If:
- Input is a full document (> 5 pages)
- Enterprise-scale project (> 100 people affected, budget > $1M)
- The user requests "comprehensive", "thorough", "full evaluation"
- The project is high-stakes (public policy, large investment, irreversible decision)

---

## Framework Compatibility Notes

Some frameworks complement each other especially well; pair them when possible:

| Strong Pairing | Why |
|---|---|
| SWOT + PESTLE | PESTLE feeds the Opportunities and Threats of SWOT |
| Porter's + SWOT | Porter's informs competitive Threats in SWOT |
| Theory of Change + Risk Matrix | ToC chain assumptions become risk scenarios |
| McKinsey 7S + Balanced Scorecard | 7S diagnoses the org; BSC measures performance |
| NPV/ROI + Risk Matrix | Financial projections need risk-adjusted scenarios |
| JTBD + Kano Model | JTBD identifies the job; Kano prioritizes how to serve it |
| Design Thinking + Lean Canvas | Process + business model together |
