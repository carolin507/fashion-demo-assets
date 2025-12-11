import React, { useState, useEffect } from 'react';
import { Icons } from './components/Icons';
import { TrendChart, SentimentChart, KpiCard } from './components/DashboardCharts';

// --- Sub-components for structure ---

const Header = () => (
  <nav className="fixed w-full bg-white/80 backdrop-blur-md z-50 border-b border-stone-200">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="flex justify-between items-center h-16">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 bg-brand-500 rounded-lg flex items-center justify-center text-white">
            <Icons.Shirt size={20} />
          </div>
          <span className="font-bold text-xl text-stone-800 tracking-tight">Lookbook Studio</span>
        </div>
        <div className="hidden md:flex items-center space-x-8 text-sm font-medium text-stone-600">
          <a href="#consumer" className="hover:text-brand-600 transition-colors">智慧衣櫥</a>
          <a href="#business" className="hover:text-brand-600 transition-colors">商業儀表板</a>
          <a href="#tech" className="hover:text-brand-600 transition-colors">核心技術</a>
          <a href="#future" className="hover:text-brand-600 transition-colors">未來展望</a>
        </div>
        <button className="bg-brand-600 text-white px-5 py-2 rounded-full text-sm font-semibold hover:bg-brand-700 transition-all shadow-lg shadow-brand-200">
          立即體驗
        </button>
      </div>
    </div>
  </nav>
);

const Hero = () => (
  <header className="relative pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden bg-sand-50">
    {/* Abstract background elements */}
    <div className="absolute top-0 right-0 w-1/2 h-full bg-brand-50 opacity-50 rounded-bl-[100px] -z-10"></div>
    <div className="absolute bottom-0 left-0 w-64 h-64 bg-stone-200 rounded-full blur-3xl opacity-20 -z-10"></div>

    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <h1 className="text-5xl md:text-7xl font-bold text-stone-900 tracking-tight mb-6 leading-tight">
        驅動時尚的<span className="text-brand-600">雙引擎</span>
      </h1>
      <p className="text-xl md:text-2xl text-stone-600 max-w-3xl mx-auto mb-10 leading-relaxed">
        融合 <span className="text-brand-600 font-semibold">AI 穿搭靈感</span> 與 <span className="text-brand-600 font-semibold">商業智慧</span>，<br className="hidden md:block"/>
        打造消費者與品牌的共生生態系
      </p>
      <div className="flex flex-col sm:flex-row gap-4 justify-center">
        <button className="px-8 py-4 bg-stone-900 text-white rounded-xl font-bold text-lg hover:bg-stone-800 transition-all flex items-center justify-center gap-2">
          探索智慧衣櫥 <Icons.ArrowRight size={20} />
        </button>
        <button className="px-8 py-4 bg-white text-stone-900 border border-stone-200 rounded-xl font-bold text-lg hover:bg-stone-50 transition-all">
          查看商業洞察
        </button>
      </div>
    </div>
  </header>
);

