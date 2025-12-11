import React from 'react';
import { 
  AreaChart, 
  Area, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer,
  BarChart,
  Bar,
  Cell,
  PieChart,
  Pie
} from 'recharts';

// Color Trend Data
const trendData = [
  { month: '1月', value: 4000 },
  { month: '2月', value: 3000 },
  { month: '3月', value: 2000 },
  { month: '4月', value: 2780 },
  { month: '5月', value: 1890 },
  { month: '6月', value: 2390 },
  { month: '7月', value: 3490 },
];

// Sentiment Data
const sentimentData = [
  { name: '版型極佳', score: 85 },
  { name: '材質舒適', score: 72 },
  { name: '出貨快速', score: 60 },
  { name: '顏色色差', score: 20 },
  { name: '尺寸偏小', score: 35 },
];

const COLORS = ['#be123c', '#fb7185', '#e5e7eb', '#fecdd3', '#9f1239'];

export const TrendChart = () => (
  <div className="h-64 w-full bg-white p-4 rounded-xl shadow-sm border border-stone-100">
    <h3 className="text-sm font-semibold text-stone-600 mb-4">色彩趨勢分析 (Color Trends)</h3>
    <ResponsiveContainer width="100%" height="100%">
      <AreaChart data={trendData}>
        <defs>
          <linearGradient id="colorValue" x1="0" y1="0" x2="0" y2="1">
            <stop offset="5%" stopColor="#f43f5e" stopOpacity={0.8}/>
            <stop offset="95%" stopColor="#f43f5e" stopOpacity={0}/>
          </linearGradient>
        </defs>
        <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e5e5e5"/>
        <XAxis dataKey="month" axisLine={false} tickLine={false} tick={{fontSize: 12, fill: '#666'}} />
        <YAxis axisLine={false} tickLine={false} tick={{fontSize: 12, fill: '#666'}} />
        <Tooltip contentStyle={{ borderRadius: '8px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }} />
        <Area type="monotone" dataKey="value" stroke="#f43f5e" fillOpacity={1} fill="url(#colorValue)" />
      </AreaChart>
    </ResponsiveContainer>
  </div>
);

export const SentimentChart = () => (
  <div className="h-64 w-full bg-white p-4 rounded-xl shadow-sm border border-stone-100">
    <h3 className="text-sm font-semibold text-stone-600 mb-4">顧客評論與 VOC 分析</h3>
    <ResponsiveContainer width="100%" height="100%">
      <BarChart layout="vertical" data={sentimentData}>
        <CartesianGrid strokeDasharray="3 3" horizontal={true} vertical={false} stroke="#e5e5e5" />
        <XAxis type="number" hide />
        <YAxis dataKey="name" type="category" width={70} tick={{fontSize: 11}} axisLine={false} tickLine={false} />
        <Tooltip cursor={{fill: 'transparent'}} />
        <Bar dataKey="score" radius={[0, 4, 4, 0]}>
           {sentimentData.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={entry.score > 50 ? '#f43f5e' : '#9ca3af'} />
            ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  </div>
);

export const KpiCard = ({ title, value, change }: { title: string, value: string, change: string }) => (
  <div className="bg-white p-4 rounded-xl shadow-sm border border-stone-100 flex flex-col justify-between">
    <span className="text-xs text-stone-500 font-medium uppercase tracking-wider">{title}</span>
    <div className="flex items-end justify-between mt-2">
      <span className="text-2xl font-bold text-stone-800">{value}</span>
      <span className="text-xs font-semibold text-green-600 bg-green-50 px-2 py-1 rounded-full">{change}</span>
    </div>
  </div>
);
