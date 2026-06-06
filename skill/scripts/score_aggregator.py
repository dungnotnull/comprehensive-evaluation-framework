#!/usr/bin/env python3
"""
score_aggregator.py — Framework Score Aggregation and Report Table Generator
Part of the evaluation-framework skill.

Takes dimension scores for one or more frameworks and produces:
- Composite score per framework
- Overall project health score
- Markdown score table for the report
- Priority insights (weakest/strongest areas)

Usage:
    # From JSON file:
    python score_aggregator.py --file scores.json

    # From inline JSON:
    python score_aggregator.py --json '[{"framework": "SWOT", "dimensions": [{"name": "Strengths", "score": 4}, ...]}]'

    # From stdin:
    echo '[...]' | python score_aggregator.py --stdin

Input JSON format:
    [
        {
            "framework": "SWOT Analysis",
            "dimensions": [
                {"name": "Strengths", "score": 4, "evidence": "Two unique IP assets identified"},
                {"name": "Weaknesses", "score": 2, "evidence": "No mitigation plan for talent gap"},
                {"name": "Opportunities", "score": 4, "evidence": "$2B TAM growing 18% CAGR"},
                {"name": "Threats", "score": 3, "evidence": "Three competitors named, no differentiation analysis"}
            ]
        },
        {
            "framework": "Risk Matrix",
            "dimensions": [
                {"name": "Overall Risk Level", "score": 2, "evidence": "Three high-severity risks identified"}
            ]
        }
    ]

Output (JSON):
    {
        "framework_scores": [...],
        "overall_score": 3.2,
        "overall_classification": "moderate",
        "overall_badge": "🟡",
        "weakest_framework": "...",
        "strongest_framework": "...",
        "weakest_dimensions": [...],
        "strongest_dimensions": [...],
        "markdown_table": "...",
        "markdown_summary": "..."
    }
"""

import sys
import json
import argparse
import statistics
from pathlib import Path


# ─── Classification Thresholds ─────────────────────────────────────────────────

SCORE_CLASSIFICATIONS = [
    (4.5, 5.0, "Exemplary", "🟢"),
    (3.5, 4.4, "Strong", "🟢"),
    (2.5, 3.4, "Acceptable", "🟡"),
    (1.5, 2.4, "Weak", "🔴"),
    (0.0, 1.4, "Critical", "🔴"),
]


def classify_score(score: float) -> tuple[str, str]:
    """Return (classification_label, badge_emoji) for a numeric score."""
    for low, high, label, badge in SCORE_CLASSIFICATIONS:
        if low <= score <= high:
            return label, badge
    return "Unknown", "❓"


# ─── Core Aggregation Logic ────────────────────────────────────────────────────

def aggregate_framework(framework_data: dict) -> dict:
    """Compute composite score and metadata for a single framework."""
    name = framework_data.get("framework", "Unknown Framework")
    dimensions = framework_data.get("dimensions", [])
    
    if not dimensions:
        return {
            "framework": name,
            "composite_score": None,
            "classification": "No Data",
            "badge": "❓",
            "dimension_count": 0,
            "dimensions": [],
            "weakest": None,
            "strongest": None,
            "error": "No dimensions provided",
        }
    
    # Validate scores
    scored_dimensions = []
    for dim in dimensions:
        score = dim.get("score")
        if score is None:
            continue
        try:
            score = float(score)
            if not (1 <= score <= 5):
                score = max(1.0, min(5.0, score))  # Clamp to valid range
        except (ValueError, TypeError):
            continue
        scored_dimensions.append({
            "name": dim.get("name", "Unnamed"),
            "score": score,
            "evidence": dim.get("evidence", ""),
        })
    
    if not scored_dimensions:
        return {
            "framework": name,
            "composite_score": None,
            "classification": "Invalid",
            "badge": "❓",
            "error": "No valid numeric scores found",
        }
    
    scores = [d["score"] for d in scored_dimensions]
    composite = round(statistics.mean(scores), 2)
    classification, badge = classify_score(composite)
    
    # Find weakest and strongest
    sorted_dims = sorted(scored_dimensions, key=lambda x: x["score"])
    weakest = sorted_dims[0] if sorted_dims else None
    strongest = sorted_dims[-1] if sorted_dims else None
    
    return {
        "framework": name,
        "composite_score": composite,
        "classification": classification,
        "badge": badge,
        "dimension_count": len(scored_dimensions),
        "dimensions": scored_dimensions,
        "weakest": weakest,
        "strongest": strongest,
        "score_distribution": {
            "min": min(scores),
            "max": max(scores),
            "stddev": round(statistics.stdev(scores), 2) if len(scores) > 1 else 0.0,
        },
    }


