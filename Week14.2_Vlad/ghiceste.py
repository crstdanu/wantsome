import string


def brute_force_guess(password_to_guess):
    # Alfabetul [a-z]
    for char1 in string.ascii_lowercase:
        for char2 in string.ascii_lowercase:
            for char3 in string.ascii_lowercase:
                for char4 in string.ascii_lowercase:
                    for char5 in string.ascii_lowercase:
                        for char6 in string.ascii_lowercase:
                            # Verificare parolă
                            current_guess = char1 + char2 + char3 + char4 + char5 + char6
                            if current_guess == password_to_guess:
                                return current_guess

    # Alfabetul [0-9]
    for char1 in string.digits:
        for char2 in string.digits:
            for char3 in string.digits:
                for char4 in string.digits:
                    for char5 in string.digits:
                        for char6 in string.digits:
                            for char7 in string.digits:
                                for char8 in string.digits:
                                    for char9 in string.digits:
                                        # Verificare parolă
                                        current_guess = char1 + char2 + char3 + \
                                            char4 + char5 + char6 + char7 + char8 + char9
                                        if current_guess == password_to_guess:
                                            return current_guess

    # Alfabetul [a-zA-Z0-9]
    for char1 in string.ascii_letters + string.digits:
        for char2 in string.ascii_letters + string.digits:
            for char3 in string.ascii_letters + string.digits:
                for char4 in string.ascii_letters + string.digits:
                    for char5 in string.ascii_letters + string.digits:
                        # Verificare parolă
                        current_guess = char1 + char2 + char3 + char4 + char5
                        if current_guess == password_to_guess:
                            return current_guess

    return None


# Exemplu de utilizare
# Schimbă aceasta cu parola generată în scriptul anterior
password_to_guess = "abc123"
guessed_password = brute_force_guess(password_to_guess)

if guessed_password:
    print(f"Parola a fost ghicită: {guessed_password}")
else:
    print("Parola nu a putut fi ghicită.")
