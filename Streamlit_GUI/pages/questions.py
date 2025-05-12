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
    page_title="Dermatology Prediction System",
    page_icon="🧑🏼‍⚕️",
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
    
    .stRadio label, .stRadio div, .stRadio p {
        color: #000000 !important;
    }
    
    .stNumberInput label, .stNumberInput p {
        color: #000000 !important;
    }
    
    input[type="number"] {
        color: #FFFFFF !important;
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
    add_bg_from_local("Streamlit_GUI/GUI Page Images/7816782.jpg")
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

st.markdown("<h1 style='color: #000000; font-family: Arial; text-align: center;'>Dermatology Prediction System</h1>", unsafe_allow_html=True)

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
    
    label, .stRadio div, .stRadio label, .stRadio p {
        color: #000000 !important;
        font-size: 16px !important;
    }
    
    div[role="radiogroup"] > label {
        font-size: 16px;
        color: #000000 !important;
        padding: 10px;
    }
    
    div[role="radiogroup"] {
        margin-left: 10px;
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
    
    .stProgress > div > div {
        background-color: #4CAF50 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

questions = [
  {
    "key": "knee_and_elbow_involvement",
    "text": "How would you rate the degree of knee and elbow (extensor surface) involvement?",
    "type": "radio",
    "options": ["Please select", "None", "Low", "Medium", "High"],
    "help": "Rate the severity of skin symptoms on knees and elbows"
  },
  {
    "key": "exocytosis",
    "text": "What is the level of epidermal exocytosis observed?",
    "type": "radio",
    "options": ["Please select", "None", "Low", "Medium", "High"],
    "help": "Exocytosis refers to the presence of inflammatory cells in the epidermis"
  },
  {
    "key": "age",
    "text": "How old is the patient?",
    "type": "number",
    "min": 0,
    "max": 120,
    "placeholder": "Enter the patient's age",
    "help": "Enter the patient's current age in years"
  },
  {
    "key": "follicular_papules",
    "text": "What is the density of follicular papules present?",
    "type": "radio",
    "options": ["Please select", "None", "Low", "Medium", "High"],
    "help": "Follicular papules are small raised bumps centered around hair follicles"
  },
  {
    "key": "fibrosis_papillary_dermis",
    "text": "How pronounced is the fibrosis in the papillary dermis?",
    "type": "radio",
    "options": ["Please select", "None", "Low", "Medium", "High"],
    "help": "Fibrosis refers to the thickening or scarring of connective tissue"
  },
  {
    "key": "thinning_suprapapillary_epidermis",
    "text": "What degree of thinning of the suprapapillary epidermis do you observe?",
    "type": "radio",
    "options": ["Please select", "None", "Low", "Medium", "High"],
    "help": "This refers to the thinning of the epidermis above the dermal papillae"
  },
  {
    "key": "focal_hypergranulosis",
    "text": "How extensive is focal hypergranulosis in the biopsy?",
    "type": "radio",
    "options": ["Please select", "None", "Low", "Medium", "High"],
    "help": "Hypergranulosis is the thickening of the granular layer of the epidermis"
  },
  {
    "key": "PNL_infiltrate",
    "text": "What is the intensity of polymorphonuclear leukocyte (PNL) infiltrate?",
    "type": "radio",
    "options": ["Please select", "None", "Low", "Medium", "High"],
    "help": "PNL infiltrate indicates the presence of neutrophils in the affected tissue"
  },
  {
    "key": "clubbing_rete_ridges",
    "text": "To what extent are the rete ridges clubbed or broadened?",
    "type": "radio",
    "options": ["Please select", "None", "Low", "Medium", "High"],
    "help": "Rete ridges are epithelial extensions that project into the underlying connective tissue"
  },
  {
    "key": "spongiosis",
    "text": "How marked is the presence of spongiosis?",
    "type": "radio",
    "options": ["Please select", "None", "Low", "Medium", "High"],
    "help": "Spongiosis is the presence of fluid in between the cells of the epidermis"
  },
  {
    "key": "koebner_phenomenon",
    "text": "How would you grade the Koebner phenomenon in this case?",
    "type": "radio",
    "options": ["Please select", "None", "Low", "Medium", "High"],
    "help": "Koebner phenomenon is the appearance of skin lesions at sites of trauma"
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
    current_q = questions[st.session_state.question_index]
    key = current_q["key"]
    
    if key not in st.session_state:
        if current_q["type"] == "radio":
            st.session_state[key] = "Please select"
        elif current_q["type"] == "number":
            st.session_state[key] = None
    
    val = st.session_state[key]

    st.session_state['form_valid'] = True
    
    if current_q["type"] == "radio" and val == "Please select":
        st.session_state['form_valid'] = False
        st.session_state['error_message'] = "Please select an option before continuing."
    elif current_q["type"] == "number" and (val is None or val < 0 or (current_q.get("max") and val > current_q.get("max"))):
        st.session_state['form_valid'] = False
        st.session_state['error_message'] = f"Please enter a valid number between {current_q.get('min', 0)} and {current_q.get('max', '∞')}."
    else:
        st.session_state.responses[key] = val
        if st.session_state.question_index < len(questions) - 1:
            st.session_state.question_index += 1

def submit_form():
    st.session_state['form_valid'] = True
    
    current_q = questions[st.session_state.question_index]
    key = current_q["key"]
    val = st.session_state[key]
    
    if current_q["type"] == "radio" and val == "Please select":
        st.session_state['form_valid'] = False
        st.session_state['error_message'] = "Please select an option before submitting."
        return
    elif current_q["type"] == "number" and (val is None or val < 0 or (current_q.get("max") and val > current_q.get("max"))):
        st.session_state['form_valid'] = False
        st.session_state['error_message'] = f"Please enter a valid number between {current_q.get('min', 0)} and {current_q.get('max', '∞')}."
        return
    
    st.session_state.responses[key] = val
    
    st.session_state['ans'] = list(st.session_state['responses'].values())
    
    st.session_state['ready_to_switch'] = True

idx = st.session_state.question_index
q = questions[idx]

progress = (idx) / (len(questions) - 1)
st.progress(progress)

st.markdown('<div class="question-container">' \
    '<div style="display: flex; justify-content: space-between;">'
        '<h2 style="font-family: Arial; color: black;">Dermatology Assessment</h2>'
        f"<h3 style='font-family: Arial; margin-top: 5px; margin-bottom: 0px; color: black;'>Question {idx + 1} of {len(questions)}</h3>"
    '</div>', unsafe_allow_html=True)

st.markdown(f"<h4 style='color: black; margin-left: 10px; margin-top: 20px; font-family: Arial;'>{q['text']}</h4>", unsafe_allow_html=True)

if q["type"] == "radio":
    if q["key"] not in st.session_state:
        st.session_state[q["key"]] = q["options"][0]
    
    response = st.radio(
        " ",
        q["options"], 
        index=q["options"].index(st.session_state[q["key"]]), 
        key=q["key"],
        help=q.get("help", ""),
        label_visibility="collapsed"
    )

elif q["type"] == "number":
    if q["key"] not in st.session_state:
        st.session_state[q["key"]] = None
    
    response = st.number_input(
        " ",
        min_value=q.get("min", 0),
        max_value=q.get("max", None),
        value=st.session_state[q["key"]] if st.session_state[q["key"]] is not None else None,
        placeholder=q.get("placeholder", ""),
        key=q["key"],
        help=q.get("help", ""),
        label_visibility="collapsed"
    )

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
    st.switch_page("pages/results.py")

st.markdown('<div class="button-container" style="margin-top: 30px;">', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    if idx > 0:
        st.button("⬅️ Previous", on_click=prev_question, use_container_width=True)

with col2:
    if idx < len(questions) - 1:
        st.button("Next ➡️", on_click=next_question, use_container_width=True)
    else:
        st.button("Submit", on_click=submit_form, use_container_width=True)

st.markdown('</div></div>', unsafe_allow_html=True)
