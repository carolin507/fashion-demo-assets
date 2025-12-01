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
.topnav {
    background: linear-gradient(120deg, #ffdce8, #ffc0d9);
    border-bottom: 1px solid rgba(255, 181, 204, 0.55);
}
.topnav .stButton>button {
    background: linear-gradient(120deg, #ffe6f0, #ffd1e4);
    color: #6c2a44;
    border: 1px solid rgba(255, 181, 204, 0.5);
    box-shadow: 0 10px 22px rgba(255, 181, 204, 0.35);
}
.topnav .brand {
    font-size: 30px !important;
    font-family: 'Noto Serif TC', serif !important;
    font-weight: 700 !important;
    line-height: 1.1;
}
.topnav [data-testid="baseButton-primary"] {
    background: linear-gradient(120deg, #ff6f95, #ff8fb8);
    color: #fff8fb;
}
.topnav [data-testid="baseButton-secondary"] {
    background: linear-gradient(120deg, #fff1f7, #ffe3ed);
    color: #6c2a44;
}
.topnav .stButton>button:hover { box-shadow: 0 12px 24px rgba(255, 181, 204, 0.45); }

.hero-wrapper {
    width: calc(100% + (var(--page-pad) * 2));
    margin-left: calc(-1 * var(--page-pad));
    height: 420px;
}
.hero-overlay {
    background: linear-gradient(90deg, rgba(0,0,0,0.50), rgba(0,0,0,0.12), transparent);
}
@media (max-width: 768px) {
    .hero-wrapper {
        width: 100vw;
        margin-left: calc(-1 * (50vw - 50%));
        height: 260px;
    }
}

.gallery-grid {
    display: flex;
    gap: 16px;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    padding: 4px 2px 10px;
}
.gallery-grid::-webkit-scrollbar { height: 8px; }
.gallery-grid::-webkit-scrollbar-thumb {
    background: rgba(0,0,0,0.12);
    border-radius: 999px;
}
.gallery-item {
    flex: 0 0 clamp(240px, 28vw, 320px);
    scroll-snap-align: start;
}
.gallery-item img { height: 260px; }
</style>
<script>
(() => {
  const attach = (grid) => {
    if (grid.dataset.carouselAttached) return;
    grid.dataset.carouselAttached = "1";
    let dir = 1;
    setInterval(() => {
      const maxScroll = grid.scrollWidth - grid.clientWidth;
      if (grid.scrollLeft >= maxScroll - 2) dir = -1;
      if (grid.scrollLeft <= 2) dir = 1;
      grid.scrollBy({ left: dir * grid.clientWidth * 0.35, behavior: "smooth" });
    }, 1000);
  };
  const scan = () => document.querySelectorAll(".gallery-grid").forEach(attach);
  window.addEventListener("load", scan);
  const observer = new MutationObserver(scan);
  observer.observe(document.body, { childList: true, subtree: true });
})();
</script>
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
