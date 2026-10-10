import streamlit as st

from engine.scoring import load_questions
from engine.sensitivity import sensitivity_table


def render_sensitivity():
    questions = load_questions()
    st.title("Sensitivity Analysis")
    st.markdown("This is a mathematical sensitivity analysis of the chosen scoring framework, not evidence that implementing a change will produce a specific business outcome.")

    if "scores" not in st.session_state:
        st.warning("Assessment scores are not available yet.")
        return

    result = sensitivity_table(st.session_state["scores"], questions)
    for row in result["rows"]:
        st.write(row)


if __name__ == "__main__":
    render_sensitivity()
