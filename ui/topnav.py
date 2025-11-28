# ui/topnav.py

import streamlit as st

def inject_nav_js():
    """注入 JS：讓 top-nav 的按鈕可以切換 Streamlit multipage（SPA 模式）"""
    st.markdown("""
    <script>
    function go(page){
        window.parent.postMessage({type: "streamlit:setPage", page: page}, "*");
    }
    </script>
    """, unsafe_allow_html=True)

def render_topnav():
    """右上四個按鈕（Lookbook / Trend / Intro）"""

    st.markdown("""
    <div style="
        position:sticky; top:0; z-index:999;
        background:white;
        padding:14px 10px;
        border-bottom:1px solid #eee;
        display:flex; justify-content:space-between;
    ">
        <div style="font-family:'Noto Serif TC';font-size:20px;font-weight:700;">
            Lookbook Studio
        </div>

        <div style="display:flex; gap:12px;">
            <button onclick="go('wardrobe')" class="navbtn">AI 穿搭示範</button>
            <button onclick="go('lookbook')" class="navbtn">街拍靈感</button>
            <button onclick="go('trend')" class="navbtn">本月流行色系</button>
            <button onclick="go('intro')" class="navbtn">專案介紹</button>
        </div>
    </div>

    <style>
    .navbtn {
        padding:7px 16px;
        background:#f6f2eb;
        border:1px solid rgba(0,0,0,0.05);
        border-radius:999px;
        cursor:pointer;
        font-size:13px;
    }
    .navbtn:hover {
        background:#eaddd2;
    }
    </style>
    """, unsafe_allow_html=True)
