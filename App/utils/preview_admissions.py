from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
CSV = ROOT / "Data" / "Raw_data" / "admissions.csv"

def to_markdown_simple(df: pd.DataFrame) -> str:
    cols = list(df.columns)
    header = "| " + " | ".join(cols) + " |"
    sep = "| " + " | ".join(["---"] * len(cols)) + " |"
    rows = []
    for _, row in df.iterrows():
        vals = [str(row[c]) for c in cols]
        rows.append("| " + " | ".join(vals) + " |")
    return "\n".join([header, sep] + rows)

def main():
    cols = [
        "subject_id",
        "hadm_id",
        "admittime",
        "dischtime",
        "admission_type",
        "admission_location",
        "discharge_location",
        "insurance",
        "race",
        "hospital_expire_flag",
    ]
    df = pd.read_csv(CSV, usecols=cols, nrows=3)
    print(to_markdown_simple(df))

if __name__ == "__main__":
    main()
