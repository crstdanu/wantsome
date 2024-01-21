import argparse
from datetime import datetime


def converter(amount: float, currency_in="USD", currency_out="RON"):
    print(f"Data: {datetime.date()}")
    print(f"Input amount: {amount} {currency_in}")
    if currency_in == "USD" and currency_out == "EUR":
        converted_amount = amount * 0.92
        print(f"Converted amount: {converted_amount} {currency_out}")
    if currency_in == "USD" and currency_out == "RON":
        converted_amount = amount * 4.59
        print(f"Converted amount: {converted_amount} {currency_out}")
    if currency_in == "EUR" and currency_out == "RON":
        converted_amount = amount * 4.97
        print(f"Converted amount: {converted_amount} {currency_out}")
    if currency_in == "EUR" and currency_out == "USD":
        converted_amount = amount * 1.08
        print(f"Converted amount: {converted_amount} {currency_out}")
    if currency_in == "RON" and currency_out == "EUR":
        converted_amount = amount * 0.20
        print(f"Converted amount: {converted_amount} {currency_out}")
    if currency_in == "RON" and currency_out == "USD":
        converted_amount = amount * 0.22
        print(f"Converted amount: {converted_amount} {currency_out}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='A simple currency converter')

    # Add positional argument
    parser.add_argument('--amount', type=float, help='Amount to be converted')

    # Add optional argument with choices
    parser.add_argument(
        '--currency_in', choices=['EUR', 'USD', 'RON'], default='USD', help='the input currency')
    parser.add_argument(
        '--currency_out', choices=['EUR', 'USD', 'RON'], default='EUR', help='the output currency')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values using dot notation
    amount = args.amount
    currency_in = args.currency_in
    currency_out = args.currency_out

    converter(amount, currency_in, currency_out)
