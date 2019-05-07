from tkinter import *
import os

class Langas:
    def __init__(self, first_button):
        self.command1 = first_button
        self.root = Tk()
        self.root.title('OOO')
        self.root.geometry('500x250')
        self.root.resizable(0, 0)

        apibudinimas1 = Label(self.root, text='Ši programa skirta rušiuoti failams. Noredami testi į Path lauka įrašykite kelia iki direktorijos.')
        apibudinimas1.grid(row=0, columnspan=2)
        apibudinimas2 = Label(self.root, text='Ir paspauskite mygtuką Rušiuoti.')
        apibudinimas2.grid(row=1, columnspan=2, sticky=W)
        path_uzrasas = Label(self.root, text='Path:')
        path_uzrasas.grid(row=2, column=0, ipadx=50, sticky=W)
        self.path_laukas = Entry(self.root)
        self.path_laukas.insert(END, os.getcwd())
        self.path_laukas.grid(row=2, column=1, ipadx=100, command=self.command1)
        mygtukas = Button(self.root, text='Add')
        mygtukas.grid(row=3, columnspan=2)
