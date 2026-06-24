import pandas as pd
from sqlalchemy import create_engine, event
from sqlite3 import Connection as SQLite3Connection
import sqlite3
import os

@event.listens_for(create_engine("sqlite:///dummy.db").__class__, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

engine = create_engine("sqlite:///bluestock_mf.db")

with engine.connect() as conn:
    conn.exec_driver_sql("PRAGMA foreign_keys = ON;")

fund = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/processed/nav_history_cleaned.csv")
inv = pd.read_csv("data/processed/investor_transactions_cleaned.csv")
perf = pd.read_csv("data/processed/scheme_performance_cleaned.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
inv.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf.to_sql("fact_performance", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)

print("Loaded SQLite DB successfully")
print("dim_fund:", len(fund))
print("fact_nav:", len(nav))
print("fact_transactions:", len(inv))
print("fact_performance:", len(perf))
print("fact_aum:", len(aum))