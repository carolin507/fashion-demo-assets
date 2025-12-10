# pages/dashboard_trend_analysis.py
import streamlit as st
import pandas as pd
import plotly.express as px
from modules.analytics.insights.sales_insights import _fmt_pct
WARM = ["#FF5A5F", "#F97316", "#E9C46A", "#F4A261", "#FB7185", "#F59E0B"]


@st.cache_data
def load_trend_data():
    """Load look data and flatten top/bottom fields."""
    df = pd.read_json("data/verified_photo_data.json")

    if {"top", "bottom"}.issubset(df.columns):
        top_df = pd.json_normalize(df["top"]).add_prefix("top_")
        bottom_df = pd.json_normalize(df["bottom"]).add_prefix("bottom_")
        df = pd.concat(
            [df.drop(columns=["top", "bottom"]), top_df, bottom_df],
            axis=1,
        )

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        df["year_month"] = df["date"].dt.to_period("M").astype(str)

    return df


def _counts(series: pd.Series, top_n: int = 10):
    if series is None or series.empty:
        return pd.DataFrame(columns=["value", "count"])
    vc = series.dropna().value_counts().reset_index()
    vc.columns = ["value", "count"]
    return vc.head(top_n)


def _pair_counts(df: pd.DataFrame, left: str, right: str, top_n: int = 10):
    if left not in df.columns or right not in df.columns:
        return pd.DataFrame(columns=["pair", "count"])
    pairs = df[[left, right]].dropna()
    if pairs.empty:
        return pd.DataFrame(columns=["pair", "count"])
    pairs["pair"] = pairs[left].astype(str) + " / " + pairs[right].astype(str)
    vc = pairs["pair"].value_counts().reset_index()
    vc.columns = ["pair", "count"]
    return vc.head(top_n)


