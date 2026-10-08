import pandas as pd

input_file = input("CSV file: ")

df = pd.read_csv(input_file)

print("Original shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove completely empty columns
df = df.dropna(axis=1, how="all")

# Fill numeric missing values
for column in df.select_dtypes(include="number"):
    df[column] = df[column].fillna(df[column].median())

# Fill text missing values
for column in df.select_dtypes(include="object"):
    df[column] = df[column].fillna("Unknown")

output = "cleaned_data.csv"

df.to_csv(output, index=False)

print("Cleaned shape:", df.shape)
print("Saved:", output)