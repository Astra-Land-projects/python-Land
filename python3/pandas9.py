import pandas as pd

# csv خواندن فایل
df = pd.read_csv("products.csv")

# ساخت دیتافریم جدید برای اضافه کردن ردیف
new_row = pd.DataFrame([{
  "Product": "Electric Kettle",
  "Category": "Home Application",
  "Price": 60,
  "Inventory": 30,
  "Annual Sales": 0
}])

# چسباندن دیتافریم جدید به دیتافریم اصلی
df = pd.concat([df, new_row], ignore_index=True)

# دسترسی به اطلاعات آخرین ردیف
print(df.loc[len(df)-1])