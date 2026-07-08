import pandas as pd

# Read the original dataset
df = pd.read_csv("data/postings.csv")

# Randomly select 500 jobs
small_df = df.sample(n=500, random_state=42)

# Save the smaller dataset
small_df.to_csv("data/postings_small.csv", index=False)

print("Done!")
print(f"Original rows: {len(df)}")
print(f"New rows: {len(small_df)}")