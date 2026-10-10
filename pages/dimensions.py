import streamlit as st

from engine.scoring import calculate_dimension_scores, load_questions


def render_dimensions():
    questions = load_questions()
    st.title("Dimension Analysis")

    if "scores" not in st.session_state:
        st.warning("Assessment scores are not available yet.")
        return

    scores = st.session_state["scores"]
    all_dim_scores = calculate_dimension_scores(scores, questions)

    for dim in questions["dimensions"]:
        dim_id = dim["id"]
        dim_score = all_dim_scores.get(dim_id, 0.0)
        st.subheader(dim["name"])
        st.write(f"Dimension score: {dim_score:.2f}")
        st.write(f"Dimension weight: {dim['weight']} (published) | Normalized internal weight: {dim['weight'] / sum(d['weight'] for d in questions['dimensions']):.4f}")
        items = [item for item in questions["items"] if item["dimension"] == dim_id]
        for item in items:
            item_score = scores.get(item["id"], 0)
            st.markdown(f"- **{item['construct']}**: Score {item_score} | Weight {item['weight']} | Gap {5-item_score}")
        st.write("---")


if __name__ == "__main__":
    render_dimensions()
