import streamlit as st


def render_home():
    st.title("Industry 5.0 SME Readiness Assessment")
    st.caption("Research-informed interactive decision-support system for manufacturing SMEs")

    st.markdown("""
    This prototype helps a manufacturing SME understand its current digital and organisational maturity, assess readiness for Industry 5.0, identify capability gaps, simulate improvements, and generate a personalised roadmap.

    The system is research-informed and explicitly distinguishes between the underlying research foundation and our project-specific extensions.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Overall score", "—", "Model-based")
    col2.metric("Maturity level", "—", "Research-informed")
    col3.metric("Primary pillars", "Sustainability, Resilience, Human-centricity", "EU concept")

    st.subheader("Quick start")
    st.markdown("1. Complete the company profile")
    st.markdown("2. Run the 38-item assessment")
    st.markdown("3. Review the dashboard")
    st.markdown("4. Generate the roadmap")


if __name__ == "__main__":
    render_home()
