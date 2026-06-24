import pandas as pd
import os

raw_path = "data/raw"
processed_path = "data/processed"
os.makedirs(processed_path, exist_ok=True)

nav = pd.read_csv(f"{raw_path}/02_nav_history.csv")
nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav = nav.drop_duplicates()
nav = nav[nav["nav"] > 0]

nav.to_csv(f"{processed_path}/nav_history_cleaned.csv", index=False)

print("NAV cleaned:", nav.shape)
print(nav.head())


inv = pd.read_csv(f"{raw_path}/08_investor_transactions.csv")

inv["transaction_date"] = pd.to_datetime(inv["transaction_date"], errors="coerce")
inv["transaction_type"] = inv["transaction_type"].str.strip().str.title()
inv["kyc_status"] = inv["kyc_status"].str.strip().str.title()

inv = inv[inv["amount_inr"] > 0]
inv = inv.drop_duplicates()

inv.to_csv(f"{processed_path}/investor_transactions_cleaned.csv", index=False)

print("Investor transactions cleaned:", inv.shape)
print(inv.head())

perf = pd.read_csv(f"{raw_path}/07_scheme_performance.csv")

num_cols = [
    "return_1yr_pct", "return_3yr_pct", "return_5yr_pct",
    "benchmark_3yr_pct", "alpha", "beta", "sharpe_ratio",
    "sortino_ratio", "std_dev_ann_pct", "max_drawdown_pct",
    "aum_crore", "expense_ratio_pct", "morningstar_rating"
]

for col in num_cols:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

perf = perf.drop_duplicates()
perf = perf[(perf["expense_ratio_pct"] >= 0.1) & (perf["expense_ratio_pct"] <= 2.5)]

perf.to_csv(f"{processed_path}/scheme_performance_cleaned.csv", index=False)

print("Scheme performance cleaned:", perf.shape)
print(perf.head())