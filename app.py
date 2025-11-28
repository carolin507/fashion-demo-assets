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
load_global_css()

# Initialize page
if "page" not in st.session_state:
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