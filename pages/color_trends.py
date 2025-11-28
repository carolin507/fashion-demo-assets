# pages/color_trends.py

import streamlit as st
from textwrap import dedent
from ui.layout import card


def _streetstyle_dataset():
    return [
        {"file": "20170324095254453_500.jpg", "top": "黑色", "bottom": "灰色"},
        {"file": "20170324095730988_500.jpg", "top": "白色", "bottom": "綠色"},
        {"file": "20170324100124006_500.jpg", "top": "卡其", "bottom": "卡其"},
        {"file": "20170324100303683_500.jpg", "top": "藍色", "bottom": "黑色"},
        {"file": "20170324101207506_500.jpg", "top": "咖啡", "bottom": "咖啡"},
        {"file": "20170324101213181_500.jpg", "top": "白色", "bottom": "藍色"},
        {"file": "20170324101342210_500.jpg", "top": "綠色", "bottom": "卡其"},
        {"file": "20170324101553293_500.jpg", "top": "灰色", "bottom": "灰色"},
        {"file": "20170324101642714_500.jpg", "top": "黑色", "bottom": "棕色"},
        {"file": "20170324101732000_500.jpg", "top": "白色", "bottom": "白色"},
        {"file": "20170324101754087_500.jpg", "top": "米色", "bottom": "米色"},
        {"file": "20170324101839553_500.jpg", "top": "紅色", "bottom": "黑色"},
        {"file": "20170324102113466_500.jpg", "top": "灰色", "bottom": "黑色"},
        {"file": "20170324102428957_500.jpg", "top": "藍色", "bottom": "藍色"},
        {"file": "20170324102521935_500.jpg", "top": "米色", "bottom": "綠色"},
        {"file": "20170324102544688_500.jpg", "top": "藍色", "bottom": "卡其"},
        {"file": "20170324102806575_500.jpg", "top": "卡其", "bottom": "黑色"},
        {"file": "20170324103244682_500.jpg", "top": "黑色", "bottom": "黑色"},
        {"file": "20170324103356507_500.jpg", "top": "白色", "bottom": "咖啡"},
        {"file": "20170324103547162_500.jpg", "top": "綠色", "bottom": "黑色"},
    ]


def render_color_trends():
    """流行色系子頁（SPA）"""

    st.markdown(card(
        "流行色系",
        dedent("""
        <p class='subtle'>
            點選色票即可瀏覽該色系的街拍圖片；快速抓取穿搭靈感。
        </p>
        """).strip()
    ), unsafe_allow_html=True)

    data = _streetstyle_dataset()
    palette = [
        ("黑色", "#2b2b2b"),
        ("白色", "#f6f6f6"),
        ("米色", "#e9dcc6"),
        ("藍色", "#3f68b5"),
        ("綠色", "#5e8c6a"),
        ("紅色", "#d95555"),
    ]

    st.markdown("<div class='trend-row'>", unsafe_allow_html=True)
    cols = st.columns(len(palette))
    choice = st.session_state.get("trend_color_choice")
    for (name, hexv), col in zip(palette, cols):
        with col:
            if st.button(name, key=f"trend_{name}"):
                choice = name
                st.session_state["trend_color_choice"] = name
    st.markdown("</div>", unsafe_allow_html=True)
    if not choice:
        st.info("請先點選色票查看對應照片")
        return

    base = (
        "https://raw.githubusercontent.com/carolin507/"
        "fashion-demo-assets/main/assets/streetstyle/"
    )

    filtered = [
        d for d in data
        if d["top"] == choice or d["bottom"] == choice
    ]

    if not filtered:
        st.info("目前沒有符合的街拍圖片")
        return

    # render fixed-height 3-column grid
    html_items = "".join(
        f"""
        <div class="gallery-item">
            <img src="{base + item['file']}" alt="street look">
            <div class="caption">上衣：{item['top']}｜下著：{item['bottom']}</div>
        </div>
        """
        for item in filtered
    )
    st.markdown(f"""
    <div class="gallery-grid">
        {html_items}
    </div>
    """, unsafe_allow_html=True)
