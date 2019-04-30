import os
from tkinter import *

os.chdir('C:\\Users\\Student\\Desktop\\kkk')
current_path = os.getcwd()

def isvalymas():
    laukas.delete(0, 'end')


def sukurimas():
    os.mkdir(laukas.get())
    isvalymas()

def sort():
    os.chdir(path_laukas.get())


def file_detection():
    files = os.listdir(current_path)
    txt = 0
    exe = 0
    pptx = 0
    png = 0
    jpg = 0
    for each in files:
        if '.txt' in each:
            txt += 1
        if '.exe' in each:
            exe += 1
        if '.pptx' in each:
            pptx += 1
        if '.png' in each:
            png += 1
        if '.jpg' in each:
            jpg += 1


langas = Tk()

path_uzrasas = Label(langas, text='Path:')
path_uzrasas.grid(row=0, column=0)

path_laukas = Entry(langas)
path_laukas.grid(row=0, column=1)

path_mygtukas = Button(langas, text='search', command=sort)
path_mygtukas.grid(row=0, column=3)

uzrasas = Label(langas, text='Name')
uzrasas.grid(row=1, column=0)

laukas = Entry(langas)
laukas.grid(row=1, column=1)

mygtukas = Button(langas, text='Add', command=sukurimas)
mygtukas.grid(row=2, columnspan=2)


with open('failas.txt', 'w') as failas:
    failas.write('Nauja pradzia')

print(os.listdir(current_path))
langas.mainloop()
