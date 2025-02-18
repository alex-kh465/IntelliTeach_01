import streamlit as st
from lesson_planner import lesson_planner
from question_generator import question_generator
from presentation_generator import presentation_generator
from rubrics_generator import rubrics_generator
from question_paper_generator import question_paper_generator
from file_upload import handle_file_upload

# App Configuration
st.set_page_config(page_title="Christ IntelliTeach", page_icon="📚", layout="wide")

# Custom Styles
st.markdown(
    """
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { background-color: #4CAF50; color: white; }
    .sidebar .sidebar-content { background-color: #f4f4f4; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.image("assets/Picture1.jpg", width=200)
st.sidebar.title("🔍 Christ IntelliTeach")
st.sidebar.subheader("AI-Powered Education Toolkit")

# # Custom CSS for horizontal navbar
# st.markdown(
#     """
#     <style>
#         .navbar {
#             display: flex;
#             justify-content: center;
#             background-color: #4CAF50;
#             padding: 10px;
#             border-radius: 10px;
#         }
#         .navbar a {
#             color: white;
#             text-decoration: none;
#             padding: 14px 20px;
#             font-size: 18px;
#             font-weight: bold;
#         }
#         .navbar a:hover {
#             background-color: #45a049;
#             border-radius: 5px;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # JavaScript for URL routing in Streamlit
# st.markdown(
#     """
#     <div class="navbar">
#         <a href="?nav=🏠 Home">Home</a>
#         <a href="?nav=❓ Question Generator">Question Generator</a>
#         <a href="?nav=📖 Lesson Planner">Lesson Planner</a>
#         <a href="?nav=📽️ Presentation Generator">Presentation Generator</a>
#         <a href="?nav=✅ Rubrics Generator">Rubrics Generator</a>
#         <a href="?nav=📄 Question Paper Generator">Question Paper Generator</a>

#     </div>
#     <br>
#     """,
#     unsafe_allow_html=True
# )

# # Extract the selected page from the URL query parameter
# query_params = st.query_params
# choice = query_params.get("nav") or "🏠 Home"  # Default to Home if no query param exists

# Menu Options
menu = ["🏠 Home", "📖 Lesson Planner", "❓ Question Generator", "📽️ Presentation Generator",
        "✅ Rubrics Generator", "📄 Question Paper Generator"]

choice = st.sidebar.radio("📌 Select a Tool", menu)
# Call the function inside your main Streamlit app
handle_file_upload()


# Render Pages
if choice == "🏠 Home":

    # Custom CSS for improved UI
    st.markdown("""
        <style>
            /* Background gradient */
            .stApp {
                background: linear-gradient(to bottom, #3a7bd5, #3a6073);
                color: white;
            }
            
            /* Centered content */
            .main-container {
                text-align: center;
                padding-top: 50px;
            }
            
            /* Styling for the welcome text */
            .welcome-title {
                font-size: 36px;
                font-weight: bold;
                margin-bottom: 10px;
            }

            /* Subtitle */
            .subtitle {
                font-size: 18px;
                opacity: 0.9;
                margin-bottom: 20px;
            }

            /* Call-to-action button */
            .cta-button {
                display: inline-block;
                padding: 12px 25px;
                font-size: 18px;
                font-weight: bold;
                color: white;
                background: #AFE1AF;
                border-radius: 8px;
                text-decoration: none;
                transition: background 0.3s ease-in-out;
            }

            .cta-button:hover {
                background: #e67e22;
            }

            /* Animation */
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-10px); }
                to { opacity: 1; transform: translateY(0); }
            }

            .animated {
                animation: fadeIn 1s ease-in-out;
            }
        </style>
    """, unsafe_allow_html=True)

    # Home Page Content
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    st.markdown('<h1 class="welcome-title animated">🎓 Welcome to Christ IntelliTeach</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle animated">AI-powered tools to simplify teaching, from lesson planning to question generation.</p>', unsafe_allow_html=True)

    st.image("assets/christ.jpg", use_container_width=True)

    st.markdown('<a href="?page=Lesson Planner" class="cta-button animated">Get Started</a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    
elif choice == "📖 Lesson Planner":
    lesson_planner()

elif choice == "❓ Question Generator":
    question_generator()

elif choice == "📽️ Presentation Generator":
    presentation_generator()

elif choice == "✅ Rubrics Generator":
    rubrics_generator()

elif choice == "📄 Question Paper Generator":
    question_paper_generator()
