# pages/project_intro.py

import streamlit as st
from textwrap import dedent


def render_project_intro():
    """Product-style landing page for Lookbook Studio."""

    base = "https://raw.githubusercontent.com/carolin507/fashion-demo-assets/main/assets/intro"
    street_base = "https://raw.githubusercontent.com/carolin507/fashion-demo-assets/main/assets/streetstyle"
    st.markdown(
        dedent(
            """
            <style>
            :root { --bg-main:#f8f6f2; --card-bg:#ffffff; }
            .intro-shell { display:flex; flex-direction:column; gap:32px; }
            .intro-section { background:var(--card-bg); border-radius:20px; padding:28px 28px 26px;
                             box-shadow:0 12px 30px rgba(55,80,140,0.08); border:1px solid rgba(0,0,0,0.03); }
            .hero-intro { position:relative; overflow:hidden; border-radius:22px; min-height:360px;
                          color:#f7f9ff; box-shadow:0 18px 40px rgba(55,80,140,0.16); }
            .hero-bg { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }
            .hero-mask { position:absolute; inset:0; background:linear-gradient(115deg, rgba(0,0,0,0.6), rgba(0,0,0,0.25)); }
            .hero-content { position:relative; z-index:1; padding:42px; max-width:760px; display:flex; flex-direction:column; gap:16px; color:#f7f9ff; }
            .eyebrow { display:inline-flex; gap:8px; align-items:center; background:rgba(255,255,255,0.78);
                       padding:8px 14px; border-radius:999px; font-weight:700; letter-spacing:0.4px; color:#25315b; }
            .hero-title { font-family:'Noto Serif TC', serif; font-size:36px; margin:0; line-height:1.2; color:#f7f9ff; }
            .hero-sub { font-size:15px; opacity:0.98; line-height:1.8; color:#f4f7ff; }
            .hero-cta { display:flex; flex-wrap:wrap; gap:12px; align-items:center; }
            .btn-primary { display:inline-flex; align-items:center; gap:8px; padding:12px 20px; border-radius:999px;
                           background:linear-gradient(120deg, #ffb7a3, #ff9f9a); color:#3b2423; font-weight:800;
                           text-decoration:none; box-shadow:0 14px 30px rgba(120,60,60,0.18); }
            .btn-secondary { display:inline-flex; align-items:center; gap:8px; padding:10px 16px; border-radius:999px;
                             background:linear-gradient(120deg, #f4f1ed, #ebe7e3); color:#3c3432; font-weight:700;
                             border:1px solid rgba(80,70,70,0.18); text-decoration:none; box-shadow:0 8px 18px rgba(90,70,70,0.10); }
            .btn-mini { padding:6px 10px; font-size:12px; box-shadow:0 6px 12px rgba(90,70,70,0.10); }
            .btn-secondary:hover, .btn-primary:hover { transform:translateY(-1px); }
            .hero-note { font-size:13px; opacity:0.95; color:#e7ecff; }
            .pill-grid { display:grid; gap:12px; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); }
            .pill { padding:14px 16px; border-radius:14px; background:linear-gradient(140deg, #f5f7ff, #fbf9ff); border:1px solid rgba(0,0,0,0.04); box-shadow:0 8px 20px rgba(45,90,180,0.06); }
            .pill strong { display:block; font-size:15px; margin-bottom:6px; color:#2e2a48; }
            .pill span { color:#4c455b; font-size:13px; line-height:1.6; }
            .section-title { font-family:'Noto Serif TC', serif; font-size:22px; margin:0 0 8px; color:#2b263f; }
            .section-sub { color:#5a5363; margin:0 0 16px; font-size:14px; line-height:1.7; }
            .two-col { display:grid; grid-template-columns:1.05fr 1fr; gap:20px; align-items:center; }
            .two-col.reverse { grid-template-columns:1fr 1.05fr; }
            .feature-list { margin:10px 0 0 0; padding-left:18px; color:#3e3848; line-height:1.7; }
            .feature-list li { margin-bottom:8px; }
            .tagline { background:#eef3ff; color:#1f2f5a; padding:16px 18px; border-radius:14px; line-height:1.7; box-shadow:inset 0 1px 0 rgba(255,255,255,0.7); }
            .image-frame { width:100%; border-radius:16px; overflow:hidden; background:#f8f9ff; box-shadow:0 14px 32px rgba(45,90,180,0.10); border:1px solid rgba(45,90,180,0.10); }
            .image-frame img { width:100%; display:block; }
            .stat-hero { background:linear-gradient(120deg,#ffd7c8,#f6e6df); border-radius:18px; padding:24px; box-shadow:0 16px 36px rgba(120,70,60,0.14); color:#2f2523; }
            .stat-hero h3 { margin:0 0 6px; font-size:22px; color:#2f2523; }
            .stat-hero p { margin:0 0 14px; color:#463b39; opacity:0.9; }
            .stat-row { display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:14px; align-items:center; }
            .stat-item { display:flex; flex-direction:column; gap:4px; align-items:flex-start; }
            .stat-num { font-size:40px; font-weight:800; color:#2c1f1e; line-height:1; }
            .stat-label { font-size:14px; color:#433836; }
            .stat-cta { margin-top:12px; }
            .stat-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:12px; }
            .stat-card { background:linear-gradient(135deg, #f7e7e1, #f2ece9); color:#2f2a28; border-radius:14px; padding:16px 16px 18px; box-shadow:0 14px 34px rgba(120,70,60,0.10); }
            .stat-card h4 { margin:0 0 6px; font-size:16px; }
            .stat-card p { margin:0; color:#4a3f3e; line-height:1.6; font-size:13px; }
            .lookbook-inline { display:grid; grid-template-columns:1fr 1.1fr; gap:18px; align-items:center; }
            .lookbook-carousel { position:relative; width:100%; height:320px; border-radius:16px; overflow:hidden; background:#fbf7f5; box-shadow:0 12px 26px rgba(120,70,60,0.1); border:1px solid rgba(0,0,0,0.05); }
            .lookbook-carousel img { position:absolute; inset:10px; width:calc(100% - 20px); height:calc(100% - 20px); object-fit:contain; object-position:center; background:#fbf7f5; border-radius:12px; opacity:0; animation:fadeShow 18s infinite; }
            .lookbook-carousel img:nth-child(1) { animation-delay:0s; }
            .lookbook-carousel img:nth-child(2) { animation-delay:6s; }
            .lookbook-carousel img:nth-child(3) { animation-delay:12s; }
            @keyframes fadeShow {
                0% { opacity:0; }
                10% { opacity:1; }
                40% { opacity:1; }
                55% { opacity:0; }
                100% { opacity:0; }
            }
            .module-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:12px; }
            .module-card { border-radius:14px; padding:14px; background:linear-gradient(145deg,#f0f4ff,#faf7ff); border:1px solid rgba(0,0,0,0.04); box-shadow:0 10px 26px rgba(45,90,180,0.08); }
            .module-card h4 { margin:0 0 8px; font-size:15px; color:#2b263f; }
            .module-card p, .module-card ul { margin:0; color:#3b3547; font-size:13px; line-height:1.6; padding-left:0; }
            .mini-modules { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:10px; margin-top:12px; }
            .mini-card { background:#f7f8ff; border-radius:12px; padding:12px; border:1px solid rgba(0,0,0,0.04); box-shadow:0 8px 20px rgba(45,90,180,0.06); }
            .mini-card h5 { margin:0 0 6px; font-size:14px; color:#2b263f; }
            .mini-card ul { margin:0; padding-left:16px; color:#3b3547; line-height:1.6; font-size:13px; }
            .usecase-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:12px; }
            .usecase-card { border-radius:14px; padding:14px; background:#fff7f0; color:#3a2720; border:1px solid rgba(0,0,0,0.05); box-shadow:0 12px 28px rgba(120,70,40,0.08); }
            .usecase-card h4 { margin:0 0 6px; font-size:16px; }
            .usecase-card ul { margin:0; padding-left:18px; line-height:1.7; color:#4a372f; }
            .tech-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:12px; }
            .tech-card { background:#fff4ec; color:#3a2720; border-radius:14px; padding:14px; border:1px solid rgba(0,0,0,0.05); box-shadow:0 12px 30px rgba(120,70,40,0.08); }
            .tech-card h4 { margin:0 0 8px; font-size:15px; }
            .tech-card ul { margin:0; padding-left:18px; line-height:1.7; color:#4a372f; }
            .cta-block { display:grid; grid-template-columns:1fr 0.9fr; gap:16px; align-items:center; background:linear-gradient(135deg,#ffe9d6,#ffd1b8); color:#3a2720; padding:20px; border-radius:18px; box-shadow:0 14px 34px rgba(120,70,40,0.12); }
            .cta-text h3 { margin:0 0 8px; font-size:22px; }
            .cta-text p { margin:0 0 14px; line-height:1.7; }
            .cta-img { width:100%; border-radius:14px; overflow:hidden; border:1px solid rgba(120,70,40,0.16); }
            .cta-img img { width:100%; display:block; }
            .bi-hero { display:grid; grid-template-columns:1.05fr 1fr; gap:18px; align-items:center; }
            .bi-copy h3 { margin:0 0 8px; font-size:20px; color:#3a2720; }
            .bi-copy p { margin:0 0 12px; color:#5a463c; line-height:1.7; }
            .bi-points { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:10px; }
            .bi-point { background:#fffaf6; border-radius:12px; padding:10px 12px; border:1px solid rgba(0,0,0,0.04); box-shadow:0 8px 20px rgba(120,70,40,0.06); }
            .bi-point h5 { margin:0 0 6px; font-size:14px; color:#3a2720; }
            .bi-point ul { margin:0; padding-left:16px; color:#4a372f; line-height:1.6; font-size:13px; }
            .tilted-frame { position:relative; width:100%; padding:12px; background:linear-gradient(135deg,#e9ecf5,#f8f9ff); border-radius:18px; box-shadow:0 16px 32px rgba(0,0,0,0.12); }
            .tilted-frame::after { content:""; position:absolute; inset:10px -10px -12px 18px; background:#2f4a80; border-radius:16px; z-index:0; transform:skew(-4deg); opacity:0.9; }
            .tilted-inner { position:relative; z-index:1; border-radius:14px; overflow:hidden; background:white; box-shadow:0 10px 26px rgba(0,0,0,0.12); }
            .tilted-inner img { width:100%; display:block; }
            @media (max-width: 900px) {
                .two-col, .cta-block, .lookbook-inline { grid-template-columns:1fr; }
                .hero-content { padding:26px; }
                .hero-title { font-size:28px; }
                .lookbook-carousel { height:280px; }
            }
            </style>
            """
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        dedent(
            f"""
            <div class="intro-shell">
              <section class="hero-intro">
                <img src="{base}/7776aec2089baec3783e19ac6f7f2c9a.jpg" class="hero-bg" alt="hero background">
                <div class="hero-mask"></div>
                <div class="hero-content">
                  <div class="eyebrow">Lookbook Studio · AI 穿搭體驗</div>
                  <h1 class="hero-title">AI 解析穿搭，打造個人化靈感推薦</h1>
                  <p class="hero-sub">
                    結合 Body Segmentation、CLIP 時尚理解模型與穿搭大數據，顧客只要「上傳一張照片」，
                    就能獲得專屬色彩分析、穿搭解析與商品推薦，讓電商從被動陳列進化成主動理解顧客的購物體驗。
                  </p>
                  <div class="hero-cta">
                    <a class="btn-primary" href="?page=wardrobe">立即體驗 Lookbook Studio Demo</a>
                    <span class="hero-note">即時解析＋個人化推薦 → 提升轉換與回購</span>
                  </div>
                </div>
              </section>

              <section class="intro-section">
                <h2 class="section-title">為何電商需要 AI 穿搭推薦？（2025–2026 服飾電商洞察）</h2>
                <p class="section-sub">個人化、以圖搜圖、內容成本三股趨勢正同時發生，AI 是最直接的解法。</p>
                <div class="stat-hero">
                  <h3>AI 時代的服飾電商關鍵數字</h3>
                  <p>顧客期待更快、更個人化，並轉向圖片作為入口；同時拍攝成本逐年上升。</p>
                  <div class="stat-row">
                    <div class="stat-item">
                      <div class="stat-num">76%</div>
                      <div class="stat-label">願意購買個人化推薦商品（McKinsey State of Fashion 2025）</div>
                      <a class="btn-secondary btn-mini" href="https://www.mckinsey.com/industries/retail/our-insights/state-of-fashion" style="margin-top:6px;">了解更多</a>
                    </div>
                    <div class="stat-item">
                      <div class="stat-num">40%</div>
                      <div class="stat-label">預計以「圖片」開啟購物旅程（Google Visual Search Insights）</div>
                      <a class="btn-secondary btn-mini" href="https://www.thinkwithgoogle.com/consumer-insights/consumer-trends/visual-search-shopping/" style="margin-top:6px;">了解更多</a>
                    </div>
                    <div class="stat-item">
                      <div class="stat-num">15–20%</div>
                      <div class="stat-label">品牌拍攝成本年增（Shopify / Deloitte 2024–2025）</div>
                      <a class="btn-secondary btn-mini" href="https://www.deloittedigital.com/nl/en/insights/perspective/marketing-trends-2025.html" style="margin-top:6px;">了解更多</a>
                    </div>
                  </div>
                </div>
              </section>

              <section class="intro-section two-col">
                <div>
                  <h3 class="section-title">AI 解析穿搭：顏色、花紋、品類一次完成。</h3>
                  <p class="section-sub">上傳穿搭照，Lookbook Studio 自動產生結構化標籤，為後續推薦與營運決策鋪路。</p>
                  <ul class="feature-list">
                    <li><strong>辨識內容：</strong>顏色（主色 / 輔色）、花紋（Solid / Striped / Floral / Plaid / Spotted）、服飾類別（Top / Shirt / Jacket / Pants / Skirt…）、穿搭部位（上身 / 下身）。</li>
                    <li><strong>技術能力：</strong>Body Segmentation、CLIP 時尚語意辨識、KMeans 色彩量化。</li>
                    <li class="tagline">Demo：上傳一張照片，立即得到顏色 / 花紋 / 類別標籤，並可同步看到色票。</li>
                  </ul>
                  <div style="margin-top:12px;">
                    <a class="btn-secondary" href="?page=wardrobe">前往 AI 解析與推薦 Demo</a>
                  </div>
                </div>
                <div class="image-frame">
                  <img src="{base}/64cfd0c6d3768d39b77b7495_maskingClothes.png" alt="body segmentation and color readout">
                </div>
              </section>

              <section class="intro-section two-col reverse">
                <div class="image-frame">
                  <img src="{base}/73ead4d5-aa17-4c9d-9b1e-f57c4cd73bd8_outfit-recom-flow.png" alt="outfit recommendation flow">
                </div>
                <div>
                  <h3 class="section-title">AI 共現推薦引擎：從數萬筆搭配資料找到最適合你的 Look。</h3>
                  <p class="section-sub">共現矩陣挖掘全球街拍，找出最常與你穿搭一起出現的下身組合，回傳真實街拍影像作為參照。</p>
                  <ul class="feature-list">
                    <li><strong>推薦引擎基礎：</strong>分析上衣 color-pattern-category 與下身搭配的統計規律，提供 Top-K 下身色系與風格。</li>
                    <li><strong>使用者會看到：</strong>依照片生成的搭配建議、下身常見色系，搭配 Streetstyle 參照圖。</li>
                  </ul>
                  <div class="tagline">品牌可即時提供「個人化穿搭與色彩推薦」，提升互動、降低決策門檻。</div>
                  <div style="margin-top:12px;">
                    <a class="btn-secondary" href="?page=lookbook">查看更多街拍參照</a>
                  </div>
                </div>
              </section>

              <section class="intro-section">
                <h3 class="section-title">Lookbook 靈感牆｜街拍精選</h3>
                <p class="section-sub">提供 30,000+ 街拍作為靈感庫，這裡示意輪播部分精選圖，完整版可進入 Lookbook 頁面瀏覽。</p>
                <div class="lookbook-inline">
                  <div>
                    <ul class="feature-list">
                      <li>依性別、色系、上身 / 下身品類快速篩選。</li>
                      <li>同步作為推薦引擎的參照素材，亦可用於行銷創意。</li>
                    </ul>
                    <div style="margin-top:12px;">
                      <a class="btn-secondary" href="?page=lookbook">開啟 Lookbook 全部靈感</a>
                    </div>
                  </div>
                  <div class="lookbook-carousel">
                    <img src="{street_base}/20170324095254453_500.jpg" alt="street style 1">
                    <img src="{street_base}/20170324100124006_500.jpg" alt="street style 2">
                    <img src="{street_base}/20170324101342210_500.jpg" alt="street style 3">
                  </div>
                </div>
              </section>

              <section class="intro-section">
                <h3 class="section-title">BI 模組｜掌握成效與顧客脈動</h3>
                <p class="section-sub">精簡呈現核心圖表，其他報表以重點列點說清楚；想看更多可直接進入各 Dashboard。</p>
                <div class="bi-hero">
                  <div class="bi-copy">
                    <h3>CRM ＋ 成效監控</h3>
                    <p>RFM、地域、渠道、留存指標一次檢視；可自訂營收、流量、轉換率的門檻告警，快速聚焦異常。</p>
                    <div class="bi-points">
                      <div class="bi-point">
                        <h5>色彩與趨勢</h5>
                        <ul>
                          <li>上下身色彩占比、年度趨勢</li>
                          <li>常見配色組合、上架建議</li>
                        </ul>
                        <div style="margin-top:8px;"><a class="btn-secondary" href="?page=dashboard">進入色彩趨勢</a></div>
                      </div>
                      <div class="bi-point">
                        <h5>CRM 洞察</h5>
                        <ul>
                          <li>VIP 比例、Recency & Monetary</li>
                          <li>國家 / 渠道分佈、留存走勢</li>
                        </ul>
                        <div style="margin-top:8px;"><a class="btn-secondary" href="?page=crm">進入 CRM</a></div>
                      </div>
                      <div class="bi-point">
                        <h5>銷售表現</h5>
                        <ul>
                          <li>Top Product、Price Range</li>
                          <li>促銷 / 新品 A/B 成效</li>
                        </ul>
                        <div style="margin-top:8px;"><a class="btn-secondary" href="?page=sales">進入銷售</a></div>
                      </div>
                      <div class="bi-point">
                        <h5>評論與 VOC</h5>
                        <ul>
                          <li>評分分布、情緒趨勢</li>
                          <li>正負面關鍵字、客服 SOP</li>
                        </ul>
                        <div style="margin-top:8px;"><a class="btn-secondary" href="?page=reviews">進入評論</a></div>
                      </div>
                    </div>
                  </div>
                  <div class="tilted-frame">
                    <div class="tilted-inner">
                      <img src="{base}/Dashboard_CRM客戶分析_part.png" alt="CRM dashboard preview">
                    </div>
                  </div>
                </div>
              </section>

              <section class="intro-section">
                <h3 class="section-title">產品能為品牌帶來的價值（Use Cases）</h3>
                <p class="section-sub">讓 AI 成為品牌顧客的穿搭顧問，提升轉換與黏著。</p>
                <div class="usecase-grid">
                  <div class="usecase-card">
                    <h4>對品牌</h4>
                    <ul>
                      <li>降低轉換門檻：即時回答「我現在穿這樣，下身要搭什麼」。</li>
                      <li>提升會員互動：穿搭 → 推薦 → 收藏 → 購買的循環。</li>
                      <li>強化商品曝光：以顏色 / 風格 / 場景導購。</li>
                      <li>降低內容製作成本：街拍素材可作創意來源。</li>
                    </ul>
                    <div style="margin-top:10px;"><a class="btn-secondary" href="?page=wardrobe">立即體驗推薦流程</a></div>
                  </div>
                  <div class="usecase-card">
                    <h4>對顧客</h4>
                    <ul>
                      <li>一張照片即可獲得色彩解析。</li>
                      <li>找到更適合自己的穿搭靈感。</li>
                      <li>更快做出購買決策。</li>
                    </ul>
                  </div>
                  <div class="usecase-card">
                    <h4>成效指標</h4>
                    <ul>
                      <li>顧客購物信心倍增，退換率顯著降低。</li>
                      <li>流量有效轉化，轉換率提升，客單與回購成長。</li>
                    </ul>
                  </div>
                </div>
              </section>

              <section class="intro-section">
                <h3 class="section-title">技術架構亮點（簡化版）</h3>
                <div class="tech-grid">
                  <div class="tech-card">
                    <h4>模型組成</h4>
                    <ul>
                      <li>Image → Feature Extraction</li>
                      <li>Color Extraction（KMeans）</li>
                      <li>CLIP Fashion Category + Pattern Classification</li>
                      <li>Co-occurrence Recommendation Engine</li>
                      <li>Streetstyle Lookbook Database</li>
                    </ul>
                  </div>
                  <div class="tech-card">
                    <h4>可嵌入品牌電商（API Friendly）</h4>
                    <ul>
                      <li>串接 PDP（商品頁）做「搭配推薦」。</li>
                      <li>會員 App 作為「穿搭顧問」入口。</li>
                      <li>首頁模組：「AI 試穿靈感」行銷落點。</li>
                    </ul>
                  </div>
                </div>
              </section>

              <section class="cta-block" id="cta">
                <div class="cta-text">
                  <h3>立即體驗 Lookbook Studio</h3>
                  <p>探索 AI 如何理解穿搭、提供推薦，並強化品牌的個人化購物旅程。</p>
                  <a class="btn-primary" href="?page=wardrobe">預約 Demo / 索取 PoC</a>
                </div>
                <div class="cta-img">
                  <img src="{base}/AI穿搭推薦_251210_part.png" alt="lookbook studio preview">
                </div>
              </section>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )
