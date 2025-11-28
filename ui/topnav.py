# ui/topnav.py

import streamlit as st


def render_topnav():
    """Top navigation with Japanese pastel palette."""
    labels = [
        ("AI 穿搭示範", "wardrobe"),
        ("街拍靈感", "lookbook"),
        ("本月流行色系", "trend"),
        ("專案介紹", "intro"),
    ]

    current = st.session_state.get("page", "wardrobe")
    nav = st.container()
    with nav:
        left, right = st.columns([1, 3])
        left.markdown("<div class='brand'>Lookbook Studio</div>", unsafe_allow_html=True)
        cols = right.columns(len(labels))
        for (text, target), col in zip(labels, cols):
            btn = col.button(
                text,
                key=f"nav_{target}",
                type="primary" if current == target else "secondary",
                use_container_width=True,
            )
            if btn:
                st.session_state.page = target
                try:
                    st.query_params = {"page": target}
                except Exception:
                    try:
                        st.experimental_set_query_params(page=target)
                    except Exception:
                        pass
                st.rerun()
