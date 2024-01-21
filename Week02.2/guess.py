

# this is the secret number
secret = 155


print("\nPoti sa ghicesti un numar?\n")

while True:
    nr = int(input("Introduceti numarul: "))

    if abs(nr - secret) >= 50:
        print("\n🤔🤔!!! Esti FOARTE RECE !!! 🤣🤣\n")

    elif (abs(nr - secret) >= 10) and (abs(nr - secret) < 50):
        print("\n👌👌👌 !!   Esti RECE  !!   👌👌👌\n")

    elif (abs(nr - secret) < 10) and (abs(nr - secret) > 0):
        print("\n❤️❤️❤️  !  Esti FIERBINTE   !    ❤️❤️❤️\n")

    else:
        print("\n🎉🎉🎉 BRAVO! 🎆🎆🎆  AI GHICIT!  🎉🎉🎉\n")
        break


