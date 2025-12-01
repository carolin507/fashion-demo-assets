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

    /* top nav */
    .topnav {
        position: sticky;
        top: 0;
        z-index: 999;
        background: linear-gradient(120deg, #fefbf8, #f4e9dc);
        padding: 12px 16px;
        border-bottom: 1px solid #eadfce;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 8px 22px rgba(0,0,0,0.05);
    }
    .topnav .brand {
        font-family:'Noto Serif TC';
        font-size:23px;
        font-weight:700;
        color:#3b2d27;
        letter-spacing:0.5px;
    }
    .topnav .nav-group { display:flex; gap:12px; }
    .topnav .stButton>button {
        padding:10px 16px;
        border-radius:999px;
        border:1px solid rgba(58,44,33,0.06);
        color:#3b2d27;
        background:linear-gradient(120deg, #fdf7f0, #f3e7da);
        box-shadow:0 6px 15px rgba(0,0,0,0.05);
        font-weight:600;
        transition:transform 0.14s ease, box-shadow 0.14s ease, background 0.14s ease;
    }
    .topnav [data-testid="baseButton-secondary"] {
        background:linear-gradient(120deg, #f9f2e9, #f4ebe0);
        color:#5b4a3f;
    }
    .topnav [data-testid="baseButton-primary"] {
        background:linear-gradient(120deg, #eabf9c, #e08fa2);
        color:#3a241e;
        box-shadow:0 8px 18px rgba(224,156,164,0.35);
        border:1px solid rgba(224,156,164,0.35);
    }
    .topnav .stButton>button:hover { transform:translateY(-1px); box-shadow:0 9px 18px rgba(0,0,0,0.08); }
    .topnav .stButton>button:active { transform:translateY(0); box-shadow:0 5px 12px rgba(0,0,0,0.05); }

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
        width: calc(100vw);   /* 滿版 */
        margin-left: calc(-1 * var(--page-pad));  
        margin-right: calc(-1 * var(--page-pad)); 
        margin-top: 0;
        margin-bottom: 18px;

        height: 360px;
        overflow: hidden;

        border-radius: 0;  /* full-bleed 通常不保留圓角，可以保留也行 */
        box-shadow: none;  /* 可依需求 */
    }
    .hero-img {
        width:100%;
        height:100%;
        object-fit:cover;
        display:block;
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
    .trend-row .stButton>button,
    .stButton>button[aria-label="黑色"],
    .stButton>button[aria-label="白色"],
    .stButton>button[aria-label="米色"],
    .stButton>button[aria-label="藍色"],
    .stButton>button[aria-label="綠色"],
    .stButton>button[aria-label="紅色"] {
        width:100%;
        height:120px;
        border-radius:14px;
        border:1px solid rgba(0,0,0,0.08);
        box-shadow:0 8px 18px rgba(0,0,0,0.08);
        font-weight:700;
        font-size:14px;
        color:#3b2d27;
    }
    .stButton>button[aria-label="黑色"] { background:#2b2b2b; color:#ffffff; }
    .stButton>button[aria-label="白色"] { background:#f6f6f6; color:#3b2d27; }
    .stButton>button[aria-label="米色"] { background:#e9dcc6; color:#3b2d27; }
    .stButton>button[aria-label="藍色"] { background:#3f68b5; color:#ffffff; }
    .stButton>button[aria-label="綠色"] { background:#5e8c6a; color:#ffffff; }
    .stButton>button[aria-label="紅色"] { background:#d95555; color:#ffffff; }

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
        height:260px;
        object-fit:cover;
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
    </style>
    """).strip()
