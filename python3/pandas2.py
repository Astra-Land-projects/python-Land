import pandas as pd

# csv خواندن فایل
df = pd.read_csv("products.csv")

# نمایش اسم ستون‌ها
print(df.columns)
print("----------")

# نمایش مقدار ستون‌ها
print(df[["Product", "Annual Sales"]])