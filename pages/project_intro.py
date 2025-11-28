# pages/project_intro.py

import streamlit as st
from textwrap import dedent
from ui.layout import card


def render_project_intro():
    """專案介紹模組（SPA）"""

    st.markdown(card(
        "專案介紹｜Lookbook Studio",
        dedent("""
        <p class='subtle'>
            Lookbook Studio 是一個 AI 穿搭靈感示範，
            由圖片辨識（顏色 / 花紋 / 品類）、搭配建議、色彩趨勢與街拍靈感組成。
        </p>
        """).strip()
    ), unsafe_allow_html=True)

    st.markdown(card(
        "功能模組 Modules",
        dedent("""
        <ul>
            <li><strong>AI Wardrobe</strong>：上傳照 → 辨識 → 搭配 → 靈感</li>
            <li><strong>Street Lookbook</strong>：街拍穿搭輪播</li>
            <li><strong>Color Trends</strong>：熱門色彩觀察</li>
            <li><strong>Project Intro</strong>：架構與技術說明</li>
        </ul>
        """).strip()
    ), unsafe_allow_html=True)

    st.markdown(card(
        "流程架構 Architecture",
        dedent("""
        <pre style="white-space:pre-wrap; font-size:13px; color:#4a362f;">
使用者上傳穿搭 → 模型辨識色彩/花紋/品類
        →
搭配建議（規則/數據匹配）
        →
推薦下身穿搭（顏色 + 類型）
        →
精選單品（GitHub 靜態圖）
        →
街拍 Lookbook 參考
        </pre>
        """).strip()
    ), unsafe_allow_html=True)
