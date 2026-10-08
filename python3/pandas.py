import pandas as pd

# csv خواندن فایل
df = pd.read_csv("products.csv")

# دریافت خلاصه اطلاعات
df.info()