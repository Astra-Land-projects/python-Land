import pandas as pd

# csv خواندن فایل
df = pd.read_csv("products.csv")

# چاپ اطلاعات چهار محصول اول
print(df.loc[0:3])