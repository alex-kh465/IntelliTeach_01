import streamlit as st
import base64
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

# ---- FUNCTION TO SET BACKGROUND IMAGE ----
def set_bg(image_file):
    """Set a background image using base64 encoding."""
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---- SET LOCAL IMAGE AS BACKGROUND ----
set_bg("assets/bg_2.jpg") 


# Sidebar Navigation
st.sidebar.image("assets/Picture1.jpg", width=200)
st.sidebar.title("🔍 Christ IntelliTeach")
st.sidebar.subheader("AI-Powered Education Toolkit")

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

    st.markdown('<a href="?page=Lesson Planner" class="cta-button animated">Get Started</a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    
elif choice == "📖 Lesson Planner":
    # Custom CSS for improved UI
    st.markdown("""
        <style>

            
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

    st.markdown('<h1 class="welcome-title animated">🎓 Lesson Planning Area</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle animated">AI-powered tools to perform lesson planning.</p>', unsafe_allow_html=True)

    lesson_planner()

elif choice == "❓ Question Generator":
    # Custom CSS for improved UI
    st.markdown("""
        <style>
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

    st.markdown('<h1 class="welcome-title animated">🎓 Question Generation Area</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle animated">AI-powered tools to perform Question Generation.</p>', unsafe_allow_html=True)

    question_generator()

elif choice == "📽️ Presentation Generator":
    # Custom CSS for improved UI
    st.markdown("""
        <style>

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

    st.markdown('<h1 class="welcome-title animated">🎓 Presentation Area</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle animated">AI-powered tools to perform presentation Generation.</p>', unsafe_allow_html=True)

    presentation_generator()

elif choice == "✅ Rubrics Generator":
    # Custom CSS for improved UI
    st.markdown("""
        <style>

            
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

    st.markdown('<h1 class="welcome-title animated">🎓 Rubic Generator Area</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle animated">AI-powered tools to perform Rubic Generation.</p>', unsafe_allow_html=True)

    rubrics_generator()

elif choice == "📄 Question Paper Generator":
    # Custom CSS for improved UI
    st.markdown("""
        <style>
            
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

    st.markdown('<h1 class="welcome-title animated">🎓 Question Paper Generator</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle animated">AI-powered tools to perform Question Paper Generation.</p>', unsafe_allow_html=True)

    question_paper_generator()
