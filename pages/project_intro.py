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
        "AI Flow：Pair-Based 共現推薦",
        dedent("""
        <style>
        .flow-rail {display:flex; flex-direction:column; gap:14px; max-width:780px; margin:0 auto;}
        .flow-step {display:flex; align-items:flex-start; gap:14px; padding:16px 18px; border-radius:16px;
                    background:linear-gradient(135deg, #f5f7ff, #ffffff); border:1px solid #e5e7f5;
                    box-shadow:0 12px 36px rgba(12, 53, 83, 0.07);}
        .flow-icon {width:44px; height:44px; border-radius:14px; display:grid; place-items:center;
                    background:linear-gradient(135deg, #00c6ff, #0072ff); color:white; font-weight:800;}
        .flow-text {flex:1; line-height:1.6;}
        .flow-label {display:inline-flex; align-items:center; gap:6px; padding:4px 10px; border-radius:999px;
                     background:rgba(0,114,255,0.12); color:#1f3c7a; font-size:12px; font-weight:700;}
        .flow-arrow {text-align:center; color:#6b7280; font-size:22px;}
        .flow-badge {display:inline-flex; gap:6px; flex-wrap:wrap; margin-top:6px;}
        .pill {padding:4px 10px; border-radius:999px; font-size:12px; border:1px solid #d6dcf4; color:#31436b;}
        .json-box {font-family: "SFMono-Regular","Consolas","Liberation Mono","Menlo",monospace; background:#0b1220; color:#e7edf7;
                   padding:10px 12px; border-radius:10px; font-size:12px; margin-top:8px;}
        </style>
        <div class='flow-rail'>
            <div class='flow-step'>
                <div class='flow-icon'>1</div>
                <div class='flow-text'>
                    <div class='flow-label'>STEP 1｜上傳 (Streamlit)</div>
                    使用者選擇性別（female / male / unisex）並上傳穿搭圖片（JPG）。
                    <div class='flow-badge'>
                        <span class='pill'>Gender toggle</span><span class='pill'>Image upload</span>
                    </div>
                </div>
            </div>
            <div class='flow-arrow'>↓</div>
            <div class='flow-step'>
                <div class='flow-icon'>2</div>
                <div class='flow-text'>
                    <div class='flow-label'>STEP 2｜AI 辨識衣服屬性</div>
                    來源可用 infer_labels（既有模型）或 CLIP prompt-based（不取 embedding），僅輸出文字標籤。
                    <div class='json-box'>
{<br/>
&nbsp;&nbsp;"part": "Top",<br/>
&nbsp;&nbsp;"color": "White",<br/>
&nbsp;&nbsp;"pattern": "Solid",<br/>
&nbsp;&nbsp;"category": "Shirt",<br/>
&nbsp;&nbsp;"gender": "female"<br/>
}
                    </div>
                </div>
            </div>
            <div class='flow-arrow'>↓</div>
            <div class='flow-step'>
                <div class='flow-icon'>3</div>
                <div class='flow-text'>
                    <div class='flow-label'>STEP 3｜Pair-Based 共現推薦器</div>
                    以上身文字屬性（color / pattern / category）找相似上身 pair，統計共現 Bottom，依 matching 分數排序取 Top-K。
                    <div class='flow-badge'>
                        <span class='pill'>顏色相似</span><span class='pill'>花紋相似</span><span class='pill'>類別相似</span>
                    </div>
                </div>
            </div>
            <div class='flow-arrow'>↓</div>
            <div class='flow-step'>
                <div class='flow-icon'>4</div>
                <div class='flow-text'>
                    <div class='flow-label'>STEP 4｜前端展示 (Streamlit)</div>
                    展示 Bottom 商品圖、類別、花紋、顏色標籤與色塊，並顯示推薦分數/排序。
                    <div class='flow-badge'>
                        <span class='pill'>Bottom 1</span><span class='pill'>Bottom 2</span><span class='pill'>Bottom 3</span>
                        <span class='pill'>Score</span>
                    </div>
                </div>
            </div>
        </div>
        """).strip()
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
