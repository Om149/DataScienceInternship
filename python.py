import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
print(df.head())

print("Rows and columns:", df.shape)
df.info()

print("Missing values by column:")
print(df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())
 
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
print(df.dtypes)
df = df.drop_duplicates()
df = df.dropna(subset=["OrderDate", "Quantity", "UnitPrice", "Product", "CustomerID"])
df = df[(df["Quantity"] >= 0) & (df["UnitPrice"] >= 0)]
print("Rows after cleaning:", len(df))
 
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
print(df[["OrderID", "Product", "Quantity", "UnitPrice", "Revenue"]].head())
 

df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)
monthly_revenue = df.groupby("Month", as_index=False)["Revenue"].sum()
print(monthly_revenue)
plt.figure(figsize=(7, 4))
plt.plot(monthly_revenue["Month"], monthly_revenue["Revenue"], marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
