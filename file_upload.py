import streamlit as st
from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_docx(docx_file):
    """Extract text from a .docx Word file"""
    doc = Document(docx_file)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file"""
    pdf_reader = PdfReader(pdf_file)
    return "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])

def handle_file_upload():
    """Upload and extract text from PDF or Word files"""
    uploaded_file = st.file_uploader("📂 Upload a PDF or Word Document", type=["pdf", "docx"])

    if uploaded_file:
        file_type = uploaded_file.name.split(".")[-1].lower()
        
        if file_type == "pdf":
            extracted_text = extract_text_from_pdf(uploaded_file)
        elif file_type == "docx":
            extracted_text = extract_text_from_docx(uploaded_file)
        else:
            st.error("❌ Unsupported file format.")
            return None

        # Store extracted text in session state
        st.session_state["uploaded_content"] = extracted_text

        st.success("✅ File uploaded successfully! Content will be used for all features.")

        # Show extracted text (for debugging)
        with st.expander("📄 Extracted Content Preview"):
            st.write(extracted_text[:1000] + ("..." if len(extracted_text) > 1000 else ""))

