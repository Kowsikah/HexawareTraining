import numpy as np
import pandas as pd
df = pd.read_csv("stock_movements.csv")
df=df.dropna(subset=['date_movement'])
print("\n--- Processing Stock with NumPy ---")

grouped = df.groupby(['product_id', 'product_name', 'reorder_level'])

products = []
current_balances = []
reorder_thresholds = []

for (pid, pname, rlevel), group in grouped:
    # Extract the quantities series into a raw NumPy array
    quantities_array = group['quantity'].to_numpy()

    # Calculate net stock using numpy calculation speed
    net_stock = np.sum(quantities_array)

    products.append((pid, pname))
    current_balances.append(net_stock)
    reorder_thresholds.append(rlevel)

# Re-building the clean summary DataFrame
summary_df = pd.DataFrame({
    'product_id': [p[0] for p in products],
    'product_name': [p[1] for p in products],
    'current_stock': current_balances,
    'reorder_level': reorder_thresholds
})

print("--- Initial Summary DataFrame ---")
print(summary_df)

print("\n--- Low Stock Alerts (Below Reorder Threshold) ---")

# CRITICAL FIX: Coerce data types to numeric before evaluation to strip errors like '50-15'
summary_df['current_stock'] = pd.to_numeric(summary_df['current_stock'], errors='coerce').fillna(0).astype(int)
summary_df['reorder_level'] = pd.to_numeric(summary_df['reorder_level'], errors='coerce').fillna(0).astype(int)


summary_df['needs_reorder'] = summary_df['current_stock'] < summary_df['reorder_level']
low_stock_alerts = summary_df[summary_df['needs_reorder'] == True]

if not low_stock_alerts.empty:
    print(low_stock_alerts[['product_id', 'product_name', 'current_stock', 'reorder_level']])
else:
    print("All products are safely above their reorder thresholds.")
# ... (after your existing logic where summary_df is created)

# 1. Flag items needing reorder
# Logic: If current_stock < reorder_level, set needs_reorder to True
summary_df['needs_reorder'] = summary_df['current_stock'] < summary_df['reorder_level']

# 2. Filter for only those items
reorder_list = summary_df[summary_df['needs_reorder'] == True]

# 3. Export to CSV 
# This file name MUST match the targetPath in your YAML pipeline
output_filename = 'reorder_list.csv'
reorder_list.to_csv(output_filename, index=False)

print(f"\n--- Reorder list successfully exported to {output_filename} ---")
print(reorder_list)