import streamlit as st

def render_topnav():
    labels = [
        ("AI 穿搭示範", "wardrobe"),
        ("街拍靈感", "lookbook"),
        ("本月流行色系", "trend"),
        ("專案介紹", "intro"),
    ]

    current = st.session_state.get("page", "wardrobe")

    # --- 左右欄位 ---
    nav_left, nav_right = st.columns([1.2, 3], vertical_alignment="center")

    # --- 左側品牌 ---
    with nav_left:
        st.markdown('<div class="topnav-left brand">Lookbook Studio</div>', unsafe_allow_html=True)

    # --- 右側按鈕（加入 topnav-right wrapper） ---
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
                    except:
                        st.experimental_set_query_params(page=target)
                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)