const ProblemSection = () => (
  <section className="py-20 bg-white">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="text-center mb-16">
        <h2 className="text-3xl md:text-4xl font-bold text-stone-900">時尚產業的雙向難題</h2>
        <div className="w-16 h-1 bg-brand-500 mx-auto mt-4 rounded-full"></div>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-12 relative">
        {/* Vertical divider */}
        <div className="hidden md:block absolute top-0 bottom-0 left-1/2 w-px bg-stone-200 -ml-px"></div>

        {/* Consumer Pain Point */}
        <div className="flex flex-col items-center text-center p-6 group">
          <div className="relative w-full h-64 mb-6 rounded-2xl overflow-hidden shadow-lg group-hover:shadow-xl transition-all">
             <img src="https://picsum.photos/600/400?random=1" alt="Wardrobe chaos" className="w-full h-full object-cover opacity-90 group-hover:scale-105 transition-transform duration-500" />
             <div className="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors"></div>
          </div>
          <h3 className="text-2xl font-bold text-stone-800 mb-3">缺乏搭配靈感</h3>
          <p className="text-stone-600 leading-relaxed max-w-sm">
            消費者在選購服飾時，時常面臨選擇困難與搭配的挑戰，影響購物體驗與意願。
          </p>
          <div className="mt-6 text-brand-500 font-bold text-4xl">?</div>
        </div>

        {/* Brand Pain Point */}
        <div className="flex flex-col items-center text-center p-6 group">
          <div className="relative w-full h-64 mb-6 rounded-2xl overflow-hidden shadow-lg group-hover:shadow-xl transition-all">
             <img src="https://picsum.photos/600/400?random=2" alt="Design process" className="w-full h-full object-cover opacity-90 group-hover:scale-105 transition-transform duration-500" />
             <div className="absolute inset-0 bg-black/20 group-hover:bg-black/10 transition-colors"></div>
          </div>
          <h3 className="text-2xl font-bold text-stone-800 mb-3">難以掌握市場趨勢</h3>
          <p className="text-stone-600 leading-relaxed max-w-sm">
            電商品牌若無法精準預測熱門色系、款式與搭配組合，將面臨庫存風險與錯失商機的壓力。
          </p>
          <div className="mt-6 text-brand-500 font-bold text-4xl flex gap-1">
            <Icons.TrendingUp className="rotate-180" size={40} />
          </div>
        </div>
      </div>
    </div>
  </section>
);

