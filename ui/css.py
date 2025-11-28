def load_global_css():
       return """
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
       position: sticky;
       top: 0;
       z-index: 999;
       background: #ffffff;
       border-bottom: 1px solid var(--border-soft);
       box-shadow: 0 4px 12px rgba(0,0,0,0.04);
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
       position: relative !important;
       width: 100vw !important;
       margin-left: calc(50% - 50vw) !important;
       margin-right: calc(50% - 50vw) !important;
       height: 360px !important;
       overflow: hidden !important;
       box-shadow: var(--shadow-soft) !important;
       }

       .hero-img {
       width: 100% !important;
       height: 100% !important;
       object-fit: cover !important;
       display: block !important;
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

       /* Hide legacy top nav; using sidebar navigation instead */
       .top-nav { display: none !important; }
       </style>
       """