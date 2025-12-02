# app.py

import streamlit as st
st.set_page_config(page_title="Lookbook Studio", layout="wide")

from ui.css import load_global_css
from ui.topnav import render_topnav

from pages.wardrobe import render_wardrobe
from pages.lookbook import render_lookbook
from pages.dashboard import render_color_trends
from pages.project_intro import render_project_intro

import pandas as pd
from modules.model_core import build_recommender_from_pairs
from pages.wardrobe import render_wardrobe
import ast


# ------------------------------------------------------------
# 讀取穿搭共現資料集，並建立推薦器
# ------------------------------------------------------------
@st.cache_resource

def load_recommender():
    file_path = "data/pairs_from_vlabels.csv" 

    try:
        df_pairs = pd.read_csv(
            file_path,
            converters={
                "top": ast.literal_eval,
                "bottom": ast.literal_eval,
            }
        )
    except Exception as e:
        st.error(f"⚠️ 無法讀取推薦資料集：{file_path}\n{e}")
        return None

    recommender = build_recommender_from_pairs(df_pairs)
    return recommender

RECOMMENDER = load_recommender()


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
allowed_pages = {"wardrobe", "lookbook", "dashboard", "intro"}
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
    render_wardrobe(RECOMMENDER)
elif page == "lookbook":
    render_lookbook()
elif page == "dashboard":
    render_color_trends()
elif page == "intro":
    render_project_intro()
