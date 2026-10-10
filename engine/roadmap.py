from engine.scoring import calculate_overall_score


def generate_roadmap(scores, questions):
    roadmap = [
        {"phase": "Phase 1 — Analysis", "window": "0–3 months", "items": []},
        {"phase": "Phase 2 — Design", "window": "3–6 months", "items": []},
        {"phase": "Phase 3 — Execution", "window": "6–12 months", "items": []},
        {"phase": "Phase 4 — Monitoring", "window": "12+ months", "items": []},
    ]

    priorities = []
    for item in questions["items"]:
        score = float(scores.get(item["id"], 0))
        if score < 3.5:
            priorities.append({
                "action": item["construct"],
                "gap": 5 - score,
                "pillar": item["pillar"],
                "dimension": item["dimension"],
            })
    priorities.sort(key=lambda x: x["gap"], reverse=True)

    for idx, item in enumerate(priorities[:8]):
        phase = roadmap[idx % len(roadmap)]
        phase["items"].append({
            "action": item["action"],
            "gap": item["gap"],
            "timeline": phase["window"],
            "responsible_role": "Operations or Digital Lead",
            "kpi": f"{item['action']} maturity score >= 3.5",
            "pillar": item["pillar"],
            "expected_maturity_effect": "Model-based improvement roadmap",
        })

    return roadmap
