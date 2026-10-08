import pygal

# ساخت نمودار
bar_chart = pygal.Bar()
# مشخص کردن عنوان نمودار
bar_chart.title = "فروش سالانه برخی محصولات"

# افزودن داده به نمودار
bar_chart.add("Mobile Phone", 320)
bar_chart.add("Laptop", 150)
bar_chart.add("Television", 220)

# رسم نمودار
bar_chart.render()