const ConsumerEngine = () => (
  <section id="consumer" className="py-24 bg-stone-50">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="mb-16">
        <span className="text-brand-600 font-bold tracking-wider uppercase text-sm">Engine I</span>
        <h2 className="text-3xl md:text-5xl font-bold text-stone-900 mt-2">為消費者注入靈感 - AI 智慧衣櫥</h2>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-12">
        {/* Interactive Step Visualizer */}
        <div className="lg:col-span-7 space-y-8">
          <div className="bg-white p-8 rounded-3xl shadow-xl border border-stone-100 relative overflow-hidden">
             {/* Mock UI for Lookbook Studio */}
             <div className="flex justify-between items-center mb-6 border-b border-stone-100 pb-4">
                <span className="font-bold text-stone-800">Lookbook Studio</span>
                <div className="flex gap-2">
                  <div className="w-3 h-3 rounded-full bg-red-400"></div>
                  <div className="w-3 h-3 rounded-full bg-yellow-400"></div>
                  <div className="w-3 h-3 rounded-full bg-green-400"></div>
                </div>
             </div>
             
             <div className="grid grid-cols-2 gap-6">
                <div className="space-y-4">
                  <div className="aspect-[3/4] bg-stone-100 rounded-xl relative overflow-hidden group">
                     <img src="https://picsum.photos/400/533?random=3" alt="User upload" className="w-full h-full object-cover" />
                     <div className="absolute top-4 left-4 bg-black/70 text-white text-xs px-2 py-1 rounded backdrop-blur-sm">原始上傳</div>
                  </div>
                </div>
                <div className="space-y-4">
                  <div className="aspect-[3/4] bg-stone-100 rounded-xl relative overflow-hidden p-4 flex flex-col gap-4">
                      {/* Simulated Recommendations */}
                      <div className="flex-1 bg-white rounded-lg shadow-sm p-2 flex gap-3 items-center transform translate-x-2 transition-transform">
                        <div className="w-12 h-16 bg-stone-200 rounded"></div>
                        <div className="flex-1 space-y-2">
                          <div className="h-2 w-20 bg-stone-200 rounded"></div>
                          <div className="h-2 w-12 bg-stone-100 rounded"></div>
                        </div>
                      </div>
                      <div className="flex-1 bg-white rounded-lg shadow-sm p-2 flex gap-3 items-center transform hover:-translate-y-1 transition-transform cursor-pointer border-2 border-brand-100">
                        <div className="w-12 h-16 bg-brand-100 rounded flex items-center justify-center text-brand-500">
                          <Icons.Shirt size={20} />
                        </div>
                        <div className="flex-1 space-y-2">
                          <div className="h-2 w-20 bg-stone-200 rounded"></div>
                          <div className="text-xs text-brand-600 font-bold">推薦單品</div>
                        </div>
                      </div>
                      <div className="flex-1 bg-white rounded-lg shadow-sm p-2 flex gap-3 items-center transform translate-x-2 transition-transform">
                        <div className="w-12 h-16 bg-stone-200 rounded"></div>
                        <div className="flex-1 space-y-2">
                          <div className="h-2 w-20 bg-stone-200 rounded"></div>
                          <div className="h-2 w-12 bg-stone-100 rounded"></div>
                        </div>
                      </div>
                  </div>
                </div>
             </div>

             {/* Connection Lines Overlay */}
             <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white rounded-full p-2 shadow-lg z-10">
               <Icons.ArrowRight className="text-brand-500" />
             </div>
          </div>
        </div>

        {/* Steps Description */}
        <div className="lg:col-span-5 flex flex-col justify-center space-y-10">
          <div className="flex gap-4">
            <div className="flex-shrink-0 w-12 h-12 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold text-xl">1</div>
            <div>
              <h3 className="text-xl font-bold text-stone-900 mb-2">上傳你的穿搭</h3>
              <p className="text-stone-600">使用者只需上傳一張上半身穿搭照片，系統即刻開始分析。</p>
            </div>
          </div>
          <div className="flex gap-4">
            <div className="flex-shrink-0 w-12 h-12 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold text-xl">2</div>
            <div>
              <h3 className="text-xl font-bold text-stone-900 mb-2">AI 辨識單品</h3>
              <p className="text-stone-600">系統自動分析顏色、花紋與類別，精準理解你的風格。</p>
            </div>
          </div>
          <div className="flex gap-4">
            <div className="flex-shrink-0 w-12 h-12 rounded-full bg-brand-100 text-brand-600 flex items-center justify-center font-bold text-xl">3</div>
            <div>
              <h3 className="text-xl font-bold text-stone-900 mb-2">獲取搭配推薦</h3>
              <p className="text-stone-600">即時生成多款風格一致的下半身搭配建議，激發購物靈感。</p>
            </div>
          </div>
        </div>
      </div>
      
      {/* Tech Diagram (Slide 4) */}
      <div className="mt-20 border-t border-stone-200 pt-16">
         <h3 className="text-2xl font-bold text-center mb-12">智慧之眼：AI 如何理解時尚</h3>
         <div className="flex flex-col md:flex-row justify-between items-center max-w-5xl mx-auto gap-8">
            {/* Step 1 */}
            <div className="bg-white p-6 rounded-2xl shadow-md flex-1 w-full text-center">
              <div className="mx-auto w-16 h-16 bg-stone-100 rounded-full flex items-center justify-center mb-4 text-stone-600">
                <Icons.Upload size={28} />
              </div>
              <h4 className="font-bold text-stone-800">影像輸入</h4>
              <p className="text-sm text-stone-500 mt-2">高品質時尚穿搭照片</p>
            </div>

            <Icons.ArrowRight className="text-stone-300 rotate-90 md:rotate-0" size={32} />

            {/* Step 2 */}
            <div className="bg-white p-6 rounded-2xl shadow-md flex-1 w-full text-center border-b-4 border-brand-400">
              <div className="mx-auto w-16 h-16 bg-brand-50 rounded-full flex items-center justify-center mb-4 text-brand-500">
                <Icons.Scissors size={28} />
              </div>
              <h4 className="font-bold text-stone-800">U2Net 精準分割</h4>
              <p className="text-sm text-stone-500 mt-2">去除背景，分離服飾輪廓</p>
            </div>

            <Icons.ArrowRight className="text-stone-300 rotate-90 md:rotate-0" size={32} />

            {/* Step 3 */}
            <div className="bg-white p-6 rounded-2xl shadow-md flex-1 w-full text-center border-b-4 border-brand-600">
              <div className="mx-auto w-16 h-16 bg-brand-50 rounded-full flex items-center justify-center mb-4 text-brand-500">
                <Icons.Layers size={28} />
              </div>
              <h4 className="font-bold text-stone-800">CLIP 語意標籤</h4>
              <p className="text-sm text-stone-500 mt-2">向量分析，匹配 42+ 個關鍵屬性</p>
            </div>
         </div>
         <div className="mt-8 text-center bg-stone-200 py-2 px-4 rounded-lg inline-block mx-auto w-full max-w-md font-mono text-sm text-stone-700">
            [ 'Blue', 'Solid', 'Jeans', 'Casual' ]
         </div>
      </div>
    </div>
  </section>
);

