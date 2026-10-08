import pandas as pd

file = input("Dataset: ")

df = pd.read_csv(file)

print("\n===== DATASET REPORT =====")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(list(df.columns))

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistics:")
print(df.describe(include="all"))

print("\nDuplicate rows:")
print(df.duplicated().sum())