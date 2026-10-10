import pytest

from engine.scoring import calculate_overall_score, load_questions, simulate_what_if

questions = load_questions()


def test_scenario_changes_score():
    baseline = {item["id"]: 2 for item in questions["items"]}
    scenario = {"D1": 4.0, "D2": 3.5}
    result = simulate_what_if(baseline, scenario, questions)
    assert result["overall_score"] > result["current_score"]


def test_scenario_out_of_range_produces_warning():
    baseline = {item["id"]: 2 for item in questions["items"]}
    scenario = {"D1": 10}
    with pytest.raises(ValueError):
        calculate_overall_score({**baseline, "D1_1": 10}, questions)
