import pytest

from engine.recommendations import generate_rule_based_recommendations
from engine.scoring import (
    calculate_dimension_scores,
    calculate_overall_score,
    calculate_pillar_scores,
    generate_recommendations,
    get_maturity_level,
    load_questions,
    normalize_dimension_weights,
    normalize_item_weights,
    simulate_what_if,
    summarize_gaps,
)


@pytest.fixture
def questions():
    return load_questions()


def test_all_ones(questions):
    scores = {item["id"]: 1 for item in questions["items"]}
    assert calculate_overall_score(scores, questions) == pytest.approx(1.0)


def test_all_fives(questions):
    scores = {item["id"]: 5 for item in questions["items"]}
    assert calculate_overall_score(scores, questions) == pytest.approx(5.0)


def test_all_threes(questions):
    scores = {item["id"]: 3 for item in questions["items"]}
    assert calculate_overall_score(scores, questions) == pytest.approx(3.0)


def test_dimension_weight_normalization(questions):
    normalized = normalize_dimension_weights(questions["dimensions"])
    assert sum(item["normalized_weight"] for item in normalized) == pytest.approx(1.0)


def test_item_weight_normalization(questions):
    by_dimension = {}
    for item in questions["items"]:
        by_dimension.setdefault(item["dimension"], []).append(item)

    for dim_id, items in by_dimension.items():
        normalized = normalize_item_weights(items)
        assert sum(item["normalized_weight"] for item in normalized) == pytest.approx(1.0)


def test_overall_score_range(questions):
    scores = {item["id"]: 4 for item in questions["items"]}
    result = calculate_overall_score(scores, questions)
    assert 1.0 <= result <= 5.0


def test_maturity_level_boundaries(questions):
    assert get_maturity_level(1.0)[0] == "Level 1"
    assert get_maturity_level(2.0)[0] == "Level 2"
    assert get_maturity_level(3.0)[0] == "Level 3"
    assert get_maturity_level(4.0)[0] == "Level 4"
    assert get_maturity_level(5.0)[0] == "Level 4"


def test_what_if_calculation(questions):
    baseline = {item["id"]: 2 for item in questions["items"]}
    scenario = {"D1": 4.0, "D2": 3.5}
    result = simulate_what_if(baseline, scenario, questions)
    assert "overall_score" in result
    assert "change" in result
    assert result["overall_score"] >= 1.0


def test_gap_calculation(questions):
    scores = {item["id"]: 2 for item in questions["items"]}
    gaps = summarize_gaps(scores, questions)
    assert "critical_gaps" in gaps
    assert "moderate_gaps" in gaps
    assert "strengths" in gaps


def test_recommendation_generation(questions):
    scores = {item["id"]: 1 for item in questions["items"]}
    recommendations = generate_recommendations(scores, questions)
    assert len(recommendations) > 0
    assert "priority" in recommendations[0]
    assert "problem" in recommendations[0]


def test_rule_based_recommendations_include_construct(questions):
    scores = {item["id"]: 1 for item in questions["items"]}
    recommendations = generate_rule_based_recommendations(scores, questions)

    assert recommendations
    assert all("construct" in recommendation for recommendation in recommendations)
