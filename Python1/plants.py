temperatures = [23.48, 22.17, 25.63, 24.09, 21.85, 26.74, 22.95, 23.60, 24.88, 20.41, 25.12, 22.68, 23.15, 24.50, 21.33 ]
temperatures.sort()

maximum = temperatures[len(temperatures) - 1]
minimum = temperatures[0]

avg = (maximum + minimum) / 2

print(avg)