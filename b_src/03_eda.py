import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned data
file_path = "a_data/processed data/cleaned_online_retail.csv"
df = pd.read_csv(file_path)

print("Data Loaded:", df.shape)
df["Revenue"] = df["Quantity"] * df["Price"]

print(df.head())
top_products = df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(10)

print(top_products)
plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

os.makedirs("outputs/graphs", exist_ok=True)
plt.savefig("outputs/graphs/top_products.png")
plt.show()
top_countries = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10)

print(top_countries)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Revenue"].sum()

print(monthly_sales)
plt.figure(figsize=(10,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/graphs/monthly_sales.png")
plt.show()
top_customers = (
    df.groupby("Customer ID")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))
top_customers.plot(kind="bar", color="green")

plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("outputs/graphs/top_customers.png")
plt.show()

print("\nTop 10 Customers by Revenue")
print(top_customers)
top_quantity = (
    df.groupby("Description")["Quantity"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))
top_quantity.plot(kind="bar", color="orange")

plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("outputs/graphs/top_quantity_products.png")
plt.show()

print("\nTop 10 Products by Quantity Sold")
print(top_quantity)
plt.figure(figsize=(10,6))

revenue = df[df["Revenue"] < 500]["Revenue"]

plt.hist(revenue, bins=50)

plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("outputs/graphs/revenue_distribution.png")
plt.show()
plt.figure(figsize=(10,6))

quantity = df[df["Quantity"] < 100]["Quantity"]

plt.hist(quantity, bins=50)

plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("outputs/graphs/quantity_distribution.png")
plt.show
# Convert Invoice Date to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create Month column
df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

# Count unique orders each month
monthly_orders = (
    df.groupby("Month")["Invoice"]
      .nunique()
)

plt.figure(figsize=(12,6))
monthly_orders.plot(kind="line", marker="o")

plt.title("Monthly Orders")
plt.xlabel("Month")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.savefig("outputs/graphs/monthly_orders.png")
plt.show()

print("\nMonthly Orders")
print(monthly_orders)
top_countries = (
    df.groupby("Country")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))
top_countries.plot(kind="bar", color="purple")

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/graphs/top_countries.png")
plt.show()

print("\nTop 10 Countries by Revenue")
print(top_countries)
purchase_frequency = (
    df.groupby("Customer ID")["Invoice"]
      .nunique()
)

plt.figure(figsize=(10,6))

plt.hist(purchase_frequency, bins=30)

plt.title("Customer Purchase Frequency")
plt.xlabel("Number of Orders")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("outputs/graphs/purchase_frequency.png")
plt.show()

print("\nCustomer Purchase Frequency")
print(purchase_frequency.describe())
order_value = (
    df.groupby("Invoice")["Revenue"]
      .sum()
)

plt.figure(figsize=(10,6))

plt.hist(order_value, bins=30)

plt.title("Average Order Value")
plt.xlabel("Order Value")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.savefig("outputs/graphs/average_order_value.png")
plt.show()

print("\nAverage Order Value")
print(order_value.describe())
import seaborn as sns
df["Month"] = df["InvoiceDate"].dt.month
df["Day"] = df["InvoiceDate"].dt.day

heatmap_data = df.pivot_table(
    values="Revenue",
    index="Month",
    columns="Day",
    aggfunc="sum",
    fill_value=0
)

plt.figure(figsize=(14,6))

sns.heatmap(heatmap_data, cmap="YlGnBu")

plt.title("Sales Heatmap (Month vs Day)")
plt.xlabel("Day")
plt.ylabel("Month")

plt.tight_layout()
plt.savefig("outputs/graphs/sales_heatmap.png")
plt.show()
country_sales = (
    df.groupby("Country")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,6))

country_sales.plot(kind="barh", color="teal")

plt.title("Country-wise Sales")
plt.xlabel("Revenue")
plt.ylabel("Country")

plt.tight_layout()
plt.savefig("outputs/graphs/country_sales.png")
plt.show()

print("\nCountry-wise Sales")
print(country_sales)

