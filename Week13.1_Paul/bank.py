# Write a Python program to create a class representing a bank and bank account.

# TODO: replace numbers with random ones
# The bank must keep track of all its Bank Accounts (IBAN)
# make sure the currency is accepted by the bank


# An IBAN consists of a two-letter country code, two check digits, four digits bank identifier and sixteen digits account number
# total: 24 digits


import random


class Bank:
    def __init__(self, name, code, country, currencies):
        self.name = name
        self.code = code
        self.country = country
        self.currencies = currencies
        self.accounts = []

    def create_iban(self):
        two_digits = ''.join(str(random.randint(0, 9)) for _ in range(2))
        bank_identifier = ''.join(
            str(random.choice(f'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')) for _ in range(4))
        account_number = ''.join(str(random.randint(0, 9)) for _ in range(16))
        return f"{self.country[:2].upper()}{two_digits} {bank_identifier} {account_number}"

    def open_bank_account(self, owner, currency, balance=0, overdraft=0):

        assert currency in self.currencies, f"Currency not available. Choose from {self.currencies}"

        iban = self.create_iban()
        account = BankAccount(owner, currency, iban, balance, overdraft)
        self.accounts.append(account)
        return account

    def close_bank_account(self, acct_owner):
        for account in self.accounts:
            if account.acct_owner == acct_owner:
                self.accounts.remove(account)

    def cauta_iban(self, iban):
        for cont in self.accounts:
            if iban == cont.iban:
                return cont


class BankAccount:
    default_language = 'ro'

    def __init__(self, acct_owner, currency, iban, balance=0,  overdraft: int = 0):
        self.acct_owner = acct_owner
        self.balance = balance
        self.currency = currency
        self.overdraft = overdraft
        self.iban = iban

    def verifica_balanta(self, amount):
        if self.balance > amount:
            return True
        else:
            return False

    def transfer(self, amount, banca, iban):
        if self.verifica_balanta(amount):
            cont = banca.cauta_iban(iban)
            if cont:
                cont.balance += amount
                self.balance -= amount
                return "Transfer efectuat"
            else:
                return "Cont inexistent"
        else:
            return "Fonduri insuficiente"


transilvania = Bank('Transilvania', 'BTR', 'Romania', ['RON', 'EUR', 'USD'])

mihai = transilvania.open_bank_account('Mihai', 'RON', 1000)
vasile = transilvania.open_bank_account('Vasile', 'RON')

print(mihai.currency)
print(mihai.balance)
print(mihai.default_language)
print(mihai.acct_owner)
print(mihai.iban)

print(vasile.iban)
print(transilvania.accounts)
print(mihai.transfer(1500, transilvania, vasile.iban))
print(mihai.balance)
print(vasile.balance)
