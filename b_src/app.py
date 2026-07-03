import plotly.express as px
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Purchase Pattern Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Purchase Pattern Analysis")
st.write("Interactive Data Analytics Dashboard")

df = pd.read_csv("a_data/processed data/cleaned_online_retail.csv")
df['Revenue'] = df['Quantity'] * df['Price']
st.sidebar.title("Filters")

country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df["Country"].unique().tolist())
)

if country != "All":
    df = df[df["Country"] == country]

total_revenue = df["Revenue"].sum()
total_customers = df["Customer ID"].nunique()
total_orders = df["Invoice"].nunique()
total_quantity = df["Quantity"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Revenue", f"${total_revenue:,.0f}")
col2.metric("Customers", total_customers)
col3.metric("Orders", total_orders)
col4.metric("Quantity Sold", f"{total_quantity:,.0f}")

st.subheader("Dataset Preview")
st.dataframe(df)
st.subheader("📈 Monthly Revenue Trend")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Month"] = df["InvoiceDate"].dt.strftime("%b")

monthly = df.groupby("Month")["Revenue"].sum()

monthly_df = monthly.reset_index()

fig = px.line(
    monthly_df,
    x="Month",
    y="Revenue",
    markers=True,
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("🌍 Top 10 Countries")

country = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10)

country_df = country.reset_index()

fig = px.bar(
    country_df,
    x="Country",
    y="Revenue",
    title="Revenue by Country"
)

st.plotly_chart(fig, use_container_width=True)
st.subheader("🏆 Top 10 Products")

products = df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(10)

st.bar_chart(products)
st.subheader("💰 Top 10 Customers by Revenue")

top_customers = (
    df.groupby("Customer ID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_customers)
st.subheader("📌 Business Insights")

st.success(f"💵 Total Revenue: ${total_revenue:,.2f}")
st.info(f"👥 Total Customers: {total_customers}")
st.warning(f"🛒 Total Orders: {total_orders}")
st.write(f"📦 Total Quantity Sold: {total_quantity:,.0f}")
st.set_page_config(
    page_title="Customer Purchase Dashboard",
    page_icon="📊",
    layout="wide"
)
st.subheader("Revenue Distribution")

fig = px.pie(
    country_df,
    names="Country",
    values="Revenue"
)

st.plotly_chart(fig, use_container_width=True)