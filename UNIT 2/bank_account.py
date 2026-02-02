class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        return self.balance

# Example usage
if __name__ == "__main__":
    account = BankAccount("123456", 1000)
    print("Initial balance:", account.check_balance())
    account.deposit(500)
    print("After deposit:", account.check_balance())
    account.withdraw(200)
    print("After withdraw:", account.check_balance())
