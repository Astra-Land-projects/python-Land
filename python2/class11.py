file = open("books.txt", "r")
# خواندن فایل
content = file.read()
# چاپ محتوای فایل
print(content)
# بستن فایل
file.close()