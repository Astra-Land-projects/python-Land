def convert_temp(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

celsius_temp = convert_temp(77)

if celsius_temp > 22:
  print("هشدار! دمای گلخانه بیشتر از 22 درجه سانتی‌گراد است")