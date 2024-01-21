import tkinter


def guess_the_number():
    global lbl2
    secret = 10
    print("\nPoti sa ghicesti un numar?\n")

    while True:
        nr = int(txt.get())

        if abs(nr - secret) >= 50:
            lbl2.tkinter.Label(windotext="\n🤔🤔!!! Esti FOARTE RECE !!! 🤣🤣\n")

        elif (abs(nr - secret) >= 10) and (abs(nr - secret) < 50):
            print("\n👌👌👌 !!   Esti RECE  !!   👌👌👌\n")

        elif (abs(nr - secret) < 10) and (abs(nr - secret) > 0):
            print("\n❤️❤️❤️  !  Esti FIERBINTE   !    ❤️❤️❤️\n")

        else:
            print("\n🎉🎉🎉 BRAVO! 🎆🎆🎆  AI GHICIT!  🎉🎉🎉\n")
            break

# sa facem asta

# sa incercam sa afisam grafic o functie: E GREU!!
# sa folosim un canvas
# sa desenam pe canvad -> rezolutia o setam noi
# o ecuatie de gradul intai
# daca reusim poate vedem o functie de gradul 2
# un buto, un canvas si un entry in care bagam formula
# sa dam valori x-ului
# pe masura ce obtinem y punem un pixel la coord din desen
#  0.0 al planului e in stanga sus


count = 0


# def trateaza_apasa():
#     global count

#     if count % 2 == 0:
#         lbl.configure(text="Par: " + str(count) + txt.get())
#     else:
#         lbl.configure(text="Impar: " + str(count) + txt.get())
#     count += 1


window = tkinter.Tk()

window.title("Guess the number")

# lbl = tkinter.Label(window, text="Hello")
# lbl.grid(column=0, row=0)

lbl2 = tkinter.Label(window, text="Hello")
lbl2.grid(column=2, row=0)

txt = tkinter.Entry(window, width=20)
txt.grid(column=0, row=2)

window.geometry('600x400')
btn = tkinter.Button(window, text="Click Me!",
                     command=guess_the_number).grid(column=1, row=0)
window.mainloop()
print("Am inchis programul")


# un entry ptr nr curent
# un label ptr mesaj
# un label ptr scor (100-nr_incercari)
# un buton care sa aplice calculele pe nr crt
