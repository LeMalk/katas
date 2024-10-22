from datetime import datetime

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({
            'date': datetime.now().strftime('%Y-%m-%d'),
            'amount': amount,
            'balance': self.balance
        })

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append({
            'date': datetime.now().strftime('%Y-%m-%d'),
            'amount': -amount,
            'balance': self.balance
        })

    def printStatement(self):
        print("Date       || Amount || Balance")
        for transaction in reversed(self.transactions):
            print(f"{transaction['date']} || {transaction['amount']}   || {transaction['balance']}")

# Exemplo de uso
account = BankAccount()
account.deposit(1000)
account.deposit(2000)
account.withdraw(500)
account.printStatement()