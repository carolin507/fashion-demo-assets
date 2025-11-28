# pages/lookbook.py

import random
import streamlit as st
from ui.layout import card, lookbook_carousel


def render_lookbook():
    """街拍 Lookbook 主頁面（SPA）"""

    st.markdown(card(
        "街拍靈感 Lookbook",
        "<p class='subtle'>以大量真實街拍為靈感來源，協助你快速找到喜歡的配色與風格。</p>"
    ), unsafe_allow_html=True)

    streetstyle_files = [
        "20170324095254453_500.jpg",
        "20170324095730988_500.jpg",
        "20170324100124006_500.jpg",
        "20170324100303683_500.jpg",
        "20170324101207506_500.jpg",
        "20170324101213181_500.jpg",
        "20170324101342210_500.jpg",
        "20170324101553293_500.jpg",
        "20170324101642714_500.jpg",
    ]

    base = (
        "https://raw.githubusercontent.com/carolin507/"
        "fashion-demo-assets/main/assets/streetstyle/"
    )

    st.markdown(
        lookbook_carousel(streetstyle_files, base),
        unsafe_allow_html=True,
    )
