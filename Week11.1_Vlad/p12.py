import math
import random
import tkinter
import json
import threading

#clasa de baza cu proprietatile (x,y,nume) si metodele (Arie,Perimetru) comune
class Shape:
    def __init__(self, x, y, width, height, nume):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.nume = nume
        self.childs = []

    def Adauga(self):
        pass
    
    def Deseneaza(self):
        pass

class my_label(Shape):
    def __init__(self, x, y, width, height, text, border, bg):
        super().__init__(x, y, width, height, text)
        self.border = border
        self.bg = bg

    def Adauga(self, child):
        self.childs += [child]

    def Deseneaza(self):        
        if self.border:
            if self.bg != None:
                desen.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.bg)
            else:
                desen.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height)
        elif self.bg != None:
            desen.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.bg)
            
        desen.create_text(self.x + self.width // 2, self.y + self.height // 2, text=self.nume)
        for child in self.childs:
            child.Deseneaza()

class my_panel(Shape):
    def __init__(self, x, y, width, height, bg, text):
        super().__init__(x, y, width, height, text)
        self.bg = bg

    def Adauga(self, child):
        self.childs += [child]

    def Deseneaza(self):        
        if self.bg != None:
            desen.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.bg)
        else:
            desen.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height)
        
        for child in self.childs:
            child.Deseneaza()

class my_button(Shape):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height, text)

    def Adauga(self, child):
        self.childs += [child]

    def Deseneaza(self):        
        desen.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="white")
        desen.create_text(self.x + self.width // 2, self.y + self.height // 2, text=self.nume)
        for child in self.childs:
            child.Deseneaza()            
       

window = tkinter.Tk()
window.title("Forme Geometrice")
window.geometry("600x600")

desen = tkinter.Canvas(window, width=600, height=600)
desen.grid(row=0, column=0)

m_window = my_panel(50, 50, 500, 500, "white", "panel1")
m_panel1 = my_panel(70, 70, 440, 180, "gray", "panel2")
m_panel2 = my_panel(70, 260, 440, 180, "orange", "panel3")
m_label1 = my_label(350, 90, 80, 30, "label-1", True, None)
m_label2 = my_label(350, 130, 80, 30, "label-2", False, None)
m_panel3 = my_panel(80, 80, 200, 90, "red", "panel4")
m_label3 = my_label(90, 90, 80, 30, "label-3", True, "olive")
m_buton1 = my_button(90, 130, 60, 30, "OK")
m_panel3.Adauga(m_label3)
m_panel3.Adauga(m_buton1)
m_panel2.Adauga(m_label1)
m_panel2.Adauga(m_label2)
m_panel2.Adauga(m_panel3)
m_window.Adauga(m_panel1)

m_buton2 = my_button(80, 270, 60, 30, "B1")
m_buton3 = my_button(80, 310, 60, 30, "B2")
m_buton4 = my_button(80, 350, 60, 30, "B3")
m_buton5 = my_button(150, 270, 100, 90, "STOP")
m_panel5 = my_panel(260, 270, 100, 90, "lime", "panel6")
m_panel6 = my_panel(280, 290, 60, 50, "blue", "panel7")
m_buton6 = my_button(170, 330, 60, 20, "Cancel")
m_panel2.Adauga(m_buton2)
m_panel2.Adauga(m_buton3)
m_panel2.Adauga(m_buton4)
m_panel2.Adauga(m_panel5)
m_panel2.Adauga(m_buton5)
m_panel5.Adauga(m_panel6)
m_buton5.Adauga(m_buton6)
m_window.Adauga(m_panel2)

m_window.Deseneaza()



window.mainloop()