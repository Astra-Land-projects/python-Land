import pandas as pd

# csv خواندن فایل
df = pd.read_csv("products.csv")

# گروه‌بندی محصولات بر اساس دسته‌بندی
grouped_df = df.groupby("Category")

# محاسبه میانگین قیمت محصولات در هر دسته‌بندی
avg_price_by_category = grouped_df["Price"].mean()

print(avg_price_by_category)