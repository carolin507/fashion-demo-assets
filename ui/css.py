# ui/css.py

from textwrap import dedent


def load_global_css():
    return dedent("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600;700&family=Noto+Serif+TC:wght@600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
    }

    :root {
        --bg-main: #F7F5EF;
        --card-bg: #FFFFFF;
        --text-main: #3b332d;
        --text-subtle: #6f6055;
        --accent-1: #E9B78C;
        --accent-2: #E79BAF;
        --border-soft: rgba(0,0,0,0.06);
        --shadow-soft: 0 8px 20px rgba(15,15,20,0.08);
        --page-pad: min(5vw, 38px);
    }

    .stApp { background: var(--bg-main); }

    /* hide Streamlit sidebar */
    section[data-testid="stSidebar"] { display: none; }
    /* shift main width when sidebar hidden */
    div[data-testid="collapsedControl"] { display: none; }

    /* layout width */
    .main .block-container {
        max-width: 1180px;
        width: 100%;
        padding: 0 var(--page-pad) 32px;
        margin-top: 0 !important;
    }

    /* top nav built with Streamlit columns */
    /* =============================== */
/*          TOP NAVBAR            */
/* =============================== */

/* 抓 Streamlit Columns 外層容器 */
    div[data-testid="stHorizontalBlock"]:has(.topnav-left.brand) {
        position: sticky;
        top: 0;
        z-index: 999;

        width: 100%;
        padding: 12px var(--page-pad);
        margin: 0 calc(-1 * var(--page-pad)) 0;   /* ⬅ 移除底部空白（避免底色） */

        display: flex;
        align-items: center;
        justify-content: space-between;

        /* ⬅⬅ 背景改為全站主背景色 */
        background: var(--bg-main) !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* 左右 cols 的 padding 修正 */
    div[data-testid="stHorizontalBlock"]:has(.topnav-left.brand) > div[data-testid="column"] {
        padding: 0 !important;
    }

    /* ------------------------------- */
    /*            左側品牌             */
    /* ------------------------------- */

    .topnav-left.brand,
    .topnav-left.brand * {
        font-family: 'Noto Serif TC', serif !important;
        font-size: 30px !important;
        font-weight: 700 !important;
        color: #3b2d27 !important;
        line-height: 1.2 !important;
        margin: 0;
        padding: 0;
        white-space: nowrap;
    }

    /* ------------------------------- */
    /*           右側按鈕群            */
    /* ------------------------------- */

    .topnav-right {
        display: flex;
        align-items: center;
        gap: 14px;
    }

    /* 所有按鈕基礎樣式 */
    .topnav-right .stButton > button {
        padding: 10px 18px !important;
        border-radius: 999px !important;
        border: 1px solid rgba(0,0,0,0.06) !important;

        font-size: 15px;
        font-weight: 600;
        color: #3b2d27 !important;

        background: linear-gradient(120deg, #fdf7f0, #f3e7da) !important;
        box-shadow: 0 6px 15px rgba(0,0,0,0.05) !important;

        transition: transform .15s ease,
                    box-shadow .15s ease,
                    background .15s ease;
    }

    /* 次要按鈕（未選中） */
    .topnav-right [data-testid="baseButton-secondary"] {
        background: linear-gradient(120deg, #fbeff4, #f4e3ea) !important;
        color: #6c4a53 !important;
        border-color: rgba(0,0,0,0) !important;
        box-shadow: none !important;
    }

    /* 主要按鈕（當前頁） */
    .topnav-right [data-testid="baseButton-primary"] {
        background: linear-gradient(120deg, #eabf9c, #e08fa2) !important;
        color: #3a241e !important;
        border-color: rgba(224,156,164,0.35) !important;
        box-shadow: 0 8px 18px rgba(224,156,164,0.35) !important;
    }

    /* hover / active 效果 */
    .topnav-right .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 9px 18px rgba(0,0,0,0.08) !important;
    }
    .topnav-right .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 5px 12px rgba(0,0,0,0.05) !important;
    }

    
    /* cards */
    .card {
        background: var(--card-bg);
        padding: 20px 22px;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(15,15,20,0.06);
        margin-bottom: 18px;
        border:1px solid rgba(0,0,0,0.03);
    }
    .card-title {
        font-family: 'Noto Serif TC';
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 8px;
        color:var(--text-main);
    }

    /* hero banner (full-bleed) */
    .hero-wrapper {
        position: relative;
        width: 100%;
        height: 360px;
        overflow: hidden;

        border-radius: 14px;
        margin: 0 0 18px 0;

        box-shadow: var(--shadow-soft);
    }

    .hero-img {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
        display: block;
    }
    .hero-overlay {
        position:absolute;
        inset:0;
        background:linear-gradient(90deg, rgba(0,0,0,0.45), rgba(0,0,0,0.15), transparent);
        display:flex;
        align-items:center;
        padding:0 40px;
        color:#FDF8F1;
    }
    .hero-outer {
        margin-left: calc(-1 * var(--page-pad)) !important;
        margin-right: calc(-1 * var(--page-pad)) !important;
        width: calc(100% + 2 * var(--page-pad)) !important;
    }


    .hero-title { font-family:'Noto Serif TC'; font-size:30px; font-weight:700; margin-bottom:6px; }
    .hero-sub { font-size:14px; opacity:0.92; }
    .hero-btn {
        margin-top: 14px;
        display: inline-block;
        padding: 9px 22px;
        border-radius: 999px;
        background: linear-gradient(120deg, var(--accent-1), var(--accent-2));
        color: #4A362F;
        font-weight: 600;
        font-size: 14px;
        text-decoration: none;
    }

    .subtle {
        color:var(--text-subtle);
        opacity:0.9;
        font-size:13px;
        line-height:1.6;
    }

    .tag {
        background:#F1EDE5;
        padding:6px 12px;
        border-radius:999px;
        font-size:13px;
        display:inline-flex;
        align-items:center;
        gap:6px;
        color:#57493A;
    }

    .color-tag {
        background:#7a6a5a;
        padding:6px 12px;
        color:white;
        border-radius:999px;
        font-size:13px;
        font-weight:600;
    }

    .uploaded-photo {
        width:100%;
        height:clamp(320px, 50vh, 560px);
        border-radius:14px;
        border:1px solid rgba(0,0,0,0.06);
        display:block;
        object-fit:contain;
        background:#f5ede1;
        padding:12px;
    }

    .tag-row {
        display:flex;
        flex-wrap:wrap;
        gap:8px;
        align-items:center;
        margin:6px 0 10px;
    }
    .tag-label { font-weight:600; color:#3b332d; margin-right:2px; }

    /* form controls: white background for clarity */
    .stSelectbox div[data-baseweb="select"] > div {
        background:white;
        border:1px solid rgba(0,0,0,0.06);
    }
    .stFileUploader [data-testid="stFileUploadDropzone"] {
        background:white;
        border:1px dashed rgba(0,0,0,0.15);
    }

            /* trend color chips */
    .trend-row .stButton>button {
        width:100%;
        height:150px;
        border-radius:10px;
        border:1px solid rgba(0,0,0,0.15);
        box-shadow:0 10px 24px rgba(0,0,0,0.08);
        font-weight:700;
        font-size:0 !important;
        color:transparent !important;
        padding:0;
        text-align:center;
        display:block;
        letter-spacing:0;
        background:linear-gradient(180deg, var(--chip-top, #ddd) 58%, var(--chip-bottom, #fff) 58%) !important;
        transition:transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease, background 0.15s ease;
        position:relative;
        overflow:hidden;
        text-shadow:none !important;
        line-height:0 !important;
    }
    .trend-row .stButton>button * {
        font-size:0 !important;
        line-height:0 !important;
        color:transparent !important;
        text-shadow:none !important;
    }
    .trend-row .stButton>button:hover {
        transform:translateY(-2px);
        box-shadow:0 14px 28px rgba(0,0,0,0.12);
        border-color:rgba(0,0,0,0.28);
    }
    .trend-row .stButton>button[aria-label="pair_bw"] { --chip-top:#2b2b2b; --chip-bottom:#f6f6f6; }
    .trend-row .stButton>button[aria-label="pair_bg"] { --chip-top:#3f68b5; --chip-bottom:#5e8c6a; }
    .trend-row .stButton>button[aria-label="pair_mg"] { --chip-top:#e9dcc6; --chip-bottom:#5e8c6a; }
    .trend-row .stButton>button[aria-label="pair_br"] { --chip-top:#2b2b2b; --chip-bottom:#d95555; }
    .trend-row .stButton>button[aria-label="pair_cb"] { --chip-top:#7a5537; --chip-bottom:#3f68b5; }
    .trend-row .stButton>button[aria-label="pair_gb"] { --chip-top:#7d7d7d; --chip-bottom:#7aa2c4; }

/* product grid */
    .product-grid {
        display:grid;
        grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
        gap:16px;
        align-items:start;
    }
    .product-card {
        background:white;
        padding:14px;
        border-radius:16px;
        box-shadow:0 6px 14px rgba(0,0,0,0.05);
        display:flex;
        flex-direction:column;
        gap:6px;
        border:1px solid rgba(0,0,0,0.03);
    }
    .product-card img {
        width:100%;
        height:clamp(320px, 50vh, 540px);
        object-fit:contain;
        background:#f6f0e6;
        border-radius:12px;
        padding:10px;
        transition:transform 0.18s ease, box-shadow 0.18s ease;
    }
    .product-card img:hover {
        transform:scale(1.02);
        box-shadow:0 10px 24px rgba(0,0,0,0.12);
    }
    .product-card .caption {
        font-size:12px;
        color:#6a5d52;
        text-align:center;
        margin-top:4px;
    }

    /* lookbook multi-column carousel */
    .gallery-grid {
        display:grid;
        grid-template-columns:repeat(3,1fr);
        gap:14px;
    }
    .gallery-item {
        background:white;
        padding:10px;
        border-radius:14px;
        box-shadow:0 6px 14px rgba(0,0,0,0.05);
        border:1px solid rgba(0,0,0,0.03);
    }
    .gallery-item img {
        width:100%;
        height:auto;
        max-height:480px;
        object-fit:contain;
        border-radius:10px;
        display:block;
    }
    .gallery-item .caption {
        margin-top:6px;
        font-size:12px;
        color:#6a5d52;
        text-align:center;
    }
    @media (max-width: 768px) {
        .hero-wrapper { width:100%; margin:0 0 24px 0; height:260px; border-radius:0; }
        .hero-overlay { padding: 0 18px; background: linear-gradient(120deg, rgba(0,0,0,0.55), rgba(0,0,0,0.1)); }
        .hero-title { font-size:24px; }
        .look-carousel { height: 360px; }
    }
                  

    /* ========================================= */
    /*   Wardrobe mini Lookbook: 3~4 slots auto carousel   */
    /* ========================================= */


    .mini-lookbook-grid {
        display: grid;
        grid-template-columns: repeat(var(--slot-count, 3), minmax(0, 1fr));
        gap: 18px;
        margin: 12px 0 24px;
    }

    .mini-lookbook-slot {
        position: relative;
        width: 100%;
        height: 300px;
        overflow: hidden;
        border-radius: 16px;
        background: linear-gradient(160deg, #fdf7f0, #f1e6da);
        border: 1px solid var(--border-soft);
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        isolation: isolate;
        --frame: 4s;
    }

    .mini-lookbook-img {
        position: absolute;
        inset: 10px;
        width: calc(100% - 20px);
        height: calc(100% - 20px);
        object-fit: contain;
        object-position: center;
        background: #f8f3ec;
        border-radius: 12px;
        box-shadow: 0 10px 24px rgba(0,0,0,0.08);
        opacity: 0;
        animation: fadeCycle calc(var(--img-count, 1) * var(--frame, 4s)) ease-in-out infinite both;
        animation-delay: calc(-1 * var(--i, 0) * var(--frame, 4s));
    }

    .fade-img { pointer-events: none; }

    .mini-lookbook-img.first-img {
        opacity: 1;
        animation-delay: 0s;
    }

    @keyframes fadeCycle {
        0%   { opacity: 0; }
        12%  { opacity: 1; }
        70%  { opacity: 1; }
        85%  { opacity: 0; }
        100% { opacity: 0; }
    }

    @media (max-width: 1024px) {
        .mini-lookbook-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 640px) {
        .mini-lookbook-grid { grid-template-columns: 1fr; }
    }
                  
    .hero-wrapper {
        margin-left: calc(-1 * var(--page-pad)) !important;
        margin-right: calc(-1 * var(--page-pad)) !important;
        width: calc(100% + 2 * var(--page-pad)) !important;
    }
    .hero-wrapper {
        position: relative;
        width: 100%;
        height: 360px;
        overflow: hidden;

        border-radius: 18px; /* ← 真正的圓角應該放這裡 */
        box-shadow: var(--shadow-soft);
    }

        </style>
    """).strip()
