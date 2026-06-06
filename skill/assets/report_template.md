# Evaluation Framework Report: {{PROJECT_NAME}}

**Date:** {{DATE}}  
**Analyst:** Claude (evaluation-framework skill v1.0)  
**Domain:** {{PRIMARY_DOMAIN}} {{#SECONDARY_DOMAIN}}/ {{SECONDARY_DOMAIN}}{{/SECONDARY_DOMAIN}}  
**Frameworks Applied:** {{FRAMEWORK_LIST}}  
**Input Mode:** {{INPUT_MODE}} — {{INPUT_DESCRIPTION}}  
**Overall Health Score:** {{OVERALL_SCORE}} / 5.0 {{HEALTH_BADGE}}

---

## Executive Summary

> _250 words maximum. Answer three questions: (1) What is this project? (2) What are the 3 most critical findings? (3) What should happen next?_

{{EXECUTIVE_SUMMARY}}

**Top Finding:** {{TOP_FINDING}}  
**Immediate Action Required:** {{IMMEDIATE_ACTION}}

---

## 1. Input Overview

### 1.1 Project Description
{{PROJECT_DESCRIPTION}}

### 1.2 Information Used
| Source | Status | Notes |
|---|---|---|
| {{SOURCE_1}} | Found / Partial / Not Found | {{NOTE}} |
| {{SOURCE_2}} | Found / Partial / Not Found | {{NOTE}} |

### 1.3 Assumptions Made
The following assumptions were applied where information was not provided. All assumptions are marked **[ASSUMED]** throughout this report.

{{ASSUMPTIONS_LIST}}

### 1.4 Information Gaps
The following information was not available and may affect evaluation accuracy:

{{GAPS_LIST}}

---

## 2. Framework Selection Rationale

**Primary Domain:** {{PRIMARY_DOMAIN}}  
**Secondary Domain:** {{SECONDARY_DOMAIN}}  
**Project Scale:** {{SCALE}} ({{SCALE_RATIONALE}})

| # | Framework | Rationale for Selection |
|---|---|---|
| 1 | {{FRAMEWORK_1}} | {{RATIONALE_1}} |
| 2 | {{FRAMEWORK_2}} | {{RATIONALE_2}} |
| 3 | {{FRAMEWORK_3}} | {{RATIONALE_3}} |
{{ADDITIONAL_FRAMEWORKS}}

**Frameworks Considered but Excluded:**  
{{EXCLUDED_FRAMEWORKS}}

---

## 3. Framework Analyses

> _Each framework section is populated from the templates in references/output-templates.md. Replace each section below with the completed template output._

{{FRAMEWORK_SECTION_1}}

---

{{FRAMEWORK_SECTION_2}}

---

{{FRAMEWORK_SECTION_3}}

---

{{FRAMEWORK_SECTION_4_IF_APPLICABLE}}

---

{{FRAMEWORK_SECTION_5_IF_APPLICABLE}}

---

{{FRAMEWORK_SECTION_6_IF_APPLICABLE}}

---

## 4. Cross-Framework Synthesis

### 4.1 Convergent Findings (HIGH CONFIDENCE)
_These findings appeared across 2 or more frameworks — treat them as the highest-priority insights._

| Finding | Frameworks That Identified It | Confidence |
|---|---|---|
| {{CONVERGENT_1}} | {{FRAMEWORKS_1}} | HIGH |
| {{CONVERGENT_2}} | {{FRAMEWORKS_2}} | HIGH |
| {{CONVERGENT_3}} | {{FRAMEWORKS_3}} | HIGH |

### 4.2 Framework Contradictions
_Where frameworks suggested opposing conclusions, explained here:_

{{CONTRADICTIONS_OR_NONE}}

### 4.3 Blind Spots
_Important dimensions that no selected framework fully covered for this specific input:_

{{BLIND_SPOTS_OR_NONE}}

---

## 5. Priority Matrix

### 🟢 Top Strengths (Well-Evidenced)
1. **{{STRENGTH_1}}** — Supported by: {{FRAMEWORKS_SUPPORTING}}
2. **{{STRENGTH_2}}** — Supported by: {{FRAMEWORKS_SUPPORTING}}
3. **{{STRENGTH_3}}** — Supported by: {{FRAMEWORKS_SUPPORTING}}

### 🔴 Critical Risks (Highest Convergence)
1. **{{RISK_1}}** — Flagged by: {{FRAMEWORKS}} | Severity: {{SEVERITY}} | Mitigation: {{MITIGATION}}
2. **{{RISK_2}}** — Flagged by: {{FRAMEWORKS}} | Severity: {{SEVERITY}} | Mitigation: {{MITIGATION}}
3. **{{RISK_3}}** — Flagged by: {{FRAMEWORKS}} | Severity: {{SEVERITY}} | Mitigation: {{MITIGATION}}

### 🔵 Key Opportunities (Underexplored)
1. **{{OPPORTUNITY_1}}** — Rationale: {{RATIONALE}}
2. **{{OPPORTUNITY_2}}** — Rationale: {{RATIONALE}}
3. **{{OPPORTUNITY_3}}** — Rationale: {{RATIONALE}}

---

## 6. Recommended Next Steps

_Ordered by Impact × Feasibility. Each action is specific and attributable._

| Priority | Action | Suggested Owner | Timeline | Success Metric | Impact |
|---|---|---|---|---|---|
| 1 | {{ACTION_1}} | {{OWNER_1}} | {{TIMELINE_1}} | {{METRIC_1}} | 🔴 Critical |
| 2 | {{ACTION_2}} | {{OWNER_2}} | {{TIMELINE_2}} | {{METRIC_2}} | 🔴 High |
| 3 | {{ACTION_3}} | {{OWNER_3}} | {{TIMELINE_3}} | {{METRIC_3}} | 🟡 Medium |
| 4 | {{ACTION_4}} | {{OWNER_4}} | {{TIMELINE_4}} | {{METRIC_4}} | 🟡 Medium |
| 5 | {{ACTION_5}} | {{OWNER_5}} | {{TIMELINE_5}} | {{METRIC_5}} | 🟢 Strategic |

**Non-Obvious Insight:**  
> {{NON_OBVIOUS_INSIGHT}}
> _This is the finding most likely to have been missed without this structured evaluation._

---

## Appendix A: Quantitative Score Summary

### Overall Scores by Framework

| Framework | Composite Score | Classification | Weakest Dimension | Strongest Dimension |
|---|---|---|---|---|
| {{FRAMEWORK_1}} | {{SCORE_1}} / 5.0 | 🔴/🟡/🟢 | {{WEAKEST_1}} | {{STRONGEST_1}} |
| {{FRAMEWORK_2}} | {{SCORE_2}} / 5.0 | 🔴/🟡/🟢 | {{WEAKEST_2}} | {{STRONGEST_2}} |
| {{FRAMEWORK_3}} | {{SCORE_3}} / 5.0 | 🔴/🟡/🟢 | {{WEAKEST_3}} | {{STRONGEST_3}} |
| **OVERALL** | **{{OVERALL_SCORE}} / 5.0** | **{{OVERALL_CLASS}}** | | |

### Scoring Methodology Notes
- All scores use a 1–5 scale (1 = Critical Gap, 5 = Exemplary)
- Composite score = mean of all dimensions within a framework
- Overall score = weighted mean across all frameworks
- Scores marked [ASSUMED] are based on domain benchmarks, not direct evidence

---

## Appendix B: Evidence References

_All evidence cited in this report, organized by source section._

{{EVIDENCE_REFERENCES}}

_Format:_
```
[Doc-01] Section "Risks", p. 4: "The primary risk is regulatory approval timelines..."
[Doc-02] Section "Financial", p. 7: Budget of $2.3M allocated for FY2026
[INFERRED-01] Market size estimate based on industry benchmark (source: domain knowledge)
[ASSUMED-01] Timeline estimated at 18 months based on comparable projects in this domain
```

---

_Report generated by evaluation-framework skill v1.0_  
_Frameworks applied are internationally recognized methodologies — see references/frameworks-catalog.md for full citations_
