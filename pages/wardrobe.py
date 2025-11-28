# pages/wardrobe.py

"""
AI Wardrobe｜上傳穿搭照 → AI 辨識顏色 / 品類 → 推薦下身搭配與靈感。
此模組僅負責「內容渲染」，由 app.py 控制頁面切換（SPA Routing）。
"""

import base64
import random
import urllib.parse
from io import BytesIO

import streamlit as st
from PIL import Image

from ui.layout import card, product_grid, lookbook_carousel
from modules.inference import predict_labels
from modules.recommend import recommend_bottom
from modules.utils import (
    zh_label, color_to_zh, pattern_to_zh, category_to_zh
)


def render_wardrobe():
    """主渲染函式，由 app.py 呼叫"""

    # ------------------------------------------------------------
    # 1. Hero Banner
    # ------------------------------------------------------------
    st.markdown("""
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
    """, unsafe_allow_html=True)

    # ------------------------------------------------------------
    # 框：頁面說明
    # ------------------------------------------------------------
    st.markdown(card(
        "AI 穿搭靈感推薦｜AI Wardrobe",
        """
        <p class="subtle">
            上傳一張日常穿搭照，AI 會協助辨識主色 / 花紋 / 服飾品類，
            並推薦適合的下身搭配方向，再延伸相似單品與街拍 Lookbook。
        </p>
        """
    ), unsafe_allow_html=True)

    # ------------------------------------------------------------
    # STEP 1｜上傳區
    # ------------------------------------------------------------
    st.markdown(card(
        "STEP 1｜上傳你的穿搭照",
        "<p class='subtle'>選擇性別並上傳穿搭圖片。</p>"
    ), unsafe_allow_html=True)

    col_u1, col_u2 = st.columns([1, 2])
    with col_u1:
        gender = st.selectbox("性別", ["female", "male", "unisex"])

    with col_u2:
        uploaded_img = st.file_uploader(
            "上傳穿搭圖片（支援 JPG / JPEG / PNG）",
            type=["jpg", "jpeg", "png"]
        )

    # ------------------------------------------------------------
    # 若已上傳圖片 → 執行後續流程
    # ------------------------------------------------------------
    if uploaded_img:

        # 讀入圖片
        img = Image.open(uploaded_img)
        buf = BytesIO()
        img.save(buf, format="PNG")
        img_b64 = base64.b64encode(buf.getvalue()).decode()

        # 模型辨識（目前為 mock）
        result = predict_labels(img, gender)

        # --------------------------------------------------------
        # STEP 2｜顯示辨識結果
        # --------------------------------------------------------
        col1, col2 = st.columns([1.1, 0.9])

        # 左側：原始圖片
        with col1:
            st.markdown(card("你的穿搭照片", f"""
                <img src="data:image/png;base64,{img_b64}"
                     style="width:100%;border-radius:14px;
                            border:1px solid rgba(0,0,0,0.04);" />
            """), unsafe_allow_html=True)

        # 右側：AI label
        with col2:
            st.markdown(card(
                "AI 辨識結果（Demo 模式）",
                f"""
                <p><strong>顏色：</strong>{zh_label(result['color'], color_to_zh)}</p>
                <p><strong>花紋：</strong>{zh_label(result['pattern'], pattern_to_zh)}</p>
                <p><strong>品類：</strong>{zh_label(result['category'], category_to_zh)}</p>
                <p class="subtle">
                    ※ 模型邏輯位於 <code>modules/inference.py</code><br>
                </p>
                """
            ), unsafe_allow_html=True)

        # --------------------------------------------------------
        # STEP 3｜下身搭配建議
        # --------------------------------------------------------
        rec = recommend_bottom(
            color=result["color"],
            category=result["category"],
            gender=gender
        )

        color_tags_html = " ".join(
            f"<span class='color-tag'>{zh_label(c, color_to_zh)}</span>"
            for c in rec["bottom_color"]
        )
        cat_tags_html = " ".join(
            f"<span class='tag'>{cat}</span>"
            for cat in rec["bottom_category"]
        )

        # Google Shopping
        recommended_color = rec["bottom_color"][0]
        recommended_cat = rec["bottom_category"][0]
        query = f"{zh_label(recommended_color, color_to_zh)} {recommended_cat}"
        google_url = "https://www.google.com/search?tbm=shop&q=" + urllib.parse.quote(query)

        st.markdown(card(
            "STEP 2｜AI 建議的下身搭配方向",
            f"""
            <p class="subtle">
              規則由 <code>modules/recommend.py</code> 提供，未來可換成資料計算出的搭配邏輯。
            </p>

            <strong>建議顏色：</strong> {color_tags_html}<br>
            <strong>建議類別：</strong> {cat_tags_html}<br>

            <a href="{google_url}" target="_blank"
               class="hero-btn" style="margin-top:14px;display:inline-block;">
               前往 Google 購物查看相近單品
            </a>
            """
        ), unsafe_allow_html=True)

        # --------------------------------------------------------
        # STEP 4｜相似單品（示意）
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

        st.markdown(product_grid(
            random.sample(product_files, min(3, len(product_files))),
            product_base
        ), unsafe_allow_html=True)

        # --------------------------------------------------------
        # STEP 5｜Lookbook 輪播
        # --------------------------------------------------------
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
        streetstyle_base = (
            "https://raw.githubusercontent.com/carolin507/"
            "fashion-demo-assets/main/assets/streetstyle/"
        )

        st.markdown(lookbook_carousel(streetstyle_files, streetstyle_base),
                    unsafe_allow_html=True)

    # ------------------------------------------------------------
    # 尚未上傳：顯示引導
    # ------------------------------------------------------------
    else:
        st.markdown(card(
            "準備開始體驗 AI 穿搭靈感了嗎？",
            """
            <p class="subtle">
              上傳一張穿搭照，示範「穿搭 → 標籤 → 搭配 → 商品靈感」的 AI Flow。
            </p>
            """
        ), unsafe_allow_html=True)
