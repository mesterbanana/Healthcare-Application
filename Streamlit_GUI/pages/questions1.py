import streamlit as st
import base64
import time
import os

PAGE_NAME = "questions1"

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
    
    section[data-testid="stSidebar"] {
        display: none !important;
        width: 0px !important;
        height: 0px !important;
        margin: 0px !important;
        padding: 0px !important;
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
    
    .stTextInput label, .stTextInput div, .stTextInput p {
        color: #000000 !important;
    }
    
    input[type="text"] {
        color: #FFFFFF !important;
        background-color: #333333 !important;
    }
    
    .css-1adrfps p {
        color: #000000 !important;
        opacity: 1 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.page_link("app.py", label="Home", icon="🏠")

def loader():
    with st.spinner('Loading...'):
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

st.markdown("<h1 style='color: #000000; font-family: Arial; text-align: center;'>Mental Disorders Prediction System</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .question-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 25px;
        margin: 0px auto;
        max-width: 2600px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .shaker-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 10px;
        margin: 10px auto;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button {
        background-color: #2E8B57;
        color: white !important;
        font-size: 18px;
        font-weight: bold;
        padding: 0.5em 1.2em;
        border-radius: 8px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: none;
        box-shadow: 0px 3px 6px rgba(0,0,0,0.15);
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 5px 12px rgba(0,0,0,0.2);
        cursor: pointer;
    }
    
    .stButton>button:active {
        transform: scale(0.98);
    }
    
    .stTextInput div, .stTextInput label, .stTextInput p {
        color: #000000 !important;
        font-size: 16px !important;
    }
    
    .error-message {
        color: #ff4b4b;
        font-weight: bold;
        font-size: 16px;
        padding: 10px;
        background-color: rgba(255, 75, 75, 0.1);
        border-radius: 5px;
        margin: 10px 0;
        border-left: 4px solid #ff4b4b;
    }
    
    .helper-text {
        font-size: 14px;
        color: #555555;
        font-style: italic;
        margin-top: 5px;
        margin-bottom: 15px;
    }
    
    .stProgress > div > div {
        background-color: #4CAF50 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

questions = [
  {
    "key": "mental_state",
    "text": "Express your current feelings and what you are going through in your life (Please be honest and open)",
    "type": "text",
    "placeholder": "Enter your thoughts here...",
    "help": "This is a free text field. Please provide a detailed description of your current mental state."
  }
]

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "responses" not in st.session_state:
    st.session_state.responses = {}

def prev_question():
    if st.session_state.question_index > 0:
        st.session_state.question_index -= 1

def next_question():
    pass

def submit_form():
    st.session_state['form_valid'] = True
    
    current_q = questions[st.session_state.question_index]
    key = current_q["key"]
    val = st.session_state[key]
    
    if val == "":
        st.session_state['form_valid'] = False
        st.session_state['error_message'] = "Please provide an answer before submitting."
        return
    else:
        st.session_state.responses[key] = val
    
    st.session_state['ans'] = [st.session_state.responses[key]]
    
    st.session_state['ready_to_switch'] = True

idx = st.session_state.question_index
q = questions[idx]

st.progress(1.0)

st.markdown('<div class="question-container">' \
    '<div style="display: flex; justify-content: space-between;">'
        '<h2 style="font-family: Arial; color: black;">Mental Disorders Assessment</h2>'
        '<h3 style="font-family: Arial; margin-top: 5px; margin-bottom: 0px; color: black;">Question 1 of 1</h3>'
    '</div>', unsafe_allow_html=True)

st.markdown(f"<h4 style='color: black; margin-left: 10px; margin-top: 20px; font-family: Arial;'>{q['text']}</h4>", unsafe_allow_html=True)

if q["key"] not in st.session_state:
    st.session_state[q["key"]] = ""

response = st.text_input(
    label="",
    value=st.session_state[q["key"]],
    placeholder=q.get("placeholder", ""),
    key=q["key"]
)

st.markdown(f"<div class='helper-text'>{q.get('help', '')}</div>", unsafe_allow_html=True)

if response is not None:
    st.session_state.responses[q["key"]] = response

if 'ready_to_switch' not in st.session_state:
    st.session_state['ready_to_switch'] = False

if 'form_valid' not in st.session_state:
    st.session_state['form_valid'] = True
    
if 'error_message' not in st.session_state:
    st.session_state['error_message'] = ""

if not st.session_state['form_valid']:
    st.markdown(f'<div class="shaker-container"><p class="error-message">{st.session_state["error_message"]}</p></div>', unsafe_allow_html=True)
    st.session_state['form_valid'] = True

if st.session_state['ready_to_switch']:
    st.session_state['ready_to_switch'] = False
    st.switch_page("Streamlit_GUI/pages/results1.py")

st.markdown('<div class="button-container" style="margin-top: 30px;">', unsafe_allow_html=True)

st.button("Submit", on_click=submit_form, use_container_width=True)

st.markdown('</div></div>', unsafe_allow_html=True)
