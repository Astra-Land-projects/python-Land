import pandas as pd

# csv خواندن فایل
df = pd.read_csv("products.csv")

# کمترین موجودی در انبار
print(f"{df['Inventory'].min()} :کمترین موجودی در انبار")

# بیشترین موجودی در انبار
print(f"{df['Inventory'].max()} :بیشترین موجودی در انبار")

# تعداد محصولات فروخته شده در سال قبل
print(f"{df['Annual Sales'].sum()} :تعداد محصولات فروخته شده در سال قبل")

# میانگین قیمت محصولات
print(f"{df['Price'].mean()} :میانگین قیمت محصولات")