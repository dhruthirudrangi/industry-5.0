import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
QUESTIONS_PATH = DATA_DIR / "questions.json"
COMPANIES_PATH = DATA_DIR / "companies.json"


def load_questions():
    with QUESTIONS_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def load_companies():
    with COMPANIES_PATH.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def default_scores():
    data = load_questions()
    return {item["id"]: 3 for item in data["items"]}


def dimension_order():
    data = load_questions()
    return [d["id"] for d in data["dimensions"]]


def question_lookup():
    data = load_questions()
    lookup = {}
    for item in data["items"]:
        lookup[item["id"]] = item
    return lookup


def get_dimension_name(dim_id):
    data = load_questions()
    for dim in data["dimensions"]:
        if dim["id"] == dim_id:
            return dim["name"]
    return dim_id


def get_item_by_id(item_id):
    return question_lookup().get(item_id, {})

def build_company_profile():
    return {
        "company_name": "",
        "industry": "Manufacturing",
        "company_size": "50-249 employees",
        "assessment_date": "",
    }
