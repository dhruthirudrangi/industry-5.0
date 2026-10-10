import streamlit as st

from engine.scoring import load_questions
from utils import default_scores


def render_assessment():
    questions = load_questions()
    st.title("Assessment")

    if "scores" not in st.session_state:
        st.session_state["scores"] = default_scores()

    all_items = questions["items"]
    progress = st.progress(0)
    current = 0

    for dim in questions["dimensions"]:
        dim_items = [item for item in all_items if item["dimension"] == dim["id"]]
        st.subheader(dim["name"])
        st.caption(f"{len(dim_items)} items")
        for item in dim_items:
            st.markdown(f"**{item['question']}**")
            score = st.slider(
                f"{item['id']} — {item['construct']}",
                min_value=1,
                max_value=5,
                value=int(st.session_state["scores"].get(item["id"], 3)),
                step=1,
                help=f"{item['help_text']}\n\n[RESEARCH-DERIVED] Item weight: {item['weight']} | Pillar: {item['pillar']}"
            )
            st.session_state["scores"][item["id"]] = score
            st.text_area(f"Evidence / Notes for {item['construct']}", value="", key=f"evidence_{item['id']}", help="Optional evidence, notes, or observations.")
            st.selectbox(
                f"Evidence confidence for {item['construct']}",
                ["No evidence", "Self-reported", "Documented", "System-generated", "Verified"],
                key=f"confidence_{item['id']}",
                help="Project-specific evidence heuristic: not a scientific score."
            )
            st.caption(f"Research-derived item weight: {item['weight']} | Pillar mapping: {item['pillar']}")
            current += 1
            progress.progress(current / len(all_items))

    if st.button("Calculate Maturity"):
        st.session_state["assessment_complete"] = True
        st.success("Assessment ready for scoring and dashboard analysis.")

    if "assessment_complete" in st.session_state:
        st.markdown("Open the Results Dashboard in the sidebar.")


if __name__ == "__main__":
    render_assessment()
