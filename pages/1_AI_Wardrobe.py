# pages/1_AI_Wardrobe.py
# -*- coding: utf-8 -*-

"""
AI Wardrobe｜上傳穿搭照 → AI 辨識顏色 / 品類 → 推薦下身搭配與靈感。

此頁面專注在「AI 穿搭靈感推薦」這個主功能，不負責 Landing Page 或專案介紹。
"""

import sys
import os

# 將專案根路徑加入 Python 搜尋路徑
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)


import base64
import random
import urllib.parse
from io import BytesIO

import streamlit as st
from PIL import Image

from ui.css import load_global_css
from ui.layout import card, product_grid, lookbook_carousel
from modules.inference import predict_labels
from modules.recommend import recommend_bottom
from modules.utils import (
    zh_label,
    color_to_zh,
    pattern_to_zh,
    category_to_zh,
)

# ------------------------------------------------------------
# 全域 CSS
# ------------------------------------------------------------
st.markdown(load_global_css(), unsafe_allow_html=True)

# ------------------------------------------------------------
# 頁面標題
# ------------------------------------------------------------
st.markdown(
    """
    <div class="card">
      <div class="card-title">AI 穿搭靈感推薦｜AI Wardrobe</div>
      <p class="subtle">
        上傳一張日常穿搭照，AI 會協助辨識主色 / 花紋 / 服飾品類，並推薦適合的下身搭配方向，
        再延伸到相似單品與街拍 Lookbook，幫你把靈感變成實際購物線索。
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)
with st.sidebar:
    st.markdown("### Lookbook Studio")
    st.markdown("""
<style>
.sidebar-nav {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 6px;
}
.sidebar-nav a {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 12px;
    border-radius: 12px;
    background: #f6f2eb;
    color: #4a362f;
    text-decoration: none;
    border: 1px solid rgba(0,0,0,0.04);
    box-shadow: 0 6px 16px rgba(0,0,0,0.05);
    transition: transform .12s ease, box-shadow .12s ease, background .12s ease;
    white-space: nowrap;  /* 讓文字不要被切成一直排 */
}
.sidebar-nav a:hover {
    transform: translateY(-1px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}
.sidebar-nav a .icon {
    width: 28px;
    height: 28px;
    border-radius: 8px;
    background: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
}
</style>

<div class="sidebar-nav">
  <a href="https://fashion-demo-assets-1-ai-wardrobe.streamlit.app/">
    <span class="icon">🌟</span>AI 穿搭靈感推薦
  </a>
  <a href="https://fashion-demo-assets-2-street-lookbook.streamlit.app/">
    <span class="icon">📸</span>街頭穿搭直擊
  </a>
  <a href="https://fashion-demo-assets-3-color-trends.streamlit.app/">
    <span class="icon">🎨</span>本月流行色系
  </a>
  <a href="https://fashion-demo-assets-4-project-intro.streamlit.app/">
    <span class="icon">💡</span>專案介紹
  </a>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# STEP 1｜上傳區（性別 + 圖片）
# ------------------------------------------------------------
st.markdown(
    card(
        "STEP 1｜上傳你的穿搭照",
        "<p class='subtle'>選擇性別並上傳穿搭圖片，AI 會從上半身或整體穿搭中抓出主色與品類。</p>",
    ),
    unsafe_allow_html=True,
)

col_u1, col_u2 = st.columns([1, 2])
with col_u1:
    gender = st.selectbox("性別", ["female", "male", "unisex"])

with col_u2:
    uploaded_img = st.file_uploader(
        "上傳穿搭圖片（支援 JPG / JPEG / PNG）", type=["jpg", "jpeg", "png"]
    )

# ------------------------------------------------------------
# STEP 2｜處理上傳圖片 → 模型辨識 → 顯示結果
# ------------------------------------------------------------
if uploaded_img:
    # 讀取圖片並轉為 base64（用於 HTML <img>）
    img = Image.open(uploaded_img)
    buf = BytesIO()
    img.save(buf, format="PNG")
    img_b64 = base64.b64encode(buf.getvalue()).decode()

    # 呼叫模型（目前為 mock，未來可由 inference.py 串接真實模型）
    result = predict_labels(img, gender)

    col1, col2 = st.columns([1.1, 0.9])

    # 左側：原始穿搭圖片
    with col1:
        st.markdown(
            card(
                "你的穿搭照片",
                f"""
                <img src="data:image/png;base64,{img_b64}"
                     style="width:100%;border-radius:14px;
                            border:1px solid rgba(0,0,0,0.04);" />
                """,
            ),
            unsafe_allow_html=True,
        )

    # 右側：AI 辨識結果
    with col2:
        st.markdown(
            card(
                "AI 辨識結果（目前為 Demo Mock）",
                f"""
                <p><strong>顏色：</strong>{zh_label(result["color"], color_to_zh)}</p>
                <p><strong>花紋：</strong>{zh_label(result["pattern"], pattern_to_zh)}</p>
                <p><strong>品類：</strong>{zh_label(result["category"], category_to_zh)}</p>
                <p><strong>性別：</strong>{result["gender"]}</p>
                <p class='subtle'>
                  ※ 此頁面目前使用 <strong>mock 模型</strong>，實際課程專案中可由
                  <code>modules/inference.py</code> 串接 Body Segmentation / 顏色抽取 / CLIP 等模組。
                </p>
                """,
            ),
            unsafe_allow_html=True,
        )

    # --------------------------------------------------------
    # STEP 3｜依據辨識結果給出下身搭配建議
    # --------------------------------------------------------
    rec = recommend_bottom(
        color=result["color"], category=result["category"], gender=gender
    )

    # 顏色 + 類別 tag
    color_tags_html = " ".join(
        f"<span class='color-tag'>{zh_label(c, color_to_zh)}</span>"
        for c in rec["bottom_color"]
    )
    cat_tags_html = " ".join(
        f"<span class='tag'>{cat}</span>" for cat in rec["bottom_category"]
    )

    # 拿第一組建議，組成 Google 購物搜尋
    recommended_color = rec["bottom_color"][0]
    recommended_cat = rec["bottom_category"][0]
    search_query = f"{zh_label(recommended_color, color_to_zh)} {recommended_cat}"
    google_url = (
        "https://www.google.com/search?tbm=shop&q="
        + urllib.parse.quote(search_query)
    )

    st.markdown(
        card(
            "STEP 2｜AI 建議的下身搭配方向",
            f"""
            <p class="subtle">
              以下搭配規則目前由 <code>modules/recommend.py</code> 提供，
              可透過未來的 <code>logic_rules.py</code> 改為由資料計算出「最大宗搭配」邏輯。
            </p>
            <div style="margin-top:8px;">
                <strong>建議下身顏色：</strong> {color_tags_html}
            </div>
            <div style="margin-top:8px;">
                <strong>建議下身類別：</strong> {cat_tags_html}
            </div>
            <a href="{google_url}" target="_blank"
               style="margin-top:14px;display:inline-block;" class="hero-btn">
                前往 Google 購物查看相近單品
            </a>
            """,
        ),
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # STEP 4｜相似單品靈感（示意：隨機選取 GitHub 圖片）
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

    samples = random.sample(product_files, k=min(3, len(product_files)))

    st.markdown(
        product_grid(samples, product_base),
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # STEP 5｜街拍 Lookbook（垂直輪播靈感）
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

    st.markdown(
        lookbook_carousel(streetstyle_files, streetstyle_base),
        unsafe_allow_html=True,
    )

else:
    # 尚未上傳圖片時顯示引導卡片
    st.markdown(
        card(
            "準備開始體驗 AI 穿搭靈感了嗎？",
            """
            <p class="subtle">
              在上方選擇性別並上傳一張日常穿搭照，
              系統會透過 <strong>顏色 / 花紋 / 品類</strong> 等特徵，
              示範如何建立一個從「穿搭 → 搭配規則 → 商品靈感」的 AI Recommendation Flow。
            </p>
            """,
        ),
        unsafe_allow_html=True,
    )
