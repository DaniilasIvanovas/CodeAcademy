from tkinter import *
import os


class Langas:
    def __init__(self):
        self.root = Tk()
        self.root.title('OOO')
        self.root.geometry('700x350')
        self.root.resizable(0, 0)
        self.a = os.listdir(os.getcwd())
        apibudinimas1 = Label(self.root, text='Ši programa skirta rušiuoti failams. Noredami testi į Path lauka įrašykite kelia iki direktorijos.')
        apibudinimas1.config(font=('Courrier', 12))
        apibudinimas1.grid(row=0, columnspan=2)

        apibudinimas2 = Label(self.root, text='Ir paspauskite mygtuką Rušiuoti.')
        apibudinimas2.config(font=('Courrier', 12))
        apibudinimas2.grid(row=1, columnspan=2, sticky=W)

        path_uzrasas = Label(self.root, text='Path:')
        path_uzrasas.config(font=('Courrier', 12))
        path_uzrasas.grid(row=2, column=0, sticky=E)

        self.path_laukas = Entry(self.root)
        self.path_laukas.config(font=('Courrier', 12))
        self.path_laukas.insert(END, os.getcwd())
        self.path_laukas.grid(row=2, column=1, ipadx=100)

        self.uzrasas_error = Label(self.root, text='')
        self.uzrasas_error.config(font=('Courrier', 12))
        self.uzrasas_error.grid(row=4, columnspan=2)

        mygtukas = Button(self.root, text='Rusiuoti' ,command=lambda: self.search_type())
        mygtukas.grid(row=2, column=3, sticky=W)

    # def mygtukask(self):
    #     mygtukas_tikras = Button(self.root, text='Add', command=self.search_type)
    #

    def search_type(self):
        try:
            if any('.txt' in s for s in self.a):
                os.mkdir(self.path_laukas.get() + '\\Txt')
                global txt
                txt= []
            if any('.exe' in s for s in self.a):
                os.mkdir(self.path_laukas.get() + '\\Exe')
                # = []
            if any('.jpg' in s for s in self.a):
                os.mkdir(self.path_laukas.get() + '\\Jpg')
                # = []
            if any('.png' in s for s in self.a):
                os.mkdir(self.path_laukas.get() + '\\Png')
                # = []
            if any('.docx' in s for s in self.a):
                os.mkdir(self.path_laukas.get() + '\\Word')
                # = []
            if any('.pptx' in s for s in self.a):
                os.mkdir(self.path_laukas.get() + '\\Power Point')
                # = []
            if any('.html' in s for s in self.a):
                os.mkdir(self.path_laukas.get() + '\\Html')
                # = []
            if any('.css' in s for s in self.a):
                os.mkdir(self.path_laukas.get() + '\\Css')
                # = []
            if any('.js' in s for s in self.a):
                os.mkdir(self.path_laukas.get() + '\\Js')
                # = []
            if any('.mp4' in s for s in self.a):
                os.mkdir(self.path_laukas.get() + '\\Mp4')
                # = []
            if any('.mov' in s for s in self.a):
                os.mkdir(self.path_laukas.get() + '\\Mov')
                # = []
            if any('.zip' in s for s in self.a):
                os.mkdir(self.path_laukas.get() + '\\Zip')
                # = []
            # self.move_files()
        except FileExistsError:
            self.uzrasas_error['text'] = 'Please delete all directories named by file endings'

    # def sort_files(self):
    #     for each in self.a:
    #         if '.txt' in each:


