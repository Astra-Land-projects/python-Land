import numpy as np

numbers = np.array([
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90]
])

print(numbers)
print(f"{numbers[0, 0]} :اولین سطر از ستون اول")
print(f"{numbers[1, 1]} :دومین سطر از ستون دوم")
print(f"{numbers[2, 2]} :سومین سطر از ستون سوم")