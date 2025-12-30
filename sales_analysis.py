import pandas as pd
import matplotlib.pyplot as plt

# 1. Read Excel file
df = pd.read_excel("sales_data.xlsx")

# 2. Calculate Total Sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# 3. Grouping (Analysis)
product_sales = df.groupby("Product")["Total_Sales"].sum()
region_sales = df.groupby("Region")["Total_Sales"].sum()
category_sales = df.groupby("category")["Total_Sales"].sum()

# 4. Print results (for understanding)
print("Product-wise Sales:")
print(product_sales)

print("\nRegion-wise Sales:")
print(region_sales)

print("\nCategory-wise Sales:")
print(category_sales)

# 5. Create side-by-side bar charts
plt.figure(figsize=(15, 5))

# Product-wise chart
plt.subplot(1, 3, 1)
product_sales.plot(kind="bar")
plt.title("Product-wise Total Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")

# Region-wise chart
plt.subplot(1, 3, 2)
region_sales.plot(kind="bar")
plt.title("Region-wise Total Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")

# Category-wise chart
plt.subplot(1, 3, 3)
category_sales.plot(kind="bar")
plt.title("Category-wise Total Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")

# Adjust layout and show all charts together
plt.tight_layout()
plt.show()
