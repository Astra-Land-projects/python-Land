def fibonacci_iterative(n):
    """
    اعداد فیبوناچی رو با استفاده از روش تکراری تولید می‌کنه.
    """
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

# مثال استفاده
n = 10
print("\nnumber fibonachi with again:")
fibonacci_iterative(n)