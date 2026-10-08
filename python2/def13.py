def is_leap_year(year):
  if year % 4 == 0 and year % 100 != 0:
    return True

  if year % 400 == 0:
    return True

  return False

print(is_leap_year(2024))
print(is_leap_year(2028))
print(is_leap_year(2029))