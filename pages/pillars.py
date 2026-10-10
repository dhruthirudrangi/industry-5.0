import streamlit as st
import plotly.express as px

from engine.pillar_analysis import get_pillar_profile
from engine.scoring import load_questions


def render_pillars():
    questions = load_questions()
    st.title("Pillar Analysis")
    st.markdown(
        "This pillar profile is a project-specific diagnostic view and should not be interpreted "
        "as a replacement for the research model's full pillar-based assessment methodology."
    )

    if "scores" not in st.session_state:
        st.warning("Assessment scores are not available yet.")
        return

    profile = get_pillar_profile(st.session_state["scores"], questions)
    metrics = st.columns(len(profile))
    for column, (pillar, value) in zip(metrics, profile.items()):
        column.metric(pillar, f"{value:.2f} / 5")

    chart = px.bar(
        [{"Pillar": pillar, "Score": value} for pillar, value in profile.items()],
        x="Pillar",
        y="Score",
        range_y=[0, 5],
        text="Score",
        color="Score",
        color_continuous_scale=["#dce9e8", "#56aaa1", "#087e78"],
        labels={"Score": "Maturity score (out of 5)"},
    )
    chart.update_traces(texttemplate="%{text:.2f}", textposition="outside", cliponaxis=False)
    chart.update_layout(
        height=360,
        margin=dict(l=12, r=12, t=18, b=55),
        coloraxis_showscale=False,
        yaxis=dict(range=[0, 5], dtick=1, gridcolor="#e7eeee"),
        xaxis=dict(tickangle=-12),
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#243b45"),
    )
    st.plotly_chart(chart, use_container_width=True)


if __name__ == "__main__":
    render_pillars()
