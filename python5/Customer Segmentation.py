import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("customers.csv")

features = [
    "income",
    "spending_score"
]

X = df[features]

X = StandardScaler().fit_transform(X)

model = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

df["segment"] = model.fit_predict(X)

print(df)

df.to_csv(
    "segmented_customers.csv",
    index=False
)