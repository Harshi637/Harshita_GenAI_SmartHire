import streamlit as st


def show_resume(profile):

    st.subheader("📋 Resume Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.write("### 👤 Basic Information")

        st.write("**Name:**", profile.get("name", ""))

        st.write("**Email:**", profile.get("email", ""))

        st.write("**Phone:**", profile.get("phone", ""))

    with col2:

        st.write("### 🎯 Target Role")

        st.write(profile.get("target_role", ""))

    st.markdown("---")

    st.write("### 🛠 Skills")

    skills = profile.get("skills", [])

    if skills:
        st.write(", ".join(str(skill) for skill in skills))
    else:
        st.info("No skills detected.")

    st.markdown("---")

    st.write("### 🎓 Education")

    education = profile.get("education", [])

    if education:
        for item in education:
            st.write("-", item)
    else:
        st.info("No education found.")