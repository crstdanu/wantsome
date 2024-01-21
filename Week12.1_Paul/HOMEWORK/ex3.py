# argparse
# 1. Password Generator
# Create a simple password generator that generates a random password with a
# specified length. Allow users to include uppercase letters, lowercase letters,
# numbers, and symbols in the generated password.

# python password_generator.py --length 12 --uppercase --numbers
# Output: Generated Password: Ks7pRg4qXtLz
import argparse
import random
import string


def parola(length=12, upper=False, digits=False, punctuation=False):
    caractere = string.ascii_lowercase
    if upper:
        caractere += string.ascii_uppercase
    if digits:
        caractere += string.digits
    if punctuation:
        caractere += string.punctuation
    parola = "".join(random.choice(caractere) for i in range(length))
    print(parola)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password generator")
    parser.add_argument('--length', type=int, default=12,
                        help="choose the number of characters of the password")
    parser.add_argument('--upper', action='store_True',
                        help="choose True if you want uppercase letters included in the password")
    parser.add_argument('--digits', action='store_True',
                        help="choose True if you want digits included in the password")
    parser.add_argument('--punctuation', action='store_True',
                        help="choose True if you want punctuation signs included in the password")
    args = parser.parse_args()

    length = args.length
    upper = args.upper
    digits = args.digits
    punctuation = args.punctuation
    parola(length, upper, digits, punctuation)
