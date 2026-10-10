import streamlit as st
import plotly.express as px

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
    st.subheader("Highest-priority opportunities")
    st.caption("Items are ranked by distance from the target score of 5. The thresholds below are project-defined.")
    priority_rows = ranked[:10]
    chart_data = [
        {
            "Capability": row["construct"],
            "Gap": row["gap"],
            "Score": row["score"],
            "Classification": row["classification"],
        }
        for row in priority_rows
    ]
    color_map = {
        "High-priority gap": "#bd5146",
        "Development opportunity": "#d59a31",
        "Relative strength": "#087e78",
    }
    chart = px.bar(
        chart_data,
        x="Gap",
        y="Capability",
        orientation="h",
        text="Score",
        color="Classification",
        color_discrete_map=color_map,
        labels={"Gap": "Gap to target score (5)", "Capability": ""},
        hover_data={"Score": ":.2f", "Gap": ":.2f", "Classification": True},
    )
    chart.update_traces(texttemplate="Score %{text:.2f}", textposition="inside")
    chart.update_layout(
        height=max(360, len(priority_rows) * 42),
        margin=dict(l=8, r=18, t=12, b=48),
        xaxis=dict(range=[0, 4], dtick=1, gridcolor="#e7eeee"),
        yaxis=dict(categoryorder="array", categoryarray=[row["Capability"] for row in chart_data][::-1]),
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#243b45"),
        legend_title_text="",
    )
    st.plotly_chart(chart, use_container_width=True)
    st.dataframe(
        [
            {
                "Capability": row["construct"],
                "Dimension": row["dimension"],
                "Current score": row["score"],
                "Gap to target": row["gap"],
                "Priority": row["classification"],
            }
            for row in priority_rows
        ],
        hide_index=True,
        use_container_width=True,
    )


if __name__ == "__main__":
    render_gaps()
