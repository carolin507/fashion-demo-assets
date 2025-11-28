# pages/project_intro.py

import streamlit as st
from ui.layout import card


def render_project_intro():
    """專案介紹頁｜SPA"""

    st.markdown(card(
        "專案介紹｜Lookbook Studio",
        """
        <p class='subtle'>
            Lookbook Studio 是一個 AI 穿搭靈感原型，
            結合圖像辨識（顏色 / 花紋 / 品類）、搭配邏輯、街拍資料庫與商品靈感。
        </p>
        """
    ), unsafe_allow_html=True)

    st.markdown(card(
        "核心功能 Modules",
        """
        <ul>
            <li><strong>AI Wardrobe</strong>：上傳 → 標註 → 推薦 → 商品靈感</li>
            <li><strong>Street Lookbook</strong>：街拍靈感輪播庫</li>
            <li><strong>Color Trends</strong>：動態流行色分析</li>
            <li><strong>Project Intro</strong>：架構、流程與技術</li>
        </ul>
        """
    ), unsafe_allow_html=True)

    st.markdown(card(
        "系統架構 Architecture",
        """
        <pre style="white-space:pre-wrap; font-size:13px; color:#4a362f;">
使用者上傳穿搭 → 模型抽取特徵（顏色 / 花紋 / 品類）
        ↓
搭配邏輯（規則版 / 資料統計版）
        ↓
推薦下身方向（顏色 + 類別）
        ↓
相似商品（GitHub 靜態圖）
        ↓
街拍 Lookbook 延伸靈感
        </pre>
        """
    ), unsafe_allow_html=True)
