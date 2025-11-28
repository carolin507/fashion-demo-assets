# pages/color_trends.py

import streamlit as st
from ui.layout import card


def render_color_trends():
    """本月流行色系｜SPA"""

    st.markdown(card(
        "本月流行色系",
        """
        <p class='subtle'>
            根據全球街拍資料與穿搭標籤，統整本月最常出現的顏色趨勢。
            未來可串接 PyTrends 或流行色資料庫，動態更新色彩熱度。
        </p>
        """
    ), unsafe_allow_html=True)

    colors = {
        "奶油白 (#F2ECE4)": "#F2ECE4",
        "焦糖棕 (#A47551)": "#A47551",
        "霧藍灰 (#9AA5B1)": "#9AA5B1",
        "莓果粉 (#D56A8C)": "#D56A8C",
        "薄荷綠 (#A6C8A9)": "#A6C8A9",
    }

    blocks = "".join(
        f"""
        <div style="
            width:140px;
            height:140px;
            background:{v};
            border-radius:16px;
            display:flex;
            align-items:flex-end;
            padding:8px;
            font-size:12px;
            color:#3b332d;
            box-shadow:0 6px 16px rgba(0,0,0,0.06);
        ">{k}</div>
        """
        for k, v in colors.items()
    )

    st.markdown(card(
        "熱門色卡 Hot Colors",
        f"""
        <div style="display:flex;gap:12px;flex-wrap:wrap;">
            {blocks}
        </div>
        """
    ), unsafe_allow_html=True)
