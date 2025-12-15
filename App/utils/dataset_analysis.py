import json
import os
import re
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "Data" / "Raw_data"
OUT_DIR = ROOT / "Artifacts"
OUT_DIR.mkdir(parents=True, exist_ok=True)


DATE_COL_PATTERNS = re.compile(
    r"(time|date|dob|dod|charttime|storetime|admittime|dischtime|deathtime|intime|outtime)$",
    re.IGNORECASE,
)


def infer_dtypes_for_csv(csv_path: Path, sample_rows: int = 2000) -> dict:
    # Read a small sample to infer dtypes, then lightly coerce datetimes
    try:
        df = pd.read_csv(csv_path, nrows=sample_rows, low_memory=False)
    except Exception as e:
        return {"__error__": str(e)}

    # Attempt to convert likely datetime columns
    for col in df.columns:
        if df[col].dtype == "object" and DATE_COL_PATTERNS.search(col):
            try:
                df[col] = pd.to_datetime(df[col], errors="ignore")
            except Exception:
                pass

    dtypes = {}
    for col, dtype in df.dtypes.items():
        # Normalize pandas dtypes to simpler strings
        if pd.api.types.is_datetime64_any_dtype(dtype):
            dtypes[col] = "datetime64[ns]"
        elif pd.api.types.is_integer_dtype(dtype):
            dtypes[col] = "int64"
        elif pd.api.types.is_float_dtype(dtype):
            dtypes[col] = "float64"
        elif pd.api.types.is_bool_dtype(dtype):
            dtypes[col] = "bool"
        else:
            dtypes[col] = "object"

    return dtypes


def main():
    summary = {}
    for name in sorted(os.listdir(RAW_DIR)):
        if not name.lower().endswith(".csv"):
            continue
        path = RAW_DIR / name
        summary[name] = infer_dtypes_for_csv(path)

    out_json = OUT_DIR / "schema_summary.json"
    with out_json.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"Wrote schema summary to {out_json}")


if __name__ == "__main__":
    main()
