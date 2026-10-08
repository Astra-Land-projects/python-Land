import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("sales.csv")

df["date"] = pd.to_datetime(df["date"])

df["day"] = (
    df["date"] - df["date"].min()
).dt.days

X = df[["day"]]
y = df["sales"]

model = LinearRegression()

model.fit(X, y)

future_day = int(
    input("Future day number: ")
)

prediction = model.predict(
    [[future_day]]
)[0]

print("Forecast:", prediction)