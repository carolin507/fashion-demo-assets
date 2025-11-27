# -*- coding: utf-8 -*-
import random

import streamlit as st

st.set_page_config(page_title="街頭穿搭直擊", layout="wide")

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
"""
)

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


def pseudo_tags(filename: str):
    seed = sum(ord(c) for c in filename)
    genders = ["female", "male", "unisex"]
    colors = ["黑", "白", "米色", "藍", "綠", "棕", "灰", "粉"]
    return {
        "gender": genders[seed % len(genders)],
        "top_color": colors[seed % len(colors)],
        "bottom_color": colors[(seed // 3) % len(colors)],
    }


st.markdown("## 街頭穿搭直擊")
st.markdown("依性別與色彩快速篩選街拍靈感。下方圖片與標籤為示意標註。")

gender_choice = st.selectbox("性別", ["全部", "female", "male", "unisex"], key="gender_filter")
top_choice = st.selectbox("上衣色彩", ["全部", "黑", "白", "米色", "藍", "綠", "棕", "灰", "粉"], key="top_filter")
bottom_choice = st.selectbox("下著色彩", ["全部", "黑", "白", "米色", "藍", "綠", "棕", "灰", "粉"], key="bottom_filter")

filtered = []
for img in streetstyle_files:
    tags = pseudo_tags(img)
    if gender_choice != "全部" and tags["gender"] != gender_choice:
        continue
    if top_choice != "全部" and tags["top_color"] != top_choice:
        continue
    if bottom_choice != "全部" and tags["bottom_color"] != bottom_choice:
        continue
    filtered.append((img, tags))

if not filtered:
    st.info("沒有符合條件的穿搭，請調整篩選條件試試。")
else:
    cols = st.columns(3)
    for idx, (img, tags) in enumerate(filtered):
        with cols[idx % 3]:
            st.markdown(
                f"""
                <div class="card">
                  <img src="{streetstyle_base + img}" style="width:100%;border-radius:14px;" />
                  <p class="subtle" style="margin-top:6px;">
                    性別：{tags['gender']}｜上衣：{tags['top_color']}｜下著：{tags['bottom_color']}
                  </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
