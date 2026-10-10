from collections import defaultdict


def get_pillar_profile(scores, questions):
    pillar_items = defaultdict(list)
    for item in questions["items"]:
        pillar_items[item["pillar"]].append(item)

    profile = {}
    for pillar, items in pillar_items.items():
        weighted_total = 0.0
        weight_total = 0.0
        for item in items:
            score = float(scores.get(item["id"], 0))
            weighted_total += score * item["weight"]
            weight_total += item["weight"]
        profile[pillar] = weighted_total / weight_total if weight_total else 0.0
    return profile
