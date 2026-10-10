import streamlit as st

from engine.roadmap import generate_roadmap
from engine.scoring import load_questions


def render_roadmap():
    questions = load_questions()
    st.title("Model-based Improvement Roadmap")

    if "scores" not in st.session_state:
        st.warning("Assessment scores are not available yet.")
        return

    roadmap = generate_roadmap(st.session_state["scores"], questions)
    for phase in roadmap:
        st.subheader(phase["phase"])
        st.caption(phase["window"])
        for item in phase["items"]:
            st.write(f"- Action: {item['action']} | Gap: {item['gap']} | Priority: {item['gap']} | Timeline: {item['timeline']} | KPI: {item['kpi']} | Pillar: {item['pillar']}")
        st.write("---")


if __name__ == "__main__":
    render_roadmap()
