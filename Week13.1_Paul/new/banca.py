# Write a Python program to create a class representing a bank and bank account.


import random

class Bank:
    """
    Represents a Bank entity
    """
    def __init__(self, name, code, country, currencies: list):
        self.name = name
        self.code = code
        self.country = country
        self.currencies = currencies

    def generate_iban(self, currency):
        # TODO: replace numbers with random ones
        # The bank must keep track of all its Bank Accounts (IBAN)
        # make sure the currency is accepted by the bank
        return f"{self.country[:2].upper()}55{self.code}{currency}8945794832489384"

    def open_bank_account(self, currency, balance=0, overdraft=0):
        """Creates and returns a bank account. The bank must keep track of all opened bank accounts"""
        pass

    def close_bank_account(self, bank_account):
        """Closes the bank account, if it has a 0 balance"""
        pass


class BankAccount:
    # class attribute
    default_language = 'ro'

    def __init__(self, bank: Bank, currency, balance=0, overdraft: int = 0):
        self._currency = None
        self.__balance = 0
        self.bank = bank
        self.overdraft = overdraft
        self.balance = balance
        self.currency = currency
        self.iban = bank.generate_iban(self._currency)

    def __str__(self):
        return f"{BankAccount.account_description()} {self.iban}"

    @staticmethod
    def calculate_interest(amount, interest_rate):
        return amount * interest_rate

    @classmethod
    def account_description(cls, language=None):
        if language is None:
            language = cls.default_language
        if language == "ro":
            return "Cont Bancar"
        elif language == "en":
            return "Bank Account"

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        if self._currency is None:
            self._currency = value
        else:
            raise ValueError("Nu poti schimba moneda contului!")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if self.__balance + amount < -self.overdraft:
            raise ValueError("Fonduri insuficiente")
        self.__balance = amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Nu poti depune valori negative")
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def send_money(self, other):
        """Sends an amount to another BankAccount. Fees may apply, depending on the bank"""
        pass


bcr = Bank("BCR", "BCR", "Romania", ["RON", "EUR", "USD"])
cont = BankAccount(bcr, currency="RON")
print(BankAccount.calculate_interest(1000, 0.05))


# cont2 = BankAccount(bcr, currency="EUR")
# print(cont)
# BankAccount.default_language = 'en'
# print(cont)
# print(cont2)


# Take an object from everyday life and model it in a class,
# giving it at least 3 attributes and 3 methods
