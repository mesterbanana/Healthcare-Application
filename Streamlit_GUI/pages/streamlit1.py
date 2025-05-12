import streamlit as st
import base64
import time
import os

PAGE_NAME = "home1"

if "last_page" not in st.session_state:
    st.session_state.last_page = None

if "last_page" in st.session_state and st.session_state.last_page != PAGE_NAME:
    for key in list(st.session_state.keys()):
        if key != "last_page":
            del st.session_state[key]  
            
st.session_state.last_page = PAGE_NAME

st.set_page_config(
    page_title="Mental Disorder Prediction System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={'Get Help': None, 'Report a bug': None, 'About': None}
)

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Force-hide the sidebar */
    section[data-testid="stSidebar"] {
        display: none !important;
        width: 0px !important;
        height: 0px !important;
        margin: 0px !important;
        padding: 0px !important;
        opacity: 0 !important;
        visibility: hidden !important;
    }
    
    /* Force black text globally */
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
    </style>
""", unsafe_allow_html=True)

st.page_link("app.py", label="Home", icon="🏠")

def start_button_action():
    st.switch_page("pages/questions1.py")

def add_bg_from_local(image_file):
    try:
        if os.path.exists(image_file):
            with open(image_file, "rb") as image:
                encoded = base64.b64encode(image.read()).decode()
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.9)), url("data:image/png;base64,{encoded}");
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-position: center;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <style>
                .stApp {
                    background-color: #f5f5f5;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
    except Exception as e:
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #f5f5f5;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

try:
    add_bg_from_local("Streamlit_GUI/GUI Page Images/anxiety-2902575_1920.jpg")
except:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f5f5f5;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <style>
    body, p, div, span, li, h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
    }
    
    .main-heading {
        color: #000000 !important; 
        font-family: Arial, sans-serif;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.15);
    }
    
    .welcome-message {
        color: #000000 !important;
        font-family: Arial, sans-serif;
        font-size: 1.3rem;
        text-align: center;
        margin-bottom: 2rem;
        background-color: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
        line-height: 1.6;
    }
    
    .instructions-heading {
        color: #000000 !important;
        font-family: Arial, sans-serif;
        font-size: 1.7rem;
        font-weight: bold;
        margin-bottom: 1.2rem;
    }
    
    .instructions-container {
        color: #000000 !important;
        font-family: Arial, sans-serif;
        background-color: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 2.5rem;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
    }
    
    .instruction-item {
        margin-bottom: 15px;
        font-size: 1.2rem;
        line-height: 1.5;
        color: #000000 !important;
    }
    
    .stButton>button {
        background-color: #2E8B57;
        color: white !important;
        font-size: 26px;
        font-weight: bold;
        padding: 0.9em 1.8em;
        border-radius: 12px;
        transition: all 0.4s ease;
        border: none;
        margin-top: 1.5rem;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
    }

    .stButton>button:hover {
        transform: scale(1.05);
        background-color: #3CB371;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.25);
        cursor: pointer;
    }
    
    .stButton>button:active {
        transform: scale(0.98);
    }
    
    .note-text {
        color: #000000 !important;
        font-style: italic;
        text-align: center;
        margin-top: 1.2rem;
        font-weight: 500;
        background-color: rgba(255, 240, 230, 0.7);
        padding: 10px;
        border-radius: 8px;
        border-left: 4px solid #FF8C00;
    }
    
    .divider {
        border: none; 
        border-top: 5px solid #000000; 
        margin-top: 10px; 
        margin-bottom: 2.5rem;
    }
    
    .important-note {
        background-color: rgba(255, 255, 220, 0.9);
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #FFD700;
        margin: 20px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        color: #000000 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-heading'>Mental Disorder Prediction System</h1>", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

st.markdown(
    "<div class='welcome-message'>"
    "Welcome to the <strong>Mental Disorder Predictor</strong>, designed to help Doctors assess and predict potential disorders conditions for all of your patients! "
    "This tool uses advanced machine learning to provide accurate predictions based on clinical observations."
    "</div>",
    unsafe_allow_html=True
)

st.markdown("<h2 class='instructions-heading'>Instructions:</h2>", unsafe_allow_html=True)

st.markdown(
    "<div class='instructions-container'>"
    "<p class='instruction-item'><strong>1.</strong> To execute the program, click the Start button below.</p>"
    "<p class='instruction-item'><strong>2.</strong> Respond to the questions based on the answers provided by the patient and your clinical observations.</p>"
    "<p class='instruction-item'><strong>3.</strong> Once all questions have been answered, click the Submit button to complete the process.</p>"
    "<p class='instruction-item'><strong>4.</strong> Review the prediction results and recommended actions for better patient care.</p>"
    "<div class='note-text'>Note: This app may use your previous answers for making enhancements to our service</div>"
    "</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='important-note'>"
    "⚠️ <strong>Important:</strong> This tool is designed to assist medical professionals and should not replace proper medical diagnosis. "
    "Always use your clinical judgment when interpreting results."
    "</div>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Start Assessment", use_container_width=True):
        with st.spinner("Loading assessment form..."):
            time.sleep(0.5)
            start_button_action()
