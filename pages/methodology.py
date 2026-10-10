import streamlit as st


def render_methodology():
    st.title("Methodology & Sources")

    st.subheader("Research foundation")
    st.markdown("[RESEARCH-DERIVED] The main maturity model is informed by Latino (2025), who proposes a seven-dimension Industry 5.0 maturity model for manufacturing SMEs. The paper articulates 38 maturity items, pillar-based assessment, and maturity levels for SME evaluation. The project uses the published dimension weights and item weights as the foundation for the interactive assessment engine.")

    st.subheader("Project extensions")
    st.markdown("[PROJECT EXTENSION] The software adds evidence capture, transparent scoring, interactive dashboards, prioritisation heuristic, simulation, sensitivity analysis, roadmap generation, synthetic validation, and downloadable reporting.")

    st.subheader("Methodology statement")
    st.markdown("The software is a research-informed prototype and does not claim to reproduce the original authors' complete validated instrument.")

    st.subheader("Source links")
    links = [
        ("Latino (2025)", "https://doi.org/10.1016/j.techfore.2025.124045"),
        ("ScienceDirect", "https://www.sciencedirect.com/science/article/pii/S0040162525000769"),
        ("European Commission: Industry 5.0", "https://research-and-innovation.ec.europa.eu/research-area/industrial-research-and-innovation/industry-50_en"),
        ("European Commission: Industry 5.0 report", "https://research-and-innovation.ec.europa.eu/knowledge-publications-tools-and-data/publications/all-publications/industry-50-towards-sustainable-human-centric-and-resilient-european-industry_en"),
        ("European Commission: Industry 5.0 and future of work", "https://research-and-innovation.ec.europa.eu/knowledge-publications-tools-and-data/publications/all-publications/industry-50-and-future-work_en"),
        ("acatech maturity index", "https://en.acatech.de/publication/industrie-4-0-maturity-index-update-2020/"),
        ("acatech project page", "https://en.acatech.de/project/industry-4-0-maturity-index/"),
    ]
    for label, url in links:
        st.markdown(f"- [{label}]({url})")


if __name__ == "__main__":
    render_methodology()
