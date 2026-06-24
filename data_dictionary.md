# Data Dictionary

## 1. fund_master / dim_fund
- amfi_code: Unique AMFI scheme code
- fund_house: Mutual fund company
- scheme_name: Scheme name
- category: Broad category
- sub_category: Scheme subtype
- plan: Regular or Direct plan
- launch_date: Launch date of scheme
- benchmark: Benchmark index
- expense_ratio_pct: Expense ratio in percent
- exit_load_pct: Exit load percent
- min_sip_amount: Minimum SIP amount
- min_lumpsum_amount: Minimum lump sum amount
- fund_manager: Fund manager name
- risk_category: Risk label
- sebi_category_code: SEBI scheme code

## 2. nav_history / fact_nav
- amfi_code: Scheme code
- date: NAV date
- nav: Net asset value

## 3. investor_transactions / fact_transactions
- investor_id: Unique investor ID
- transaction_date: Date of transaction
- amfi_code: Scheme code
- transaction_type: SIP, Lumpsum, Redemption
- amount_inr: Transaction amount
- state: Investor state
- city: Investor city
- city_tier: City tier
- age_group: Investor age group
- gender: Investor gender
- 