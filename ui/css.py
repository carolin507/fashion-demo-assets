# ui/css.py

def load_global_css():
    return """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600&family=Noto+Serif+TC:wght@600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans TC', sans-serif;
    }

    :root {
        --bg-main: #F7F5EF;
        --card-bg: #FFFFFF;
        --accent-1: #E9B78C;
        --accent-2: #E79BAF;
    }

    .stApp {
        background: var(--bg-main);
    }

    .card {
        background: var(--card-bg);
        padding: 20px 22px;
        border-radius: 16px;
        box-shadow: 0 8px 20px rgba(15,15,20,0.06);
        margin-bottom: 18px;
    }

    .card-title {
        font-family: 'Noto Serif TC';
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 8px;
        color:#3b332d;
    }

    /* hero banner */
    .hero-wrapper {
        width:100%;
        height:360px;
        overflow:hidden;
        border-radius:14px;
        position:relative;
        margin-bottom:22px;
    }

    .hero-img {
        width:100%;
        height:100%;
        object-fit:cover;
    }

    .hero-overlay {
        position:absolute;
        inset:0;
        background:linear-gradient(90deg, rgba(0,0,0,0.45), transparent);
        display:flex;
        align-items:center;
        padding-left:38px;
        color:white;
    }

    .hero-title {
        font-family:'Noto Serif TC';
        font-size:30px;
        font-weight:700;
    }
    .hero-sub {
        font-size:14px;
        opacity:0.92;
    }

    .tag {
        background:#F1EDE5;
        padding:6px 12px;
        border-radius:999px;
        font-size:13px;
    }

    .color-tag {
        background:#7a6a5a;
        padding:6px 12px;
        color:white;
        border-radius:999px;
        font-size:13px;
    }

    .hero-btn {
        background:linear-gradient(120deg, var(--accent-1), var(--accent-2));
        padding:8px 22px;
        border-radius:999px;
        color:#4a362f;
        display:inline-block;
        text-decoration:none;
        font-weight:600;
        margin-top:12px;
    }

    </style>
    """
