import streamlit as st
from PIL import Image
import sys
import os

# Page Config
st.set_page_config(
    page_title="Athena AI App",
    page_icon="👩‍💼",
    layout="wide"
)

# Custom CSS with better organization
def load_css():
    st.markdown(
        """
        <style>
        /* Main background and text colors */
        .stApp {
            background: linear-gradient(135deg, #81334C, #81334C);
            color: #ffffff;
        }

        /* Headings */
        h1, h2, h3 {
            color: #ffffff !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        /* Paragraphs */
        p {
            font-size: 1.1em;
            line-height: 1.6;
        }

        /* Links */
        a {
            color: #FFB6C1 !important;
            text-decoration: none;
            transition: all 0.3s ease;
        }

        a:hover {
            color: #FFC0CB !important;
            text-decoration: underline;
        }

        /* Buttons */
        .stButton > button {
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
            font-size: 1em;
            padding: 10px 20px;
        }

        .stButton > button:hover {
            background-color: rgba(255, 255, 255, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        /* Spacing */
        .block-container {
            padding-top: 3rem !important;
            padding-bottom: 3rem !important;
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: rgba(129, 51, 76, 0.1);
        }

        /* Custom class for centered text */
        .centered-text {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def init_session_state():
    if "todo_list" not in st.session_state:
        st.session_state["todo_list"] = []

def display_header():
    st.markdown("<h1 class='centered-text'>Athena AI App</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='centered-text'>Women's AI Ally for Leadership Success</h3>", unsafe_allow_html=True)
    
    # Display banner image
    default_image_url = "https://images.pexels.com/photos/6400345/pexels-photo-6400345.jpeg"
    st.image(default_image_url, use_container_width=True)

def display_about():
    st.markdown("## About Athena AI App")
    st.write("""
    Empowered by the wisdom of Athena, Athena AI App is your go-to app for women entrepreneurs. 
    With our innovative tools and supportive community, you can unlock your creativity, boost your business, 
    and achieve your goals.
    """)

def display_features():
    st.markdown("## Key Features")
    
    features = {
        "Athena AI Genie": "Get instant answers and guidance on entrepreneurship and personal growth.",
        "Business Genie": "Track your progress in your business, do smart analysis, and suggest improvements.",
        "Summarize Genie": "Paste or upload your text, get a summary, and listen to the summarized content.",
        "InstaPost Genie": "Turn your photos into captivating Instagram posts effortlessly.",
        "Resource Genie": """
        Access various resources:
        - **Business Plan Templates**: Comprehensive templates for business growth
        - **Support Groups**: Connect with fellow women entrepreneurs
        - **Organizations**: Discover supporting organizations
        """
    }
    
    for i, (title, description) in enumerate(features.items(), 1):
        st.markdown(f"### {i}. {title}")
        st.write(description)

def display_todo_list():
    for index, item in enumerate(st.session_state.todo_list):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"{item['task']}")
        with col2:
            if st.button("Mark as Done", key=f"done_{index}"):
                item["done"] = True

def display_partners():
    st.markdown("## Partners")
    partners = {
        "Google": "https://www.google.com",
        "She Builds AI Hackathon": "https://womentechmakers.devpost.com/",
        "Streamlit App": "https://www.streamlit.io"
    }
    
    for partner, link in partners.items():
        st.markdown(f"* [{partner}]({link})")

def main():
    # Initialize session state
    init_session_state()
    
    # Load CSS
    load_css()
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["Home", "Athena Genie", "Business Genie", "Summarize Genie", "InstaPost Genie", "Resources Genie"]
    )
    
    if page == "Home":
        display_header()
        display_about()
        display_features()
        display_todo_list()
        display_partners()

if __name__ == "__main__":
    main()
