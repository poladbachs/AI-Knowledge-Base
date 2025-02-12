import streamlit as st
import requests
import base64
from PIL import Image

st.set_page_config(page_title="Spitch AI Knowledge Base", page_icon="🔍", layout="wide")

def render_svg(svg_path, width="180px", link="https://spitch.ai/"):
    """Embeds an SVG logo as a clickable hyperlink, centered in Streamlit, with margin-bottom."""
    with open(svg_path, "r") as f:
        svg_data = f.read()
    b64 = base64.b64encode(svg_data.encode("utf-8")).decode("utf-8")
    img_tag = f'''
        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <a href="{link}" target="_blank">
                <img src="data:image/svg+xml;base64,{b64}" width="{width}"/>
            </a>
        </div>
    '''
    return img_tag

st.markdown("""
    <style>
        /* Center Title */
        .title-text {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            margin-bottom: 5px;
        }

        /* Subheader */
        .subheader-text {
            text-align: center;
            font-size: 20px;
            opacity: 0.9;
            margin-bottom: 30px;
        }

        /* Search Bar Styling */
        .search-input input {
            font-size: 18px !important;
            padding: 15px !important;
            border-radius: 10px !important;
            border: 1px solid #ffffff !important;
            background-color: #222 !important;
            color: white !important;
            width: 100%;
        }

        /* Sidebar Styling */
        .sidebar-text {
            font-size: 18px;
            font-weight: 600;
            margin-top: 15px;
        }

        .sidebar-info {
            font-size: 15px;
            opacity: 0.8;
            margin-bottom: 20px;
        }

        /* Search Button */
        .search-button {
            font-size: 18px !important;
            padding: 12px !important;
            width: 100%;
            border-radius: 8px;
            background: linear-gradient(90deg, #ff8c00, #ff5500);
            color: white !important;
            font-weight: bold;
            transition: 0.3s;
        }

        .search-button:hover {
            background: linear-gradient(90deg, #ff5500, #ff2200);
        }

        /* Sidebar Links */
        .sidebar-link a {
            text-decoration: none;
            font-weight: bold;
            color: #FFD700;
            font-size: 16px;
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 16px;
            opacity: 0.7;
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(render_svg("spitch_white_new.svg", width="160px"), unsafe_allow_html=True)
    st.markdown("🚀 **AI-powered speech & voice solutions.**")
    st.markdown("""
    <p class='sidebar-text'>💡 Hints:</p>
    <ul>
        <li class='sidebar-info'>🔹 Ask about Spitch AI's features.</li>
        <li class='sidebar-info'>🔹 Learn about security & compliance.</li>
        <li class='sidebar-info'>🔹 Discover industry applications.</li>
    </ul>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>🔍 <a href='https://spitch.ai/' target='_blank' style='text-decoration: none; color: inherit;'>Spitch AI Knowledge Base</a></h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subheader-text'>💡 Ask any question about Spitch AI and get real AI-powered answers.</h3>", unsafe_allow_html=True)

query_text = st.text_input("Enter your question:", placeholder="E.g., What does Spitch AI offer?", key="query_input", label_visibility="collapsed")
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Search", key="search_button", help="Click to search", use_container_width=True):
    if query_text.strip():
        with st.spinner("Thinking... 🤔"):
            response = requests.post("http://127.0.0.1:8000/query", json={"query": query_text})
        
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer found.")
                st.success(f"**💡 Answer:** {answer}")
            else:
                st.error("❌ Error querying knowledge base!")
    else:
        st.warning("⚠️ Please enter a valid question!")

st.markdown("---")
st.markdown("<div class='footer'>💡 Developed for <strong>Spitch AI</strong></div>", unsafe_allow_html=True)