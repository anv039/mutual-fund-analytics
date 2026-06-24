import requests
import pandas as pd

scheme_codes = [125497, 119551, 120503, 118632, 119092, 120841]

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        meta = data.get("meta", {})
        values = data.get("data", [])

        df = pd.DataFrame(values)
        df["amfi_code"] = code

        file_name = f"data/raw/nav_{code}.csv"
        df.to_csv(file_name, index=False)

        print(f"Saved: {file_name}")
        print("Scheme Name:", meta.get("scheme_name", "N/A"))
        print("Records:", len(df))
        print("-" * 50)
    else:
        print(f"Failed for code {code}: {response.status_code}")