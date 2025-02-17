import streamlit as st
from utils.file_handler import generate_docx, generate_pdf
from utils.ai_helper import generate_questions_paper
from utils.difficulty_handler import get_blooms_taxonomy_distribution

def question_paper_generator():
    st.subheader("📄 AI-Powered Question Paper Generator")
    st.write("Generate a structured question paper based on topics, subtopics, and difficulty levels.")

    subject = st.text_input("📘 Subject", help="Enter the subject (e.g., Physics).")
    num_questions = st.number_input("❓ Total Number of Questions", min_value=1, max_value=100, value=10, step=1)

    # Topic & Subtopic Input
    topics = []
    num_topics = st.number_input("📌 Number of Topics", min_value=1, max_value=10, value=3, step=1)

    for i in range(num_topics):
        topic = st.text_input(f"🔹 Topic {i+1}", key=f"topic_{i}")
        subtopics = st.text_area(f"📑 Subtopics for Topic {i+1}", key=f"subtopic_{i}", help="Enter subtopics, separated by commas.")
        if topic and subtopics:
            topics.append({"topic": topic, "subtopics": subtopics.split(",")})

    # Get difficulty distribution
    difficulty_distribution = get_blooms_taxonomy_distribution()
    if not difficulty_distribution:
        return  # Stop if invalid

    if st.button("Generate Question Paper"):
        with st.spinner("Generating questions..."):
            question_paper_content = generate_questions_paper(subject, num_questions, topics, difficulty_distribution)
            st.session_state["question_paper"] = question_paper_content
            st.success("Question paper generated successfully!")

    # Display & Download
    if "question_paper" in st.session_state:
        st.subheader("📖 Preview Question Paper")
        st.text_area("Generated Question Paper", value=st.session_state["question_paper"], height=400)

        docx_data = generate_docx(st.session_state["question_paper"])
        pdf_data = generate_pdf(st.session_state["question_paper"])

        st.download_button("📥 Download Question Paper (DOCX)", docx_data, "question_paper.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        st.download_button("📥 Download Question Paper (PDF)", pdf_data, "question_paper.pdf", "application/pdf")
