# -*- coding: utf-8 -*-
import base64
import random
import urllib.parse
from io import BytesIO

import streamlit as st
from PIL import Image

# ----------------------------------
# Streamlit page config
# ----------------------------------
st.set_page_config(page_title="🪩 AI 穿搭靈感 Demo", layout="wide")

# ----------------------------------
# Custom CSS：淺色奶油雜誌風
# ----------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600;700&family=Noto+Serif+TC:wght@600;700&display=swap');

/* 色票設定 */
:root {
    --bg-main: #F7F5EF;      /* 奶油米色背景 */
    --card-bg: #FFFFFF;      /* 卡片白底 */
    --text-main: #333333;    /* 主要文字 */
    --text-subtle: #777777;  /* 次要文字 */
    --accent-1: #E9B78C;     /* 奶油金 */
    --accent-2: #E79BAF;     /* 淡粉金 */
    --border-soft: rgba(0,0,0,0.04);
    --shadow-soft: 0 8px 20px rgba(15,15,20,0.06);
}

/* 全域字體 */
html, body {
    font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
}

/* App 背景 */
.stApp {
    background: var(--bg-main);
}

/* 主要容器寬度 & 文字顏色 */
.block-container {
    max-width: 1120px;
    padding-top: 18px;
    padding-bottom: 32px;
    color: var(--text-main);
}

/* Sidebar 淺色風格 */
section[data-testid="stSidebar"] {
    background: #FFFFFF !important;
    border-right: 1px solid rgba(0,0,0,0.05) !important;
    box-shadow: inset -4px 0 12px rgba(0,0,0,0.03);
}

section[data-testid="stSidebar"] * {
    color: #444444 !important;
    font-weight: 500;
}

section[data-testid="stSidebar"] h2 {
    font-size: 20px !important;
    font-weight: 700 !important;
    margin-bottom: 8px;
}

