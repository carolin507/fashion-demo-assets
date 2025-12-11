# pages/lookbook.py

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import streamlit as st

from ui.layout import card


DATA_PATH = Path("data/verified_photo_data.json")
IMG_BASE = (
    "https://raw.githubusercontent.com/carolin507/"
    "fashion-demo-assets/main/assets/streetstyle/"
)

# 繁中顯示字典
GENDER_ZH = {"women": "女生", "men": "男生"}
CATEGORY_ZH = {
    "Top": "上衣", "T-Shirt": "T 恤", "Shirt": "襯衫", "Cardigan": "開襟衫",
    "Blazer": "西裝外套", "Sweatshirt": "大學 T", "Vest": "背心", "Jacket": "外套",
    "Dress": "洋裝", "Coat": "大衣", "Skirt": "裙子", "Pants": "長褲",
    "Jeans": "牛仔褲", "Jumpsuit": "連身褲", "Kimono_Yukata": "和服/浴衣",
    "Swimwear": "泳裝", "Stockings": "襪類",
}
COLOR_ZH = {
    "Black": "黑色", "Gray": "灰色", "White": "白色", "Beige": "米色",
    "Orange": "橘色", "Pink": "粉紅色", "Red": "紅色", "Green": "綠色",
    "Brown": "咖啡色", "Blue": "藍色", "Yellow": "黃色", "Purple": "紫色",
}
COLOR_HEX = {
    "Black": "#161616",
    "Gray": "#7f7f7f",
    "White": "#f5f5f5",
    "Beige": "#d9c7b1",
    "Orange": "#e67a2e",
    "Pink": "#e88abf",
    "Red": "#d64541",
    "Green": "#4a8c64",
    "Brown": "#7b4b32",
    "Blue": "#3f68b5",
    "Yellow": "#d3a018",
    "Purple": "#7d5fb2",
}
LIGHT_COLORS = {"White", "Beige", "Yellow", "Pink", "Orange"}


@st.cache_data
def load_lookbook_data() -> List[Dict[str, Any]]:
    """Load verified streetstyle data."""
    if not DATA_PATH.exists():
        st.error(f"無法找到資料檔案：{DATA_PATH}")
        return []
    try:
        with DATA_PATH.open(encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"載入 Lookbook 資料失敗：{e}")
        return []


def _options_from(values) -> List[str]:
    return ["全部"] + sorted({v for v in values if v})

def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    return tuple(int(h[idx:idx+2], 16) for idx in (0, 2, 4))



def _filter_data(
    data: List[Dict[str, Any]],
    gender: str,
    category: str,
    top_color: str,
    bottom_color: str,
) -> List[Dict[str, Any]]:
    def match_gender(item: Dict[str, Any]) -> bool:
        return gender == "全部" or item.get("gender") == gender

    def match_category(item: Dict[str, Any]) -> bool:
        if category == "全部":
            return True
        for part_key in ("top", "bottom"):
            part: Optional[Dict[str, Any]] = item.get(part_key) or {}
            if part.get("category") == category:
                return True
        return False

    def match_color(item: Dict[str, Any], part_key: str, selected: str) -> bool:
        if selected == "全部":
            return True
        part: Optional[Dict[str, Any]] = item.get(part_key) or {}
        return part.get("color") == selected

    return [
        d for d in data
        if match_gender(d)
        and match_category(d)
        and match_color(d, "top", top_color)
        and match_color(d, "bottom", bottom_color)
    ]


def render_lookbook():
    """Lookbook page: show verified streetstyle photos with filters."""

    st.markdown(card(
        "潮流 Lookbook",
        "<p class='subtle'>串接 verified_photo_data.json，依性別 / 品類 / 上下身顏色快速瀏覽街拍穿搭。</p>"
    ), unsafe_allow_html=True)

    data = load_lookbook_data()
    if not data:
        return

    genders = _options_from(d.get("gender") for d in data)
    categories = _options_from(
        part.get("category")
        for d in data
        for part in (d.get("top") or {}, d.get("bottom") or {})
        if isinstance(part, dict)
    )
    top_colors = _options_from(
        (d.get("top") or {}).get("color")
        for d in data
        if isinstance(d.get("top"), dict)
    )
    bottom_colors = _options_from(
        (d.get("bottom") or {}).get("color")
        for d in data
        if isinstance(d.get("bottom"), dict)
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        gender = st.selectbox(
            "性別", genders, format_func=lambda g: "全部" if g == "全部" else GENDER_ZH.get(g, g)
        )
    with c2:
        category = st.selectbox(
            "品類", categories, format_func=lambda c: "全部" if c == "全部" else CATEGORY_ZH.get(c, c)
        )
    with c3:
        top_color = st.selectbox(
            "上身顏色", top_colors, format_func=lambda c: "全部" if c == "全部" else COLOR_ZH.get(c, c)
        )
    with c4:
        bottom_color = st.selectbox(
            "下身顏色", bottom_colors, format_func=lambda c: "全部" if c == "全部" else COLOR_ZH.get(c, c)
        )

    filtered = _filter_data(data, gender, category, top_color, bottom_color)

    if not filtered:
        st.info("沒有符合條件的穿搭，換個條件試試吧！")
        return

    def _color_chip(color: str) -> str:
        color_hex = COLOR_HEX.get(color, "#7a6a5a")
        r, g, b = _hex_to_rgb(color_hex)
        alpha = 0.2 if color in LIGHT_COLORS else 0.16
        bg = f"rgba({r},{g},{b},{alpha})"
        text_color = "#2f241e"
        color_zh = COLOR_ZH.get(color, color or "-")
        return (
            f'<span class="lookbook-chip" style="--chip-color:{color_hex}; --chip-bg:{bg}; --chip-fg:{text_color};">'
            f'<span class="chip-dot"></span>{color_zh}'
            "</span>"
        )

    def _part_label(part: Dict[str, Any]) -> str:
        if not isinstance(part, dict):
            return "-"
        cat = part.get("category", "-")
        color = part.get("color", "-")
        cat_zh = CATEGORY_ZH.get(cat, cat)
        color_zh = COLOR_ZH.get(color, color)
        color_chip = _color_chip(color) if color != "-" else color_zh
        return f"{cat_zh} · {color_chip}"

    html_items = "".join(
        f"""
<div class="gallery-item">
  <img src="{IMG_BASE + item['filename']}" alt="street look">
  <div class="caption">
    性別：{GENDER_ZH.get(item.get('gender', ''), item.get('gender', '-'))}｜上身：{_part_label(item.get('top'))}｜下身：{_part_label(item.get('bottom'))}
  </div>
</div>"""
        for item in filtered
    )

    st.markdown(f"""
<div class="gallery-grid">
{html_items}
</div>
""", unsafe_allow_html=True)
