import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def insights(df):
    return {
        "by_region": df.groupby("region")["revenue"].sum().sort_values(ascending=False).round(2),
        "top_products": df.groupby("product")["revenue"].sum().nlargest(3).round(2),
        "by_month": df.groupby("month")["revenue"].sum().round(2),
    }


if __name__ == "__main__":
    df = pd.read_csv("sales.csv")
    r = insights(df)
    print(r["by_region"], "\n")
    print(r["top_products"])
    r["by_month"].plot(kind="line", marker="o", title="Revenue by month")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.savefig("revenue_by_month.png", dpi=120, bbox_inches="tight")
    print("Saved revenue_by_month.png")
