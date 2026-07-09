import streamlit as st


def show_jobs(results):

    st.subheader("🎯 Top Matching Jobs")

    for i, job in enumerate(results, start=1):

        with st.expander(f"{i}. {job['job_title']}"):

            st.write(f"**🏢 Company:** {job['company']}")

            st.write(f"**📍 Location:** {job['job_location']}")

            st.write(f"**💼 Type:** {job['job_type']}")

            st.write("### 🧠 Skills")

            st.write(job["job_skills"])

            st.write("### 📄 Summary")

            st.write(job["job_summary"])