import tkinter
import random

nr_incercari = 0
nr_random = random.randint(1, 100)


def trateaza_apasa():
    global nr_incercari
    global nr_random
    crt = int(nr_crt.get())
    distanta = abs(crt - nr_random)
    if distanta > 50:
        hint.configure(text="RECE")
        nr_incercari += 1
    elif distanta > 10 and distanta <= 50:
        hint.configure(text="CALD")
        nr_incercari += 1
    elif distanta > 0 and distanta <= 10:
        hint.configure(text="FIERBINTE")
        nr_incercari += 1
    else:
        hint.configure(text="FELICITARI! AI GHICIT!")
    scor.configure(text=str(100-nr_incercari))


window = tkinter.Tk()
window.geometry("300x150")
window.title("Guess the Number")

tkinter.Label(window, text="Numar curent: ").grid(column=0, row=0)
nr_crt = tkinter.Entry(window, width=20)
nr_crt.grid(column=1, row=0)

tkinter.Label(window, text="Hint: ").grid(column=0, row=1)
hint = tkinter.Label(window, text="RECE")
hint.grid(column=1, row=1)

tkinter.Label(window, text="Scor: ").grid(column=0, row=2)
scor = tkinter.Label(window, text="100")
scor.grid(column=1, row=2)

tkinter.Button(window, text="Ghiceste!",
               command=trateaza_apasa).grid(column=0, row=3)

window.mainloop()
