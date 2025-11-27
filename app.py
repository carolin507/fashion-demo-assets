# app.py 
# -*- coding: utf-8 -*-
import base64
import random
import urllib.parse
from io import BytesIO

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# ------------------------------------------------------------
# Page config
# ------------------------------------------------------------
st.set_page_config(
    page_title="🪩 AI 穿搭靈感 Demo",
    layout="wide"
)

# ------------------------------------------------------------
# 全域 CSS
# ------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600;700&family=Noto+Serif+TC:wght@600;700&display=swap');

:root {
    --bg-main: #F7F5EF;
    --card-bg: #FFFFFF;
    --text-main: #333333;
    --text-subtle: #777777;
    --accent-1: #E9B78C;
    --accent-2: #E79BAF;
    --border-soft: rgba(0,0,0,0.06);
    --shadow-soft: 0 8px 20px rgba(15,15,20,0.08);
    --page-pad: min(5vw, 38px);
}

html, body, [class*="css"] {
    font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
}

.stApp {
    background: var(--bg-main);
}

.block-container {
    max-width: 1180px;
    width: 100%;
    padding: 0 var(--page-pad) 32px;
    margin-top: 0 !important;
}
/* Navbar 上方 Logo + 導覽文字（只是視覺，真正切頁由 Streamlit 做） */
.top-nav {
    width: 100%;
    padding: 14px 8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
    color: #3E3029;
    font-size: 14px;
}
.top-nav-left {
    font-family: 'Noto Serif TC';
    font-weight: 700;
    font-size: 20px;
}
.top-nav-right {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-end;
    gap: 14px;
    color: #7a6a5a;
}
.top-nav-right span { color: #7a6a5a; }

/* Hero Banner 圖片版型 A */
.hero-wrapper {
    position: relative;
    width: calc(100% + 2 * var(--page-pad));
    margin: 0 calc(-1 * var(--page-pad)) 28px;
    border-radius: 22px;
    overflow: hidden;
    box-shadow: var(--shadow-soft);
}
.hero-img {
    width: 100%;
    height: 320px;
    object-fit: cover;
    display: block;
}
.hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(90deg, rgba(0,0,0,0.45), rgba(0,0,0,0.15), transparent);
    display: flex;
    align-items: center;
    padding: 0 40px;
}
.hero-text {
    max-width: 420px;
    color: #FDF8F1;
}
.hero-title {
    font-family: 'Noto Serif TC';
    font-size: 30px;
    font-weight: 700;
    margin-bottom: 6px;
}
.hero-sub {
    font-size: 14px;
    opacity: 0.92;
}
.hero-btn {
    margin-top: 18px;
    display: inline-block;
    padding: 9px 22px;
    border-radius: 999px;
    background: linear-gradient(120deg, var(--accent-1), var(--accent-2));
    color: #4A362F;
    font-weight: 600;
    font-size: 14px;
    text-decoration: none;
}

/* 卡片 */
.card {
    background: var(--card-bg);
    padding: 20px 22px;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(15,15,20,0.06);
    margin-bottom: 16px;
}
.card-title {
    font-size: 18px;
    font-weight: 700;
    color: #3b332d;
    margin-bottom: 8px;
}
.subtle {
    font-size: 13px;
    color: var(--text-subtle);
}

/* tag 樣式 */
.tag {
    display: inline-block;
    padding: 5px 11px;
    margin: 4px 8px 0 0;
    border-radius: 999px;
    background: #F1EDE5;
    font-size: 13px;
    color: #57493A;
}
.color-tag {
    display: inline-block;
    padding: 5px 13px;
    margin: 4px 8px 0 0;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    color: #FFFFFF;
}

