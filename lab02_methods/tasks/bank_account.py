class BankAccount:
    """Задача: bank_account"""

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount: int):
        pass

    def withdraw(self, amount: int):
        """Снимает только если достаточно средств"""
        if self.balance >= amount:
            self.balance -= amount
        return self.balance
