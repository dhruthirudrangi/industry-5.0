import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "questions.json"


def load_questions():
    with DATA_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def normalize_dimension_weights(dimensions):
    total = sum(dim["weight"] for dim in dimensions)
    if total <= 0:
        raise ValueError("Dimension weights sum must be greater than zero.")
    normalized = []
    for dim in dimensions:
        normalized.append({**dim, "normalized_weight": dim["weight"] / total})
    return normalized


def normalize_item_weights(items):
    total = sum(item["weight"] for item in items)
    if total <= 0:
        raise ValueError("Item weights sum must be greater than zero.")
    normalized = []
    for item in items:
        normalized.append({**item, "normalized_weight": item["weight"] / total})
    return normalized


def calculate_dimension_scores(scores, questions):
    by_dim = defaultdict(list)
    for item in questions["items"]:
        by_dim[item["dimension"]].append(item)

    dimension_scores = {}
    for dim_id, items in sorted(by_dim.items()):
        weighted_total = 0.0
        weight_total = 0.0
        for item in items:
            item_score = float(scores.get(item["id"], 0))
            weighted_total += item_score * item["weight"]
            weight_total += item["weight"]
        if weight_total <= 0:
            raise ValueError(f"No valid item weights for dimension {dim_id}.")
        dimension_scores[dim_id] = weighted_total / weight_total
    return dimension_scores


def calculate_overall_score(scores, questions):
    if not scores:
        raise ValueError("No scores were provided.")

    valid_scores = []
    for item in questions["items"]:
        value = scores.get(item["id"])
        if value is None:
            raise ValueError(f"Missing score for item {item['id']}.")
        if not isinstance(value, (int, float)):
            raise ValueError(f"Invalid score type for item {item['id']}.")
        if value < 1 or value > 5:
            raise ValueError(f"Score out of range for item {item['id']}: {value}")
        valid_scores.append(float(value))

    dimension_scores = calculate_dimension_scores(scores, questions)
    dim_weights = normalize_dimension_weights(questions["dimensions"])
    weight_map = {dim["id"]: dim["normalized_weight"] for dim in dim_weights}

    total = 0.0
    for dim in questions["dimensions"]:
        dim_id = dim["id"]
        total += dimension_scores.get(dim_id, 0.0) * weight_map[dim_id]
    return total


def get_maturity_level(score):
    if score < 1 or score > 5:
        raise ValueError("Score must be between 1 and 5.")
    if 1.0 <= score <= 1.99:
        return "Level 1", "Outsider"
    if 2.0 <= score <= 2.99:
        return "Level 2", "Beginner"
    if 3.0 <= score <= 3.99:
        return "Level 3", "Advanced"
    return "Level 4", "Senior"


def calculate_pillar_scores(scores, questions):
    items_by_pillar = defaultdict(list)
    for item in questions["items"]:
        items_by_pillar[item["pillar"]].append(item)

    pillar_scores = {}
    for pillar, items in items_by_pillar.items():
        weighted = 0.0
        total_w = 0.0
        for item in items:
            item_score = float(scores.get(item["id"], 0))
            weighted += item_score * item["weight"]
            total_w += item["weight"]
        pillar_scores[pillar] = weighted / total_w if total_w else 0.0
    return pillar_scores


def summarize_gaps(scores, questions):
    critical = []
    moderate = []
    strengths = []
    for item in questions["items"]:
        score = float(scores.get(item["id"], 0))
        gap = 5 - score
        if score < 2.5:
            critical.append({"id": item["id"], "construct": item["construct"], "score": score, "gap": gap})
        elif score < 3.5:
            moderate.append({"id": item["id"], "construct": item["construct"], "score": score, "gap": gap})
        else:
            strengths.append({"id": item["id"], "construct": item["construct"], "score": score, "gap": gap})
    return {"critical_gaps": critical, "moderate_gaps": moderate, "strengths": strengths}


def generate_recommendations(scores, questions):
    recommendations = []
    for item in questions["items"]:
        score = float(scores.get(item["id"], 0))
        if score >= 3.5:
            continue
        gap = 5 - score
        priority = "High" if gap >= 2 else "Medium" if gap >= 1 else "Low"
        recommendations.append({
            "id": item["id"],
            "dimension": item["dimension"],
            "construct": item["construct"],
            "problem": f"{item['construct']} is below target maturity.",
            "why_it_matters": f"This construct contributes to {item['pillar']} performance and influences the broader SME readiness profile.",
            "suggested_action": f"Create a focused improvement plan for {item['construct']} with measurable milestones.",
            "first_step": f"Assess current practices and map the main gaps for {item['construct']}.",
            "kpi": f"Improvement in {item['construct']} maturity score over the next review cycle.",
            "timeframe": "0-6 months",
            "responsible_role": "Operations Manager",
            "resources": "Cross-functional team support, internal data, and targeted investment.",
            "pillar": item["pillar"],
            "priority": priority,
            "gap": gap,
        })
    recommendations.sort(key=lambda x: (x["gap"], x["priority"]), reverse=True)
    return recommendations[:10]


def simulate_what_if(baseline_scores, scenario, questions):
    if not baseline_scores:
        raise ValueError("Baseline scores are missing.")

    simulated = dict(baseline_scores)
    for dim_id, value in scenario.items():
        for item in questions["items"]:
            if item["dimension"] == dim_id:
                simulated[item["id"]] = value

    current_score = calculate_overall_score(baseline_scores, questions)
    new_score = calculate_overall_score(simulated, questions)
    return {
        "current_score": current_score,
        "overall_score": new_score,
        "change": new_score - current_score,
        "scenario": scenario,
    }


def compute_dimension_gap(item_score):
    return 5 - item_score
