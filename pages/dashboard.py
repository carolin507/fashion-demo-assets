# pages/color_trends.py

import streamlit as st
import pandas as pd
from textwrap import dedent
from ui.layout import card


def _mock_trend_data():
    # month, gender, top, bottom, outfits, clicks (mocked)
    return [
        {"month": "2024-08", "gender": "female", "top": "米色", "bottom": "卡其", "outfits": 120, "clicks": 340},
        {"month": "2024-08", "gender": "female", "top": "酒紅", "bottom": "米色", "outfits": 90, "clicks": 280},
        {"month": "2024-08", "gender": "male", "top": "藍色", "bottom": "黑色", "outfits": 150, "clicks": 360},
        {"month": "2024-08", "gender": "unisex", "top": "黑色", "bottom": "黑色", "outfits": 110, "clicks": 310},
        {"month": "2024-09", "gender": "female", "top": "粉色", "bottom": "藍色", "outfits": 130, "clicks": 420},
        {"month": "2024-09", "gender": "male", "top": "軍綠", "bottom": "卡其", "outfits": 95, "clicks": 240},
        {"month": "2024-09", "gender": "unisex", "top": "白色", "bottom": "黑色", "outfits": 140, "clicks": 390},
        {"month": "2024-10", "gender": "female", "top": "焦糖", "bottom": "棕色", "outfits": 160, "clicks": 450},
        {"month": "2024-10", "gender": "male", "top": "灰色", "bottom": "深藍", "outfits": 125, "clicks": 280},
        {"month": "2024-10", "gender": "unisex", "top": "黑色", "bottom": "米色", "outfits": 105, "clicks": 260},
    ]


def _aggregate_by_pair(records):
    bucket = {}
    for r in records:
        key = f"{r['top']}/{r['bottom']}"
        if key not in bucket:
            bucket[key] = {"pair": key, "outfits": 0, "clicks": 0}
        bucket[key]["outfits"] += r["outfits"]
        bucket[key]["clicks"] += r["clicks"]
    return list(bucket.values())


def _aggregate_by_top(records):
    bucket = {}
    for r in records:
        key = r["top"]
        if key not in bucket:
            bucket[key] = {"color": key, "outfits": 0, "clicks": 0}
        bucket[key]["outfits"] += r["outfits"]
        bucket[key]["clicks"] += r["clicks"]
    return list(bucket.values())


def render_color_trends():
    """商業趨勢報表 Demo"""

    st.markdown(dedent("""
    <style>
    .kpi-row { display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:10px; margin:6px 0 14px; }
    .kpi-card { background:#fff; border:1px solid rgba(0,0,0,0.05); border-radius:12px; padding:14px; box-shadow:0 8px 20px rgba(0,0,0,0.06); }
    .kpi-card .label { color:#6f6055; font-size:12px; margin-bottom:4px; }
    .kpi-card .value { font-weight:800; font-size:22px; color:#3b332d; }
    </style>
    """), unsafe_allow_html=True)

    st.markdown(card(
        "本月流行色系｜商業趨勢 Demo",
        dedent("""
        <p class='subtle'>
            使用虛構資料示範：依月份 / 性別 / 上身色 / 下身色篩選，檢視各色系的穿搭人數與點擊表現。
            未接上真實資料前，此頁為 demo 版例展示。
        </p>
        """).strip()
    ), unsafe_allow_html=True)


    data = _mock_trend_data()

    months = sorted({d["month"] for d in data})
    genders = ["全部", "female", "male", "unisex"]
    top_colors = sorted({d["top"] for d in data})
    bottom_colors = sorted({d["bottom"] for d in data})

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        sel_month = st.selectbox("月份", ["全部"] + months)
    with col2:
        sel_gender = st.selectbox("性別", genders)
    with col3:
        sel_top = st.selectbox("上身顏色", ["全部"] + top_colors)
    with col4:
        sel_bottom = st.selectbox("下身顏色", ["全部"] + bottom_colors)

    filtered = [
        d for d in data
        if (sel_month == "全部" or d["month"] == sel_month)
        and (sel_gender == "全部" or d["gender"] == sel_gender)
        and (sel_top == "全部" or d["top"] == sel_top)
        and (sel_bottom == "全部" or d["bottom"] == sel_bottom)
    ]

    if not filtered:
        st.info("目前條件下沒有資料 (demo)。")
        return

    total_outfits = sum(d["outfits"] for d in filtered)
    total_clicks = sum(d["clicks"] for d in filtered)

    st.markdown("<div class='kpi-row'>" +
                f"<div class='kpi-card'><div class='label'>穿搭人數 (demo)</div><div class='value'>{total_outfits:,}</div></div>" +
                f"<div class='kpi-card'><div class='label'>點擊次數 (demo)</div><div class='value'>{total_clicks:,}</div></div>" +
                "</div>", unsafe_allow_html=True)

    pair_rows = _aggregate_by_pair(filtered)
    top_rows = _aggregate_by_top(filtered)

    pair_df = pd.DataFrame(pair_rows)
    top_df = pd.DataFrame(top_rows)

    st.markdown(card(
        "色彩搭配表現 (上/下身組合)",
        pair_df.to_html(index=False, escape=False)
    ), unsafe_allow_html=True)

    st.markdown(card(
        "色彩趨勢圖 (demo)",
        "<p class='subtle'>左: 組合穿搭人數 / 右: 上身色點擊數</p>"
    ), unsafe_allow_html=True)

    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        if not pair_df.empty:
            st.bar_chart(pair_df.set_index("pair")["outfits"])
    with chart_col2:
        if not top_df.empty:
            st.bar_chart(top_df.set_index("color")["clicks"])

    st.markdown(card(
        "原始明細 (demo 資料)",
        pd.DataFrame(filtered).to_html(index=False, escape=False)
    ), unsafe_allow_html=True)
