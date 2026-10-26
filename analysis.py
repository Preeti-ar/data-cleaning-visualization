"""
Data Cleaning & Visualization Project
Run: pip install -r requirements.txt
     python analysis.py
This project uses a sample sales dataset created for demonstration.
"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).parent
raw_file = BASE / "raw_sales_data.csv"
output_dir = BASE / "outputs"
output_dir.mkdir(exist_ok=True)

df = pd.read_csv(raw_file)
print("RAW DATA SHAPE:", df.shape)
print("\nMissing values before cleaning:\n", df.isna().sum())
print("\nDuplicate rows before cleaning:", df.duplicated().sum())

# Clean column names and date format
df.columns = df.columns.str.strip().str.replace(" ", "_")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Handle missing values
df["Units_Sold"] = df["Units_Sold"].fillna(df["Units_Sold"].median())
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].median())
df["City"] = df["City"].fillna("Unknown")

# Remove duplicate rows
df = df.drop_duplicates().copy()

# Ensure numeric columns are numeric and create a revenue feature
df["Units_Sold"] = pd.to_numeric(df["Units_Sold"], errors="coerce")
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

# Save cleaned data and summary
df.to_csv(output_dir / "cleaned_sales_data.csv", index=False)
summary = df.groupby("Product", as_index=False).agg(
    Units_Sold=("Units_Sold", "sum"),
    Revenue=("Revenue", "sum")
).sort_values("Revenue", ascending=False)
summary.to_csv(output_dir / "product_summary.csv", index=False)

print("\nCLEANED DATA SHAPE:", df.shape)
print("\nMissing values after cleaning:\n", df.isna().sum())
print("\nRevenue by product:\n", summary.to_string(index=False))
print("\nTotal revenue:", round(df["Revenue"].sum(), 2))

# Chart 1: revenue by product
plt.figure(figsize=(8, 5))
summary.sort_values("Revenue").plot(
    x="Product", y="Revenue", kind="bar", legend=False, color="steelblue"
)
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(output_dir / "revenue_by_product.png", dpi=150)
plt.close()

# Chart 2: units sold by city
city_sales = df.groupby("City")["Units_Sold"].sum().sort_values(ascending=False)
plt.figure(figsize=(7, 5))
city_sales.plot(kind="bar", color="seagreen")
plt.title("Units Sold by City")
plt.xlabel("City")
plt.ylabel("Units Sold")
plt.tight_layout()
plt.savefig(output_dir / "units_by_city.png", dpi=150)
plt.close()

print(f"\nFinished. Results are saved in: {output_dir}")
