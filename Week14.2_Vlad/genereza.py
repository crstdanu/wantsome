import random
import string


def generate_password():
    # Alfabet [a-z] cu 6/7 caractere
    password_part1 = ''.join(random.choice(string.ascii_lowercase)
                             for _ in range(random.randint(6, 7)))

    # Alfabet [0-9] cu 8/9 caractere
    password_part2 = ''.join(random.choice(string.digits)
                             for _ in range(random.randint(8, 9)))

    # Alfabet [a-zA-Z0-9] cu 5 caractere
    password_part3 = ''.join(random.choice(
        string.ascii_letters + string.digits) for _ in range(5))

    # Concatenarea celor trei părți pentru a forma parola finală
    password = password_part1 + password_part2 + password_part3

    return password


# Exemplu de utilizare
password_example = generate_password()
print("Parola generată:", password_example)
