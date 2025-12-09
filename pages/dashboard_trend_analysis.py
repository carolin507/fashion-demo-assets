# pages/dashboard_trend_analysis.py

import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def load_trend_data():
    # Load structured JSON then flatten nested top/bottom fields so downstream
    # code still sees top_color/top_style/top_category columns.
    df = pd.read_json("data/verified_photo_data.json")

    if {"top", "bottom"}.issubset(df.columns):
        top_df = pd.json_normalize(df["top"]).add_prefix("top_")
        bottom_df = pd.json_normalize(df["bottom"]).add_prefix("bottom_")
        df = pd.concat(
            [df.drop(columns=["top", "bottom"]), top_df, bottom_df],
            axis=1,
        )

    return df


def _combine_columns(df: pd.DataFrame, columns):
    """Combine multiple columns into one Series, skipping missing columns."""
    series_list = [df[col] for col in columns if col in df.columns]
    if not series_list:
        return pd.Series(dtype=object)
    return pd.concat(series_list, ignore_index=True).dropna()


def generate_insights(df: pd.DataFrame):
    insights = []

    color_series = _combine_columns(df, ["top_color", "bottom_color"])
    style_series = _combine_columns(df, ["top_style", "bottom_style"])
    category_series = _combine_columns(df, ["top_category", "bottom_category"])

    if not color_series.empty:
        top_color = color_series.value_counts().idxmax()
        color_ratio = color_series.value_counts(normalize=True).max() * 100
        insights.append(f"近來最熱主色系為 **{top_color}**（佔比{color_ratio:.1f}%）")

    if not style_series.empty:
        top_style = style_series.value_counts().idxmax()
        insights.append(f"常見的風格元素為 **{top_style}**，顯示穿搭細節偏好正在轉向")

    if not category_series.empty:
        top_cat = category_series.value_counts().idxmax()
        insights.append(f"在單品中，**{top_cat}** 出現比例較高，可能受季節或情境影響")

    return insights


def render_trend_analysis():

    st.markdown("## 穿搭潮流洞察 Trend Analysis")
    df = load_trend_data()

    # =========================
    # KPI 區塊
    # =========================
    st.subheader("本期潮流觀測 KPI")

    c1, c2, c3 = st.columns(3)

    color_series = _combine_columns(df, ["top_color", "bottom_color"])
    style_series = _combine_columns(df, ["top_style", "bottom_style"])
    category_series = _combine_columns(df, ["top_category", "bottom_category"])

    top_color = color_series.value_counts().idxmax() if not color_series.empty else "-"
    top_style = style_series.value_counts().idxmax() if not style_series.empty else "-"
    top_cat = category_series.value_counts().idxmax() if not category_series.empty else "-"

    c1.metric("主色系", top_color)
    c2.metric("風格元素", top_style)
    c3.metric("最高出現類別", top_cat)

    st.markdown("---")

    # =========================
    # 色彩趨勢
    # =========================
    st.subheader("色彩趨勢 Color Trends")

    if color_series.empty:
        st.info("無色彩資料可供統計。")
    else:
        color_counts = color_series.value_counts().reset_index()
        color_counts.columns = ["color", "count"]

        fig_color = px.bar(
            color_counts,
            x="color",
            y="count",
            title="Color Popularity",
            text_auto=True
        )
        st.plotly_chart(fig_color, use_container_width=True)

    st.markdown("---")

    # =========================
    # 圖案趨勢
    # =========================
    st.subheader("紋理／風格趨勢 Pattern Trends")

    if style_series.empty:
        st.info("無風格／紋理資料可供統計。")
    else:
        pattern_counts = style_series.value_counts().reset_index()
        pattern_counts.columns = ["pattern", "count"]

        fig_pattern = px.pie(
            pattern_counts,
            names="pattern",
            values="count",
            title="Pattern Distribution",
        )
        st.plotly_chart(fig_pattern, use_container_width=True)

    st.markdown("---")

    # =========================
    # 類別趨勢
    # =========================
    st.subheader("品類趨勢 Category Trends")

    if category_series.empty:
        st.info("無品類資料可供統計。")
    else:
        cat_counts = category_series.value_counts().reset_index()
        cat_counts.columns = ["category", "count"]

        fig_cat = px.bar(
            cat_counts,
            x="category",
            y="count",
            title="Category Frequency",
            text_auto=True
        )
        fig_cat.update_layout(xaxis_tickangle=-45)

        st.plotly_chart(fig_cat, use_container_width=True)

    st.markdown("---")

    # =========================
    # AI 洞察
    # =========================
    st.subheader("AI 趨勢洞察 Trend Insights")

    insights = generate_insights(df)
    if not insights:
        st.info("暫無足夠資料產生洞察。")
    else:
        for i in insights:
            st.markdown(f"- {i}")


# Alias to match existing imports in app.py and ai-optimization.py
def render_color_trends():
    return render_trend_analysis()
