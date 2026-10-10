import streamlit as st
import plotly.express as px

from engine.scoring import calculate_dimension_scores, calculate_overall_score, load_questions


def render_what_if():
    questions = load_questions()
    st.title("What-if improvement simulator")
    st.caption("Explore how a proposed improvement scenario could change maturity scores.")

    if "scores" not in st.session_state:
        st.warning("Assessment scores are not available yet.")
        return

    current_scores = st.session_state["scores"]
    current_overall = calculate_overall_score(current_scores, questions)
    current_dimensions = calculate_dimension_scores(current_scores, questions)
    st.metric("Current overall maturity", f"{current_overall:.2f} / 5")

    scenario = {}
    for dim in questions["dimensions"]:
        options = [1, 2, 3, 4, 5]
        default_score = round(current_dimensions.get(dim["id"], 3.0))
        scenario[dim["id"]] = st.selectbox(
            f"Set {dim['name']} score",
            options,
            index=max(0, min(4, default_score - 1)),
        )

    if st.button("Simulate scenario"):
        simulated = dict(current_scores)
        for item in questions["items"]:
            if item["dimension"] in scenario:
                simulated[item["id"]] = scenario[item["dimension"]]
        new_overall = calculate_overall_score(simulated, questions)
        simulated_dimensions = calculate_dimension_scores(simulated, questions)
        change = new_overall - current_overall

        col1, col2 = st.columns(2)
        col1.metric("Scenario overall maturity", f"{new_overall:.2f} / 5", f"{change:+.2f}")
        col2.metric("Baseline overall maturity", f"{current_overall:.2f} / 5")

        dimension_names = {dim["id"]: dim["name"] for dim in questions["dimensions"]}
        comparison = [
            {"Dimension": dimension_names.get(dim_id, dim_id), "Scenario": "Current", "Score": score}
            for dim_id, score in current_dimensions.items()
        ]
        comparison.extend(
            {
                "Dimension": dimension_names.get(dim_id, dim_id),
                "Scenario": "Simulated",
                "Score": score,
            }
            for dim_id, score in simulated_dimensions.items()
        )
        chart = px.bar(
            comparison,
            x="Dimension",
            y="Score",
            color="Scenario",
            barmode="group",
            range_y=[0, 5],
            color_discrete_map={"Current": "#9aadb2", "Simulated": "#087e78"},
            labels={"Score": "Maturity score (out of 5)"},
            category_orders={
                "Dimension": [dimension_names[dim["id"]] for dim in questions["dimensions"]],
                "Scenario": ["Current", "Simulated"],
            },
        )
        chart.update_layout(
            height=390,
            margin=dict(l=12, r=12, t=18, b=80),
            yaxis=dict(range=[0, 5], dtick=1, gridcolor="#e7eeee"),
            xaxis=dict(tickangle=-18),
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(color="#243b45"),
            legend_title_text="",
        )
        st.plotly_chart(chart, use_container_width=True)
        st.caption(
            "The simulator changes item scores to the selected dimension-level values. "
            "Treat this as a mathematical scenario, not a forecast of business outcomes."
        )


if __name__ == "__main__":
    render_what_if()
