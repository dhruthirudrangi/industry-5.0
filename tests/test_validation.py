import pytest

from engine.scoring import calculate_overall_score, load_questions

questions = load_questions()


def test_all_scores_between_1_and_5():
    scores = {item["id"]: 2 for item in questions["items"]}
    assert 1 <= calculate_overall_score(scores, questions) <= 5


def test_no_zero_denominator():
    scores = {item["id"]: 3 for item in questions["items"]}
    assert calculate_overall_score(scores, questions) > 0


def test_invalid_score_raises():
    scores = {item["id"]: 6 for item in questions["items"]}
    with pytest.raises(ValueError):
        calculate_overall_score(scores, questions)
