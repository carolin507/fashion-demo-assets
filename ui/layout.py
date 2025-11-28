# ui/layout.py

def card(title, body_html):
    return f"""
    <div class="card">
        <div class="card-title">{title}</div>
        {body_html}
    </div>
    """

def product_grid(files, base):
    items = "".join(
        f"""
        <div style="
            background:white;
            padding:12px;
            border-radius:16px;
            box-shadow:0 6px 14px rgba(0,0,0,0.05);
        ">
            <img src="{base + f}" style="width:100%;border-radius:12px;">
            <div style="font-size:12px;color:#6a5d52; text-align:center;margin-top:4px;">
                靈感單品
            </div>
        </div>
        """
        for f in files
    )

    return f"""
    <div class="card">
        <div class="card-title">相似單品推薦</div>
        <div style="
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
            gap:12px;">
            {items}
        </div>
    </div>
    """

def lookbook_carousel(files, base):
    slides = "".join(
        f"""
        <div class="slide">
            <img src="{base + f}">
        </div>
        """
        for f in files
    )

    return f"""
    <div class="card">
        <div class="card-title">街拍 Lookbook</div>
        <div class="look-container">
            {slides}
        </div>
    </div>

    <style>
    .look-container {{
        height:520px;
        position:relative;
        overflow:hidden;
    }}
    .slide {{
        position:absolute;
        inset:0;
        opacity:0;
        animation:fade 12s infinite;
        display:flex;
        align-items:center;
        justify-content:center;
        padding:12px;
    }}
    .slide img {{
        max-width:100%;
        max-height:100%;
        border-radius:16px;
    }}
    @keyframes fade {{
        0% {{ opacity:1; }}
        40% {{ opacity:1; }}
        50% {{ opacity:0; }}
        100% {{ opacity:0; }}
    }}
    </style>
    """