def aggregate_all(frameworks: list[dict]) -> dict:
    """Aggregate scores across all frameworks and generate full output."""
    framework_results = [aggregate_framework(f) for f in frameworks]
    
    # Filter out frameworks with no valid scores
    valid_results = [r for r in framework_results if r.get("composite_score") is not None]
    
    if not valid_results:
        return {
            "error": "No valid framework scores to aggregate",
            "framework_scores": framework_results,
        }
    
    # Overall score: mean of all framework composites
    all_scores = [r["composite_score"] for r in valid_results]
    overall_score = round(statistics.mean(all_scores), 2)
    overall_classification, overall_badge = classify_score(overall_score)
    
    # Global weakest/strongest frameworks
    sorted_results = sorted(valid_results, key=lambda x: x["composite_score"])
    weakest_framework = sorted_results[0]["framework"] if sorted_results else None
    strongest_framework = sorted_results[-1]["framework"] if sorted_results else None
    
    # Global weakest/strongest individual dimensions (across all frameworks)
    all_dimensions = []
    for r in valid_results:
        for dim in r.get("dimensions", []):
            all_dimensions.append({
                "framework": r["framework"],
                "dimension": dim["name"],
                "score": dim["score"],
                "evidence": dim.get("evidence", ""),
            })
    
    all_dimensions_sorted = sorted(all_dimensions, key=lambda x: x["score"])
    weakest_dimensions = all_dimensions_sorted[:3]
    strongest_dimensions = all_dimensions_sorted[-3:][::-1]
    
    # Generate markdown tables
    markdown_table = generate_markdown_table(valid_results, overall_score, overall_badge, overall_classification)
    markdown_summary = generate_markdown_summary(
        overall_score, overall_badge, overall_classification,
        weakest_dimensions, strongest_dimensions,
        weakest_framework, strongest_framework
    )
    
    return {
        "framework_scores": valid_results,
        "overall_score": overall_score,
        "overall_classification": overall_classification,
        "overall_badge": overall_badge,
        "weakest_framework": weakest_framework,
        "strongest_framework": strongest_framework,
        "weakest_dimensions": weakest_dimensions,
        "strongest_dimensions": strongest_dimensions,
        "markdown_table": markdown_table,
        "markdown_summary": markdown_summary,
    }


# ─── Markdown Generators ───────────────────────────────────────────────────────

def generate_markdown_table(results: list[dict], overall: float, badge: str, classification: str) -> str:
    """Generate the Appendix A score table for the report."""
    lines = [
        "## Appendix A: Quantitative Score Summary",
        "",
        "| Framework | Score | Classification | Weakest Dimension | Strongest Dimension |",
        "|---|---|---|---|---|",
    ]
    
    for r in results:
        fw = r["framework"]
        score = f"{r['composite_score']:.1f} / 5.0"
        badge_class = f"{r['badge']} {r['classification']}"
        weakest = r["weakest"]["name"] if r.get("weakest") else "N/A"
        strongest = r["strongest"]["name"] if r.get("strongest") else "N/A"
        lines.append(f"| {fw} | {score} | {badge_class} | {weakest} | {strongest} |")
    
    # Overall row
    lines.append(f"| **OVERALL** | **{overall:.1f} / 5.0** | **{badge} {classification}** | | |")
    
    lines += [
        "",
        "**Scoring Scale:** 1 = 🔴 Critical Gap | 2 = 🔴 Significant Weakness | "
        "3 = 🟡 Acceptable | 4 = 🟢 Strong | 5 = 🟢 Exemplary",
    ]
    
    return "\n".join(lines)


