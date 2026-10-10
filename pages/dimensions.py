import streamlit as st
import plotly.express as px

from engine.scoring import calculate_dimension_scores, load_questions


def render_dimensions():
    questions = load_questions()
    st.title("Dimension analysis")
    st.caption("Compare maturity across all dimensions, then expand a dimension to inspect its item-level scores.")

    if "scores" not in st.session_state:
        st.warning("Assessment scores are not available yet.")
        return

    scores = st.session_state["scores"]
    all_dim_scores = calculate_dimension_scores(scores, questions)
    dimension_data = [
        {"Dimension": dim["name"], "Score": all_dim_scores.get(dim["id"], 0.0)}
        for dim in questions["dimensions"]
    ]
    chart = px.bar(
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
    chart.update_traces(texttemplate="%{text:.2f}", textposition="outside", cliponaxis=False)
    chart.update_layout(
        height=390,
        margin=dict(l=8, r=36, t=12, b=36),
        coloraxis_showscale=False,
        xaxis=dict(range=[0, 5], dtick=1, gridcolor="#e7eeee"),
        yaxis=dict(categoryorder="array", categoryarray=[row["Dimension"] for row in dimension_data]),
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#243b45"),
    )
    st.plotly_chart(chart, use_container_width=True)

    for dim in questions["dimensions"]:
        dim_id = dim["id"]
        dim_score = all_dim_scores.get(dim_id, 0.0)
        normalized_weight = dim["weight"] / sum(d["weight"] for d in questions["dimensions"])
        with st.expander(f"{dim['name']} · {dim_score:.2f} / 5"):
            st.caption(
                f"Published weight: {dim['weight']:.2f} · "
                f"Normalized internal weight: {normalized_weight:.1%}"
            )
            items = [item for item in questions["items"] if item["dimension"] == dim_id]
            st.dataframe(
                [
                    {
                        "Capability": item["construct"],
                        "Score": int(scores.get(item["id"], 0)),
                        "Gap to target": 5 - int(scores.get(item["id"], 0)),
                        "Item weight": item["weight"],
                    }
                    for item in items
                ],
                hide_index=True,
                use_container_width=True,
            )


if __name__ == "__main__":
    render_dimensions()
