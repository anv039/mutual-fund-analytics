import pandas as pd
import numpy as np

def recommend_funds(risk_appetite, n=3):
    """
    risk_appetite: 'Low', 'Moderate', or 'High'
    Maps to risk_grade values in scheme_performance.csv:
      Low -> 'Low'
      Moderate -> 'Moderate' or 'Moderately High'
      High -> 'High' or 'Very High'
    Returns top n funds by Sharpe ratio within matching risk_grade.
    """
    nav = pd.read_csv("data/processed/nav_history_cleaned.csv", parse_dates=["date"])
    nav = nav.sort_values(["amfi_code","date"])
    nav["daily_return"] = nav.groupby("amfi_code")["nav"].pct_change()

    fm = pd.read_csv("data/raw/01_fund_master.csv")
    sp = pd.read_csv("data/raw/07_scheme_performance.csv")

    Rf = 0.065
    sharpe_rows = []
    for code, g in nav.groupby("amfi_code"):
        r = g["daily_return"].dropna()
        ann_return = r.mean() * 252
        ann_std = r.std() * np.sqrt(252)
        sharpe = (ann_return - Rf) / ann_std if ann_std > 0 else np.nan
        sharpe_rows.append({"amfi_code": code, "sharpe_ratio": sharpe})
    sharpe_df = pd.DataFrame(sharpe_rows)

    risk_map = {
        "Low": ["Low"],
        "Moderate": ["Moderate", "Moderately High"],
        "High": ["High", "Very High"],
    }
    if risk_appetite not in risk_map:
        raise ValueError("risk_appetite must be one of: Low, Moderate, High")

    grades = risk_map[risk_appetite]
    matched = sp[sp["risk_grade"].isin(grades)][["amfi_code","scheme_name","risk_grade"]]
    matched = matched.merge(sharpe_df, on="amfi_code")
    top_n = matched.sort_values("sharpe_ratio", ascending=False).head(n)

    print(f"\nTop {n} funds for '{risk_appetite}' risk appetite:")
    print(top_n[["scheme_name","risk_grade","sharpe_ratio"]].to_string(index=False))
    return top_n

if __name__ == "__main__":
    recommend_funds("Moderate")
    