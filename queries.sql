-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT substr(date, 1, 7) AS month, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY substr(date, 1, 7)
ORDER BY month;

-- 3. Transactions by state
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 4. Funds with expense ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Top 5 funds by 3-year return
SELECT scheme_name, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- 6. Top 5 funds by Sharpe ratio
SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 7. Fund houses with most schemes
SELECT fund_house, COUNT(*) AS schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY schemes DESC;

-- 8. NAV rows by fund
SELECT amfi_code, COUNT(*) AS nav_rows
FROM fact_nav
GROUP BY amfi_code
ORDER BY nav_rows DESC;

-- 9. Transactions by type
SELECT transaction_type, COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total DESC;

-- 10. Average NAV by fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC;