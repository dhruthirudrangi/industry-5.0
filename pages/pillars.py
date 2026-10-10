import streamlit as st

from engine.pillar_analysis import get_pillar_profile
from engine.scoring import load_questions


def render_pillars():
    questions = load_questions()
    st.title("Pillar Analysis")
    st.markdown("This pillar profile is a software diagnostic extension and should not be interpreted as a replacement for the paper's full pillar-based assessment methodology.")

    if "scores" not in st.session_state:
        st.warning("Assessment scores are not available yet.")
        return

    profile = get_pillar_profile(st.session_state["scores"], questions)
    for pillar, value in profile.items():
        st.metric(pillar, f"{value:.2f}")


if __name__ == "__main__":
    render_pillars()
