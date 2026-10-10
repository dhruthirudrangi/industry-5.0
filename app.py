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
    page_title="Industry 5.0 SME Readiness Assessment",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)

PAGE_MAP = {
    "Home": render_home,
    "About Industry 5.0": render_about,
    "Company Profile": render_company,
    "Assessment": render_assessment,
    "Results Dashboard": render_results,
    "Dimension Analysis": render_dimensions,
    "Pillar Analysis": render_pillars,
    "Gap Analysis": render_gaps,
    "What-if Simulator": render_what_if,
    "Sensitivity Analysis": render_sensitivity,
    "Recommendations": render_recommendations,
    "Roadmap": render_roadmap,
    "Validation / 3 SMEs": render_validation,
    "Reports": render_reports,
    "Methodology & Sources": render_methodology,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGE_MAP.keys()))
PAGE_MAP[selection]()
