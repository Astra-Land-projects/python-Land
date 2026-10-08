def fibonacci_recursive(n):
    """
    عدد فیبوناچی nام رو با استفاده از روش بازگشتی محاسبه می‌کنه.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# مثال استفاده
n = 10
print("number fibonachi with back:")
for i in range(n):
    print(fibonacci_recursive(i))