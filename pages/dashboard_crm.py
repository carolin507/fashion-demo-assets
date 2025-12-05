# pages/dashboard_crm.py

import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def load_crm_data():
    """讀取在 rfm_engine 匯出的處理後資料"""
    rfm = pd.read_csv("data/processed/crm/customers_rfm.csv")
    sales_full = pd.read_csv("data/processed/crm/sales_full.csv")

    # 轉日期格式（若存在）
    if "sale_date_order" in sales_full.columns:
        sales_full["sale_date_order"] = pd.to_datetime(sales_full["sale_date_order"])

    return rfm, sales_full


def render_crm_dashboard():
    """主渲染函式：CRM & 會員洞察 Dashboard"""
    rfm, sales_full = load_crm_data()

    st.markdown("## 📊 CRM & 會員洞察 Dashboard")

    # ------------------------------------------------------
    # KPI 區塊
    # ------------------------------------------------------
    st.subheader("📌 關鍵會員指標 KPI")

    total_customers = rfm["customer_id"].nunique()
    vip_count = (rfm["segment"] == "VIP / Champions").sum()
    avg_monetary = round(rfm["monetary"].mean(), 2)

    col1, col2, col3 = st.columns(3)
    col1.metric("總顧客數", f"{total_customers:,}")
    col2.metric("VIP 顧客數", f"{vip_count} ({vip_count / total_customers:.1%})")
    col3.metric("平均消費金額 (Monetary)", f"${avg_monetary:,.0f}")

    st.markdown("---")

    # ------------------------------------------------------
    # RFM Segment 分布
    # ------------------------------------------------------
    st.subheader("🎯 RFM 顧客分群分布")

    seg_counts = rfm["segment"].value_counts().reset_index()
    seg_counts.columns = ["segment", "count"]

    fig_seg = px.bar(
        seg_counts,
        x="segment",
        y="count",
        color="segment",
        text="count",
        title="RFM Segment 顧客數量",
    )
    fig_seg.update_layout(xaxis_title="", yaxis_title="顧客數")
    st.plotly_chart(fig_seg, use_container_width=True)

    st.markdown("---")

    # ------------------------------------------------------
    # 國家分布
    # ------------------------------------------------------
    if "country" in rfm.columns:
        st.subheader("🌍 顧客國家分布")

        country_counts = rfm["country"].value_counts().reset_index()
        country_counts.columns = ["country", "count"]

        fig_country = px.choropleth(
            country_counts,
            locations="country",
            locationmode="country names",
            color="count",
            title="Customer Distribution by Country",
            color_continuous_scale="Blues",
        )
        st.plotly_chart(fig_country, use_container_width=True)

        st.markdown("---")

    # ------------------------------------------------------
    # 年齡區間 vs Segment
    # ------------------------------------------------------
    if "age_range" in rfm.columns:
        st.subheader("👥 年齡區間 × 顧客分群")

        fig_age = px.histogram(
            rfm,
            x="age_range",
            color="segment",
            barmode="group",
            title="Age Range by RFM Segment",
        )
        fig_age.update_layout(xaxis_title="年齡區間", yaxis_title="顧客數")
        st.plotly_chart(fig_age, use_container_width=True)

        st.markdown("---")

    # ------------------------------------------------------
    # 熱銷商品 Top 10
    # ------------------------------------------------------
    st.subheader("🛍 熱銷商品 Top 10")

    if "product_name" in sales_full.columns:
        top_products = (
            sales_full.groupby("product_name")["item_total"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        fig_top = px.bar(
            top_products,
            x="product_name",
            y="item_total",
            title="Top 10 Best-Selling Products (by Revenue)",
        )
        fig_top.update_layout(
            xaxis_title="商品名稱",
            yaxis_title="銷售額",
            xaxis_tickangle=-30,
        )
        st.plotly_chart(fig_top, use_container_width=True)
    else:
        st.info("sales_full 裡沒有 product_name 欄位，之後可再補上商品名稱維度。")

    st.markdown("---")

    # ------------------------------------------------------
    # 渠道表現
    # ------------------------------------------------------
    if "channel_order" in sales_full.columns:
        st.subheader("📱 銷售渠道表現")

        fig_channel = px.histogram(
            sales_full,
            x="channel_order",
            color="channel_order",
            title="Order Count by Channel",
        )
        fig_channel.update_layout(xaxis_title="渠道", yaxis_title="訂單數")
        st.plotly_chart(fig_channel, use_container_width=True)
