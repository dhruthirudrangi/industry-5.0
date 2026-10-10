import streamlit as st
import plotly.express as px

from engine.scoring import load_questions
from engine.sensitivity import sensitivity_table


def render_sensitivity():
    questions = load_questions()
    st.title("Sensitivity analysis")
    st.markdown("This is a mathematical sensitivity analysis of the chosen scoring framework, not evidence that implementing a change will produce a specific business outcome.")

    if "scores" not in st.session_state:
        st.warning("Assessment scores are not available yet.")
        return

    result = sensitivity_table(st.session_state["scores"], questions)
    st.subheader("Overall score under improvement scenarios")
    chart = px.line(
        result["rows"],
        x="dimension",
        y=["+0.5", "+1.0", "+1.5"],
        markers=True,
        labels={
            "dimension": "Dimension improved",
            "value": "Simulated overall score",
            "variable": "Score increase",
        },
        category_orders={
            "dimension": [dimension["name"] for dimension in questions["dimensions"]],
        },
    )
    chart.add_hline(
        y=result["current_total"],
        line_dash="dash",
        line_color="#7b8d93",
        annotation_text=f"Current overall · {result['current_total']:.2f}",
        annotation_position="top left",
    )
    chart.update_layout(
        height=390,
        margin=dict(l=12, r=18, t=35, b=90),
        yaxis=dict(range=[0, 5], dtick=1, gridcolor="#e7eeee"),
        xaxis=dict(tickangle=-18),
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#243b45"),
        legend_title_text="",
    )
    st.plotly_chart(chart, use_container_width=True)
    st.caption(
        "Each scenario increases one dimension’s item scores by the amount shown, capped at 5. "
        "Values are model sensitivity results, not predicted operational outcomes."
    )
    st.dataframe(result["rows"], hide_index=True, use_container_width=True)


if __name__ == "__main__":
    render_sensitivity()