def render_trend_analysis():
    ACCENT = "#FF5A5F"
    SAND = "#F9F5F0"
    INK = "#1C1917"
    MUTED = "#78716C"
    px.defaults.color_discrete_sequence = WARM
    px.defaults.color_continuous_scale = "OrRd"

    st.markdown(
        f"""
        <style>
          .block-container {{
            padding-top: 1.2rem;
            padding-bottom: 1.2rem;
            background: {SAND};
          }}
          h3, h4 {{ color: {INK}; font-family: 'Noto Sans TC', 'Inter', sans-serif; }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("## 色彩潮流分析 Trend Analysis")
    df = load_trend_data()

    def _metric_card(label: str, value: str, helper: str | None = None):
        st.markdown(
            f"""
            <div style="
                background:white;
                border:1px solid #E7E5E4;
                border-radius:14px;
                padding:16px 18px;
                box-shadow:0 12px 32px rgba(0,0,0,0.05);
                min-height:120px;
            ">
                <div style="font-size:13px;color:{MUTED};text-transform:uppercase;letter-spacing:0.08em;">{label}</div>
                <div style="font-size:26px;font-weight:700;color:{INK};margin-top:6px;">{value}</div>
                {f'<div style="margin-top:4px;color:#A8A29E;font-size:12px;">{helper}</div>' if helper else ''}
            </div>
            """,
            unsafe_allow_html=True,
        )

    # KPI cards
    st.markdown("#### 潮流概覽 KPI")
    looks = len(df)
    top_color_mode = df["top_color"].mode()[0] if "top_color" in df.columns and not df["top_color"].dropna().empty else "-"
    bottom_color_mode = df["bottom_color"].mode()[0] if "bottom_color" in df.columns and not df["bottom_color"].dropna().empty else "-"
    top_style_mode = df["top_style"].mode()[0] if "top_style" in df.columns and not df["top_style"].dropna().empty else "-"
    bottom_style_mode = df["bottom_style"].mode()[0] if "bottom_style" in df.columns and not df["bottom_style"].dropna().empty else "-"

    k1, k2, k3, k4 = st.columns(4, gap="medium")
    with k1:
        _metric_card("樣本數", f"{looks:,}", helper="looks in dataset")
    with k2:
        _metric_card("上身熱門色", top_color_mode, helper="top_color")
    with k3:
        _metric_card("下身熱門色", bottom_color_mode, helper="bottom_color")
    with k4:
        _metric_card("熱門風格", f"{top_style_mode} / {bottom_style_mode}", helper="Top / Bottom style")

    # Core insights (簡易自動摘要 + 行動)
    color_pairs = _pair_counts(df, "top_color", "bottom_color")
    style_pairs = _pair_counts(df, "top_style", "bottom_style")
    cat_pairs = _pair_counts(df, "top_category", "bottom_category")
    core_insights = []
    actions = []
    if top_color_mode != "-":
        core_insights.append(f"上身主力色為 {top_color_mode}；下身主力色為 {bottom_color_mode}。")
        actions.append("以熱門色為主題做穿搭範例，或增加該色庫存/曝光。")
    if not color_pairs.empty:
        best_pair = color_pairs.iloc[0]
        share = _fmt_pct(best_pair["count"], len(df)*2 if len(df) else best_pair["count"])
        core_insights.append(f"最常見色彩搭配：{best_pair['pair']}（占比 {share}）。")
        actions.append("將常見色彩搭配做 Lookbook/促案，讓用戶快速套用。")
    if not style_pairs.empty:
        core_insights.append(f"熱門風格搭配：{style_pairs.iloc[0]['pair']}。")
        actions.append("在熱門風格搭配上加碼新品、版型或素材敘事。")
    if not cat_pairs.empty:
        core_insights.append(f"熱門品類搭配：{cat_pairs.iloc[0]['pair']}。")
        actions.append("針對熱門品類搭配推薦相關單品組合，提升連帶購買。")

    def _insight_box(title: str, lines: list[str]) -> None:
        if not lines:
            return
        st.markdown(
            f"""
            <div style="
                margin-top:10px;
                padding:12px 14px;
                border:1px solid #E7E5E4;
                border-radius:12px;
                background:#FFFBEB;
            ">
              <div style="font-size:12px;color:{MUTED};letter-spacing:0.08em;text-transform:uppercase;">{title}</div>
              <ul style="margin:6px 0 0 18px;color:{INK};font-size:13px;line-height:1.5;">
                {"".join(f"<li>{line}</li>" for line in lines)}
              </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    _insight_box("Core Insights", core_insights)
    _insight_box("Action Plan", actions)

    st.markdown("---")

    # Color distributions
    st.markdown("#### 上身 / 下身色彩分佈")
    col_ct, col_cb = st.columns(2)
    with col_ct:
        fig_top_color = px.pie(
            _counts(df.get("top_color")),
            names="value",
            values="count",
            color_discrete_sequence=WARM,
        )
        fig_top_color.update_traces(textinfo="percent+label")
        fig_top_color.update_layout(title="上身色彩", margin=dict(l=10, r=10, t=40, b=10), paper_bgcolor="white")
        st.plotly_chart(fig_top_color, use_container_width=True)
    with col_cb:
        fig_bottom_color = px.pie(
            _counts(df.get("bottom_color")),
            names="value",
            values="count",
            color_discrete_sequence=WARM,
        )
        fig_bottom_color.update_traces(textinfo="percent+label")
        fig_bottom_color.update_layout(title="下身色彩", margin=dict(l=10, r=10, t=40, b=10), paper_bgcolor="white")
        st.plotly_chart(fig_bottom_color, use_container_width=True)

    # Monthly color trend
    st.markdown("#### 色系潮流趨勢（按月）")
    if "year_month" in df.columns and not df["year_month"].dropna().empty:
        combined_color = pd.concat(
            [
                df[["year_month", "top_color"]].rename(columns={"top_color": "color"}),
                df[["year_month", "bottom_color"]].rename(columns={"bottom_color": "color"}),
            ],
            ignore_index=True,
        ).dropna()
        if not combined_color.empty:
            top5_colors = combined_color["color"].value_counts().head(5).index
            trend = (
                combined_color[combined_color["color"].isin(top5_colors)]
                .groupby(["year_month", "color"])
                .size()
                .reset_index(name="count")
            )
            fig_trend = px.area(
                trend,
                x="year_month",
                y="count",
                color="color",
                title="Top 5 色系月度出現次數",
            )
            fig_trend.update_layout(
                xaxis_title="月份",
                yaxis_title="出現次數",
                plot_bgcolor="white",
                paper_bgcolor="white",
                margin=dict(l=10, r=10, t=40, b=40),
            )
            st.plotly_chart(fig_trend, use_container_width=True)
        else:
            st.info("無法取得色彩趨勢資料。")
    else:
        st.info("缺少日期欄位，無法計算月度色彩趨勢。")

    st.markdown("---")

    # Color pairing
    st.markdown("#### 上下身色彩搭配 Top 10")
    color_pairs = _pair_counts(df, "top_color", "bottom_color")
    if color_pairs.empty:
        st.info("目前沒有可用的色彩搭配資料。")
    else:
        fig_pair = px.bar(
            color_pairs,
            x="count",
            y="pair",
            orientation="h",
            text="count",
            color_discrete_sequence=[ACCENT],
        )
        fig_pair.update_traces(textposition="outside")
        fig_pair.update_layout(
            xaxis_title="出現次數",
            yaxis_title="色彩搭配（上 / 下）",
            margin=dict(l=10, r=40, t=20, b=10),
            plot_bgcolor="white",
            paper_bgcolor="white",
        )
        st.plotly_chart(fig_pair, use_container_width=True)

    st.markdown("---")

    # Style & Category
    st.markdown("#### 上身 / 下身風格與品類")
    sc1, sc2 = st.columns(2)
    with sc1:
        fig_ts = px.pie(
            _counts(df.get("top_style")),
            names="value",
            values="count",
            color_discrete_sequence=WARM,
        )
        fig_ts.update_traces(textinfo="percent+label")
        fig_ts.update_layout(title="上身風格", margin=dict(l=10, r=10, t=40, b=10), paper_bgcolor="white")
        st.plotly_chart(fig_ts, use_container_width=True)
    with sc2:
        fig_bs = px.pie(
            _counts(df.get("bottom_style")),
            names="value",
            values="count",
            color_discrete_sequence=WARM,
        )
        fig_bs.update_traces(textinfo="percent+label")
        fig_bs.update_layout(title="下身風格", margin=dict(l=10, r=10, t=40, b=10), paper_bgcolor="white")
        st.plotly_chart(fig_bs, use_container_width=True)

    st.markdown("##### 風格搭配 Top 10")
    style_pairs = _pair_counts(df, "top_style", "bottom_style")
    if style_pairs.empty:
        st.info("目前沒有可用的風格搭配資料。")
    else:
        fig_style_pair = px.bar(
            style_pairs,
            x="count",
            y="pair",
            orientation="h",
            text="count",
            color_discrete_sequence=["#3B82F6"],
        )
        fig_style_pair.update_traces(textposition="outside")
        fig_style_pair.update_layout(
            xaxis_title="出現次數",
            yaxis_title="風格搭配（上 / 下）",
            margin=dict(l=10, r=40, t=20, b=10),
            plot_bgcolor="white",
            paper_bgcolor="white",
        )
        st.plotly_chart(fig_style_pair, use_container_width=True)

    st.markdown("##### 品類搭配 Top 10")
    cat_pairs = _pair_counts(df, "top_category", "bottom_category")
    if cat_pairs.empty:
        st.info("目前沒有可用的品類搭配資料。")
    else:
        fig_cat_pair = px.bar(
            cat_pairs,
            x="count",
            y="pair",
            orientation="h",
            text="count",
            color_discrete_sequence=["#10B981"],
        )
        fig_cat_pair.update_traces(textposition="outside")
        fig_cat_pair.update_layout(
            xaxis_title="出現次數",
            yaxis_title="品類搭配（上 / 下）",
            margin=dict(l=10, r=40, t=20, b=10),
            plot_bgcolor="white",
            paper_bgcolor="white",
        )
        st.plotly_chart(fig_cat_pair, use_container_width=True)

# Alias for legacy import
def render_color_trends():
    return render_trend_analysis()
