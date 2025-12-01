# pages/wardrobe.py

"""
AI Wardrobe：上傳穿搭照 → AI 辨識顏色 / 品類 → 推薦下身搭配與靈感。
僅負責內容渲染，路由由 app.py 控制。
"""

import base64
import random
import urllib.parse
from io import BytesIO
from textwrap import dedent

import streamlit as st
from PIL import Image

from ui.layout import card, product_grid
from modules.inference import predict_labels
from modules.recommend import recommend_bottom
from modules.utils import (
    zh_label, color_to_zh, pattern_to_zh, category_to_zh
)

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


def render_wardrobe():
    """主渲染函式"""

    # ------------------------------------------------------------
    # 1. Hero Banner
    # ------------------------------------------------------------
    st.markdown(dedent("""
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
    """).strip(), unsafe_allow_html=True)

    # ------------------------------------------------------------
    # 說明卡
    # ------------------------------------------------------------
    st.markdown(card(
        "AI 穿搭靈感推薦｜AI Wardrobe",
        dedent("""
        <p class="subtle">
            上傳一張日常穿搭照，AI 會辨識主色 / 花紋 / 服飾品類，
            並推薦下身搭配方向，再延伸相似單品與街拍 Lookbook。
        </p>
        """).strip()
    ), unsafe_allow_html=True)

    # ------------------------------------------------------------
    # STEP 1
    # ------------------------------------------------------------
    st.markdown(card(
        "STEP 1｜上傳你的穿搭照",
        "<p class='subtle'>選擇性別並上傳穿搭圖片。</p>"
    ), unsafe_allow_html=True)

    col_u1, col_u2 = st.columns([1, 2])
    with col_u1:
        gender = st.selectbox("性別", ["female", "male", "unisex"])
        cloth_part = st.selectbox("上衣 / 下著", ["上衣", "下著"])

    with col_u2:
        uploaded_img = st.file_uploader(
            "上傳穿搭圖片（支援 JPG / JPEG / PNG）",
            type=["jpg", "jpeg", "png"]
        )

    # ------------------------------------------------------------
    # 若已上傳圖 → 流程
    # ------------------------------------------------------------
    if uploaded_img:
        img = Image.open(uploaded_img)
        buf = BytesIO()
        img.save(buf, format="PNG")
        img_b64 = base64.b64encode(buf.getvalue()).decode()

        result = predict_labels(img, gender)

        # STEP 2｜辨識結果
        col1, col2 = st.columns([1.1, 0.9])
        with col1:
            photo_html = f"""
<img src="data:image/png;base64,{img_b64}"
     class="uploaded-photo" />
            """
            st.markdown(card("你的穿搭照片", photo_html), unsafe_allow_html=True)

        with col2:
            st.markdown(card(
                "AI 辨識結果（Demo 模式）",
                dedent(f"""
                <p><strong>顏色：</strong>{zh_label(result['color'], color_to_zh)}</p>
                <p><strong>花紋：</strong>{zh_label(result['pattern'], pattern_to_zh)}</p>
                <p><strong>品類：</strong>{zh_label(result['category'], category_to_zh)}</p>
                <p class="subtle">
                    ※ 模型邏輯位於 <code>modules/inference.py</code>
                </p>
                """).strip()
            ), unsafe_allow_html=True)

        # STEP 3｜搭配建議
        rec = recommend_bottom(
            color=result["color"],
            category=result["category"],
            gender=gender
        )

        color_tags_html = "".join(
            f"<span class='color-tag' style=\"background:{COLOR_HEX.get(c, '#888')};"
            f"color:{'#2f241e' if c in LIGHT_COLORS else '#ffffff'};\">"
            f"{zh_label(c, color_to_zh)}</span>"
            for c in rec["bottom_color"]
        )
        cat_tags_html = " ".join(
            f"<span class='tag'>{cat}</span>"
            for cat in rec["bottom_category"]
        )
        recommended_color = rec["bottom_color"][0]
        recommended_cat = rec["bottom_category"][0]
        query = f"{zh_label(recommended_color, color_to_zh)} {recommended_cat}"
        google_url = "https://www.google.com/search?tbm=shop&q=" + urllib.parse.quote(query)

        st.markdown(card(
            "STEP 2｜AI 建議的下身搭配方向",
            dedent(f"""
            <p class="subtle">
              規則由 <code>modules/recommend.py</code> 提供，可替換成資料計算邏輯。
            </p>

            <div class="tag-row">
              <div class="tag-label">建議顏色：</div>
              {color_tags_html}
            </div>
            <div class="tag-row">
              <div class="tag-label">建議類別：</div>
              {cat_tags_html}
            </div>

            <a href="{google_url}" target="_blank"
               class="hero-btn" style="margin-top:14px;display:inline-block;">
               前往 Google 購物查看相近單品
            </a>
            """).strip()
        ), unsafe_allow_html=True)

        # STEP 4｜相似單品
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
        st.markdown(product_grid(
            random.sample(product_files, min(4, len(product_files))),
            product_base
        ), unsafe_allow_html=True)

    # 尚未上傳：提示
    else:
        st.markdown(card(
            "準備開始體驗 AI 穿搭靈感了嗎？",
            dedent("""
            <p class="subtle">
              上傳一張穿搭照，示範「穿搭 → 標籤 → 搭配 → 商品靈感」的 AI Flow。
            </p>
            """).strip()
        ), unsafe_allow_html=True)
