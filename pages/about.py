import streamlit as st


def render_about():
    st.title("About Industry 5.0")
    st.markdown("""
    [RESEARCH-DERIVED] Industry 5.0 is understood as a human-centred, sustainable, and resilient evolution of industrial practice. It builds on Industry 4.0 technologies and capabilities, rather than replacing them outright. The European Commission describes Industry 5.0 around three major priorities: human-centricity, sustainability, and resilience (European Commission, 2021).

    Industry 1.0 to 4.0 can be read as a progression from mechanisation to digitalisation, automation, and interconnected smart manufacturing. Industry 5.0 extends this trajectory by emphasising not only productivity and efficiency, but also worker wellbeing, ecological sustainability, and operational resilience.
    """)

    st.subheader("Industry evolution")
    st.markdown(
        """
        - Industry 1.0: mechanisation and steam power
        - Industry 2.0: mass production and electricity
        - Industry 3.0: automation and electronics
        - Industry 4.0: digitalisation, connectivity, IoT, AI, smart manufacturing
        - Industry 5.0: human-centricity, sustainability, resilience
        """
    )

    st.subheader("Industry 4.0 context")
    st.markdown("""
    Industry 4.0 provides the digital backbone of automation, sensing, analytics, connectivity, and manufacturing intelligence. The acatech Industrie 4.0 Maturity Index illustrates how maturity models help organisations assess digital transformation progress in a structured way (acatech, 2020).
    """)

    st.subheader("Industry 5.0 priorities")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Human-centricity\nThe factory is designed around human skills, wellbeing, and meaningful work.")
    with col2:
        st.markdown("### Sustainability\nThe objective is to align productivity with environmental stewardship and resource efficiency.")
    with col3:
        st.markdown("### Resilience\nOrganisations aim to maintain continuity, agility, and adaptability under uncertainty.")

    st.caption("This page is research-informed; the software itself is a project-specific operationalisation and decision-support tool.")


if __name__ == "__main__":
    render_about()
