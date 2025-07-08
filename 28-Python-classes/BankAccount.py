class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Withdrawal denied.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

    def show_balance(self):
        print(f"Balance for {self.owner}: {self.balance}")

if __name__ == "__main__":
    acc = BankAccount("Tom", 100)
    acc.deposit(50)
    acc.withdraw(30)
    acc.withdraw(200)  # Should be denied
    acc.show_balance()
