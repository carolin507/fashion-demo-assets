# -*- coding: utf-8 -*-
import random

import streamlit as st

st.set_page_config(page_title="本月流行色系", layout="wide")

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
    "20170324101732000_500.jpg",
    "20170324101754087_500.jpg",
    "20170324101839553_500.jpg",
    "20170324102113466_500.jpg",
    "20170324102428957_500.jpg",
    "20170324102521935_500.jpg",
    "20170324102544688_500.jpg",
    "20170324102806575_500.jpg",
    "20170324103244682_500.jpg",
    "20170324103356507_500.jpg",
    "20170324103547162_500.jpg",
]
streetstyle_base = "https://raw.githubusercontent.com/carolin507/fashion-demo-assets/main/streetstyle/"

palette = [
    ("拿鐵米", "#d6c4a1"),
    ("灰霧藍", "#8aa4c2"),
    ("奶油粉", "#f2c7c1"),
    ("煙燻綠", "#8aa58a"),
]

st.markdown("## 本月流行色系")
st.markdown("選擇主題色，快速瀏覽同色系街拍靈感（示意資料）。")

color_names = [p[0] for p in palette]
pick = st.selectbox("選擇主題色", color_names, key="trend_pick")

st.markdown(
    f"""
    <div class="card">
      <div class="card-title">{pick} 配色靈感</div>
      <div style="display:flex;gap:10px;align-items:center;margin-bottom:10px;">
        {''.join(f"<div style='width:46px;height:46px;border-radius:12px;background:{h};border:1px solid rgba(0,0,0,0.08);'></div>" for _, h in palette)}
      </div>
      <p class="subtle">下方為示意街拍組合，可依需求換成真實資料。</p>
    </div>
    """,
    unsafe_allow_html=True,
)

picks = random.sample(streetstyle_files, k=min(6, len(streetstyle_files)))
cols = st.columns(3)
for idx, img in enumerate(picks):
    with cols[idx % 3]:
        st.markdown(
            f"""
            <div class="card">
              <img src="{streetstyle_base + img}" style="width:100%;border-radius:14px;" />
              <p class="subtle" style="margin-top:6px;">主色：{pick}｜搭配色：{random.choice(color_names)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
