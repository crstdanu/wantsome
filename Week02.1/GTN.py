# Guess the number

import random


player_choice = input("Make your choice: ")
player = int(player_choice)

computer = random.randint(0, 10)

print(computer)

game_over = True

def guess_the_number(player, computer):
    if player == computer:
        global game_over
        game_over == False
        return "Ai ghicit!"
    elif player > computer:
        return f"Numarul ales e mai mic decat {player}"
    else:
        return f"Numarul ales e mai mare decat {player}"


rezultatul = guess_the_number(player, computer)
print(rezultatul)

while game_over: guess_the_number()
 
