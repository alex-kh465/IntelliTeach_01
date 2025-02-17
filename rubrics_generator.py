import streamlit as st
from utils.ai_helper import generate_rubrics
from utils.file_handler import generate_docx, generate_pdf
from utils.difficulty_handler import get_blooms_taxonomy_distribution

def rubrics_generator():
    st.subheader("📊 Rubrics Generator")
    st.write("Generate grading rubrics for subjective/open-ended questions.")

    # User Inputs
    subject = st.text_input("📚 Subject", help="Enter the subject name (e.g., English)")
    topic = st.text_input("📝 Topic", help="Enter the topic name (e.g., Essay Writing)")
    criteria = st.text_area("📌 Assessment Criteria", 
                            help="Enter grading criteria (e.g., Clarity, Depth of Analysis, Grammar)")
    
    difficulty_distribution = get_blooms_taxonomy_distribution()
    if not difficulty_distribution:
        return  # Stop execution if invalid

    if st.button("Generate Rubrics"):
        with st.spinner("Generating rubrics..."):
            rubrics = generate_rubrics(subject, topic, difficulty_distribution, criteria)
            st.session_state["rubrics"] = rubrics
            st.success("Rubrics generated successfully!")

    # Display Generated Rubrics
    if "rubrics" in st.session_state:
        st.subheader("📖 Generated Rubrics")
        st.text_area("Review and Edit Rubrics", value=st.session_state["rubrics"], height=300)

        # Download Buttons
        col1, col2 = st.columns(2)
        with col1:
            docx_data = generate_docx(st.session_state["rubrics"])
            st.download_button("📥 Download as DOCX", docx_data, "rubrics.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

        with col2:
            pdf_data = generate_pdf(st.session_state["rubrics"])
            st.download_button("📥 Download as PDF", pdf_data, "rubrics.pdf", "application/pdf")