import streamlit as st
from utils.ai_helper import generate_questions
from utils.file_handler import generate_docx, generate_pdf
from utils.difficulty_handler import get_blooms_taxonomy_distribution

def question_generator():
    st.subheader("📝 Question Generator")
    st.write("Generate various question types using AI.")

    # User Inputs
    subject = st.text_input("📚 Subject", help="Enter the subject name (e.g., Science)")
    topic = st.text_input("📝 Topic", help="Enter the topic name (e.g., Photosynthesis)")
    num_questions = st.number_input("🔢 Number of Questions", min_value=1, max_value=50, value=10)
    difficulty_distribution = get_blooms_taxonomy_distribution()
    if not difficulty_distribution:
        return  # Stop execution if invalid

    # Question Types
    question_types = st.multiselect("✏️ Select Question Types", 
                                    ["MCQ", "Fill in the Blanks", "Open-ended", "True/False"], 
                                    default=["MCQ"])

    if st.button("Generate Questions"):
        with st.spinner("Generating questions..."):
            questions = generate_questions(subject, topic, num_questions, difficulty_distribution, question_types)
            st.session_state["questions"] = questions
            st.success("Questions generated successfully!")

    # Display Generated Questions
    if "questions" in st.session_state:
        st.subheader("📖 Generated Questions")
        st.text_area("Review and Edit Questions", value=st.session_state["questions"], height=300)

        # Download Buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            st.download_button("📥 Download as TXT", st.session_state["questions"].encode(), "questions.txt")

        with col2:
            docx_data = generate_docx(st.session_state["questions"])
            st.download_button("📥 Download as DOCX", docx_data, "questions.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

        with col3:
            pdf_data = generate_pdf(st.session_state["questions"])
            st.download_button("📥 Download as PDF", pdf_data, "questions.pdf", "application/pdf")
