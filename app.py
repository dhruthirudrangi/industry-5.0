import streamlit as st

from pages.about import render_about
from pages.assessment import render_assessment
from pages.company import render_company
from pages.dimensions import render_dimensions
from pages.gaps import render_gaps
from pages.home import render_home
from pages.methodology import render_methodology
from pages.pillars import render_pillars
from pages.recommendations import render_recommendations
from pages.reports import render_reports
from pages.results import render_results
from pages.roadmap import render_roadmap
from pages.sensitivity import render_sensitivity
from pages.validation import render_validation
from pages.what_if import render_what_if

st.set_page_config(
    page_title="Industry 5.0 SME Readiness",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        :root {
            --ink: #142d3a;
            --muted-ink: #5c6f78;
            --brand: #087e78;
            --line: #e4ecec;
            --canvas: #f5f8f8;
        }
        .stApp {
            background: var(--canvas);
            color: var(--ink);
        }
        [data-testid="stAppViewContainer"] .main .block-container {
            max-width: 1240px;
            padding-top: 2.2rem;
            padding-bottom: 3rem;
        }
        [data-testid="stSidebar"] {
            background: #102d3a;
        }
        [data-testid="stSidebar"] * {
            color: #edf7f6;
        }
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
            color: #b9d1d1;
        }
        h1, h2, h3 {
            color: var(--ink);
            letter-spacing: -0.025em;
        }
        [data-testid="stMetric"] {
            background: #ffffff;
            border: 1px solid var(--line);
            border-radius: 14px;
            padding: 1rem 1.1rem;
            box-shadow: 0 3px 14px rgba(20, 45, 58, 0.04);
        }
        [data-testid="stMetricLabel"] {
            color: var(--muted-ink);
        }
        [data-testid="stMetricValue"] {
            color: var(--ink);
        }
        div.stButton > button, div.stFormSubmitButton > button {
            border-radius: 9px;
            border: 1px solid var(--brand);
            font-weight: 600;
        }
        div.stButton > button[kind="primary"],
        div.stFormSubmitButton > button[kind="primary"] {
            background: var(--brand);
        }
        [data-testid="stExpander"] {
            background: #ffffff;
            border: 1px solid var(--line);
            border-radius: 12px;
        }
        [data-testid="stAlert"] {
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("## Industry 5.0")
st.sidebar.markdown("SME readiness workspace")

PAGES = {
    "Workspace": [
        st.Page(render_home, title="Home", icon=":material/home:", default=True),
        st.Page(render_company, title="Company profile", icon=":material/business:"),
        st.Page(render_assessment, title="Assessment", icon=":material/checklist:"),
    ],
    "Insights": [
        st.Page(render_results, title="Results dashboard", icon=":material/space_dashboard:"),
        st.Page(render_dimensions, title="Dimension analysis", icon=":material/bar_chart:"),
        st.Page(render_pillars, title="Pillar analysis", icon=":material/donut_large:"),
        st.Page(render_gaps, title="Gap analysis", icon=":material/troubleshoot:"),
    ],
    "Planning": [
        st.Page(render_recommendations, title="Recommendations", icon=":material/lightbulb:"),
        st.Page(render_roadmap, title="Roadmap", icon=":material/route:"),
        st.Page(render_what_if, title="What-if simulator", icon=":material/tune:"),
        st.Page(render_sensitivity, title="Sensitivity analysis", icon=":material/monitoring:"),
    ],
    "Resources": [
        st.Page(render_about, title="About Industry 5.0", icon=":material/info:"),
        st.Page(render_validation, title="Validation", icon=":material/fact_check:"),
        st.Page(render_reports, title="Reports", icon=":material/description:"),
        st.Page(render_methodology, title="Methodology & sources", icon=":material/library_books:"),
    ],
}

navigation = st.navigation(PAGES, position="sidebar", expanded=True)
navigation.run()