/* 商品卡 grid */
.grid-3 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 12px;
}
.grid-5 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 12px;
}
.prod-card {
    background: #FFFFFF;
    padding: 12px;
    border-radius: 16px;
    box-shadow: var(--shadow-soft);
    text-align: center;
    border: 1px solid rgba(0,0,0,0.03);
}
.prod-card img {
    border-radius: 12px;
    width: 100%;
    height: auto;
    transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.prod-card img:hover {
    transform: scale(1.02);
    box-shadow: 0 10px 24px rgba(0,0,0,0.12);
}

/* 行動版調整 */
@media (max-width: 768px) {
    .hero-wrapper {
        width: 100%;
        margin: 0 0 24px 0;
        border-radius: 0;
    }
    .hero-img {
        height: 260px;
    }
    .hero-overlay {
        padding: 0 18px;
        background: linear-gradient(120deg, rgba(0,0,0,0.55), rgba(0,0,0,0.1));
    }
    .hero-title { font-size: 24px; }
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# Top nav（純視覺）
# ------------------------------------------------------------
st.markdown("""
<div class="top-nav">
  <div class="top-nav-left">Lookbook Studio</div>
  <div class="top-nav-right">
    <span>AI 穿搭示範</span>
    <span>主題靈感</span>
    <span>專案介紹</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# Hero Banner - GitHub raw URL
# ------------------------------------------------------------
hero_url = "https://raw.githubusercontent.com/carolin507/fashion-demo-assets/main/hero_banner.jpg"

st.markdown(
    f"""
    <div class="hero-wrapper">
        <img src="{hero_url}" class="hero-img" />
        <div class="hero-overlay">
            <div class="hero-text">
                <div class="hero-title">AI 穿搭靈感推薦</div>
                <div class="hero-sub">
                    上傳穿搭，AI 幫你標色、圖案、品類，並推薦下半身搭配與購物靈感。
                </div>
                <a class="hero-btn" href="#upload">開始體驗</a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# Mock 標籤與映射
# ------------------------------------------------------------
pattern_labels = ["Solid", "Striped", "Floral", "Plaid", "Spotted"]

color_labels = [
    "Black", "Gray", "White", "Beige", "Orange", "Pink",
    "Red", "Green", "Brown", "Blue", "Yellow", "Purple",
]

category_labels = [
    "Top","T-Shirt","Shirt","Cardigan","Blazer","Sweatshirt",
    "Vest","Jacket","Dress","Coat","Skirt","Pants","Jeans",
    "Jumpsuit","Kimono_Yukata","Swimwear","Stockings",
]

category_to_zh = {
    "Top": "上衣", "T-Shirt": "T 恤", "Shirt": "襯衫", "Cardigan": "開襟衫",
    "Blazer": "西裝外套", "Sweatshirt": "大學T", "Vest": "背心", "Jacket": "夾克",
    "Dress": "洋裝", "Coat": "大衣", "Skirt": "裙子", "Pants": "長褲",
    "Jeans": "牛仔褲", "Jumpsuit": "連身褲", "Kimono_Yukata": "和服/浴衣",
    "Swimwear": "泳裝", "Stockings": "襪褲",
}

color_to_zh = {
    "Black": "黑色", "Gray": "灰色", "White": "白色", "Beige": "米色",
    "Orange": "橘色", "Pink": "粉色", "Red": "紅色", "Green": "綠色",
    "Brown": "咖啡色", "Blue": "藍色", "Yellow": "黃色", "Purple": "紫色",
}

pattern_to_zh = {
    "Solid": "素面", "Striped": "條紋", "Floral": "花紋",
    "Plaid": "格紋", "Spotted": "點點",
}

streetstyle_files = [
    "20170324095254453_500.jpg",
    "20170324095730988_500.jpg",
    "20170324100124006_500.jpg",
    "20170324100303683_500.jpg",
    "20170324101207506_500.jpg",
    "20170324101213181_500.jpg",
    "20170324101342210_500.jpg",
    "20170324101553293_500.jpg",
    "20170324101642714_500.jpg",
    "20170324101732000_500.jpg",
    "20170324101754087_500.jpg",
    "20170324101839553_500.jpg",
    "20170324102113466_500.jpg",
    "20170324102428957_500.jpg",
    "20170324102521935_500.jpg",
    "20170324102544688_500.jpg",
    "20170324102806575_500.jpg",
    "20170324103244682_500.jpg",
    "20170324103356507_500.jpg",
    "20170324103547162_500.jpg",
]
streetstyle_base = "https://raw.githubusercontent.com/carolin507/fashion-demo-assets/main/streetstyle/"

product_files = [
    "638992503203300000.jpg",
    "638993154193030000.jpg",
    "638993413666200000.jpg",
    "638993433208400000.jpg",
    "638993433310200000.jpg",
]
product_base = "https://raw.githubusercontent.com/carolin507/fashion-demo-assets/main/product/"


def zh_label(label, table):
    return table.get(label, label)


def mock_clip_label(image, gender):
    return {
        "color": random.choice(color_labels),
        "pattern": random.choice(pattern_labels),
        "category": random.choice(category_labels),
        "gender": gender,
    }


def mock_recommendation(color, category, gender):
    bottom_colors = {
        "Red": ["White", "Black", "Blue"],
        "White": ["Black", "Blue", "Khaki"],
        "Black": ["White", "Beige", "Denim"],
        "Blue": ["White", "Beige", "Black"],
        "Beige": ["Black", "Denim", "Brown"],
        "Gray": ["White", "Black", "Blue"],
        "Orange": ["White", "Blue", "Black"],
        "Pink": ["White", "Beige", "Blue"],
        "Green": ["White", "Beige", "Black"],
        "Brown": ["White", "Beige", "Denim"],
        "Yellow": ["White", "Blue", "Beige"],
        "Purple": ["White", "Black", "Beige"],
    }

    top_like = {
        "Top","T-Shirt","Shirt","Cardigan","Blazer",
        "Sweatshirt","Vest","Jacket","Coat",
    }
    dress_like = {"Dress","Jumpsuit","Kimono_Yukata","Swimwear"}

    if category in top_like:
        cats = ["長褲", "牛仔褲", "裙子"]
    elif category in dress_like:
        cats = ["外套", "披肩", "襪褲"]
    elif category == "Skirt":
        cats = ["上衣", "T 恤", "襯衫"]
    elif category in {"Pants", "Jeans"}:
        cats = ["上衣","T 恤","襯衫","外套"]
    else:
        cats = ["上衣","長褲"]

    return {
        "bottom_color": bottom_colors.get(color, ["Black"]),
        "bottom_category": cats,
    }


# ------------------------------------------------------------
# 1. 上傳區（在 main page，而不是 sidebar）
# ------------------------------------------------------------
st.markdown('<div id="upload"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
  <div class="card-title">STEP 1｜上傳你的穿搭照</div>
  <p class="subtle">選擇性別與穿搭照片，AI 會幫你抓出主色調與品類，並給出下身搭配靈感。</p>
</div>
""", unsafe_allow_html=True)

col_u1, col_u2 = st.columns([1, 2])
with col_u1:
    gender = st.selectbox("性別", ["female", "male", "unisex"])
with col_u2:
    uploaded_img = st.file_uploader("上傳穿搭圖片（JPG / PNG）", type=["jpg","jpeg","png"])

# ------------------------------------------------------------
# 2. 顯示辨識結果 + 圖片
# ------------------------------------------------------------
if uploaded_img:
    img = Image.open(uploaded_img)
    buf = BytesIO()
    img.save(buf, format="PNG")
    img_b64 = base64.b64encode(buf.getvalue()).decode()

    result = mock_clip_label(img, gender)

    col1, col2 = st.columns([1.1, 0.9])

    with col1:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">你的穿搭照片</div>
            <img src="data:image/png;base64,{img_b64}" style="width:100%;border-radius:14px;border:1px solid rgba(0,0,0,0.04);" />
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">AI 辨識結果（Mock）</div>
            <p><strong>顏色：</strong>{zh_label(result['color'], color_to_zh)}</p>
            <p><strong>花紋：</strong>{zh_label(result['pattern'], pattern_to_zh)}</p>
            <p><strong>品類：</strong>{zh_label(result['category'], category_to_zh)}</p>
            <p><strong>性別：</strong>{result['gender']}</p>
            <p class="subtle">※ 目前為 Demo，未串接實際模型。</p>
        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # 3. AI 建議下身搭配
    # --------------------------------------------------------
    rec = mock_recommendation(result["color"], result["category"], gender)

    color_hex = {
        "Black": "#545454","Gray": "#8d8d8d","White": "#d8d8d8",
        "Beige": "#d6c3a9","Orange": "#f2a45a","Pink": "#ef8fa7",
        "Red": "#e26c6c","Green": "#6fa96a","Brown": "#9b6c4a",
        "Blue": "#5c7fd4","Yellow": "#e0c85a","Purple": "#9a7ad6",
    }

    color_tags_html = "".join(
        f"<span class='color-tag' style='background:{color_hex.get(c, '#888')}'>{zh_label(c, color_to_zh)}</span>"
        for c in rec["bottom_color"]
    )
    cat_tags_html = "".join(f"<span class='tag'>{cat}</span>" for cat in rec["bottom_category"])

    recommended_color = rec["bottom_color"][0]
    recommended_cat = rec["bottom_category"][0]
    search_query = f"{zh_label(recommended_color, color_to_zh)} {recommended_cat}"
    google_url = f"https://www.google.com/search?tbm=shop&q={urllib.parse.quote(search_query)}"

    st.markdown(f"""
    <div class="card">
        <div class="card-title">STEP 2｜AI 建議的下身搭配方向</div>
        <p class="subtle">依據上身顏色 / 品類產出下身搭配顏色與類別，方便你直接逛街或網購。</p>
        <div style="margin-top:8px;">
            <strong>建議下身顏色：</strong> {color_tags_html}
        </div>
        <div style="margin-top:8px;">
            <strong>建議下身類別：</strong> {cat_tags_html}
        </div>
        <a href="{google_url}" target="_blank" style="margin-top:14px;display:inline-block;" class="hero-btn">
            前往 Google 購物查看相近單品
        </a>
    </div>
    """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # 類似商品示意
    # --------------------------------------------------------
    
    prod_samples = random.sample(product_files, k=3) if len(product_files) >= 3 else list(product_files)
    prod_items_html = "".join(
        f"<div class='prod-card-inline'>"
        f"<img src='{product_base + img}' alt='product inspiration' />"
        f"<div class='caption'>靈感商品</div>"
        f"</div>"
        for img in prod_samples
    )
    prod_html = f'''
    <div class="card">
        <div class="card-title">相似單品推薦</div>
        <div class="product-grid">{prod_items_html}</div>
    </div>
    <style>
    .product-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 12px;
        align-items: start;
    }}
    .prod-card-inline {{
        background: #ffffff;
        border-radius: 12px;
        padding: 10px;
        box-shadow: 0 6px 14px rgba(0,0,0,0.05);
        border: 1px solid rgba(0,0,0,0.04);
    }}
    .prod-card-inline img {{
        width: 100%;
        height: auto;
        max-height: 520px;
        border-radius: 10px;
        display: block;
        object-fit: contain;
        background: #f9f6ef;
    }}
    .prod-card-inline .caption {{
        margin-top: 6px;
        font-size: 13px;
        color: #6f6055;
        text-align: center;
    }}
    @media (max-width: 640px) {{
        .product-grid {{ grid-template-columns: repeat(1, minmax(0, 1fr)); }}
    }}
    </style>
    '''
    components.html(prod_html, height=760, scrolling=True)
    
    # --------------------------------------------------------
    # 街拍 Lookbook 輪播（直式）
    # --------------------------------------------------------
    carousel_imgs = random.sample(streetstyle_files, k=min(9, len(streetstyle_files))) if len(streetstyle_files) >= 3 else list(streetstyle_files)
    columns = [[], [], []]
    for idx, img in enumerate(carousel_imgs):
        columns[idx % 3].append(img)
    for i in range(3):
        if not columns[i]:
            columns[i] = carousel_imgs

    def build_slides(imgs, base_delay):
        return "".join(
            f"<div class='slide' style='animation-delay:{base_delay + idx*3.5}s'><img src='{streetstyle_base + img}' /></div>"
            for idx, img in enumerate(imgs)
        )

    col_slides = [build_slides(columns[i], i * 1.2) for i in range(3)]
    carousel_html = f'''
    <div class="card">
        <div class="card-title">街拍靈感 Lookbook</div>
        <div class="look-grid">
            <div class="look-carousel">{col_slides[0]}</div>
            <div class="look-carousel">{col_slides[1]}</div>
            <div class="look-carousel">{col_slides[2]}</div>
        </div>
    </div>
    <style>
    .look-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 14px;
    }}
    .look-carousel {{
        position: relative;
        height: 520px;
        overflow: hidden;
        border-radius: 16px;
        background: #f7f5ef;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .look-carousel .slide {{
        position: absolute;
        inset: 0;
        opacity: 0;
        transition: opacity 0.6s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 12px;
        box-sizing: border-box;
    }}
    .look-carousel .slide:first-child {{ opacity: 1; }}
    .look-carousel .slide {{
        animation: lookSwap 12s infinite;
    }}
    @keyframes lookSwap {{
        0% {{ opacity: 1; }}
        40% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
        100% {{ opacity: 0; }}
    }}
    .look-carousel img {{
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        border-radius: 14px;
        box-shadow: 0 10px 24px rgba(0,0,0,0.08);
        background: #ffffff;
    }}
    </style>
    '''
    components.html(carousel_html, height=620)
    
    
else:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h3 style="font-family:'Noto Serif TC'; margin-bottom:6px;">準備開始體驗 AI 穿搭靈感了嗎？</h3>
        <p class="subtle">在上方選擇性別並上傳一張穿搭照，系統會自動分析顏色與品類，並給你下一步靈感。</p>
    </div>
    """, unsafe_allow_html=True)

