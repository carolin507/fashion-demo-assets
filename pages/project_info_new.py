import streamlit as st
import streamlit.components.v1 as components
from textwrap import dedent


def render_project_info_new():
    """Streamlit landing page for Lookbook Studio with spacious, slide-like layout."""

    info_base = "https://raw.githubusercontent.com/carolin507/fashion-demo-assets/main/assets/intro"

    css = dedent(
        """
        <style>
        :root {
          --sand: #fff6ed;
          --amber: #f6b37c;
          --ink: #2c170f;
          --line: rgba(0,0,0,0.06);
        }
        body, .lp-shell { background:var(--sand); color:var(--ink); font-family:'Manrope','Noto Sans TC',sans-serif; }
        .lp-shell { padding:12px; }
        .container { max-width:1160px; margin:0 auto; display:flex; flex-direction:column; gap:28px; }
        .card { background:#fff; border-radius:16px; padding:24px 24px 22px; border:1px solid var(--line); box-shadow:0 16px 38px rgba(55,24,5,0.08); }
        .hero { display:grid; grid-template-columns:1.02fr 0.98fr; gap:20px; align-items:center; background:linear-gradient(120deg,#2c140a,#6b3218 45%,#f7b680); color:#fff7ee; border-radius:18px; padding:30px; box-shadow:0 24px 52px rgba(30,12,4,0.28); }
        .hero-visual { border-radius:14px; overflow:hidden; border:1px solid rgba(255,239,223,0.22); background:rgba(255,239,223,0.08); }
        .hero-visual img { width:100%; display:block; }
        .eyebrow { display:inline-flex; gap:8px; padding:7px 12px; background:rgba(255,239,223,0.2); border:1px solid rgba(255,239,223,0.3); border-radius:999px; font-weight:800; }
        h1 { margin:10px 0 8px; font-size:34px; line-height:1.2; }
        .hero-sub { margin:0 0 14px; line-height:1.7; opacity:0.96; }
        .pill-row { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:10px; }
        .pill { padding:12px 14px; border-radius:12px; border:1px solid rgba(255,239,223,0.32); background:rgba(255,239,223,0.16); font-weight:700; }
        .cta-row { display:flex; flex-wrap:wrap; gap:12px; margin-top:6px; }
        .btn-primary { background:#ffdfb0; color:#2f1408; padding:12px 18px; border-radius:12px; font-weight:800; text-decoration:none; box-shadow:0 12px 26px rgba(0,0,0,0.18); }
        .btn-ghost { background:rgba(255,239,223,0.14); color:#fff7ee; padding:11px 16px; border-radius:12px; text-decoration:none; border:1px solid rgba(255,239,223,0.5); font-weight:700; }
        h2 { margin:0 0 8px; font-size:22px; }
        p { margin:0 0 10px; line-height:1.7; color:#422b1f; }
        .two-col { display:grid; grid-template-columns:repeat(auto-fit,minmax(320px,1fr)); gap:16px; }
        .soft { background:linear-gradient(135deg,#fff9f3,#fff2e5); border:1px solid var(--line); border-radius:14px; padding:14px 14px 12px; box-shadow:0 12px 24px rgba(87,50,20,0.08); }
        .soft h4 { margin:0 0 6px; }
        .badge { display:inline-flex; padding:6px 10px; border-radius:10px; background:#ffe5cc; font-weight:700; font-size:12px; }
        .flow { display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:10px; }
        .flow-step { padding:12px; border-radius:12px; border:1px dashed rgba(0,0,0,0.07); background:#fff; box-shadow:0 10px 22px rgba(50,30,10,0.06); }
        .stat { padding:12px; border-radius:12px; background:#fff; border:1px solid var(--line); box-shadow:0 10px 22px rgba(50,30,10,0.06); }
        .img-frame { border-radius:14px; overflow:hidden; border:1px solid var(--line); background:#fff7ef; box-shadow:0 12px 26px rgba(70,40,16,0.1); }
        .img-frame img { width:100%; display:block; }
        .strip { display:grid; grid-template-columns:1.05fr 0.95fr; gap:16px; align-items:center; }
        .cta-footer { background:linear-gradient(125deg,#2c140a,#4b2410 50%,#f0a667); color:#fff7ee; padding:20px; border-radius:18px; box-shadow:0 20px 44px rgba(25,12,6,0.3); display:grid; grid-template-columns:1.05fr 0.95fr; gap:18px; align-items:center; }
        .cta-footer p { color:#fff5ec; }
        ul { margin:6px 0 0 0; padding-left:18px; line-height:1.6; color:#4a2f21; }
        @media (max-width: 960px) {
          .hero, .strip, .cta-footer { grid-template-columns:1fr; }
        }
        </style>
        """
    )

    html = dedent(
        f"""
        <div class="lp-shell">
          <div class="container">
            <section class="hero">
              <div>
                <div class="eyebrow">Lookbook Studio · AI 穿搭 × 商業智慧</div>
                <h1>Lookbook Studio：時尚產業的智慧飛輪</h1>
                <p class="hero-sub">融合 AI 穿搭靈感與 BI，讓設計、採購、行銷、銷售都有數據支撐，以暖色調科技感建立信任。</p>
                <div class="pill-row">
                  <div class="pill">✓ 提升消費者購買意願</div>
                  <div class="pill">✓ 精準預測市場趨勢</div>
                  <div class="pill">✓ 數據驅動設計與庫存</div>
                </div>
                <div class="cta-row">
                  <a class="btn-primary" href="/?page=wardrobe" target="_blank" rel="noreferrer noopener">立即啟動 · 免費試用</a>
                  <a class="btn-ghost" href="/?page=wardrobe" target="_blank" rel="noreferrer noopener">預約演示</a>
                </div>
              </div>
              <div class="hero-visual">
                <img src="{info_base}/ai_fashion.png" alt="AI fashion hero">
              </div>
            </section>

            <section class="card">
              <h2>雙向痛點，一頁看懂</h2>
              <p>依據 intro slide 風格，保持「痛點 + 解方 + 視覺」的輕量呈現，避免訊息過載。</p>
              <div class="two-col">
                <div class="soft">
                  <span class="badge">消費者挑戰</span>
                  <h4>缺乏搭配靈感，猶豫不決</h4>
                  <p>選擇困難拖慢結帳，靈感缺口降低購買意願。</p>
                  <h4>【解方】引擎 I：AI 智慧衣櫥</h4>
                  <p>一張照片即時出多款同風格穿搭，讓靈感帶動下單。</p>
                </div>
                <div class="soft">
                  <span class="badge">品牌挑戰</span>
                  <h4>看不清趨勢，庫存風險高</h4>
                  <p>熱銷色系 / 款式不可見，補貨決策晚半拍。</p>
                  <h4>【解方】引擎 II：商業智慧儀表板</h4>
                  <p>行為數據匯總成儀表板，趨勢、庫存、行銷提早布局。</p>
                </div>
              </div>
              <div class="two-col" style="margin-top:12px;">
                <div class="img-frame"><img src="{info_base}/storytelling1.webp" alt="consumer journey visual"></div>
                <div class="img-frame"><img src="{info_base}/storytelling2.jpg" alt="brand dashboard visual"></div>
              </div>
            </section>

            <section class="card">
              <div class="strip">
                <div>
                  <h2>引擎 I · AI 智慧穿搭</h2>
                  <p>三步驟、零學習成本，並以一句話點出技術亮點。</p>
                  <div class="flow">
                    <div class="flow-step"><strong>上傳穿搭</strong> 上半身照片</div>
                    <div class="flow-step"><strong>AI 辨識</strong> 顏色 / 花紋 / 品類</div>
                    <div class="flow-step"><strong>獲取推薦</strong> 即時產生同風格下半身</div>
                  </div>
                  <div class="two-col" style="margin-top:10px;">
                    <div class="stat">
                      <h4>智慧之眼</h4>
                      <p>U2Net 去背 + CLIP 語意標籤，推薦貼合風格語境。</p>
                    </div>
                    <div class="stat">
                      <h4>靈感牆</h4>
                      <p>真實穿搭資料庫生成靈感牆，延伸探索路徑。</p>
                    </div>
                  </div>
                </div>
                <div class="img-frame">
                  <img src="{info_base}/wardrobe_demo.png" alt="wardrobe AI demo">
                </div>
              </div>
              <div class="two-col" style="margin-top:12px;">
                <div class="img-frame"><img src="{info_base}/pic_process.png" alt="process visualization"></div>
                <div class="img-frame"><img src="{info_base}/lookbook_demo.png" alt="lookbook inspiration wall"></div>
              </div>
            </section>

            <section class="card">
              <div class="strip">
                <div>
                  <h2>引擎 II · 商業智慧洞察</h2>
                  <p>一句話交代數據流向，再拆兩個洞察重點。</p>
                  <div class="soft" style="margin-bottom:12px;">
                    <span class="badge">數據流向</span>
                    <p>上傳 / 點擊 / 搜尋 → Data Repository → Lookbook Studio BI Dashboard</p>
                  </div>
                  <div class="two-col">
                    <div class="soft">
                      <h4>洞察 1：顧客輪廓 + 銷售脈動</h4>
                      <ul>
                        <li>RFM 分群：VIP / 潛力 / 流失 + 國家貢獻度</li>
                        <li>熱銷單品、色系、尺寸與 AOV，用於補貨決策</li>
                      </ul>
                    </div>
                    <div class="soft">
                      <h4>洞察 2：趨勢 + 顧客心聲</h4>
                      <ul>
                        <li>色彩潮流：季節性顏色 / 圖案視覺化</li>
                        <li>VOC：NLP 情緒分類＋關鍵字，定位尺寸 / 布料 / 版型痛點</li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="img-frame">
                  <img src="{info_base}/dashboard_detail.png" alt="dashboard details">
                </div>
              </div>
              <div class="two-col" style="margin-top:12px;">
                <div class="img-frame"><img src="{info_base}/dataflow.png" alt="data flow"></div>
                <div class="img-frame"><img src="{info_base}/dashboard.png" alt="dashboard overview"></div>
              </div>
            </section>

            <section class="card">
              <h2>自動化洞察 & 飛輪</h2>
              <p>保留兩個核心亮點，並配上輕量視覺。</p>
              <div class="two-col">
                <div class="soft">
                  <h4>自動化洞察 · 主動預警</h4>
                  <p>內建自然語言摘要與警示模組，主動提醒趨勢、風險、機會。</p>
                  <div class="soft" style="background:#fff4ed; border-color:rgba(242,107,58,0.35); margin-top:8px;">
                    <strong>[系統警示]</strong> Lost 客群佔比 30%，建議立即召回並檢視流失前主力品類。
                  </div>
                </div>
                <div class="soft">
                  <h4>飛輪效應 · 共生生態系</h4>
                  <p>AI 推薦吸引用戶 → 累積偏好數據 → BI 洞察 → 優化產品與行銷 → 體驗升級。</p>
                  <div class="img-frame" style="margin-top:6px;"><img src="{info_base}/productcircle.png" alt="product flywheel"></div>
                </div>
              </div>
              <div class="two-col" style="margin-top:12px;">
                <div class="img-frame"><img src="{info_base}/insight.png" alt="insight alerts"></div>
                <div class="img-frame"><img src="{info_base}/aiflow.png" alt="ai flow"></div>
              </div>
            </section>

            <section class="cta-footer">
              <div>
                <h2 style="margin:0 0 8px;">未來展望：從數據洞察到商業價值</h2>
                <p>Lookbook Studio 致力成為時尚產業的智慧決策中樞，深化跨品類搭配、色彩與新興風格預測，協助設計、採購、行銷快一步。</p>
                <p>技術支援：基於 U2Net、CLIP 等模型迭代，確保處理穩定且精準。</p>
                <div class="cta-row">
                  <a class="btn-primary" href="/?page=wardrobe" target="_blank" rel="noreferrer noopener">預約產品演示</a>
                  <a class="btn-ghost" href="/?page=wardrobe" target="_blank" rel="noreferrer noopener" style="border-color:rgba(255,239,223,0.65);">立即免費試用</a>
                </div>
              </div>
              <div class="img-frame">
                <img src="{info_base}/ai_fashion.png" alt="ai flow diagram">
              </div>
            </section>
          </div>
        </div>
        """
    )

    components.html(css + html, height=4200, scrolling=True)
