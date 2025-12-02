# pages/wardrobe.py

"""
AI Wardrobe：上傳穿搭照 → AI 辨識顏色 / 品類 → 推薦下身搭配與靈感。
新版：整合 model_core.infer_labels / infer_and_recommend
"""

import base64
import urllib.parse
from io import BytesIO
from textwrap import dedent

import streamlit as st
from PIL import Image

from ui.layout import card, product_grid
from modules.model_core import infer_labels, infer_and_recommend
from modules.utils import zh_label, color_to_zh, pattern_to_zh, category_to_zh


COLOR_HEX = {
    "Black": "#2b2b2b",
    "Gray": "#7d7d7d",
    "White": "#f6f6f6",
    "Beige": "#e9dcc6",
    "Orange": "#f0a35c",
    "Pink": "#f3a6b4",
    "Red": "#d95555",
    "Green": "#5e8c6a",
    "Brown": "#7a5537",
    "Blue": "#3f68b5",
    "Yellow": "#f3d75c",
    "Purple": "#8b6fb5",
}
LIGHT_COLORS = {"White", "Beige", "Yellow", "Pink", "Orange"}


def render_wardrobe(recommender):
    """主渲染函式（新版：使用推薦器）"""

    # ------------------------------------------------------------
    # Hero Banner
    # ------------------------------------------------------------
    st.markdown(dedent("""
        <div class="hero-outer">
            <div class="hero-wrapper">
                <img class="hero-img"
                     src="https://raw.githubusercontent.com/carolin507/fashion-demo-assets/main/assets/hero_banner.jpg">
                <div class="hero-overlay">
                    <div>
                        <div class="hero-title">AI 穿搭靈感推薦</div>
                        <div class="hero-sub">上傳穿搭，AI 幫你分析主色、花紋與品類</div>
                    </div>
                </div>
            </div>
        </div>
    """), unsafe_allow_html=True)

    # Intro card
    st.markdown(card(
        "AI 穿搭靈感推薦｜AI Wardrobe",
        dedent("""
        <p class="subtle">
            上傳一張穿搭照，AI 會辨識主色 / 花紋 / 服飾品類，
            並推薦下身搭配方向，再延伸相似單品與 Lookbook。
        </p>
        """)
    ), unsafe_allow_html=True)

    # ------------------------------------------------------------
    # STEP 1 — 上傳圖片
    # ------------------------------------------------------------
    st.markdown(card(
        "STEP 1｜上傳你的穿搭照",
        "<p class='subtle'>選擇性別並上傳穿搭圖片。</p>"
    ), unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 2])
    with col_left:
        gender = st.selectbox("性別", ["female", "male", "unisex"])

    with col_right:
        uploaded_img = st.file_uploader(
            "上傳穿搭圖片（JPG / PNG）",
            type=["jpg", "jpeg", "png"]
        )

    # ------------------------------------------------------------
    # 若已上傳 → 開始推論
    # ------------------------------------------------------------
    if uploaded_img:
        img = Image.open(uploaded_img)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_b64 = base64.b64encode(buffer.getvalue()).decode()

        # ====== 1) AI 標籤推論 ======
        labels = infer_labels(img)

        color_label = labels["color"]
        style_label = labels["style"]
        cat_label = labels["category"]
        part = labels["part"]

        # ====== 2) AI 推薦 ======
        rec_result = infer_and_recommend(img, recommender)
        recommendations = rec_result["recommendations"]

        # --------------------------------------------------------
        # STEP 2 — 顯示上傳圖片 + 推論標籤
        # --------------------------------------------------------
        c1, c2 = st.columns([1.1, 0.9])
        with c1:
            st.markdown(card(
                "你的穿搭照片",
                f"""<img src="data:image/png;base64,{img_b64}" class="uploaded-photo"/>"""
            ), unsafe_allow_html=True)

        with c2:
            st.markdown(card(
                "AI 辨識結果（正式模型）",
                dedent(f"""
                <p><strong>顏色：</strong>{zh_label(color_label, color_to_zh)}</p>
                <p><strong>花紋：</strong>{zh_label(style_label, pattern_to_zh)}</p>
                <p><strong>品類：</strong>{zh_label(cat_label, category_to_zh)}</p>
                <p><strong>部位：</strong>{part}</p>
                """)
            ), unsafe_allow_html=True)

        # --------------------------------------------------------
        # STEP 3 — 正式推薦區塊（不會再破版）
        # --------------------------------------------------------
        if recommendations:
            top_rec = recommendations[0]
            rec_color = top_rec["color"]
            rec_style = top_rec["style"]
            rec_cat = top_rec["category"]

            query = f"{zh_label(rec_color, color_to_zh)} {zh_label(rec_cat, category_to_zh)}"
            google_url = "https://www.google.com/search?tbm=shop&q=" + urllib.parse.quote(query)

            st.markdown(card(
                "STEP 2｜AI 建議的下身搭配方向（正式推薦）",
                dedent(f"""
                <p class="subtle">
                    由 <code>cooccurrence_recommender.py</code> 產生真實共現推薦結果。
                </p>

                <div class="tag-row">
                    <div class="tag-label">建議顏色：</div>
                    <span class="color-tag" style="background:{COLOR_HEX.get(rec_color,'#888')};
                        color:{'#2f241e' if rec_color in LIGHT_COLORS else '#fff'};">
                        {zh_label(rec_color, color_to_zh)}
                    </span>
                </div>

                <div class="tag-row">
                    <div class="tag-label">建議類別：</div>
                    <span class="tag">{zh_label(rec_cat, category_to_zh)}</span>
                </div>

                <a href="{google_url}" target="_blank" class="hero-btn">
                    前往 Google 購物查看相近單品
                </a>
                """)
            ), unsafe_allow_html=True)


        # --------------------------------------------------------
        # STEP 4 — 精選單品（UI 完整）
        # --------------------------------------------------------
        product_files = [
            "638992503203300000.jpg",
            "638993154193030000.jpg",
            "638993413666200000.jpg",
            "638993433208400000.jpg",
            "638993433310200000.jpg",
        ]
        product_base = (
            "https://raw.githubusercontent.com/carolin507/"
            "fashion-demo-assets/main/assets/product/"
        )

        st.markdown(product_grid(product_files, product_base), unsafe_allow_html=True)

    else:
        st.markdown(card(
            "準備開始體驗 AI 穿搭靈感了嗎？",
            "<p class='subtle'>上傳穿搭照即可示範完整 AI Flow。</p>"
        ), unsafe_allow_html=True)
