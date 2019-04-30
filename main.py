import os
from tkinter import *

current_path = os.getcwd()


def isvalymas():
    laukas.delete(0, 'end')


def sukurimas():
    os.mkdir(laukas.get())
    isvalymas()


def sort():
    os.chdir(path_laukas.get())
    file_detection()


def file_detection():
    files = os.listdir(current_path)
    txt = []
    exe = []
    pptx = []
    png = []
    jpg = []
    for each in files:
        if '.txt' in each:
            txt.append(each)
        if '.exe' in each:
            exe.append(each)
        if '.pptx' in each:
            pptx.append(each)
        if '.png' in each:
            png.append(each)
        if '.jpg' in each:
            jpg.append(each)
    if len(txt) > 0:
        os.mkdir(current_path + '\\txt')
    if len(exe) > 0:
        os.mkdir(current_path + '\\exe')
    if len(pptx) > 0:
        os.mkdir(current_path + '\\pptx')
    if len(jpg) > 0:
        os.mkdir(current_path + '\\jpg')
    if len(png) > 0:
        os.mkdir(current_path + '\\png')


langas = Tk()

path_uzrasas = Label(langas, text='Path:')
path_uzrasas.grid(row=0, column=0)

path_laukas = Entry(langas)
path_laukas.askdire
path_laukas.insert(END, os.getcwd())
path_laukas.grid(row=0, column=1, ipadx=100)

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
