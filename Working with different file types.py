import pandas as pd
import json
import os

# Read the CSV file
df = pd.read_csv('sales-analysis/data/sales.csv')
print("CSV Data:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

# Create output directory
os.makedirs('output', exist_ok=True)

# Save as different formats
# 1. JSON format (good for web APIs) — write pretty JSON via json.dump for compatibility
try:
    records = df.to_dict(orient='records')
    with open('sales-analysis/output/sales_data.json', 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=2)
except Exception as e:
    print(f"Failed to write JSON: {e}")

# 2. Excel format (good for sharing)
try:
    df.to_excel('sales-analysis/output/sales_data.xlsx', index=False)
except Exception as e:
    print(f"Failed to write Excel: {e}")

# 3. Updated CSV (with our new total column)
try:
    df.to_csv('sales-analysis/output/sales_with_totals.csv', index=False)
except Exception as e:
    print(f"Failed to write CSV: {e}")

print("\nFiles saved:")
for fname in ['sales-analysis/output/sales_data.json', 'output/sales_data.xlsx', 'output/sales_with_totals.csv']:
    try:
        print(f"- {os.path.abspath(fname)}")
    except Exception:
        print(f"- {fname}")