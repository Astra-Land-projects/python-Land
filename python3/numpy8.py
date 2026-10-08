import pandas as pd

# csv خواندن فایل
df = pd.read_csv("products.csv")

# مشاهده 5 ردیف اول
print(df.head())