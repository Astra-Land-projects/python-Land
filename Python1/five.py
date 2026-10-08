def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    number = 2  # شروع از اولین عدد اول
   
    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
       
    return primes

# پیدا کردن پنج عدد اول
first_five_primes = first_n_primes(5)
print("five number first:", first_five_primes)