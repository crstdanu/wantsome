# 2. Currency Converter
# Create a currency converter that converts an amount from one currency to another.
# Allow users to specify the source currency, target currency, and amount.
# The exchange rates are read from a csv file with the following header:
# source currency, target_currency, rate

# python currency_converter.py --amount 100 --source_currency USD --target_currency EUR
# # Output:
# Date: 30.11.2023
# Input amount: 100 USD
# Converted Amount : 84.28 EUR
import csv
import argparse
from datetime import date

# header = ['source currency', 'target_currency', 'rate']
# data = [
#     ["USD", "EUR", 0.93],
#     ["USD", "RON", 4.60],
#     ["USD", "GBP", 0.80],
#     ["USD", "USD", 1],
#     ["EUR", "USD", 1.08],
#     ["EUR", "GBP", 0.86],
#     ["EUR", "RON", 4.97],
#     ["EUR", "EUR", 1],
#     ["GBP", "EUR", 1.16],
#     ["GBP", "USD", 1.26],
#     ["GBP", "RON", 5.79],
#     ["GBP", "GBP", 1],
#     ["RON", "USD", 0.22],
#     ["RON", "EUR", 0.20],
#     ["RON", "GBP", 0.17],
#     ["RON", "RON", 1],
# ]


rows = []
with open('rates.csv') as f:
    for elem in f.readlines()[1:]:
        if elem.strip():
            rows.append(elem.strip().split(','))


def convert(amount: float, in_curr: str, out_curr: str):
    result = 0.0
    for elem in rows:
        if elem[0] == in_curr.upper() and elem[1] == out_curr.upper():
            result = amount * float(elem[2])
    azi = date.today()
    data = azi.strftime('%d.%m.%Y')
    print(
        f"\nData: {data}\nInput amount: {amount:.2f} {in_curr}\nConverted amount: {result:.2f} {out_curr}")


# convert(100, 'USD', 'GBP')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Un simplu convertor de valuta")
    parser.add_argument('amount', type=int, help='Amount to be converted')
    parser.add_argument('curr_in', choices=[
                        'EUR', 'USD', 'RON', 'GBP'], help='the input currency')
    parser.add_argument('curr_out', choices=[
                        'EUR', 'USD', 'RON', 'GBP'], help='the output currency')

    args = parser.parse_args()

    amount = args.amount
    currency_in = args.curr_in
    currency_out = args.curr_out
    convert(amount, currency_in, currency_out)
