#!/usr/bin/env python3
"""
detect_domain.py — Domain Classification Script
Part of the evaluation-framework skill.

Usage:
    python detect_domain.py --text "your input text here"
    python detect_domain.py --file path/to/document.txt
    python detect_domain.py --stdin  # reads from stdin

Output (JSON):
    {
        "primary_domain": "business_strategy",
        "secondary_domain": "financial",
        "confidence": "high",
        "primary_score": 12,
        "secondary_score": 5,
        "signals_found": ["market", "revenue", "competitive advantage"],
        "all_domain_scores": { ... }
    }
"""

import sys
import json
import argparse
import re
from pathlib import Path


# ─── Domain Signal Dictionaries ────────────────────────────────────────────────

DOMAIN_SIGNALS = {
    "business_strategy": {
        "keywords": [
            "market strategy", "go-to-market", "competitive advantage", "market entry",
            "business plan", "growth strategy", "market share", "revenue model",
            "customer acquisition", "business model", "strategic plan", "expansion",
            "market penetration", "competitive landscape", "positioning", "brand",
            "partnership", "sales strategy", "market segment", "value proposition",
            "market size", "tam", "sam", "som", "differentiation", "moat",
        ],
        "single_words": [
            "competition", "competitor", "market", "revenue", "growth",
            "strategy", "strategic", "customers", "pricing", "channels",
        ],
        "weight": 1.0,
    },
    "product_development": {
        "keywords": [
            "product roadmap", "user story", "user experience", "product-market fit",
            "sprint planning", "agile development", "feature prioritization",
            "product requirements", "acceptance criteria", "product backlog",
            "minimum viable product", "mvp", "product launch", "go-to-market product",
            "product design", "wireframe", "prototype", "user research", "ux",
            "user interface", "product manager", "scrum", "kanban",
        ],
        "single_words": [
            "feature", "product", "sprint", "backlog", "users", "prototype",
            "wireframe", "persona", "journey", "requirements", "roadmap",
        ],
        "weight": 1.0,
    },
    "technology": {
        "keywords": [
            "system architecture", "software development", "api design", "cloud migration",
            "microservices", "infrastructure", "devops", "ci/cd", "database design",
            "system integration", "technical architecture", "technology stack",
            "software engineering", "backend", "frontend", "deployment",
            "kubernetes", "docker", "aws", "azure", "gcp", "cybersecurity",
            "data pipeline", "machine learning", "ai system", "platform engineering",
        ],
        "single_words": [
            "api", "system", "software", "code", "deploy", "server",
            "database", "integration", "pipeline", "architecture", "technical",
            "infrastructure", "cloud", "security", "monitoring",
        ],
        "weight": 1.0,
    },
    "financial": {
        "keywords": [
            "return on investment", "net present value", "financial model",
            "cost benefit", "payback period", "internal rate of return",
            "capital allocation", "investment decision", "financial projection",
            "budget planning", "cost structure", "revenue forecast",
            "profit margin", "cash flow", "break even", "financial viability",
            "funding round", "valuation", "due diligence", "financial analysis",
        ],
        "single_words": [
            "budget", "cost", "revenue", "profit", "investment", "roi",
            "npv", "irr", "funding", "financial", "capital", "payback",
            "margin", "cashflow", "valuation",
        ],
        "weight": 1.0,
    },
    "organizational": {
        "keywords": [
            "organizational change", "change management", "culture transformation",
            "team restructuring", "operating model", "talent management",
            "leadership development", "organizational design", "workforce planning",
            "employee engagement", "performance management", "capability building",
            "people strategy", "hr strategy", "organizational effectiveness",
        ],
        "single_words": [
            "culture", "team", "leadership", "talent", "people", "organization",
            "restructure", "transformation", "change", "employees", "workforce",
            "capability", "skills", "structure",
        ],
        "weight": 1.0,
    },
    "research_policy": {
        "keywords": [
            "theory of change", "program evaluation", "policy implementation",
            "government program", "social impact", "nonprofit", "grant proposal",
            "research methodology", "intervention design", "evidence-based",
            "outcome measurement", "impact assessment", "logic model",
            "public policy", "community program", "health program",
            "development program", "monitoring and evaluation",
        ],
        "single_words": [
            "program", "policy", "research", "evaluation", "intervention",
            "outcomes", "impact", "beneficiaries", "grant", "nonprofit",
            "social", "community", "evidence", "assessment",
        ],
        "weight": 1.0,
    },
    "risk": {
        "keywords": [
            "risk assessment", "risk management", "compliance audit",
            "regulatory compliance", "risk mitigation", "risk register",
            "business continuity", "disaster recovery", "security audit",
            "vulnerability assessment", "threat analysis", "risk matrix",
            "failure mode", "contingency plan", "risk framework",
        ],
        "single_words": [
            "risk", "compliance", "audit", "regulation", "security",
            "vulnerability", "threat", "mitigation", "contingency",
            "failure", "hazard", "control", "governance",
        ],
        "weight": 1.0,
    },
    "innovation": {
        "keywords": [
            "startup", "new venture", "disruptive innovation", "blue ocean",
            "market creation", "design thinking", "lean startup", "innovation lab",
            "new product concept", "ideation session", "innovation strategy",
            "first mover", "product innovation", "breakthrough solution",
            "digital innovation", "business model innovation",
        ],
        "single_words": [
            "startup", "innovation", "disruptive", "novel", "new",
            "creative", "breakthrough", "ideation", "experiment", "pivot",
            "venture", "incubator", "accelerator",
        ],
        "weight": 1.0,
    },
}

