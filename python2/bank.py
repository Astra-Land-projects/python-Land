class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("stock is not enough.")

    def get_balance(self):
        return self.balance

def main():
    account_number = input("enter accout number: ")
    initial_balance = float(input("enter first stock: "))

    account = BankAccount(account_number, initial_balance)

    while True:
        print("\nchoose:")
        print("1. deposit")
        print("2. removal")
        print("3. show stock")
        print("4. exsit")

        choice = input("your choose: ")

        if choice == '1':
            amount = float(input("price deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("price removal: "))
            account.withdraw(amount)
        elif choice == '3':
            balance = account.get_balance()
            print("account stock:", balance)
        elif choice == '4':
            break
        else:
            print("choose is not availble.")

if __name__ == "__main__":
    main()