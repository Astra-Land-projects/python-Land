def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def main():
    while True:
        print("\n🔢 choose one:")
        print("1️⃣ back")
        print("2️⃣ again")
        print("0️⃣ exist")
        choice = input("number choose: ")

        if choice == "0":
            break
        n = int(input("how many number fibonachi: "))

        if choice == "1":
            print("\nresult(back):")
            for i in range(n):
                print(fibonacci_recursive(i), end=" ")
        elif choice == "2":
            print("\nresult(again):")
            print(*fibonacci_iterative(n))
        else:
            print("choose not availble!")

if __name__ == "__main__":
    main()