const BusinessEngine = () => (
  <section id="business" className="py-24 bg-stone-900 text-white overflow-hidden">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
      <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-brand-900/30 rounded-full blur-[100px] pointer-events-none"></div>

      <div className="mb-16 relative z-10">
        <span className="text-brand-400 font-bold tracking-wider uppercase text-sm">Engine II</span>
        <h2 className="text-3xl md:text-5xl font-bold mt-2">為品牌賦能 - 商業智慧儀表板</h2>
        <p className="text-stone-400 mt-4 max-w-2xl">
          Lookbook Studio 不僅是靈感工具，更是數據金礦。每一次互動都轉化為可執行的商業洞察。
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        {/* Dashboard Mockup */}
        <div className="lg:col-span-8 bg-stone-50 rounded-xl p-6 shadow-2xl overflow-hidden text-stone-900">
           <div className="flex justify-between items-center mb-6">
             <h3 className="font-bold text-lg flex items-center gap-2">
               <Icons.BarChart size={20} className="text-brand-600"/> 
               Sales Performance & Insights
             </h3>
             <div className="text-sm text-stone-500 bg-white px-3 py-1 rounded-md border shadow-sm">Real-time</div>
           </div>

           {/* KPI Row */}
           <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
              <KpiCard title="平均訂單價值 (AOV)" value="$537" change="+12%" />
              <KpiCard title="本月營收" value="$146,519" change="+8.5%" />
              <KpiCard title="轉換率" value="4.2%" change="+1.1%" />
           </div>

           {/* Charts Row */}
           <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <TrendChart />
              <SentimentChart />
           </div>
           
           {/* Deep Dive Description inside dashboard wrapper for visual flow */}
           <div className="mt-6 p-4 bg-blue-50/50 rounded-lg border border-blue-100 flex gap-4 items-start">
              <Icons.Search className="text-blue-500 mt-1 flex-shrink-0" size={20} />
              <div>
                <h4 className="font-bold text-stone-800 text-sm">關鍵洞察 (Key Insight)</h4>
                <p className="text-xs text-stone-600 mt-1">
                  統計分析數十萬張穿搭照片，視覺化呈現色彩與圖案的季節性趨勢。運用 NLP 技術分析顧客評論，自動進行情緒分類並提取關鍵字。
                </p>
              </div>
           </div>
        </div>

        {/* Feature List */}
        <div className="lg:col-span-4 space-y-6">
           <div className="p-6 bg-stone-800 rounded-xl border border-stone-700 hover:border-brand-500/50 transition-colors">
              <div className="w-12 h-12 bg-stone-700 rounded-lg flex items-center justify-center mb-4 text-brand-400">
                <Icons.Users size={24} />
              </div>
              <h3 className="text-xl font-bold mb-2">顧客輪廓分析</h3>
              <p className="text-stone-400 text-sm leading-relaxed">
                透過 RFM 模型自動將客戶分為 VIP、潛力、流失等族群，實現精準分眾行銷。
              </p>
           </div>
           
           <div className="p-6 bg-stone-800 rounded-xl border border-stone-700 hover:border-brand-500/50 transition-colors">
              <div className="w-12 h-12 bg-stone-700 rounded-lg flex items-center justify-center mb-4 text-brand-400">
                <Icons.ShoppingBag size={24} />
              </div>
              <h3 className="text-xl font-bold mb-2">銷售脈動監測</h3>
              <p className="text-stone-400 text-sm leading-relaxed">
                即時追蹤熱銷單品 (Top SKUs)、顏色與尺寸，作為補貨與庫存管理的依據。
              </p>
           </div>

           <div className="p-6 bg-stone-800 rounded-xl border border-stone-700 hover:border-brand-500/50 transition-colors">
              <div className="w-12 h-12 bg-stone-700 rounded-lg flex items-center justify-center mb-4 text-brand-400">
                <Icons.MessageCircle size={24} />
              </div>
              <h3 className="text-xl font-bold mb-2">VOC 輿情分析</h3>
              <p className="text-stone-400 text-sm leading-relaxed">
                運用 NLP 技術分析，快速識別產品優缺點（如版型、布料），作為產品迭代的依據。
              </p>
           </div>
        </div>
      </div>
    </div>
  </section>
);

