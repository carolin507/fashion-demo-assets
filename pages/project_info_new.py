import streamlit as st
import streamlit.components.v1 as components
from textwrap import dedent


def render_project_info_new():
    """Clean landing page with aligned width and simplified hero/pain points/engine sections."""

    info_base = "https://raw.githubusercontent.com/carolin507/fashion-demo-assets/main/assets/intro"

    css = dedent(
        """
        <style>
        :root {
          --bg: #f6f0e8;
          --card: #ffffff;
          --ink: #22130d;
          --muted: #5a4336;
          --accent: #f0456a;
          --accent-2: #ffdbe5;
          --line: rgba(0,0,0,0.06);
        }
        body, .lp-shell { background:var(--bg); color:var(--ink); font-family:'Manrope','Noto Sans TC',sans-serif; overflow-x:hidden; }
        /* match other pages width */
        [data-testid="stAppViewContainer"] .main .block-container { padding-left:1.2rem; padding-right:1.2rem; max-width:1200px; }
        .lp-shell { padding:28px 0 64px; }
        .container { width:100%; display:flex; flex-direction:column; gap:48px; overflow:visible; }
        .card { background:var(--card); border-radius:14px; padding:34px 28px; border:1px solid rgba(0,0,0,0.02); box-shadow:0 14px 30px rgba(28,12,4,0.08); }
        h1 { margin:0 0 10px; font-size:30px; line-height:1.2; }
        h2 { margin:0 0 12px; font-size:24px; text-align:center; }
        h3 { margin:0 0 8px; font-size:18px; }
        p { margin:0 0 10px; line-height:1.65; color:var(--muted); }
        /* hero */
        .hero { display:grid; grid-template-columns:1.05fr 0.95fr; gap:18px; align-items:center; padding:36px; border-radius:16px;
                background:linear-gradient(110deg,#2b0f13,#6a1f30 45%,#f76e8b); color:#fff7ee; box-shadow:0 20px 52px rgba(22,10,4,0.3); overflow:hidden; }
        .hero-visual { border-radius:16px; overflow:hidden; border:1px solid rgba(255,239,223,0.2); background:rgba(255,239,223,0.06); box-shadow:0 12px 26px rgba(0,0,0,0.2); }
        .hero-visual img { width:100%; display:block; }
        .cta-row { display:flex; gap:10px; flex-wrap:wrap; margin-top:10px; }
        .btn-primary { background:#ffdbe5; color:#2d0f12; padding:11px 16px; border-radius:12px; font-weight:800; text-decoration:none; box-shadow:0 10px 20px rgba(0,0,0,0.14); }
        .btn-ghost { background:rgba(255,239,223,0.14); color:#fff7ee; padding:10px 14px; border-radius:12px; text-decoration:none; border:1px solid rgba(255,239,223,0.5); font-weight:700; }
        /* layout */
        .two-col { display:grid; grid-template-columns:repeat(auto-fit,minmax(320px,1fr)); gap:22px; }
        .split { display:grid; grid-template-columns:1fr 1fr; gap:20px; align-items:center; }
        .soft { background:#fff; border:1px solid var(--line); border-radius:12px; padding:18px; box-shadow:0 10px 22px rgba(87,50,20,0.05); }
        .img-frame { border-radius:14px; overflow:hidden; border:1px solid var(--line); background:#fff7ef; box-shadow:0 10px 22px rgba(70,40,16,0.08); }
        .img-frame img { width:100%; display:block; }
        .engine-block .img-frame { max-width:80%; margin:0 auto; }
        .engine-block .split { align-items:center; }
        .engine-head { display:flex; align-items:center; justify-content:center; gap:10px; margin-bottom:16px; }
        .engine-tag { background:var(--accent); color:#fff; padding:6px 12px; border-radius:999px; font-weight:800; letter-spacing:0.03em; font-size:12px; }
        /* steps */
        .flow { display:flex; flex-direction:column; gap:16px; }
        .flow-step { padding:14px; border-radius:12px; border:1px dashed rgba(0,0,0,0.08); background:linear-gradient(135deg,#fff8f4,#fffaf8); box-shadow:0 12px 22px rgba(50,30,10,0.06); display:flex; gap:12px; align-items:center; }
        .step-num { width:34px; height:34px; border-radius:50%; background:var(--accent); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:900; font-size:14px; box-shadow:0 6px 12px rgba(240,69,106,0.25); }
        .mini-process { display:grid; grid-template-columns:repeat(5, minmax(0,1fr)); gap:10px; align-items:center; justify-items:center; text-align:center; background:#fffaf6; padding:14px; border-radius:12px; border:1px dashed var(--line); }
        .mini-card { background:#fff; border:1px solid var(--line); border-radius:10px; padding:12px; box-shadow:0 10px 20px rgba(60,30,10,0.06); display:flex; flex-direction:column; gap:8px; align-items:center; }
        .mini-card img { width:100%; border-radius:8px; object-fit:cover; max-height:150px; }
        .mini-process .arrow { color:var(--accent); font-weight:800; font-size:18px; width:38px; height:38px; border-radius:50%; background:#ffe1e9; display:flex; align-items:center; justify-content:center; box-shadow:0 8px 16px rgba(240,69,106,0.15); }
        /* strip */
        .strip { background:#e3004f; color:#ffeef4; padding:12px; border-radius:12px; display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:8px; align-items:center; text-align:center; box-shadow:0 14px 28px rgba(180,0,50,0.22); }
        .strip-item { display:flex; flex-direction:column; gap:4px; align-items:center; }
        .strip-item .dot { width:32px; height:32px; border-radius:50%; background:rgba(255,255,255,0.2); display:flex; align-items:center; justify-content:center; font-weight:800; }
        /* dark panel */
        .micro-quote { font-weight:800; color:#e3004f; letter-spacing:0.02em; font-size:15px; margin:0 0 6px; }
        .dark-section { background:linear-gradient(135deg,#1b0f12,#381a1f 55%,#731f33); color:#fff7ee; border-radius:16px; padding:30px; box-shadow:0 22px 48px rgba(16,0,8,0.3); }
        .dark-section .engine-head { margin-bottom:12px; }
        .dark-grid { display:grid; grid-template-columns:1fr 0.85fr; gap:18px; align-items:center; }
        .dark-section .img-frame { max-width:85%; margin:0 auto; background:#fff; border:1px solid #f0e8e4; box-shadow:none; }
        .panel { background:#fff; color:#1f120c; border-radius:12px; padding:12px; box-shadow:0 14px 30px rgba(0,0,0,0.14); border:1px solid rgba(255,255,255,0.04); }
        .insight-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px; }
        .insight-box { background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.2); border-radius:12px; padding:12px 14px; box-shadow:0 10px 22px rgba(0,0,0,0.12); color:#f7e7ed; }
        .insight-box strong { color:#ffeef7; display:block; margin-bottom:4px; font-size:15px; letter-spacing:0.02em; }
        /* tech */
        .tech-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:16px; }
        .tech-card { background:#fff; border-radius:12px; padding:18px; border:1px solid var(--line); box-shadow:0 10px 22px rgba(50,30,10,0.07); }
        .dotlist { list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px; }
        .dotlist li { display:flex; gap:8px; align-items:flex-start; color:var(--muted); }
        .dot { width:7px; height:7px; border-radius:50%; background:#c7b4aa; margin-top:6px; }
        /* CTA */
        .cta-footer { background:#e3004f; color:#fff7ee; padding:30px; border-radius:14px; box-shadow:0 18px 38px rgba(180,0,50,0.28); display:grid; grid-template-columns:1fr 1fr; gap:18px; align-items:center; }
        .cta-footer p { color:#ffeef4; }
        @media (max-width: 1020px) {
          .hero, .split, .cta-footer, .dark-grid { grid-template-columns:1fr; }
          .hero { padding:22px; }
          .engine-block .img-frame { max-width:92%; }
          .dark-grid { gap:12px; }
        }
        </style>
        """
    )

    html = dedent(
        f"""
        <div class="lp-shell">
          <div class="container">
            <!-- Hero -->
            <section class="hero">
              <div>
                <h1>Lookbook Studio：驅動時尚的雙引擎</h1>
                <p class="hero-sub" style="color:#ffeef4;">結合 <strong style="color:#ffdbe5;">AI 穿搭靈感</strong> 與 <strong style="color:#ffdbe5;">商業智慧</strong>，打造消費者與品牌的共生生態系。</p>
                <div class="cta-row">
                  <a class="btn-primary" href="/?page=wardrobe" target="_blank" rel="noreferrer noopener">探索智慧衣櫥</a>
                  <a class="btn-ghost" href="/?page=dashboard" target="_blank" rel="noreferrer noopener">查看商業洞察</a>
                </div>
              </div>
              <div class="hero-visual">
                <img src="{info_base}/ai_fashion.png" alt="App preview">
              </div>
            </section>

            <!-- Dual pain points -->
            <section class="card">
              <h2>時尚產業的雙向難題</h2>
              <div class="two-col" style="align-items:start; text-align:center; gap:18px;">
                <div class="soft" style="padding:14px; display:flex; flex-direction:column; gap:10px;">
                  <div class="img-frame" style="max-width:520px; margin:0 auto;"><img src="{info_base}/storytelling1.webp" alt="缺乏搭配靈感"></div>
                  <div class="micro-quote">「我該穿什麼？」</div>
                  <h3 style="margin:6px 0 4px;">缺乏搭配靈感</h3>
                  <p style="margin:0; text-align:center;">消費者在選購服飾時，時常面臨選擇困難與搭配的挑戰，影響購物體驗與意願。</p>
                </div>
                <div class="soft" style="padding:14px; display:flex; flex-direction:column; gap:10px;">
                  <div class="img-frame" style="max-width:520px; margin:0 auto;"><img src="{info_base}/storytelling2.jpg" alt="難以掌握市場趨勢"></div>
                  <div class="micro-quote">「我們該賣什麼？」</div>
                  <h3 style="margin:6px 0 4px;">難以掌握市場趨勢</h3>
                  <p style="margin:0; text-align:center;">電商品牌若無法精準預測熱門色系、款式與搭配組合，將面臨庫存風險與錯失商機的壓力。</p>
                </div>
              </div>
            </section>

            <!-- Engine I -->
            <section class="card engine-block">
              <div class="engine-head">
                <span class="engine-tag">Engine I</span>
                <h2 style="margin:0;">為消費者注入靈感 - AI 穿搭靈感推薦</h2>
              </div>
              <div class="split" style="align-items:center;">
                <div class="img-frame" style="background:#fff;">
                  <img src="{info_base}/AI穿搭推薦_251210_part.png" alt="AI穿搭推薦流程圖">
                </div>
                <div style="display:flex; flex-direction:column; gap:16px; justify-content:center;">
                  <div class="flow">
                    <div class="flow-step">
                      <div class="step-num">1</div>
                      <div><strong>上傳你的穿搭</strong><br>透過一張上半身照片獲取穿搭 ID。</div>
                    </div>
                    <div class="flow-step">
                      <div class="step-num">2</div>
                      <div><strong>AI 解讀單品</strong><br>自動分析顏色、花紋與識別單品。</div>
                    </div>
                    <div class="flow-step">
                      <div class="step-num">3</div>
                      <div><strong>獲取配搭推薦</strong><br>推薦相似或下一季單品，快速完成搭配。</div>
                    </div>
                  </div>
                </div>
              </div>

              <div class="soft" style="margin-top:22px; background:#f1ede8; text-align:center;">
                <h3 style="margin-bottom:12px;">智慧之眼：AI 如何理解時尚</h3>
                <div class="mini-process">
                  <div class="mini-card"><img src="{info_base}/aiflow_1_model.png" alt="模型理解人體輪廓"><strong>模型理解人體輪廓</strong><p>U2Net 去背，鎖定身形與部位。</p></div>
                  <div class="arrow">→</div>
                  <div class="mini-card"><img src="{info_base}/aiflow_2_unet.png" alt="服飾遮罩與顏色讀取"><strong>服飾遮罩與顏色讀取</strong><p>生成服裝遮罩，萃取顏色與質感。</p></div>
                  <div class="arrow">→</div>
                  <div class="mini-card"><img src="{info_base}/aiflow_3_clip.png" alt="CLIP 語意標籤"><strong>CLIP 語意標籤</strong><p>輸出顏色 / 花紋 / 品類特徵。</p></div>
                </div>
              </div>
            </section>

            <!-- Engine II (mirrors Engine I layout) -->
            <section class="dark-section engine-block">
              <div class="engine-head">
                <span class="engine-tag" style="background:#ffdbe5; color:#2d0f12;">Engine II</span>
                <h2 style="margin:0; color:#fff7ee; font-size:26px; letter-spacing:0.01em;">為品牌賦能 · 商業智慧儀表板</h2>
              </div>
              <div class="dark-grid">
                <div>
                  <p style="color:#f6e8e6; text-align:center; margin-bottom:12px;">每一次互動都是決策燃料：上傳 / 點擊 / 搜尋 → 數據資產 → 即時 BI 儀表板。</p>
                  <div class="panel" style="margin-top:10px;">
                    <h3 style="display:flex; gap:8px; align-items:center; margin:0 0 10px; color:#2d0f12;">Sales Performance & Insights <span style="font-size:12px; color:#8b6f64; background:#f5efeb; border-radius:8px; padding:4px 8px; margin-left:auto;">Real-time</span></h3>
                    <div class="two-col" style="margin-top:10px; gap:10px;">
                      <div class="img-frame"><img src="{info_base}/dashboard_clear.png" alt="dashboard overview"></div>
                      <div class="img-frame"><img src="{info_base}/dashboard_clear.png" alt="dashboard detail"></div>
                    </div>
                  </div>
                </div>
                <div class="insight-grid" style="justify-self:center; width:100%; max-width:520px;">
                  <div class="insight-box"><strong>CRM</strong><p>RFM / VIP 分群、留存與流失預警。</p></div>
                  <div class="insight-box"><strong>TREND · 色彩分析</strong><p>Top 色系、上下身搭配熱度，洞察色彩趨勢。</p></div>
                  <div class="insight-box"><strong>SALES</strong><p>Top SKUs、尺寸/價格帶表現，支援補貨與定價。</p></div>
                  <div class="insight-box"><strong>VOC</strong><p>評論情緒與關鍵字，快速鎖定尺寸/版型痛點。</p></div>
                </div>
              </div>
            </section>

            <!-- Tech foundation -->
            <section class="card">
              <h2>穩固的技術基石與演進</h2>
              <div class="tech-grid">
                <div class="tech-card">
                  <h3>技術架構</h3>
                  <ul class="dotlist">
                    <li><div class="dot"></div><div><strong>資料來源</strong><br>RichWear Dataset (32k+), E-commerce Datasets</div></li>
                    <li><div class="dot"></div><div><strong>核心技術</strong><br>Python, SQL, Streamlit</div></li>
                    <li><div class="dot"></div><div><strong>AI 模型</strong><br>U2Net (分割), CLIP (語意), Naive Bayes (分群)</div></li>
                  </ul>
                </div>
                <div class="tech-card">
                  <h3>分割模型演進</h3>
                  <ul class="dotlist">
                    <li><div class="dot"></div><div><strong>YOLO</strong><br>從人體關鍵點入門，但易受背景干擾。</div></li>
                    <li><div class="dot"></div><div><strong>U2Net</strong><br>成功去除 95% 背景，但細節仍需補強。</div></li>
                    <li><div class="dot"></div><div><strong style="color:#f0456a;">U2Net + Erosion</strong><br>內嵌 Erosion，解決邊緣色塊干擾，大幅提升 CLIP 判斷準確率。</div></li>
                  </ul>
                </div>
              </div>
            </section>

            <!-- Footer CTA -->
            <section class="cta-footer">
              <div>
                <h2 style="margin:0 0 6px;">將 Lookbook Studio 打造成時尚產業不可或缺的智慧決策中樞</h2>
                <p>立即預約產品演示，開啟您的數據驅動時尚新時代。</p>
                <div class="cta-row">
                  <a class="btn-primary" href="/?page=wardrobe" target="_blank" rel="noreferrer noopener">預約產品演示</a>
                  <a class="btn-ghost" href="/?page=wardrobe" target="_blank" rel="noreferrer noopener" style="border-color:rgba(255,239,223,0.65);">立即免費試用</a>
                </div>
              </div>
              <div class="img-frame">
                <img src="{info_base}/ai_fashion.png" alt="cta visual">
              </div>
            </section>
          </div>
        </div>
        """
    )

    components.html(css + html, height=7600, scrolling=True)
