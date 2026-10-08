import pandas as pd

# csv خواندن فایل
df = pd.read_csv("products.csv")

# فیلتر کردن محصولات
filtered = df[(df["Price"] > 200) | (df["Annual Sales"] > 300)]
print(filtered)