const Flywheel = () => (
  <section className="py-24 bg-white relative overflow-hidden">
    <div className="max-w-4xl mx-auto px-4 text-center">
      <h2 className="text-3xl md:text-5xl font-bold text-stone-900 mb-16">
        飛輪效應：打造消費者與品牌的<span className="text-brand-600">共生生態系</span>
      </h2>

      {/* Circular Flywheel Visualization */}
      <div className="relative w-full max-w-[600px] aspect-square mx-auto hidden md:block">
         {/* Center */}
         <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-brand-50 rounded-full flex flex-col items-center justify-center text-center p-6 border-4 border-white shadow-xl z-20">
            <h3 className="text-xl font-bold text-stone-800 mb-2">數據驅動的<br/>良性循環</h3>
            <p className="text-sm text-stone-600">創造持續的競爭優勢</p>
         </div>

         {/* Orbit Items */}
         <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full animate-spin-slow origin-center">
           {/* Item 1 - Top Right */}
           <div className="absolute top-[10%] right-[10%] w-48 text-left bg-white p-4 rounded-xl shadow-lg border-l-4 border-brand-500">
             <h4 className="font-bold text-brand-600 mb-1">AI 穿搭推薦</h4>
             <p className="text-xs text-stone-600">吸引並滿足消費者對靈感的需求</p>
           </div>
           
           {/* Item 2 - Bottom Right */}
           <div className="absolute bottom-[10%] right-[10%] w-48 text-left bg-white p-4 rounded-xl shadow-lg border-l-4 border-brand-500">
             <h4 className="font-bold text-brand-600 mb-1">數據累積</h4>
             <p className="text-xs text-stone-600">產生寶貴的偏好與行為數據</p>
           </div>

           {/* Item 3 - Bottom Left */}
           <div className="absolute bottom-[10%] left-[10%] w-48 text-left bg-white p-4 rounded-xl shadow-lg border-l-4 border-brand-500">
             <h4 className="font-bold text-brand-600 mb-1">商業洞察</h4>
             <p className="text-xs text-stone-600">將數據轉化為市場趨勢</p>
           </div>

           {/* Item 4 - Top Left */}
           <div className="absolute top-[10%] left-[10%] w-48 text-left bg-white p-4 rounded-xl shadow-lg border-l-4 border-brand-500">
             <h4 className="font-bold text-brand-600 mb-1">優化產品與行銷</h4>
             <p className="text-xs text-stone-600">品牌根據洞察優化設計策略</p>
           </div>
         </div>
         
         {/* Connecting Circle */}
         <div className="absolute top-12 left-12 right-12 bottom-12 border-2 border-dashed border-stone-300 rounded-full -z-10"></div>
      </div>

      {/* Mobile Stack View */}
      <div className="md:hidden space-y-6">
        <div className="bg-brand-50 p-6 rounded-xl border border-brand-100">
            <h4 className="font-bold text-brand-700 text-lg mb-2">1. AI 穿搭推薦</h4>
            <p className="text-stone-700">吸引並滿足消費者需求</p>
        </div>
        <Icons.ArrowRight className="mx-auto rotate-90 text-stone-300" />
        <div className="bg-stone-50 p-6 rounded-xl border border-stone-200">
            <h4 className="font-bold text-stone-800 text-lg mb-2">2. 使用者數據累積</h4>
            <p className="text-stone-600">產生寶貴偏好數據</p>
        </div>
        <Icons.ArrowRight className="mx-auto rotate-90 text-stone-300" />
        <div className="bg-stone-50 p-6 rounded-xl border border-stone-200">
            <h4 className="font-bold text-stone-800 text-lg mb-2">3. 商業智慧洞察</h4>
            <p className="text-stone-600">轉化為市場趨勢分析</p>
        </div>
        <Icons.ArrowRight className="mx-auto rotate-90 text-stone-300" />
        <div className="bg-brand-50 p-6 rounded-xl border border-brand-100">
            <h4 className="font-bold text-brand-700 text-lg mb-2">4. 體驗與產品再升級</h4>
            <p className="text-stone-700">啟動下一輪循環</p>
        </div>
      </div>

    </div>
  </section>
);

