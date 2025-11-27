# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(page_title="專案介紹", layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
body, [class*="css"] {
    font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
}
.card {
    background: #ffffff;
    padding: 16px 18px;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    margin-bottom: 16px;
}
.card-title {
    font-size: 18px;
    font-weight: 700;
    color: #3b332d;
    margin-bottom: 8px;
}
.subtle { font-size: 13px; color: #777; }
</style>
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
  <a href="https://fashion-demo-assets-homepage.streamlit.app/">
    <span class="icon">🌟</span>AI 穿搭靈感推薦
  </a>
  <a href="https://fashion-demo-assets-lookbook.streamlit.app/">
    <span class="icon">📸</span>街頭穿搭直擊
  </a>
  <a href="https://fashion-demo-assets-trend-color.streamlit.app/">
    <span class="icon">🎨</span>本月流行色系
  </a>
  <a href="https://fashion-demo-assets-project.streamlit.app/">
    <span class="icon">💡</span>專案介紹
  </a>
</div>
""", unsafe_allow_html=True)


st.markdown("## 專案介紹")
st.markdown(
    """
<div class="card">
  <div class="card-title">Lookbook Studio</div>
  <p>以 AI 輔助穿搭靈感的示意專案，提供上傳分析、街拍篩選、流行色系展示與專案說明。可依未來需求接入真實模型或資料庫。</p>
  <ul>
    <li><strong>AI 穿搭靈感推薦</strong>（app.py）：上傳照片，取得 Mock 的顏色 / 品項分析與下身搭配建議、靈感商品卡片。</li>
    <li><strong>街頭穿搭直擊</strong>（lookbook.py）：依性別、上衣色彩、下著色彩篩選街拍示意圖。</li>
    <li><strong>本月流行色系</strong>（trend_color.py）：選擇主題色，瀏覽同色系街拍示意。</li>
  </ul>
  <p class="subtle">以上內容皆為 Demo。</p>
</div>
""",
    unsafe_allow_html=True,
)
