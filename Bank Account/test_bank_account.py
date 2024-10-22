import unittest
from bank_account import BankAccount
from datetime import datetime

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount()

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 0)

    def test_deposit(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.balance, 1000)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertEqual(self.account.transactions[0]['amount'], 1000)

    def test_withdraw(self):
        self.account.deposit(1000)
        self.account.withdraw(500)
        self.assertEqual(self.account.balance, 500)

    def test_print_statement(self):
        self.account.deposit(1000)
        self.account.deposit(2000)
        self.account.withdraw(500)
        
        expected_output = (
            "Date       || Amount || Balance\n"
            f"{datetime.now().strftime('%Y-%m-%d')} || -500   || 2500\n"
            f"{datetime.now().strftime('%Y-%m-%d')} || 2000   || 3000\n"
            f"{datetime.now().strftime('%Y-%m-%d')} || 1000   || 1000\n"
        )
        
        from io import StringIO
        import sys
        
        captured_output = StringIO()
        sys.stdout = captured_output
        self.account.printStatement()
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()