# pages/color_trends.py

import streamlit as st
from textwrap import dedent
from ui.layout import card


def _streetstyle_dataset():
    return [
        {"file": "20170324095254453_500.jpg", "top": "\u9ed1\u8272", "bottom": "\u7070\u8272"},
        {"file": "20170324095730988_500.jpg", "top": "\u767d\u8272", "bottom": "\u7da0\u8272"},
        {"file": "20170324100124006_500.jpg", "top": "\u5361\u5176", "bottom": "\u5361\u5176"},
        {"file": "20170324100303683_500.jpg", "top": "\u85cd\u8272", "bottom": "\u9ed1\u8272"},
        {"file": "20170324101207506_500.jpg", "top": "\u5496\u5561\u8272", "bottom": "\u5496\u5561\u8272"},
        {"file": "20170324101213181_500.jpg", "top": "\u85cd\u8272", "bottom": "\u767d\u8272"},
        {"file": "20170324101342210_500.jpg", "top": "\u7da0\u8272", "bottom": "\u5361\u5176"},
        {"file": "20170324101553293_500.jpg", "top": "\u85cd\u8272", "bottom": "\u85cd\u8272"},
        {"file": "20170324101642714_500.jpg", "top": "\u9ed1\u8272", "bottom": "\u68d5\u8272"},
        {"file": "20170324101732000_500.jpg", "top": "\u85cd\u8272", "bottom": "\u9ed1\u8272"},
        {"file": "20170324101754087_500.jpg", "top": "\u7c73\u8272", "bottom": "\u7c73\u8272"},
        {"file": "20170324101839553_500.jpg", "top": "\u7d05\u8272", "bottom": "\u9ed1\u8272"},
        {"file": "20170324102113466_500.jpg", "top": "\u7c73\u8272", "bottom": "\u9ed1\u8272"},
        {"file": "20170324102428957_500.jpg", "top": "\u767d\u8272", "bottom": "\u85cd\u8272"},
        {"file": "20170324102521935_500.jpg", "top": "\u7c73\u8272", "bottom": "\u7da0\u8272"},
        {"file": "20170324102544688_500.jpg", "top": "\u767d\u8272", "bottom": "\u5361\u5176"},
        {"file": "20170324102806575_500.jpg", "top": "\u5361\u5176", "bottom": "\u9ed1\u8272"},
        {"file": "20170324103244682_500.jpg", "top": "\u9ed1\u8272", "bottom": "\u9ed1\u8272"},
        {"file": "20170324103356507_500.jpg", "top": "\u85cd\u8272", "bottom": "\u5496\u5561\u8272"},
        {"file": "20170324103547162_500.jpg", "top": "\u7da0\u8272", "bottom": "\u9ed1\u8272"},
    ]


def render_color_trends():
    """\u6d41\u884c\u8272\u7cfb\u5b50\u9801 (SPA)"""

    st.markdown(card(
        "\u6d41\u884c\u8272\u7cfb",
        dedent("""
        <p class='subtle'>
            \u76f4\u63a5\u9ede\u9078\u96d9\u8272\u584a\uff0c\u5e36\u5165\u8fd1\u671f\u71b1\u9580\u8272\u5f69\u642d\u914d\uff0c\u5feb\u901f\u700f\u89bd\u5c0d\u61c9\u8857\u62cd\u3002
        </p>
        """).strip()
    ), unsafe_allow_html=True)

    data = _streetstyle_dataset()
    palette = [
        ("pair_bw", "\u9ed1+\u767d", ("\u9ed1\u8272", "\u767d\u8272"), "#2b2b2b", "#f6f6f6"),
        ("pair_bg", "\u85cd+\u7da0", ("\u85cd\u8272", "\u7da0\u8272"), "#3f68b5", "#5e8c6a"),
        ("pair_mg", "\u7c73+\u7da0", ("\u7c73\u8272", "\u7da0\u8272"), "#e9dcc6", "#5e8c6a"),
        ("pair_br", "\u9ed1+\u7d05", ("\u9ed1\u8272", "\u7d05\u8272"), "#2b2b2b", "#d95555"),
        ("pair_cb", "\u5496+\u85cd", ("\u5496\u5561\u8272", "\u85cd\u8272"), "#7a5537", "#3f68b5"),
        ("pair_gb", "\u7070+\u85cd", ("\u7070\u8272", "\u85cd\u8272"), "#7d7d7d", "#7aa2c4"),
    ]

    st.markdown("<div class='trend-row'>", unsafe_allow_html=True)
    cols = st.columns(len(palette))
    choice = st.session_state.get("trend_color_choice")
    pair_map = {slug: set(colors) for slug, _, colors, *_ in palette}

    for (slug, display, _, top_hex, bottom_hex), col in zip(palette, cols):
        with col:
            if st.button(slug, key=f"trend_{slug}", help=display):
                choice = slug
                st.session_state["trend_color_choice"] = slug
        st.markdown(
            f"<style>.trend-row .stButton button[aria-label='{slug}']"
            f"{{--chip-top:{top_hex};--chip-bottom:{bottom_hex};}}</style>",
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

    if not choice:
        st.info("\u8acb\u9ede\u9078\u4efb\u4e00\u96d9\u8272\u584a\uff0c\u770b\u770b\u71b1\u9580\u642d\u914d\u3002")
        return

    selected_colors = pair_map.get(choice, set())
    base = (
        "https://raw.githubusercontent.com/carolin507/"
        "fashion-demo-assets/main/assets/streetstyle/"
    )

    filtered = [
        d for d in data
        if d["top"] in selected_colors or d["bottom"] in selected_colors
    ]

    if not filtered:
        st.info("\u9019\u7d44\u8272\u5f69\u642d\u914d\u66ab\u6642\u6c92\u6709\u8857\u62cd\u7167\u7247\uff0c\u63db\u500b\u7d44\u5408\u518d\u8a66\u8a66\u3002")
        return

    html_items = "".join(
        f"""
<div class=\"gallery-item\">
<img src=\"{base + item['file']}\" alt=\"street look\">
<div class=\"caption\">\u4e0a\u8863\uff1a{item['top']} | \u4e0b\u8eab\uff1a{item['bottom']}</div>
</div>"""
        for item in filtered
    )

    st.markdown(f"""
<div class=\"gallery-grid\">
{html_items}
</div>
""", unsafe_allow_html=True)
