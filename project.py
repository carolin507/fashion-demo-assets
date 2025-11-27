# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(page_title="專案介紹", layout="wide")

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

st.sidebar.markdown("### Lookbook Studio")
st.sidebar.markdown(
    """
- AI 穿搭靈感推薦
- 街頭穿搭直擊
- 本月流行色系
- 專案介紹
""")

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
  <p class="subtle">以上內容皆為 Demo；上線前可替換為真實資料來源與模型結果。</p>
</div>
""",
    unsafe_allow_html=True,
)
