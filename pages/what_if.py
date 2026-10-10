import streamlit as st

from engine.scoring import calculate_overall_score, load_questions


def render_what_if():
    questions = load_questions()
    st.title("What-if Improvement Simulator")

    if "scores" not in st.session_state:
        st.warning("Assessment scores are not available yet.")
        return

    current_scores = st.session_state["scores"]
    current_overall = calculate_overall_score(current_scores, questions)

    st.write(f"Current overall score: {current_overall:.2f}")

    scenario = {}
    for dim in questions["dimensions"]:
        options = [1, 2, 3, 4, 5]
        scenario[dim["id"]] = st.selectbox(f"Set {dim['name']} score", options, index=2)

    if st.button("Simulate scenario"):
        simulated = dict(current_scores)
        for item in questions["items"]:
            if item["dimension"] in scenario:
                simulated[item["id"]] = scenario[item["dimension"]]
        new_overall = calculate_overall_score(simulated, questions)
        st.success(f"New overall score: {new_overall:.2f}")
        st.write(f"Score change: {new_overall - current_overall:.2f}")


if __name__ == "__main__":
    render_what_if()
