import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="SmartHire Bot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 SmartHire Bot")
st.subheader("Resume Upload Module")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    st.success("Resume uploaded successfully!")

    st.subheader("Extracted Resume Text")

    st.text_area(
    label="Resume Text",
    value=text,
    height=450
    )