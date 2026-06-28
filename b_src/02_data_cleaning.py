import pandas as pd
import os

# Load dataset
file_path = "data/raw data/online_retail_II.xlsx/online_retail_II.xlsx.xlsx"
df = pd.read_excel(file_path)

print("Original Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)
df = df.dropna(subset=["Customer ID"])

print("Shape after removing missing Customer IDs:", df.shape)
df = df[~df["Invoice"].astype(str).str.startswith("C")]

print("Shape after removing cancelled orders:", df.shape)
df = df[df["Quantity"] > 0]

print("Shape after removing invalid quantities:", df.shape)
df = df[df["Price"] > 0]

print("Shape after removing invalid prices:", df.shape)
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print(df.dtypes)
os.makedirs("data/processed data", exist_ok=True)

df.to_csv("data/processed data/cleaned_online_retail.csv", index=False)

print("\n✅ Cleaned dataset saved successfully!")