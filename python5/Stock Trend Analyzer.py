import pandas as pd

df = pd.read_csv("stock.csv")

df["MA7"] = (
    df["close"]
    .rolling(7)
    .mean()
)

df["MA30"] = (
    df["close"]
    .rolling(30)
    .mean()
)

latest = df.iloc[-1]

print("Current:", latest["close"])
print("MA7:", latest["MA7"])
print("MA30:", latest["MA30"])

if latest["MA7"] > latest["MA30"]:
    print("Trend: Upward")
else:
    print("Trend: Downward")