# Import required libraries
import os
import pandas as pd

# This automatically finds where your script is running from
file_path = r"C:\Users\hp\OneDrive\Desktop\Customer Purchase Pattern Analysis\data\raw data\online_retail_II.xlsx\online_retail_II.xlsx.xlsx"
# Load Excel file
df = pd.read_excel(file_path)

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Dataset shape
print("\nRows and Columns:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical summary
print("\nSummary Statistics:")
print(df.describe())
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
print("\nSummary Statistics:")
print(df.describe())
import os

# Create reports folder if it doesn't exist
os.makedirs("outputs/reports", exist_ok=True)

# Save summary statistics
summary = df.describe(include="all")
summary.to_csv("outputs/reports/summary_statistics.csv")

print("✅ Summary statistics saved successfully!")
missing = df.isnull().sum()
missing.to_csv("outputs/reports/missing_values.csv")

print("✅ Missing values report saved!")
dtypes = df.dtypes
dtypes.to_csv("outputs/reports/data_types.csv")

print("✅ Data types saved!")
