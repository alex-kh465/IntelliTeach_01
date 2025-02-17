import streamlit as st
from docx import Document
from io import BytesIO
from utils.ai_helper import generate_lesson_plan  # AI-based lesson plan generation
from utils.file_handler import generate_docx

def lesson_planner():
    st.subheader("📅 Lesson Planner")
    st.write("Plan your lessons with AI-generated topic structures.")

    # User Inputs
    subject = st.text_input("📚 Subject", help="Enter the subject name (e.g., Mathematics)")
    topic = st.text_input("📝 Topic", help="Enter the main topic (e.g., Algebra)")
    subtopics = st.text_area("🔹 Subtopics", help="Enter subtopics (comma-separated)")

    lesson_type = st.selectbox("🎯 Lesson Type", ["Lecture", "Activity-Based", "Quiz-Oriented"])

    if st.button("Generate Lesson Plan"):
        with st.spinner("Generating lesson plan..."):
            lesson_plan = generate_lesson_plan(subject, topic, subtopics, lesson_type)
            st.session_state["lesson_plan"] = lesson_plan
            st.success("Lesson plan generated successfully!")

    # Display the Lesson Plan
    if "lesson_plan" in st.session_state:
        st.subheader("📖 Lesson Plan")
        st.text_area("Generated Lesson Plan", value=st.session_state["lesson_plan"], height=300)

        # Download Button
        st.download_button(
            "📥 Download Lesson Plan (DOCX)",
            generate_docx(st.session_state["lesson_plan"]),
            "lesson_plan.docx",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
