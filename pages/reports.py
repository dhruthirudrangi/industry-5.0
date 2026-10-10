import streamlit as st

from engine.scoring import load_questions
from reports.report_generator import export_assessment_bundle


def render_reports():
    questions = load_questions()
    st.title("Reports")

    if "scores" not in st.session_state:
        st.warning("Assessment scores are not available yet.")
        return

    profile = st.session_state.get("company_profile", {
        "company_name": "Demo Company",
        "industry": "Manufacturing",
        "company_size": "50-249 employees",
        "assessment_date": "2026-09-28",
    })

    score_summary = {
        "overall_score": 3.0,
        "maturity_level": "Level 3",
        "scores": st.session_state["scores"],
    }

    if st.button("Download Assessment Report"):
        bundle = export_assessment_bundle(profile, score_summary, questions, [])
        st.success(f"Report generated at {bundle['html']} and {bundle['pdf']}")

    st.caption("This report clearly separates research-derived methodology from project-specific software extensions.")


if __name__ == "__main__":
    render_reports()
