import streamlit as st
import base64
from pathlib import Path

PAGE_NAME = "app"
if "last_page" not in st.session_state:
    st.session_state.last_page = None
if "last_page" in st.session_state and st.session_state.last_page != PAGE_NAME:
    for key in list(st.session_state.keys()):
        if key != "last_page":
            del st.session_state[key]  
st.session_state.last_page = PAGE_NAME

st.set_page_config(
    page_title="Health Diagnosis System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={'Get Help': None, 'Report a bug': None, 'About': None}
)


def set_bg_image(image_path: str):
    if Path(image_path).is_file():
        raw = Path(image_path).read_bytes()
        ext = Path(image_path).suffix.lstrip(".")
        img_data = base64.b64encode(raw).decode()
        img_url = f"data:image/{ext};base64,{img_data}"
    else:
        img_url = image_path 

    css = f"""
    <style>
      [data-testid="stAppViewContainer"] {{
        background: url("{img_url}") no-repeat center center fixed;
        background-size: cover;
      }}
      [data-testid="stAppViewContainer"] .css-1outpf7,
      .css-1d391kg {{
        background: transparent;
      }}
      [data-testid="stSidebar"] {{
        background: none;
      }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_bg_image("Streamlit_GUI/GUI Page Images/computer-1149148_1920.jpg")

st.page_link("app.py", label="Home", icon="🏠")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    section[data-testid="stSidebar"] {
        display: none !important;
        width: 0px !important;
        height: 0px !important;
        margin: 0px !important;
        padding: 0px !important;
        overflow: hidden !important;
        opacity: 0 !important;
        visibility: hidden !important;
    }
    
    body, p, div, span, li, h1, h2, h3, h4, h5, h6,
    .stMarkdown, .stText,
    .stButton, .stSelectbox, .stMultiselect,
    .stRadio, .stCheckbox, .stNumberInput, .stTextInput,
    .stTextArea, .stDateInput, .stTimeInput,
    .stSlider, .stProgress, .stMetric, .stDataFrame,
    .css-1d391kg, .css-hxt7ib, .css-1qxpwi4, 
    .st-ae, .st-af, .st-ag, .st-ah, .st-ai, .st-aj {
        color: #000000 !important;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        color: #000000 !important;
    }
    
    .divider {
        border: none; 
        border-top: 3px solid #2E8B57; 
        margin-top: 10px; 
        margin-bottom: 2rem;
    }
    
    .main-heading {
        font-size: 3.2rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
        padding-top: 1.5rem;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.15);
        color: #000000;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    
    .welcome-message {
        color: #000000 !important;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 1.4rem;
        text-align: center;
        margin-bottom: 2.5rem;
        background-color: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15);
        line-height: 1.6;
        border-left: 5px solid #2E8B57;
    }
    
    .card-container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        gap: 2.5rem;
        margin: 2.5rem auto;
        max-width: 1200px;
        flex-wrap: wrap;
    }
    
    .card {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 2.2rem;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12), 0 4px 8px rgba(0, 0, 0, 0.06);
        text-align: center;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        width: 100%;
        max-width: 500px;
        min-width: 300px;
        border-top: 5px solid #2E8B57;
    }
    
    .card:hover {
        transform: translateY(-12px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
    }
    
    .card-icon {
        font-size: 4.5rem;
        margin-bottom: 1.2rem;
        color: #2E8B57;
    }
    
    .card-title {
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 1.2rem;
        color: #2E8B57;
    }
    
    .card-description {
        font-size: 1.25rem;
        color: #000000;
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }
    
    .stButton>button {
        background-color: #2E8B57;
        color: white !important;
        font-size: 26px;
        font-weight: bold;
        padding: 1em 1.8em;
        border-radius: 12px;
        transition: all 0.4s ease;
        border: none;
        box-shadow: 0px 6px 12px rgba(0,0,0,0.15);
        margin-bottom: 15px;
    }

    .stButton>button:hover {
        transform: scale(1.005);
        background-color: #3CB371;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.25);
        cursor: pointer;
    }
    
    .stButton>button:active {
        transform: scale(0.98);
    }
    
    .important-note {
        background-color: rgba(255, 245, 220, 0.95);
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #FFD700;
        margin: 30px auto;
        max-width: 2600px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        color: #000000 !important;
        font-size: 1.15rem;
        line-height: 1.6;
    }
    
    .custom-footer {
        text-align: center;
        margin-top: 4rem;
        padding: 1.8rem;
        color: #000000;
        font-size: 1.1rem;
        border-top: 2px solid #2E8B57;
        max-width: 3000px;
        margin-left: auto;
        margin-right: auto;
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 0 0 15px 15px;
    }
    
    [data-testid="baseButton-secondary"] {
        visibility: hidden;
        height: 0px;
        margin-top: -50px;
    }
    
    .feature-badge {
        display: inline-block;
        background-color: #e0f5e0;
        color: #2E8B57 !important;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.9rem;
        margin: 3px;
        font-weight: 500;
    }
    
    .stats-container {
        display: flex;
        justify-content: center;
        gap: 25px;
        margin: 20px auto 40px auto;
        flex-wrap: wrap;
        max-width: 900px;
    }
    
    .stat-box {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 15px 25px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        min-width: 150px;
    }
    
    .stat-number {
        font-size: 2.2rem;
        font-weight: bold;
        color: #2E8B57 !important;
        margin-bottom: 5px;
    }
    
    .stat-label {
        font-size: 1rem;
        color: #555 !important;
    }
    
    .explanation-box {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 25px;
        margin: 20px auto;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        max-width: 2600px;
    }
    
    .explanation-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2E8B57;
        margin-bottom: 15px;
        border-bottom: 2px solid #e0f5e0;
        padding-bottom: 10px;
    }
    
    .explanation-content {
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    .step-container {
        display: flex;
        flex-direction: column;
        gap: 15px;
        margin: 20px 0;
    }
    
    .step-item {
        display: flex;
        gap: 15px;
        align-items: flex-start;
    }
    
    .step-number {
        background-color: #2E8B57;
        color: white !important;
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        font-weight: bold;
        flex-shrink: 0;
    }
    
    .step-content {
        flex-grow: 1;
    }
    
    @media (max-width: 768px) {
        .card-container {
            flex-direction: column;
            align-items: center;
        }
        
        .card {
            width: 90%;
        }
        
        .main-heading {
            font-size: 2.2rem;
        }
        
        .stats-container {
            flex-direction: column;
            align-items: center;
        }
        
        .stat-box {
            width: 80%;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-heading'>Health Diagnosis System</h1>", unsafe_allow_html=True)
st.markdown("<hr class='divider'>", unsafe_allow_html=True)

st.markdown("""
<div class="welcome-message">
    Welcome to the Health Diagnosis System! Select an option below to get started.
</div>
""", unsafe_allow_html=True)

with st.spinner("Loading..."):
    if st.button("Start Dermatology Diagnosis", use_container_width=True):
        st.session_state["last_page"] = "streamlit.py"
        st.switch_page("streamlit.py")
    elif st.button("Start Cardiology Diagnosis", use_container_width=True):
        st.session_state["last_page"] = "streamlit1.py"
        st.switch_page("streamlit1.py")

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# Add footer section
st.markdown("""
<div class="custom-footer">
    &copy; 2025 Health Diagnosis System | All Rights Reserved.
</div>
""", unsafe_allow_html=True)
