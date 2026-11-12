import random

import pandas as pd

random.seed(42)
rows = []
for month in range(1, 13):
    for _ in range(40):
        rows.append(
            {
                "month": month,
                "region": random.choice(["North", "South", "East", "West"]),
                "product": random.choice(["Laptop", "Phone", "Tablet", "Watch"]),
                "revenue": random.randint(50, 500) * (1 + month / 12),
            }
        )
pd.DataFrame(rows).round(2).to_csv("sales.csv", index=False)
print("sales.csv created")
