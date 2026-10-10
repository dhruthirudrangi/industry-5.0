import streamlit as st

from engine.recommendations import generate_rule_based_recommendations
from engine.scoring import load_questions


def render_recommendations():
    questions = load_questions()
    st.title("Recommendations")
    st.caption("Project-specific recommendation rules informed by the research context.")

    if "scores" not in st.session_state:
        st.warning("Assessment scores are not available yet.")
        return

    recs = generate_rule_based_recommendations(st.session_state["scores"], questions)
    for rec in recs:
        st.subheader(rec["construct"])
        st.write(f"Problem: {rec['problem']}")
        st.write(f"Why it matters: {rec['why_it_matters']}")
        st.write(f"Suggested action: {rec['suggested_action']}")
        st.write(f"First step: {rec['first_step']}")
        st.write(f"KPI: {rec['kpi']}")
        st.write(f"Priority: {rec['priority']}")
        st.write(f"Related pillar: {rec['related_pillar']}")
        st.write("---")


if __name__ == "__main__":
    render_recommendations()
