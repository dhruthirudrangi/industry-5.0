import streamlit as st

from engine.gap_analysis import compute_gap_rankings
from engine.scoring import load_questions


def render_gaps():
    questions = load_questions()
    st.title("Gap Analysis")
    st.caption("Project-defined diagnostic thresholds: Score < 2.5 = High-priority gap, 2.5–3.49 = Development opportunity, >= 3.5 = Relative strength.")

    if "scores" not in st.session_state:
        st.warning("Assessment scores are not available yet.")
        return

    ranked = compute_gap_rankings(st.session_state["scores"], questions)
    for row in ranked[:10]:
        st.markdown(f"- **{row['construct']}** ({row['id']}): Score {row['score']} | Gap {row['gap']} | {row['classification']}")


if __name__ == "__main__":
    render_gaps()
