import pytest

from engine.scoring import load_questions, normalize_dimension_weights, normalize_item_weights


questions = load_questions()


def test_dimension_weight_sum_approx_one():
    normalized = normalize_dimension_weights(questions["dimensions"])
    assert sum(dim["normalized_weight"] for dim in normalized) == pytest.approx(1.0)


def test_item_weight_sums_by_dimension():
    by_dim = {}
    for item in questions["items"]:
        by_dim.setdefault(item["dimension"], []).append(item)
    for dim_id, items in by_dim.items():
        normalized = normalize_item_weights(items)
        assert sum(item["normalized_weight"] for item in normalized) == pytest.approx(1.0)
