import datetime as dt

new_year = dt.date(2025, 1, 1)
today = dt.date.today()

passed = today - new_year
print(passed.days)