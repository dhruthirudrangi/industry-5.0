import streamlit as st
import plotly.express as px

from engine.scoring import calculate_overall_score, calculate_dimension_scores, get_maturity_level, load_questions
from engine.pillar_analysis import get_pillar_profile


def render_results():
    st.title("Results dashboard")
    st.caption("A concise view of overall maturity, dimension performance and Industry 5.0 pillars.")
    questions = load_questions()

    if "scores" not in st.session_state:
        st.warning("No assessment scores are available yet. Complete the assessment to see your results.")
        return

    scores = st.session_state["scores"]
    overall_score = calculate_overall_score(scores, questions)
    level, interpretation = get_maturity_level(overall_score)

    dim_scores = calculate_dimension_scores(scores, questions)

    col1, col2, col3, col4 = st.columns(4)
    dim_names = {dimension["id"]: dimension["name"] for dimension in questions["dimensions"]}
    strongest = max(dim_scores, key=dim_scores.get)
    weakest = min(dim_scores, key=dim_scores.get)
    col1.metric("Overall maturity", f"{overall_score:.2f} / 5")
    col2.metric("Maturity level", level)
    col3.metric("Strongest dimension", dim_names.get(strongest, strongest), f"{dim_scores[strongest]:.2f} / 5")
    col4.metric("Priority dimension", dim_names.get(weakest, weakest), f"{dim_scores[weakest]:.2f} / 5")

    st.caption(
        f"{interpretation}. Scores use the published dimension and item weights, "
        "with dimension weights normalized internally."
    )

    st.subheader("Maturity across seven dimensions")
    dimension_data = [
        {"Dimension": dim_names.get(dim_id, dim_id), "Score": score}
        for dim_id, score in dim_scores.items()
    ]
    dimension_data.sort(key=lambda row: row["Score"])
    dimension_chart = px.bar(
        dimension_data,
        x="Score",
        y="Dimension",
        orientation="h",
        range_x=[0, 5],
        text="Score",
        color="Score",
        color_continuous_scale=["#dce9e8", "#56aaa1", "#087e78"],
        labels={"Score": "Maturity score (out of 5)", "Dimension": ""},
    )
    dimension_chart.update_traces(texttemplate="%{text:.2f}", textposition="outside", cliponaxis=False)
    dimension_chart.update_layout(
        height=390,
        margin=dict(l=8, r=36, t=12, b=36),
        coloraxis_showscale=False,
        xaxis=dict(range=[0, 5], dtick=1, gridcolor="#e7eeee"),
        yaxis=dict(categoryorder="array", categoryarray=[row["Dimension"] for row in dimension_data]),
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#243b45"),
    )
    st.plotly_chart(dimension_chart, use_container_width=True)

    pillar_profile = get_pillar_profile(scores, questions)
    st.subheader("Industry 5.0 pillar profile")
    pillar_data = [{"Pillar": pillar, "Score": value} for pillar, value in pillar_profile.items()]
    pillar_chart = px.bar(
        pillar_data,
        x="Pillar",
        y="Score",
        range_y=[0, 5],
        text="Score",
        color="Score",
        color_continuous_scale=["#dce9e8", "#56aaa1", "#087e78"],
        labels={"Score": "Maturity score (out of 5)"},
    )
    pillar_chart.update_traces(texttemplate="%{text:.2f}", textposition="outside", cliponaxis=False)
    pillar_chart.update_layout(
        height=310,
        margin=dict(l=12, r=12, t=12, b=55),
        coloraxis_showscale=False,
        yaxis=dict(range=[0, 5], dtick=1, gridcolor="#e7eeee"),
        xaxis=dict(tickangle=-12),
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#243b45"),
    )
    st.plotly_chart(pillar_chart, use_container_width=True)

    with st.expander("How is the overall score calculated?"):
        st.write(
            f"The overall score is the weighted combination of the seven dimension scores. "
            f"The current result is **{overall_score:.2f} / 5**, corresponding to **{level} — {interpretation}**."
        )


if __name__ == "__main__":
    render_results()
