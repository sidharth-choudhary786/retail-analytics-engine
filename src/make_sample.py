import pandas as pd

# Full clean data load
df = pd.read_csv("data/sales_clean.csv", low_memory=False)

# A small representative sample — 1000 random rows
sample = df.sample(n=1000, random_state=42)

# for github - sample data
sample.to_csv("data/sample_sales.csv", index=False)
print("Sample saved:", sample.shape)