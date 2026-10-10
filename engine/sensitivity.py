from engine.scoring import calculate_overall_score


def sensitivity_table(scores, questions, deltas=(0.5, 1.0, 1.5)):
    dimension_scores = {}
    for dim in questions["dimensions"]:
        dim_id = dim["id"]
        dim_items = [item for item in questions["items"] if item["dimension"] == dim_id]
        item_scores = [float(scores.get(item["id"], 0)) for item in dim_items]
        dimension_scores[dim_id] = sum(item_scores) / len(item_scores) if item_scores else 0.0

    table = []
    current_total = calculate_overall_score(scores, questions)
    for dim in questions["dimensions"]:
        row = {"dimension": dim["name"], "current": dimension_scores[dim["id"]]}
        for delta in deltas:
            scenario_scores = dict(scores)
            for item in questions["items"]:
                if item["dimension"] == dim["id"]:
                    scenario_scores[item["id"]] = min(5.0, float(scenario_scores.get(item["id"], 0)) + delta)
            row[f"+{delta}"] = calculate_overall_score(scenario_scores, questions)
        table.append(row)
    return {"current_total": current_total, "rows": table}
