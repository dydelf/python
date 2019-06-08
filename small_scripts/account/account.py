"""
OOP model of a bank account.
"""

class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, deposit):
        self.balance = self.balance + deposit

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    def __init__(self, filepath):
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance = self.balance - amount


account = Account("balance.txt")
checking = Checking("balance.txt")

print(account.balance)
checking.transfer(100)
print(checking.balance)
