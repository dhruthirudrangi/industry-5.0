import streamlit as st


def render_company():
    st.title("Company Profile")
    st.session_state.setdefault("company_profile", {
        "company_name": "",
        "industry": "",
        "company_size": "",
        "assessment_date": "",
    })

    with st.form("company_profile_form"):
        company_name = st.text_input("Company Name", value=st.session_state["company_profile"].get("company_name", ""))
        industry = st.text_input("Industry", value=st.session_state["company_profile"].get("industry", ""))
        company_size = st.selectbox(
            "Company Size",
            ["< 50 employees", "50-249 employees", "250-500 employees", "> 500 employees"],
            index=["< 50 employees", "50-249 employees", "250-500 employees", "> 500 employees"].index(
                st.session_state["company_profile"].get("company_size", "50-249 employees")
            ) if st.session_state["company_profile"].get("company_size") in ["< 50 employees", "50-249 employees", "250-500 employees", "> 500 employees"] else 1,
        )
        assessment_date = st.date_input(
            "Assessment Date",
            value=None if not st.session_state["company_profile"].get("assessment_date") else st.session_state["company_profile"]["assessment_date"],
        )
        submitted = st.form_submit_button("Save profile")

    if submitted:
        st.session_state["company_profile"] = {
            "company_name": company_name,
            "industry": industry,
            "company_size": company_size,
            "assessment_date": assessment_date.isoformat() if hasattr(assessment_date, "isoformat") else str(assessment_date),
        }
        st.success("Company profile saved.")

    if st.session_state["company_profile"].get("company_name") or st.session_state["company_profile"].get("industry"):
        st.write(st.session_state["company_profile"])


if __name__ == "__main__":
    render_company()
