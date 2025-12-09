import streamlit as st


def render_topnav():
    labels = [
        ("AI 穿搭推薦", "wardrobe"),
        ("穿搭靈感牆", "lookbook"),
        ("色彩潮流分析", "dashboard"),
        ("CRM 客戶洞察", "crm"),
        ("銷售分析", "sales"),
        ("顧客評價分析", "reviews"),
        ("專案介紹", "intro"),
    ]

    current = st.session_state.get("page", "wardrobe")

    nav_left, nav_right = st.columns([1.2, 3], vertical_alignment="center")

    with nav_left:
        st.markdown('<div class="topnav-left brand">Lookbook Studio</div>', unsafe_allow_html=True)

    with nav_right:
        st.markdown('<div class="topnav-right">', unsafe_allow_html=True)

        btn_cols = st.columns(len(labels), gap="small")

        for (text, target), col in zip(labels, btn_cols):
            with col:
                clicked = st.button(
                    text,
                    key=f"nav_{target}",
                    type="primary" if current == target else "secondary",
                    use_container_width=True,
                )
                if clicked:
                    st.session_state.page = target
                    try:
                        st.query_params = {"page": target}
                    except Exception:
                        st.experimental_set_query_params(page=target)
                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)
