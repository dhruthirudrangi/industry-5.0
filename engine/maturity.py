from engine.scoring import calculate_dimension_scores, calculate_overall_score, get_maturity_level


def assess_company(company_name, scores, questions):
    overall = calculate_overall_score(scores, questions)
    level, interpretation = get_maturity_level(overall)
    dimensions = calculate_dimension_scores(scores, questions)
    return {
        "company_name": company_name,
        "overall_score": overall,
        "maturity_level": level,
        "interpretation": interpretation,
        "dimension_scores": dimensions,
    }
