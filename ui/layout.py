# ui/layout.py

def hero_banner(url):
    return f"""
    <div class="hero-wrapper">
        <img src="{url}" class="hero-img" />
        <div class="hero-overlay">
            <div class="hero-text">
                <div class="hero-title">AI 穿搭靈感推薦</div>
                <div class="hero-sub">上傳穿搭，AI 協助辨識顏色與品類，並推薦下身搭配靈感。</div>
                <a class="hero-btn" href="#upload">開始體驗</a>
            </div>
        </div>
    </div>
    """


def card(title, body_html):
    return f"""
    <div class="card">
        <div class="card-title">{title}</div>
        {body_html}
    </div>
    """


def product_grid(images, base_url):
    items = "".join(
        f"""
        <div class='prod-card-inline'>
            <img src='{base_url}{img}'/>
            <div class='caption'>靈感商品</div>
        </div>
        """ for img in images
    )

    return f"""
    <div class="card">
        <div class="card-title">相似單品推薦</div>
        <div class="product-grid">{items}</div>
    </div>
    """


def lookbook_carousel(imgs, base):
    slides = "".join(
        f"<div class='slide'><img src='{base}{img}'/></div>"
        for img in imgs
    )

    return f"""
    <div class="card">
        <div class="card-title">街拍靈感 Lookbook</div>
        <div class="look-carousel">{slides}</div>
    </div>
    """