const TechStack = () => (
  <section id="tech" className="py-20 bg-stone-100">
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h2 className="text-3xl font-bold text-center text-stone-900 mb-12">穩固的技術基石與演進</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-10">
        <div className="bg-white p-8 rounded-2xl shadow-sm">
           <h3 className="text-xl font-bold text-stone-800 mb-6 flex items-center gap-2">
             <Icons.Database className="text-brand-500" /> 技術架構
           </h3>
           <ul className="space-y-4">
             <li className="flex items-start gap-3">
               <div className="w-1.5 h-1.5 mt-2 bg-stone-400 rounded-full"></div>
               <div>
                 <span className="font-bold block text-stone-700">資料來源</span>
                 <span className="text-sm text-stone-500">RichWear Dataset (32萬張), E-commerce Datasets</span>
               </div>
             </li>
             <li className="flex items-start gap-3">
               <div className="w-1.5 h-1.5 mt-2 bg-stone-400 rounded-full"></div>
               <div>
                 <span className="font-bold block text-stone-700">核心技術</span>
                 <span className="text-sm text-stone-500">Python, SQL, Streamlit</span>
               </div>
             </li>
             <li className="flex items-start gap-3">
               <div className="w-1.5 h-1.5 mt-2 bg-stone-400 rounded-full"></div>
               <div>
                 <span className="font-bold block text-stone-700">AI 模型</span>
                 <span className="text-sm text-stone-500">U2Net (分割), CLIP (語意), Naive Bayes (分類)</span>
               </div>
             </li>
           </ul>
        </div>

        <div className="bg-white p-8 rounded-2xl shadow-sm">
           <h3 className="text-xl font-bold text-stone-800 mb-6 flex items-center gap-2">
             <Icons.Cpu className="text-brand-500" /> 分割模型演進
           </h3>
           <div className="space-y-6 relative pl-4 border-l-2 border-stone-200">
             <div className="relative">
               <div className="absolute -left-[21px] top-1 w-4 h-4 rounded-full bg-stone-300 border-2 border-white"></div>
               <h4 className="font-bold text-stone-600">YOLO</h4>
               <p className="text-sm text-stone-500 mt-1">依人體關節切割，但包含過多背景雜訊。</p>
             </div>
             <div className="relative">
               <div className="absolute -left-[21px] top-1 w-4 h-4 rounded-full bg-stone-300 border-2 border-white"></div>
               <h4 className="font-bold text-stone-600">U2Net</h4>
               <p className="text-sm text-stone-500 mt-1">成功去除 95% 背景，但邊緣仍有殘色。</p>
             </div>
             <div className="relative">
               <div className="absolute -left-[21px] top-1 w-4 h-4 rounded-full bg-brand-500 border-2 border-white shadow-lg shadow-brand-200"></div>
               <h4 className="font-bold text-brand-600">U2Net + Erosion</h4>
               <p className="text-sm text-stone-500 mt-1">向內限縮遮罩，解決邊緣色彩干擾，大幅提升 CLIP 判斷準確率。</p>
             </div>
           </div>
        </div>
      </div>
    </div>
  </section>
);

