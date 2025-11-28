# ui/layout.py


def card(title, body_html):
    """Wrap content in a styled card; body is stripped to avoid code blocks."""
    clean = body_html.strip()
    return (
        "<div class=\"card\">"
        f"<div class=\"card-title\">{title}</div>"
        f"{clean}"
        "</div>"
    )


def product_grid(files, base):
    items = "".join(
        (
            "<div class=\"product-card\">"
            f"<img src=\"{base}{f}\">"
            "<div class=\"caption\">精選單品</div>"
            "</div>"
        )
        for f in files
    )
    return (
        "<div class=\"card\">"
        "<div class=\"card-title\">精選單品推薦</div>"
        "<div class=\"product-grid\">"
        f"{items}"
        "</div>"
        "</div>"
    )


def lookbook_carousel(files, base):
    """Static 3-column gallery for consistent sizing."""
    items = "".join(
        (
            "<div class=\"gallery-item\">"
            f"<img src=\"{base}{f}\" alt=\"street look\">"
            "<div class=\"caption\"></div>"
            "</div>"
        )
        for f in files
    )
    return (
        "<div class=\"card\">"
        "<div class=\"card-title\">街拍 Lookbook</div>"
        "<div class=\"gallery-grid\">"
        f"{items}"
        "</div>"
        "</div>"
    )
