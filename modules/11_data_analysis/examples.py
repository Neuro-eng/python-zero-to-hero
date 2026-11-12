import pandas as pd

df = pd.DataFrame(
    {
        "region": ["North", "South", "North", "East", "South"],
        "product": ["A", "B", "A", "C", "A"],
        "revenue": [100, 150, 120, 90, 200],
    }
)
print(df.groupby("region")["revenue"].sum().sort_values(ascending=False))
print(df[df["revenue"] > 100])
