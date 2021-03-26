import os
import pandas as pd

files = [f for f in os.listdir() if f.endswith(".csv") and "xakep_index" not in f]
df = pd.concat(pd.read_csv(f) for f in files)
df.sort_values("issue", inplace=True)

df.to_csv("xakep_index.csv", index=False)