CONFIDENCE_THRESHOLDS = {
    "high": 8,    # primary score >= 8 AND primary >= 2x secondary
    "medium": 4,  # primary score >= 4
    "low": 0,     # anything else
}


# ─── Scoring Logic ──────────────────────────────────────────────────────────────

def normalize_text(text: str) -> str:
    """Lowercase, remove punctuation (except hyphens in compounds), normalize whitespace."""
    text = text.lower()
    text = re.sub(r"[^\w\s\-/]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def score_domain(text: str, domain: str, signals: dict) -> tuple[int, list[str]]:
    """Score a single domain against the text. Returns (score, matched_signals)."""
    score = 0
    matched = []

    # Multi-word keyword matches (weight 3 each)
    for keyword in signals.get("keywords", []):
        if keyword in text:
            score += 3
            matched.append(keyword)

    # Single-word matches (weight 1 each)
    words = set(text.split())
    for word in signals.get("single_words", []):
        if word in words and word not in [m for m in matched]:
            score += 1
            matched.append(word)

    return score, matched


def classify_domain(text: str) -> dict:
    """Main classification function. Returns full result dict."""
    normalized = normalize_text(text)
    
    domain_scores = {}
    domain_signals = {}
    
    for domain, signals in DOMAIN_SIGNALS.items():
        score, matched = score_domain(normalized, domain, signals)
        domain_scores[domain] = score
        domain_signals[domain] = matched

    # Sort domains by score
    sorted_domains = sorted(domain_scores.items(), key=lambda x: x[1], reverse=True)
    
    primary_domain, primary_score = sorted_domains[0]
    secondary_domain, secondary_score = sorted_domains[1] if len(sorted_domains) > 1 else (None, 0)

    # Determine confidence
    if primary_score >= CONFIDENCE_THRESHOLDS["high"] and (
        secondary_score == 0 or primary_score >= 2 * secondary_score
    ):
        confidence = "high"
    elif primary_score >= CONFIDENCE_THRESHOLDS["medium"]:
        confidence = "medium"
    else:
        confidence = "low"

    # Secondary domain: only report if meaningfully present
    if secondary_score < 3 or secondary_domain == primary_domain:
        secondary_domain = None
        secondary_score = 0

    return {
        "primary_domain": primary_domain,
        "secondary_domain": secondary_domain,
        "confidence": confidence,
        "primary_score": primary_score,
        "secondary_score": secondary_score,
        "signals_found": domain_signals[primary_domain][:5],  # Top 5 signals
        "all_domain_scores": domain_scores,
    }


# ─── CLI Entry Point ────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Classify input text into a project domain for framework selection."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", type=str, help="Input text string to classify")
    group.add_argument("--file", type=str, help="Path to text file to classify")
    group.add_argument("--stdin", action="store_true", help="Read from stdin")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")

    args = parser.parse_args()

    # Get input text
    if args.text:
        text = args.text
    elif args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(json.dumps({"error": f"File not found: {args.file}"}))
            sys.exit(1)
        text = file_path.read_text(encoding="utf-8", errors="ignore")
    else:  # stdin
        text = sys.stdin.read()

    if not text.strip():
        print(json.dumps({"error": "Empty input text provided"}))
        sys.exit(1)

    result = classify_domain(text)

    indent = 2 if args.pretty else None
    print(json.dumps(result, indent=indent))


if __name__ == "__main__":
    main()
