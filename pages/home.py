import streamlit as st


def render_home():
    st.title("Industry 5.0 Readiness")
    st.caption("A practical assessment and improvement-planning workspace for manufacturing SMEs")

    with st.container(border=True):
        st.markdown("### Make your next transformation step clearer")
        st.write(
            "Build an evidence-aware view of your organisation’s readiness across people, "
            "strategy, processes and technology. Turn the results into focused improvement "
            "priorities and a practical roadmap."
        )
        st.caption(
            "Research-informed decision support — not a certification or a formal audit."
        )

    st.subheader("A clear path from assessment to action")
    steps = st.columns(4)
    step_content = [
        ("01 · Profile", "Add basic company context to your assessment."),
        ("02 · Assess", "Rate 38 maturity items on a consistent 1–5 scale."),
        ("03 · Understand", "Review scores, strengths and priority gaps."),
        ("04 · Plan", "Explore recommendations and build an improvement roadmap."),
    ]
    for column, (title, description) in zip(steps, step_content):
        with column:
            with st.container(border=True):
                st.markdown(f"**{title}**")
                st.write(description)

    st.subheader("What the assessment covers")
    col1, col2, col3 = st.columns(3)
    col1.metric("Maturity dimensions", "7", "Research-derived model")
    col2.metric("Assessment items", "38", "Rated on a 1–5 scale")
    col3.metric("Industry 5.0 pillars", "3", "Human-centricity · sustainability · resilience")

    st.info(
        "To get started, open **Company profile** and then **Assessment** from the single "
        "navigation menu. Your results and planning tools become meaningful once scores are entered."
    )

    with st.expander("How to interpret the results"):
        st.write(
            "Scores summarize the responses using the published dimension and item weights. "
            "Gap categories and planning suggestions are project-defined diagnostics; use them "
            "as prompts for discussion and validate them against company evidence."
        )


if __name__ == "__main__":
    render_home()
