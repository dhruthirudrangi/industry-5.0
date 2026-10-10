from engine.scoring import load_questions


def base_recommendation_rules():
    with open("data/recommendations.json", "r", encoding="utf-8") as f:
        import json
        return json.load(f)


def generate_rule_based_recommendations(scores, questions=None):
    if questions is None:
        questions = load_questions()
    recommendations = []
    for item in questions["items"]:
        score = float(scores.get(item["id"], 0))
        if score >= 3.5:
            continue
        gap = 5 - score
        rule = {
            "construct": item["construct"],
            "problem": f"{item['construct']} is below target maturity.",
            "why_it_matters": f"This affects the broader {item['pillar']} capability profile and operational readiness.",
            "suggested_action": f"Deploy a focused action plan for {item['construct']} with defined steps and a measurable review cycle.",
            "first_step": f"Map the current state of {item['construct']} and identify the highest-leverage process or technology intervention.",
            "kpi": f"Maturity score of {item['construct']} improved from {score:.2f} to at least 3.5 within one review cycle.",
            "timeframe": "0-6 months",
            "responsible_role": "Operations Manager",
            "required_resources": "Internal team time, focused budget, and stakeholder alignment.",
            "related_pillar": item["pillar"],
            "priority": "High" if gap >= 2 else "Medium" if gap >= 1 else "Low",
            "gap": gap,
            "score": score,
        }
        recommendations.append(rule)
    recommendations.sort(key=lambda x: x["gap"], reverse=True)
    return recommendations
