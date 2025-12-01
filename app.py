# app.py

import streamlit as st
from ui.css import load_global_css
from ui.topnav import render_topnav

from pages.wardrobe import render_wardrobe
from pages.lookbook import render_lookbook
from pages.color_trends import render_color_trends
from pages.project_intro import render_project_intro

st.set_page_config(page_title="Lookbook Studio", layout="wide")

# Load CSS
st.markdown(load_global_css(), unsafe_allow_html=True)
st.markdown("""
<style>
:root { --bg-main: #f8f4ec; }
</style>
""", unsafe_allow_html=True)

# Initialize page
if "page" not in st.session_state:
    st.session_state.page = "wardrobe"

# Sync with URL query param if present (new API first; if not available, fallback)
allowed_pages = {"wardrobe", "lookbook", "trend", "intro"}
params = {}
try:
    params = st.query_params
except Exception:
    try:
        params = st.experimental_get_query_params()
    except Exception:
        params = {}

if "page" in params:
    value = params["page"]
    page_val = value[0] if isinstance(value, list) else value
    if page_val in allowed_pages:
        st.session_state.page = page_val
    else:
        st.session_state.page = "wardrobe"

# Top navigation bar
render_topnav()

# Routing
page = st.session_state.page

if page == "wardrobe":
    render_wardrobe()
elif page == "lookbook":
    render_lookbook()
elif page == "trend":
    render_color_trends()
elif page == "intro":
    render_project_intro()
