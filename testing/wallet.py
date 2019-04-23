"""
Wallet app created for the purpose of testing.
"""


class InsufficientAmount(Exception):
    pass


class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough money')
        self.balance -=amount

    def add_cash(self, amount):
        self.balance += amount
