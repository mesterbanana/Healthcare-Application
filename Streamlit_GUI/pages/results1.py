import streamlit as st
import base64
import joblib
import numpy as np
import requests
import os

PAGE_NAME = "results1"

if "last_page" not in st.session_state:
    st.session_state.last_page = None

if "last_page" in st.session_state and st.session_state.last_page != PAGE_NAME:
    for key in list(st.session_state.keys()):
        if key != "last_page" and key != "ans":
            del st.session_state[key]  
            
st.session_state.last_page = PAGE_NAME

if "ans" not in st.session_state:
    st.switch_page("pages/streamlit1.py")

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
    </style>
""", unsafe_allow_html=True)

st.page_link("app.py", label="Home", icon="🏠")



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
        margin-bottom: 1rem;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.15);
    }
    
    .result-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 12px;
        margin: 20px auto;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
    }
    
    .guidance-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 12px;
        margin-top: 20px;
        box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
    }
    
    .diagnosis-heading {
        font-family: Arial, sans-serif;
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 15px;
        color: #2E8B57 !important;
    }
    
    .guidance-heading {
        font-family: Arial, sans-serif;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 15px;
        color: #000000 !important;
    }
    
    .recommendation-section {
        background-color: rgba(240, 255, 240, 0.8);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        border-left: 5px solid #2E8B57;
    }
    
    .links-section {
        margin-top: 20px;
        padding: 15px;
        background-color: rgba(240, 248, 255, 0.8);
        border-radius: 10px;
        border-left: 5px solid #4682B4;
    }
    
    .links-section a {
        display: block;
        margin: 5px 0;
        color: #0066cc !important;
        text-decoration: none;
    }
    
    .links-section a:hover {
        text-decoration: underline;
    }
    
    .stButton>button {
        background-color: #2E8B57;
        color: white !important;
        font-size: 18px;
        font-weight: bold;
        padding: 0.5em 1.2em;
        border-radius: 8px;
        transition: all 0.4s ease;
        border: none;
        margin-top: 20px;
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
    
    .divider {
        border: none; 
        border-top: 5px solid #000000; 
        margin-top: 10px; 
        margin-bottom: 20px;
    }
    
    .error-message {
        background-color: rgba(255, 220, 220, 0.9);
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #FF6347;
        margin: 20px 0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        color: #000000 !important;
    }
    
    .loading-spinner {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
    }
    
    .api-content p {
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    .api-content ul {
        margin-left: 20px;
        margin-bottom: 15px;
    }
    
    .api-content a {
        color: #0066cc !important;
        text-decoration: none;
    }
    
    .api-content a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-heading'>Mental Disorders Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<hr class='divider'>", unsafe_allow_html=True)

try:
    results = st.session_state['ans']
    
    try:
        model = joblib.load('Streamlit_GUI/Mental_Model/model.pkl')
        le = joblib.load('Streamlit_GUI/Mental_Model/label_encoder.pkl')
        
        prediction = model.predict(results)
        prediction = le.inverse_transform(prediction)
        prediction = prediction[0]
    except Exception as e:
        st.markdown(
            f"""
            <div class="error-message">
                <strong>Error loading model:</strong> {str(e)}
                <p>Please contact the system administrator.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        prediction = "Unable to determine"
    
    st.markdown(
        f"""
        <div class="result-container">
            <h2 class="diagnosis-heading">{prediction}</h2>
            <p>Diagnosis Results</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    api_key = st.secrets.get("openrouter", {}).get("api_key")
    
    if api_key:
        user_question = (
            f"Explain well {prediction} in a summarized way. "
            f"Write as a paragraph. After the paragraph, write a separate recommendation on how "
            f"the {prediction} could be cured or improved for the patient. Also, provide official "
            f"only one clean link only one that are related to the {prediction} at the end of response "
            f"& make it accessible. Don't write titles or ask for additional input."
        )
        
        url = "https://openrouter.ai/api/v1/chat/completions"
        model_id = "deepseek/deepseek-chat"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": model_id,
            "messages": [{"role": "user", "content": user_question}],
        }
        
        with st.spinner('Retrieving additional information...'):
            try:
                resp = requests.post(url, headers=headers, json=payload, timeout=30)
                
                if resp.status_code == 200:
                    content = resp.json()["choices"][0]["message"]["content"]
                    
                    parts = content.split("\n\n")
                    description = parts[0] if len(parts) > 0 else ""
                    recommendation = parts[1] if len(parts) > 1 else ""
                    
                    links = []
                    for part in parts[2:]:
                        if "http" in part:
                            links.append(part.strip())
                    
                    st.markdown(
                        f"""
                        <div class="guidance-container">
                            <h3 class="guidance-heading">Condition Information</h3>
                            <div class="api-content">
                                <p>{description}</p>
                            </div>
                            
                        <div class="recommendation-section">
                            <h4 style="color: #2E8B57 !important;">Treatment Recommendations</h4>
                            <div class="api-content">
                                <p>{recommendation}</p>
                            </div>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                    
                    if links:
                        link_html = ""
                        for link in links:
                            link_html += f'<a href="{link}" target="_blank">{link}</a>\n'
                            
                        st.markdown(
                            f"""
                            <div class="links-section">
                                <h4 style="color: #4682B4 !important;">Additional Resources</h4>
                                    <p>{link_html}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.markdown(
                        """
                        <div class="error-message">
                            <strong>Unable to retrieve additional information.</strong>
                            <p>The service is currently unavailable. Please try again later.</p>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
            except Exception as e:
                st.markdown(
                    f"""
                    <div class="error-message">
                        <strong>Error retrieving information:</strong> {str(e)}
                        <p>Please try again later.</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
    else:
        st.markdown(
            """
            <div class="error-message">
                <strong>API key not configured.</strong>
                <p>Additional information is not available at this time.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("Return to Home", use_container_width=True):
            for key in list(st.session_state.keys()):
                if key != "last_page":
                    del st.session_state[key]
            st.switch_page("pages/streamlit1.py")

except Exception as e:
    st.markdown(
        f"""
        <div class="error-message">
            <strong>An error occurred:</strong> {str(e)}
            <p>Please return to the home page and try again.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Return to Home", use_container_width=True):
            st.switch_page("pages/streamlit1.py")
