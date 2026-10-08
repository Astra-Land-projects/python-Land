import pandas as pd

df = pd.read_csv("products.csv")

print(df[["Product", "Category"]])