import json

import streamlit as st

from engine.scoring import calculate_overall_score, get_maturity_level, load_questions


def render_validation():
    questions = load_questions()
    st.title("Validation / 3 Synthetic SMEs")

    with open("data/companies.json", "r", encoding="utf-8") as f:
        companies = json.load(f)["synthetic_smes"]

    for company in companies:
        st.subheader(company["name"])
        st.caption(company["type"])
        score_dict = company["scores"]
        overall = calculate_overall_score(score_dict, questions)
        level, interpretation = get_maturity_level(overall)
        st.metric("Overall Score", f"{overall:.2f}")
        st.metric("Maturity Level", f"{level} - {interpretation}")
        st.write(company["description"])
        st.write("Expected profile: " + company["expected_profile"])
        st.write("---")

    st.subheader("Consistency tests")
    all_ones = {item["id"]: 1 for item in questions["items"]}
    all_threes = {item["id"]: 3 for item in questions["items"]}
    all_fives = {item["id"]: 5 for item in questions["items"]}

    st.write(f"Test 1: all answers = 1 -> {calculate_overall_score(all_ones, questions):.2f}")
    st.write(f"Test 2: all answers = 5 -> {calculate_overall_score(all_fives, questions):.2f}")
    st.write(f"Test 3: all answers = 3 -> {calculate_overall_score(all_threes, questions):.2f}")


if __name__ == "__main__":
    render_validation()
