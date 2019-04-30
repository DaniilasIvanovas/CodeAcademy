import os
from tkinter import *

os.chdir('C:\\Users\\Student\\Desktop\\kkk')


def isvalymas():
    laukas.delete(0, 'end')


def sukurimas():
    os.mkdir(laukas.get())
    isvalymas()


langas = Tk()

uzrasas = Label(langas, text='Name')
laukas = Entry(langas)
mygtukas = Button(langas, text='Add', command=sukurimas)

uzrasas.grid(row=0, column=0)
laukas.grid(row=0, column=1)
mygtukas.grid(row=1, columnspan=2)


with open('failas.txt', 'w') as failas:
    failas.write('Nauja pradzia')

langas.mainloop()
