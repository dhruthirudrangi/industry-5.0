import streamlit as st

from engine.scoring import calculate_overall_score, calculate_dimension_scores, get_maturity_level, load_questions
from engine.pillar_analysis import get_pillar_profile


def render_results():
    st.title("Results Dashboard")
    questions = load_questions()

    if "scores" not in st.session_state:
        st.warning("No assessment has been completed yet.")
        return

    scores = st.session_state["scores"]
    overall_score = calculate_overall_score(scores, questions)
    level, interpretation = get_maturity_level(overall_score)

    dim_scores = calculate_dimension_scores(scores, questions)

    st.subheader("Main KPI")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Overall Industry 5.0 Maturity", f"{overall_score:.2f}")
    col2.metric("Maturity Level", f"{level}")
    col3.metric("Strongest Dimension", max(dim_scores, key=dim_scores.get))
    col4.metric("Weakest Dimension", min(dim_scores, key=dim_scores.get))

    st.caption("This score is a deterministic calculation using the published dimension and item weights, normalized internally where required.")

    st.subheader("Seven-dimension overview")
    for dim_id, score in dim_scores.items():
        st.markdown(f"**{next(dim['name'] for dim in questions['dimensions'] if dim['id']==dim_id)}**: {score:.2f}")

    pillar_profile = get_pillar_profile(scores, questions)
    st.subheader("Pillar profile")
    for pillar, value in pillar_profile.items():
        st.write(f"{pillar}: {value:.2f}")

    st.subheader("Explainability")
    st.markdown(
        f"Overall score = weighted combination of seven dimension scores.\n\nThe current overall result is {overall_score:.2f}, which corresponds to {level} — {interpretation}."
    )


if __name__ == "__main__":
    render_results()