def generate_markdown_summary(
    overall: float, badge: str, classification: str,
    weakest_dims: list, strongest_dims: list,
    weakest_fw: str, strongest_fw: str,
) -> str:
    """Generate a concise score summary for the Executive Summary section."""
    lines = [
        f"**Overall Project Health: {badge} {overall:.1f}/5.0 — {classification}**",
        "",
        f"**Strongest Area:** {strongest_fw}" + (
            f" (especially: {', '.join(d['dimension'] for d in strongest_dims[:2])})"
            if strongest_dims else ""
        ),
        f"**Greatest Risk:** {weakest_fw}" + (
            f" (especially: {', '.join(d['dimension'] for d in weakest_dims[:2])})"
            if weakest_dims else ""
        ),
        "",
        "**Top 3 Dimensions Requiring Attention:**",
    ]
    
    for i, dim in enumerate(weakest_dims, 1):
        score_badge = "🔴" if dim["score"] <= 2 else "🟡"
        lines.append(
            f"{i}. {score_badge} **{dim['framework']} — {dim['dimension']}** "
            f"(Score: {dim['score']}/5) — {dim['evidence'][:100] + '...' if len(dim.get('evidence', '')) > 100 else dim.get('evidence', 'No evidence cited')}"
        )
    
    return "\n".join(lines)


def generate_dimension_detail_table(result: dict) -> str:
    """Generate a detailed dimension breakdown table for a single framework."""
    lines = [
        f"#### {result['framework']} — Dimension Breakdown",
        "",
        "| Dimension | Score | Key Evidence |",
        "|---|---|---|",
    ]
    
    for dim in result.get("dimensions", []):
        score = dim["score"]
        if score <= 2:
            badge = "🔴"
        elif score == 3:
            badge = "🟡"
        else:
            badge = "🟢"
        evidence = dim.get("evidence", "")[:80] + ("..." if len(dim.get("evidence", "")) > 80 else "")
        lines.append(f"| {dim['name']} | {badge} {score}/5 | {evidence} |")
    
    return "\n".join(lines)


# ─── CLI Entry Point ────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Aggregate framework dimension scores into composite report tables."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", type=str, help="Path to JSON scores file")
    group.add_argument("--json", type=str, help="Inline JSON scores array")
    group.add_argument("--stdin", action="store_true", help="Read JSON from stdin")
    
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    parser.add_argument(
        "--markdown-only", action="store_true",
        help="Output only markdown tables (not JSON)"
    )
    
    args = parser.parse_args()
    
    # Get input JSON
    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(json.dumps({"error": f"File not found: {args.file}"}))
            sys.exit(1)
        raw = file_path.read_text(encoding="utf-8")
    elif args.json:
        raw = args.json
    else:
        raw = sys.stdin.read()
    
    try:
        frameworks = json.loads(raw)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"Invalid JSON input: {str(e)}"}))
        sys.exit(1)
    
    if not isinstance(frameworks, list):
        print(json.dumps({"error": "Input must be a JSON array of framework objects"}))
        sys.exit(1)
    
    result = aggregate_all(frameworks)
    
    if args.markdown_only:
        print(result.get("markdown_summary", ""))
        print("\n---\n")
        print(result.get("markdown_table", ""))
    else:
        indent = 2 if args.pretty else None
        print(json.dumps(result, indent=indent))


if __name__ == "__main__":
    main()
