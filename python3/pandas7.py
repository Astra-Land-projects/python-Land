import pandas as pd

# csv خواندن فایل
df = pd.read_csv("products.csv")

# خلاصه داده‌های عددی
print(df.describe())