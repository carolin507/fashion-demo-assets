# pages/project_intro.py

import streamlit as st
from textwrap import dedent
from ui.layout import card


def render_project_intro():
    """專案介紹與 AI 流程圖 (SPA)"""

    st.markdown(card(
        "專案介紹｜Lookbook Studio",
        dedent("""
        <p class='subtle'>
            Lookbook Studio 示範一條 AI 穿搭工作流：上傳穿搭照 → AI 辨識顏色 / 紋理 / 類別 → 提供下身推薦與色彩趨勢瀏覽。
            目前為 Demo，模組與資料可依實際專案再串接調整。
        </p>
        """).strip()
    ), unsafe_allow_html=True)

    st.markdown(card(
        "功能模組 Modules",
        dedent("""
        <ul>
            <li><strong>AI Wardrobe</strong>：上傳穿搭照，偵測主色、圖樣、單品類別</li>
            <li><strong>Street Lookbook</strong>：街拍靈感瀏覽，依色系篩選</li>
            <li><strong>Trend Dashboard</strong>：以月份/性別/色系的趨勢報表（示意數據）</li>
            <li><strong>Project Intro</strong>：專案說明與技術架構</li>
        </ul>
        """).strip()
    ), unsafe_allow_html=True)

    st.markdown(card(
        "AI 技術流程圖",
        """
        <div style='text-align:center;'>
            <img src="https://raw.githubusercontent.com/carolin507/fashion-demo-assets/main/moduleflow.jpg"
                 alt="AI 流程圖"
                 style="max-width:100%; border-radius:10px; box-shadow:0 10px 24px rgba(0,0,0,0.08);" />
        </div>
        """
    ), unsafe_allow_html=True)

    st.markdown(card(
        "AI Pipeline 摘要",
        dedent("""
        <ol>
            <li><strong>上傳 / 輸入</strong>：穿搭照片或來源資料</li>
            <li><strong>特徵擷取</strong>：影像模型偵測上身主色 / 紋理 / 類別</li>
            <li><strong>規則 / 模型推薦</strong>：依色彩協調與類別規則給出下身搭配清單</li>
            <li><strong>延伸瀏覽</strong>：街拍 Lookbook、色彩趨勢儀表板</li>
            <li><strong>回饋 / 疊代</strong>：點擊、偏好回饋可用於後續模型微調</li>
        </ol>
        """).strip()
    ), unsafe_allow_html=True)

    st.markdown(card(
        "未來可接軌項目",
        dedent("""
        <ul>
            <li>串接真實數據管線：商品庫、追蹤事件、GA / CDP</li>
            <li>上架 A/B：針對推薦邏輯與 UI 做實驗</li>
            <li>模型優化：色彩分群、協同過濾、Few-shot 風格辨識</li>
        </ul>
        """).strip()
    ), unsafe_allow_html=True)