/* 頂部 Banner：淺色雜誌感 */
.top-banner {
    width: 100%;
    padding: 40px 32px 32px 32px;
    border-radius: 20px;
    background: radial-gradient(circle at 0% 0%, #FDF8EC 0%, transparent 50%),
                radial-gradient(circle at 100% 0%, #FCE9F1 0%, transparent 55%),
                #FBF7F0;
    border: 1px solid var(--border-soft);
    box-shadow: 0 10px 26px rgba(0,0,0,0.06);
    text-align: center;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}

.top-banner .eyebrow {
    font-size: 12px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #A38A6B;
    margin-bottom: 6px;
}

.top-banner h1 {
    font-family: 'Noto Serif TC', 'Noto Sans TC', serif;
    font-weight: 800;
    font-size: 32px;
    margin-bottom: 8px;
    color: #3E3029;
}

.top-banner .subtitle {
    font-size: 15px;
    color: var(--text-subtle);
}

.hero-chips {
    margin-top: 10px;
    display: flex;
    gap: 8px;
    justify-content: center;
    flex-wrap: wrap;
}

.pill {
    padding: 6px 12px;
    border-radius: 999px;
    background: #F2ECE3;
    border: 1px solid rgba(0,0,0,0.04);
    font-size: 12px;
    color: #5A4B3D;
}

/* 卡片樣式：白底 + 柔和陰影，沒有醜框框 */
.card {
    background: var(--card-bg);
    padding: 20px 22px;
    border-radius: 16px;
    border: none;
    box-shadow: var(--shadow-soft);
    margin-bottom: 16px;
}

.image-card {
    /* 可以稍微帶一點底色差異 */
    background: #FFFFFF;
}

.result-card {
    background: #FFFBF4;
}

.section-card {
    background: #FFFFFF;
}

/* 分隔線：很淡 */
.divider {
    height: 1px;
    width: 100%;
    margin: 18px 0;
    background: linear-gradient(90deg, transparent, rgba(0,0,0,0.08), transparent);
}

/* Tags */
.tag {
    display: inline-block;
    padding: 6px 12px;
    margin: 6px 8px 0 0;
    border-radius: 999px;
    background: #F1EDE5;
    font-size: 13px;
    color: #57493A;
}

.color-tag {
    display: inline-block;
    padding: 6px 14px;
    margin: 6px 8px 0 0;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    color: #FFFFFF;
}

/* 圖片：圓角 + 柔和陰影 */
img {
    border-radius: 12px !important;
    border: 1px solid rgba(0,0,0,0.03);
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
}

img:hover {
    transform: scale(1.01);
    box-shadow: 0 10px 24px rgba(0,0,0,0.10);
}

/* 按鈕：奶油粉漸層 */
.stButton>button,
.stLinkButton>button {
    background: linear-gradient(120deg, var(--accent-1), var(--accent-2)) !important;
    color: #4A362F !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    padding: 10px 20px !important;
    border-radius: 999px !important;
    border: none !important;
    box-shadow: 0 8px 18px rgba(0,0,0,0.12);
}

.stButton>button:hover,
.stLinkButton>button:hover {
    filter: brightness(1.03);
    box-shadow: 0 10px 22px rgba(0,0,0,0.16);
}

.link-btn {
    display: inline-block;
    text-decoration: none;
    background: linear-gradient(120deg, var(--accent-1), var(--accent-2));
    color: #4A362F;
    font-weight: 600;
    font-size: 14px;
    padding: 10px 20px;
    border-radius: 999px;
    box-shadow: 0 8px 18px rgba(0,0,0,0.12);
    border: 1px solid rgba(0,0,0,0.06);
}

.link-btn:hover {
    filter: brightness(1.03);
    box-shadow: 0 10px 22px rgba(0,0,0,0.16);
}

/* Empty state */
.empty-state h3 {
    font-family: 'Noto Serif TC', 'Noto Sans TC', serif;
    font-size: 20px;
    color: var(--text-main);
}

.empty-state p,
.subtle {
    color: var(--text-subtle);
    font-size: 14px;
}

.card-title {
    font-size: 18px;
    font-weight: 700;
    color: #3b332d;
    margin-bottom: 10px;
}

.tag-row {
    margin-top: 6px;
    margin-bottom: 10px;
}

.grid-3,
.grid-5 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 12px;
}

.grid-5 {
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
}

.grid-item img {
    width: 100%;
    height: auto;
}

.grid-caption {
    margin-top: 6px;
    font-size: 12px;
    color: #6f6055;
    text-align: center;
}

.full-img {
    width: 100%;
    height: auto;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Mock labels and mapping
# ----------------------------

pattern_labels = ["Solid", "Striped", "Floral", "Plaid", "Spotted"]

color_labels = [
    "Black",
    "Gray",
    "White",
    "Beige",
    "Orange",
    "Pink",
    "Red",
    "Green",
    "Brown",
    "Blue",
    "Yellow",
    "Purple",
]

category_labels = [
    "Top",
    "T-Shirt",
    "Shirt",
    "Cardigan",
    "Blazer",
    "Sweatshirt",
    "Vest",
    "Jacket",
    "Dress",
    "Coat",
    "Skirt",
    "Pants",
    "Jeans",
    "Jumpsuit",
    "Kimono_Yukata",
    "Swimwear",
    "Stockings",
]

category_to_zh = {
    "Top": "上衣",
    "T-Shirt": "T 恤",
    "Shirt": "襯衫",
    "Cardigan": "開襟衫",
    "Blazer": "西裝外套",
    "Sweatshirt": "大學T",
    "Vest": "背心",
    "Jacket": "夾克",
    "Dress": "洋裝",
    "Coat": "大衣",
    "Skirt": "裙子",
    "Pants": "長褲",
    "Jeans": "牛仔褲",
    "Jumpsuit": "連身褲",
    "Kimono_Yukata": "和服/浴衣",
    "Swimwear": "泳裝",
    "Stockings": "襪褲",
}

color_to_zh = {
    "Black": "黑色",
    "Gray": "灰色",
    "White": "白色",
    "Beige": "米色",
    "Orange": "橘色",
    "Pink": "粉色",
    "Red": "紅色",
    "Green": "綠色",
    "Brown": "咖啡色",
    "Blue": "藍色",
    "Yellow": "黃色",
    "Purple": "紫色",
}

pattern_to_zh = {
    "Solid": "素面",
    "Striped": "條紋",
    "Floral": "花紋",
    "Plaid": "格紋",
    "Spotted": "點點",
}

# Demo 圖庫
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


def mock_clip_label(image, gender):
    """回傳隨機的顏色 / 花紋 / 類別（Mock）"""
    color = random.choice(color_labels)
    pattern = random.choice(pattern_labels)
    category = random.choice(category_labels)
    return {
        "color": color,
        "pattern": pattern,
        "category": category,
        "gender": gender,
    }


def mock_recommendation(color, category, gender):
    """根據上身顏色與類別，給出簡單下身搭配建議（Mock 規則）"""
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
        "Top", "T-Shirt", "Shirt", "Cardigan",
        "Blazer", "Sweatshirt", "Vest", "Jacket", "Coat",
    }
    dress_like = {"Dress", "Jumpsuit", "Kimono_Yukata", "Swimwear"}

    if category in top_like:
        bottom_cats = ["長褲", "牛仔褲", "裙子"]
    elif category in dress_like:
        bottom_cats = ["外套", "披肩", "襪褲"]
    elif category == "Skirt":
        bottom_cats = ["上衣", "T 恤", "襯衫"]
    elif category in {"Pants", "Jeans"}:
        bottom_cats = ["上衣", "T 恤", "襯衫", "外套"]
    else:
        bottom_cats = ["上衣", "長褲"]

    return {
        "bottom_color": bottom_colors.get(color, ["Black"]),
        "bottom_category": bottom_cats,
    }


def image_to_base64(pil_image):
    """Convert PIL image to base64 string for inline HTML."""
    buffer = BytesIO()
    pil_image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()


def zh_label(label, table):
    """英文標籤對應中文，若無對應則回傳原值"""
    return table.get(label, label)


# ----------------------------

# ----------------------------
# UI：頂部 Banner
# ----------------------------
st.markdown("""
<div class="top-banner">
    <div class="eyebrow">Lookbook Studio</div>
    <h1> AI 穿搭靈感工作室</h1>
    <p class="subtitle">上傳穿搭照，AI 即刻給出配色、品類與街拍靈感，讓日常穿搭更精緻。</p>
    <div class="hero-chips">
        <span class="pill">智能配色</span>
        <span class="pill">下身品類建議</span>
        <span class="pill">街拍 / 單品靈感</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.header("設定")

    gender = st.selectbox("性別", ["female", "male", "unisex"])

    uploaded_img = st.file_uploader("上傳圖片", type=["jpg", "jpeg", "png"])

    st.info("※ 目前為 Demo 模式，模型結果為 mock 範例。")

# ----------------------------
# Main
# ----------------------------
if uploaded_img:
    img = Image.open(uploaded_img)
    img_b64 = image_to_base64(img)

    col1, col2 = st.columns([1.05, 0.95])

    with col1:
        col1.markdown(
            f"""
            <div class="card image-card">
                <div class="card-title">上傳的穿搭</div>
                <img class="full-img" src="data:image/png;base64,{img_b64}" alt="uploaded outfit" />
            </div>
            """,
            unsafe_allow_html=True,
        )

    result = mock_clip_label(img, gender)
    result_html = f"""
    <div class="card result-card">
        <div class="card-title">AI 辨識結果（Mock）</div>
        <p><strong>顏色：</strong>{zh_label(result['color'], color_to_zh)}</p>
        <p><strong>花紋：</strong>{zh_label(result['pattern'], pattern_to_zh)}</p>
        <p><strong>類別：</strong>{zh_label(result['category'], category_to_zh)}</p>
        <p><strong>性別：</strong>{result['gender']}</p>
    </div>
    """
    with col2:
        col2.markdown(result_html, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    color_hex = {
        "Black": "#545454",
        "Gray": "#8d8d8d",
        "White": "#d8d8d8",
        "Beige": "#d6c3a9",
        "Orange": "#f2a45a",
        "Pink": "#ef8fa7",
        "Red": "#e26c6c",
        "Green": "#6fa96a",
        "Brown": "#9b6c4a",
        "Blue": "#5c7fd4",
        "Yellow": "#e0c85a",
        "Purple": "#9a7ad6",
    }

    rec = mock_recommendation(result["color"], result["category"], gender)

    color_tags_html = "".join(
        f"<span class='color-tag' style='background:{color_hex.get(c, '#888')}'>{zh_label(c, color_to_zh)}</span>"
        for c in rec["bottom_color"]
    )
    cat_tags_html = "".join(f"<span class='tag'>{cat}</span>" for cat in rec["bottom_category"])

    recommended_color = rec["bottom_color"][0]
    recommended_cat = rec["bottom_category"][0]
    search_query = f"{zh_label(recommended_color, color_to_zh)} {recommended_cat}"
    google_url = f"https://www.google.com/search?tbm=shop&q={urllib.parse.quote(search_query)}"

    st.markdown(
        f"""
        <div class="card section-card">
            <div class="card-title">AI 建議下身搭配</div>
            <div class="subtle">以上身顏色與類別推估下身搭配，並列出推薦色彩標籤方便挑選。</div>
            <div class="tag-row"><strong>建議下身顏色：</strong>{color_tags_html}</div>
            <div class="tag-row"><strong>建議下身類別：</strong>{cat_tags_html}</div>
            <div class="tag-row" style="margin-top: 10px;">
                <a class="link-btn" href="{google_url}" target="_blank" rel="noopener">前往 Google 購物</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    prod_samples = random.sample(product_files, k=min(3, len(product_files)))
    prod_cards = "".join(
        f"<div class='grid-item'><img src='{product_base + img_name}' alt='{img_name}' /><div class='grid-caption'>{img_name}</div></div>"
        for img_name in prod_samples
    )
    st.markdown(
        f"""
        <div class="card section-card">
            <div class="card-title">類似商品範例（Demo 庫）</div>
            <div class="grid-3">{prod_cards}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    sample_imgs = random.sample(streetstyle_files, k=min(5, len(streetstyle_files)))
    street_cards = "".join(
        f"<div class='grid-item'><img src='{streetstyle_base + img_name}' alt='{img_name}' /></div>"
        for img_name in sample_imgs
    )
    st.markdown(
        f"""
        <div class="card section-card">
            <div class="card-title">街拍靈感範例（Demo 庫）</div>
            <div class="grid-5">{street_cards}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

else:
    st.markdown(
        """
        <div class="card section-card empty-state">
            <h3>準備好讓 AI 幫你搭配今天的穿搭了嗎？</h3>
            <p class="subtle">在左側上傳一張穿搭照，立即獲得配色、品類與街拍靈感，讓日常造型更精緻。</p>
            <div class="hero-chips" style="margin-top: 10px;">
                <span class="pill">配色建議</span>
                <span class="pill">下身搭配建議</span>
                <span class="pill">街拍範例</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
