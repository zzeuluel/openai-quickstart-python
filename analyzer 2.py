# analyzer.py
import os
import pandas as pd

# Local helper replacements for missing 'helpers' module
def calculate_total(quantity, price):
    try:
        return float(quantity) * float(price)
    except Exception:
        return 0.0

def format_currency(value):
    try:
        return f"${value:,.2f}"
    except Exception:
        return str(value)

# Ensure data file exists; create sample if missing
data_path = 'data/sales.csv'
if not os.path.exists(data_path):
    os.makedirs(os.path.dirname(data_path), exist_ok=True)
    sample = [
        {'product': 'Widget A', 'quantity': 10, 'price': 2.5},
        {'product': 'Widget B', 'quantity': 5, 'price': 4.0},
        {'product': 'Widget C', 'quantity': 2, 'price': 15.0},
    ]
    pd.DataFrame(sample).to_csv(data_path, index=False)

# Read data
df = pd.read_csv(data_path)

# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

# Add totals to our data
df['total'] = totals

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

# Show grand total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")
 
