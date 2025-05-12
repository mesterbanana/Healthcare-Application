import streamlit as st
import base64
import time
import os
from transformers import pipeline  # For text analysis model

PAGE_NAME = "questions1"

# Session state management
if "last_page" not in st.session_state:
    st.session_state.last_page = None

if "last_page" in st.session_state and st.session_state.last_page != PAGE_NAME:
    for key in list(st.session_state.keys()):
        if key != "last_page":
            del st.session_state[key]  
            
st.session_state.last_page = PAGE_NAME

# Page configuration
st.set_page_config(
    page_title="Mental Disorder Prediction System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={'Get Help': None, 'Report a bug': None, 'About': None}
)

# Custom CSS styles
st.markdown("""
    <style>
    /* Hide default Streamlit elements */
    #MainMenu, header, footer {visibility: hidden;}
    
    section[data-testid="stSidebar"] {
        display: none !important;
        width: 0px !important;
        height: 0px !important;
        margin: 0px !important;
        padding: 0px !important;
        opacity: 0 !important;
        visibility: hidden !important;
    }
    
    /* Text and input styling */
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
    
    /* Text input specific styling */
    .stTextInput>div>div>input {
        color: #333333 !important;
        background-color: #ffffff !important;
        border: 1px solid #cccccc !important;
        padding: 10px !important;
        border-radius: 5px !important;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #2E8B57 !important;
        box-shadow: 0 0 0 2px rgba(46, 139, 87, 0.2) !important;
    }
    
    .css-1adrfps p {
        color: #000000 !important;
        opacity: 1 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Home link
st.page_link("app.py", label="Home", icon="🏠")

# Helper functions
def loader():
    with st.spinner('Analyzing your response...'):
        time.sleep(1)

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

# Load background image
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

# Main title
st.markdown("<h1 style='color: #000000; font-family: Arial; text-align: center;'>Mental Health Assessment</h1>", unsafe_allow_html=True)

# Additional styling
st.markdown(
    """
    <style>
    .question-container {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 25px;
        margin: 20px auto;
        max-width: 800px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .shaker-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 15px;
        margin: 15px auto;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button {
        background-color: #2E8B57;
        color: white !important;
        font-size: 18px;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 8px;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0px 3px 6px rgba(0,0,0,0.15);
        width: 100%;
        margin-top: 20px;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 5px 12px rgba(0,0,0,0.2);
        background-color: #3CB371;
    }
    
    .stButton>button:active {
        transform: translateY(0);
    }
    
    .error-message {
        color: #ff4b4b;
        font-weight: bold;
        font-size: 16px;
        padding: 12px;
        background-color: rgba(255, 75, 75, 0.1);
        border-radius: 8px;
        margin: 15px 0;
        border-left: 4px solid #ff4b4b;
    }
    
    .helper-text {
        font-size: 14px;
        color: #555555;
        font-style: italic;
        margin-top: 8px;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    
    .stProgress > div > div {
        background-color: #4CAF50 !important;
        height: 8px !important;
        border-radius: 4px !important;
    }
    
    .privacy-note {
        font-size: 12px;
        color: #666666;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the mental health analysis model
@st.cache_resource
def load_model():
    try:
        # Using a pre-trained model from Hugging Face
        return pipeline("text-classification", model="mental-health-classifier")
    except Exception as e:
        st.error(f"Could not load the analysis model: {str(e)}")
        return None

model = load_model()

# Question setup
questions = [
    {
        "key": "mental_state",
        "text": "Please describe your current feelings and what you're experiencing in your life",
        "type": "text",
        "placeholder": "I've been feeling...",
        "help": "Be as detailed as you're comfortable with. This helps us better understand your mental state. Your response is confidential.",
        "min_length": 30,
        "max_length": 1000
    }
]

# Initialize session state
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "responses" not in st.session_state:
    st.session_state.responses = {}

# Form submission functions
def validate_response(response, question):
    if len(response.strip()) < question.get("min_length", 30):
        return f"Please provide more details (at least {question['min_length']} characters)"
    if len(response.strip()) > question.get("max_length", 1000):
        return f"Please keep your response under {question['max_length']} characters"
    return None

def submit_form():
    current_q = questions[st.session_state.question_index]
    key = current_q["key"]
    val = st.session_state.get(key, "").strip()
    
    # Validate response
    error = validate_response(val, current_q)
    if error:
        st.session_state['form_valid'] = False
        st.session_state['error_message'] = error
        return
    
    # Store response
    st.session_state.responses[key] = val
    
    # Analyze the response if model is available
    if model:
        try:
            with st.spinner("Analyzing your response..."):
                analysis = model(val)
                st.session_state['analysis_result'] = analysis
        except Exception as e:
            st.error(f"Analysis failed: {str(e)}")
            st.session_state['analysis_result'] = None
    
    st.session_state['ready_to_switch'] = True

# Display current question
idx = st.session_state.question_index
q = questions[idx]

# Progress bar (shows full since there's only one question)
st.progress(1.0)

# Question container
with st.container():
    st.markdown(
        f"""
        <div class="question-container">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h2 style="font-family: Arial; color: black; margin-bottom: 0;">Mental Health Assessment</h2>
                <h3 style="font-family: Arial; color: black; margin: 0;">Question {idx + 1} of {len(questions)}</h3>
            </div>
            <h4 style='color: black; margin-top: 20px; font-family: Arial;'>{q['text']}</h4>
        """,
        unsafe_allow_html=True
    )

    # Initialize response in session state if not exists
    if q["key"] not in st.session_state:
        st.session_state[q["key"]] = ""

    # Display appropriate input based on question type
    if q["type"] == "text":
        response = st.text_area(
            label=" ",
            value=st.session_state[q["key"]],
            placeholder=q.get("placeholder", ""),
            key=q["key"],
            height=200
        )
    else:
        st.error("Unsupported question type")

    # Help text
    st.markdown(f"<div class='helper-text'>{q.get('help', '')}</div>", unsafe_allow_html=True)
    
    # Privacy note
    st.markdown(
        """<div class="privacy-note">
        Your responses are confidential and will only be used for this assessment.
        </div>""",
        unsafe_allow_html=True
    )

    # Store response
    if response is not None:
        st.session_state.responses[q["key"]] = response

# Error handling
if 'form_valid' in st.session_state and not st.session_state['form_valid']:
    st.markdown(
        f'<div class="shaker-container"><p class="error-message">{st.session_state["error_message"]}</p></div>',
        unsafe_allow_html=True
    )
    st.session_state['form_valid'] = True  # Reset for next attempt

# Submit button
st.button(
    "Submit Assessment",
    on_click=submit_form,
    type="primary",
    use_container_width=True
)

# Close question container
st.markdown('</div>', unsafe_allow_html=True)

# Page navigation
if 'ready_to_switch' in st.session_state and st.session_state['ready_to_switch']:
    st.session_state['ready_to_switch'] = False
    st.switch_page("pages/results1.py")
