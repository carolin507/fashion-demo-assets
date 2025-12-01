# pages/lookbook.py

import streamlit as st
from ui.layout import card


def _streetstyle_dataset():
    return [
        {"file": "20170324095254453_500.jpg", "top": "黑色", "bottom": "灰色"},
        {"file": "20170324095730988_500.jpg", "top": "白色", "bottom": "綠色"},
        {"file": "20170324100124006_500.jpg", "top": "卡其", "bottom": "卡其"},
        {"file": "20170324100303683_500.jpg", "top": "藍色", "bottom": "黑色"},
        {"file": "20170324101207506_500.jpg", "top": "咖啡色", "bottom": "咖啡色"},
        {"file": "20170324101213181_500.jpg", "top": "藍色", "bottom": "白色"},
        {"file": "20170324101342210_500.jpg", "top": "綠色", "bottom": "卡其"},
        {"file": "20170324101553293_500.jpg", "top": "藍色", "bottom": "藍色"},
        {"file": "20170324101642714_500.jpg", "top": "黑色", "bottom": "棕色"},
        {"file": "20170324101732000_500.jpg", "top": "藍色", "bottom": "黑色"},
        {"file": "20170324101754087_500.jpg", "top": "米色", "bottom": "米色"},
        {"file": "20170324101839553_500.jpg", "top": "紅色", "bottom": "黑色"},
        {"file": "20170324102113466_500.jpg", "top": "米色", "bottom": "黑色"},
        {"file": "20170324102428957_500.jpg", "top": "白色", "bottom": "藍色"},
        {"file": "20170324102521935_500.jpg", "top": "米色", "bottom": "綠色"},
        {"file": "20170324102544688_500.jpg", "top": "白色", "bottom": "卡其"},
        {"file": "20170324102806575_500.jpg", "top": "卡其", "bottom": "黑色"},
        {"file": "20170324103244682_500.jpg", "top": "黑色", "bottom": "黑色"},
        {"file": "20170324103356507_500.jpg", "top": "藍色", "bottom": "咖啡色"},
        {"file": "20170324103547162_500.jpg", "top": "綠色", "bottom": "黑色"},
    ]


def render_lookbook():
    """街拍 Lookbook 主畫面 (SPA)"""

    st.markdown(card(
        "街拍 Lookbook",
        "<p class='subtle'>依上衣/下身色系篩選，快速瀏覽對味街拍靈感。</p>"
    ), unsafe_allow_html=True)

    data = _streetstyle_dataset()
    colors = sorted({d["top"] for d in data} | {d["bottom"] for d in data})
    color_options = ["全部"] + colors

    col1, col2 = st.columns(2)
    with col1:
        top_color = st.selectbox("上衣顏色", color_options)
    with col2:
        bottom_color = st.selectbox("下身顏色", color_options)

    filtered = [
        d for d in data
        if (top_color == "全部" or d["top"] == top_color)
        and (bottom_color == "全部" or d["bottom"] == bottom_color)
    ]

    base = (
        "https://raw.githubusercontent.com/carolin507/"
        "fashion-demo-assets/main/assets/streetstyle/"
    )

    if not filtered:
        st.info("沒有符合條件的街拍，換個條件再試一次。")
        return

    html_items = "".join(
        f"""
<div class="gallery-item">
<img src="{base + item['file']}" alt="street look">
<div class="caption">上衣：{item['top']} | 下身：{item['bottom']}</div>
</div>"""
        for item in filtered
    )

    st.markdown(f"""
<div class="gallery-grid">
{html_items}
</div>
""", unsafe_allow_html=True)
