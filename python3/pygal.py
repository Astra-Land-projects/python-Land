import pygal

# ساخت نمودار
pie_chart = pygal.Pie()
# مشخص کردن عنوان نمودار
pie_chart.title = "سهم هر دسته‌بندی از فروش سالانه"

# افزودن داده به نمودار
pie_chart.add("Electronics", 1625)
pie_chart.add("Furniture", 925)
pie_chart.add("Home Appliances", 810)

# رسم نمودار
pie_chart.render()