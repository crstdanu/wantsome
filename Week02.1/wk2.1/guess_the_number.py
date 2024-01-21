import random

MAX_TRIALS = 3

secret_number = random.randint(0, 10)
# TODO: Remove. Cheat
# print(secret_number)

trials_count = 0

while trials_count < MAX_TRIALS:
    user_no = int(input(f"{MAX_TRIALS - trials_count} trials remaining. Guess the number (0-10): "))

    if user_no != secret_number:
        print("Bad guess. Try again!")
    else:
        print(f"Congratulations! You guessed it: {user_no}")
        trials_count = MAX_TRIALS

    trials_count = trials_count + 1
