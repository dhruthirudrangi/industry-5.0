def classify_gap(score):
    if score < 2.5:
        return "High-priority gap", "Project-defined diagnostic thresholds"
    if score < 3.5:
        return "Development opportunity", "Project-defined diagnostic thresholds"
    return "Relative strength", "Project-defined diagnostic thresholds"


def compute_gap_rankings(scores, questions):
    items = []
    for item in questions["items"]:
        score = float(scores.get(item["id"], 0))
        gap = 5 - score
        items.append({
            "id": item["id"],
            "dimension": item["dimension"],
            "construct": item["construct"],
            "score": score,
            "gap": gap,
            "classification": classify_gap(score)[0],
            "pillar": item["pillar"],
        })
    return sorted(items, key=lambda row: row["gap"], reverse=True)