const Future = () => (
  <section id="future" className="py-24 bg-gradient-to-br from-brand-600 to-brand-800 text-white text-center">
    <div className="max-w-4xl mx-auto px-4">
      <h2 className="text-3xl md:text-5xl font-bold mb-8">從數據洞察到商業價值</h2>
      <p className="text-brand-100 text-xl mb-16">我們的目標是將 Lookbook Studio 打造成時尚產業不可或缺的智慧決策中樞。</p>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 text-left">
        <div className="bg-white/10 backdrop-blur-sm p-8 rounded-2xl border border-white/20">
          <h3 className="text-2xl font-bold mb-4 text-brand-100">對消費者的價值</h3>
          <p className="leading-relaxed opacity-90">
            持續優化 AI 個人化推薦演算法，無縫整合購物車功能，打造從靈感到購買的完整線上體驗。
          </p>
        </div>
        <div className="bg-white/10 backdrop-blur-sm p-8 rounded-2xl border border-white/20">
          <h3 className="text-2xl font-bold mb-4 text-brand-100">對品牌的價值</h3>
          <p className="leading-relaxed opacity-90">
            提供更深度的趨勢預測模型，包含跨品類搭配組合分析與新興風格偵測，為設計、採購與行銷團隊提供更具前瞻性的決策支援。
          </p>
        </div>
      </div>
    </div>
  </section>
);

const Footer = () => (
  <footer className="bg-stone-900 text-stone-400 py-12">
    <div className="max-w-7xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
      <div className="flex items-center gap-2 mb-4 md:mb-0">
         <div className="w-6 h-6 bg-stone-700 rounded flex items-center justify-center text-white">
            <Icons.Shirt size={14} />
         </div>
         <span className="font-bold text-white">Lookbook Studio</span>
      </div>
      <div className="text-sm">
        &copy; {new Date().getFullYear()} Lookbook Studio. All rights reserved.
      </div>
    </div>
  </footer>
);

export default function App() {
  return (
    <div className="min-h-screen font-sans selection:bg-brand-500 selection:text-white">
      <Header />
      <Hero />
      <ProblemSection />
      <ConsumerEngine />
      <DataFlywheel />
      <BusinessEngine />
      <TechStack />
      <Future />
      <Footer />
    </div>
  );
}

// Helper to keep the file cleaner (though in a real app these would be separate files)
// Using DataFlywheel name to match the section content structure
const DataFlywheel = () => {
    return (
        <section className="bg-brand-600 text-white py-16">
            <div className="max-w-7xl mx-auto px-4 text-center">
               <h3 className="text-2xl font-bold mb-6">每一次互動，都成為商業洞察的燃料</h3>
               <div className="flex flex-col md:flex-row justify-center items-center gap-8 md:gap-16">
                  <div className="flex flex-col items-center gap-2">
                     <div className="w-16 h-16 rounded-full bg-white/20 flex items-center justify-center backdrop-blur-sm">
                        <Icons.Upload size={32} />
                     </div>
                     <span className="font-medium">Photo Upload</span>
                  </div>
                  <Icons.ArrowRight className="rotate-90 md:rotate-0 opacity-50" />
                  <div className="flex flex-col items-center gap-2">
                     <div className="w-16 h-16 rounded-full bg-white/20 flex items-center justify-center backdrop-blur-sm">
                        <Icons.Database size={32} />
                     </div>
                     <span className="font-medium">Data Repository</span>
                  </div>
                  <Icons.ArrowRight className="rotate-90 md:rotate-0 opacity-50" />
                  <div className="flex flex-col items-center gap-2">
                     <div className="w-16 h-16 rounded-full bg-white text-brand-600 flex items-center justify-center shadow-lg">
                        <Icons.BarChart size={32} />
                     </div>
                     <span className="font-bold text-lg">BI Dashboard</span>
                  </div>
               </div>
            </div>
        </section>
    );
};
