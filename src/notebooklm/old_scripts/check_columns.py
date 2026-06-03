import pandas as pd

excel_path = "02_LitRev_Sistematica/land_rent_financialization_literature_registry.xlsx"
xls = pd.ExcelFile(excel_path)

for sheet in xls.sheet_names:
    df = pd.read_excel(excel_path, sheet_name=sheet)
    print(f"\n=== {sheet} ===")
    print(df.columns.tolist())
