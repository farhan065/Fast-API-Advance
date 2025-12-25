def add (num1: int, num2: int):
    return num1 + num2

def sub (num1: int, num2: int):
    return num1 - num2

def mul (num1: int, num2: int):
    return num1 * num2

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance=initial_balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1
    