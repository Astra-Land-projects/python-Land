import pandas as pd
import pygal

# csv خواندن فایل
df = pd.read_csv("products.csv")

# ساخت نمودار
bar_chart = pygal.Bar()
bar_chart.title = "فروش سالانه محصولات"

# اضافه کردن داده‌ها از دیتافریم
for i in range(len(df)):
  bar_chart.add(df.loc[i, "Product"], df.loc[i, "Annual Sales"])

# رسم نمودار
bar_chart.render()