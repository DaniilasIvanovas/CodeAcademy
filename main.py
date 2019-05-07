import os
from modules import langas


def sort():
    a = os.listdir(current_path)
    search_type(a)


def search_type(listas):
    if any('.txt' in s for s in listas):
        os.mkdir(Appas.path_laukas.get() + '\\Txt')
    if any('.exe' in s for s in listas):
        os.mkdir(Appas.path_laukas.get() + '\\Exe')
    if any('.jpg' in s for s in listas):
        os.mkdir(Appas.path_laukas.get() + '\\Jpg')
    if any('.png' in s for s in listas):
        os.mkdir(Appas.path_laukas.get() + '\\Png')
    if any('.docx' in s for s in listas):
        os.mkdir(Appas.path_laukas.get() + '\\Word')
    if any('.pptx' in s for s in listas):
        os.mkdir(Appas.path_laukas.get() + '\\Power Point')
    if any('.html' in s for s in listas):
        os.mkdir(Appas.path_laukas.get() + '\\Html')
    if any('.css' in s for s in listas):
        os.mkdir(Appas.path_laukas.get() + '\\Css')
    if any('.js' in s for s in listas):
        os.mkdir(Appas.path_laukas.get() + '\\Js')
    if any('.mp4' in s for s in listas):
        os.mkdir(Appas.path_laukas.get() + '\\Mp4')
    if any('.mov' in s for s in listas):
        os.mkdir(Appas.path_laukas.get() + '\\Mov')


current_path = os.getcwd()
Appas = langas.Langas(sort())

Appas.root.mainloop()
