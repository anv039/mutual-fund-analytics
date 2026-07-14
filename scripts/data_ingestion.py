import pandas as pd
import os

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

data = {}

for f in files:
    path = os.path.join("data/raw", f)
    df = pd.read_csv(path)
    data[f] = df

    print(f"\n=== {f} ===")
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))
    print("Dtypes:\n", df.dtypes)
    print("Missing values:\n", df.isnull().sum())
    print("Head:\n", df.head())

fm = data["01_fund_master.csv"]
nav = data["02_nav_history.csv"]

print("\n--- Fund Master Exploration ---")
print("Fund Houses:", fm["fund_house"].unique())
print("Categories:", fm["category"].unique())
print("Sub-categories:", fm["sub_category"].unique())
print("Risk Grades:", fm["risk_category"].unique())

fm_codes = set(fm["amfi_code"].dropna().unique())
nav_codes = set(nav["amfi_code"].dropna().unique())
missing = fm_codes - nav_codes

print(f"\nMissing codes in nav_history: {len(missing)}")
print(missing if missing else "All codes matched ✅")

print("\n--- Data Quality Summary ---")
print(f"Fund master entries: {len(fm)}")
print(f"NAV history entries: {len(nav)}")
print(f"Missing AMFI codes: {len(missing)}")
summary = f"""
Data Quality Summary
--------------------
Fund master entries: {len(fm)}
NAV history entries: {len(nav)}
Missing AMFI codes: {len(missing)}
Missing values in monthly SIP inflows:
{pd.read_csv("data/raw/04_monthly_sip_inflows.csv").isnull().sum()}
"""

with open("reports/data_quality_summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print("\nSaved summary to reports/data_quality_summary.txt")