# Dataset Setup & Verification

## Virtual Environment

- Command used to create venv (PowerShell):

```powershell
py -m venv .venv
```

- Commands to activate it (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

- Python interpreter path (in this workspace):

```
D:/AI-NutriCare/.venv/Scripts/python.exe
```

## Installed Dependencies

Core data/ML stack currently installed in the venv:

| Package | Version |
|---|---|
| pandas | 2.3.3 |
| numpy | 2.3.4 |
| scipy | 1.16.3 |
| scikit-learn | 1.7.2 |
| matplotlib | 3.10.7 |
| seaborn | 0.13.2 |
| tabulate (for markdown previews) | 0.9.0 |

To (re)install from `requirements.txt` plus preview support:

```powershell
pip install -r requirements.txt
pip install tabulate
```

## Folder Structure

Key folders and files in this workspace:

```
AI-NutriCare/
├─ App/
│  └─ utils/
│     ├─ dataset_analysis.py            # infers dtypes per CSV → Artifacts/schema_summary.json
│     └─ preview_admissions.py          # prints 3-row markdown preview from admissions.csv
├─ Artifacts/
│  ├─ Dataset_Setup_And_Verification.md # this document
│  └─ schema_summary.json               # inferred dtypes for each CSV
├─ Data/
│  ├─ Raw_data/
│  │  ├─ admissions.csv
│  │  ├─ chartevents.csv
│  │  ├─ d_icd_diagnoses.csv
│  │  ├─ d_items.csv
│  │  ├─ d_labitems.csv
│  │  ├─ icustays.csv
│  │  ├─ inputevents.csv
│  │  ├─ labevents.csv
│  │  ├─ omr.csv
│  │  ├─ outputevents.csv
│  │  └─ patients.csv
│  └─ Transformed_data/
├─ requirements.txt
└─ README.md
```

## Verification Steps (CSV Loading)

1) Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

2) Quick CSV smoke test (reads 3 rows of admissions)

```powershell
python -c "import pandas as pd; df=pd.read_csv('Data/Raw_data/admissions.csv', nrows=3); print(df.shape)"
```

3) Infer dtypes across all CSVs and write summary JSON

```powershell
python .\App\utils\dataset_analysis.py
```

4) Inspect the generated schema

- Open `Artifacts/schema_summary.json` to review inferred dtypes.

## 3 Sample Rows Preview (admissions.csv)

A compact preview of 10 commonly used columns.

| subject_id | hadm_id | admittime | dischtime | admission_type | admission_location | discharge_location | insurance | race | hospital_expire_flag |
|---|---|---|---|---|---|---|---|---|---|
| 10004235 | 24181354 | 2196-02-24 14:38:00 | 2196-03-04 14:02:00 | URGENT | TRANSFER FROM HOSPITAL | SKILLED NURSING FACILITY | Medicaid | BLACK/CAPE VERDEAN | 0 |
| 10009628 | 25926192 | 2153-09-17 17:08:00 | 2153-09-25 13:20:00 | URGENT | TRANSFER FROM HOSPITAL | HOME HEALTH CARE | Medicaid | HISPANIC/LATINO - PUERTO RICAN | 0 |
| 10018081 | 23983182 | 2134-08-18 02:02:00 | 2134-08-23 19:35:00 | URGENT | TRANSFER FROM HOSPITAL | SKILLED NURSING FACILITY | Medicare | WHITE | 0 |
