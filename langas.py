from tkinter import *
import os
import shutil


class Langas:
    def __init__(self):
        self.root = Tk()
        self.root.title('OOO')
        self.root.geometry('700x150')
        self.root.resizable(0, 0)
        apibudinimas1 = Label(self.root, text='Ši programa skirta rušiuoti failams. Noredami testi į Path lauka įrašykite kelia iki direktorijos.')
        apibudinimas1.config(font=('Courrier', 11))
        apibudinimas1.grid(row=0, columnspan=2)

        apibudinimas2 = Label(self.root, text='Ir paspauskite mygtuką Rušiuoti.')
        apibudinimas2.config(font=('Courrier', 11))
        apibudinimas2.grid(row=1, columnspan=2, sticky=W)

        path_uzrasas = Label(self.root, text='Path:')
        path_uzrasas.config(font=('Courrier', 11))
        path_uzrasas.grid(row=2, column=0, sticky=E)

        self.path_laukas = Entry(self.root)
        self.path_laukas.config(font=('Courrier', 11))
        self.path_laukas.insert(END, os.getcwd())
        self.path_laukas.grid(row=2, column=1, ipadx=100)

        self.uzrasas_error = Label(self.root, text='')
        self.uzrasas_error.config(font=('Courrier', 11))
        self.uzrasas_error.grid(row=4, columnspan=2)

        mygtukas = Button(self.root, text='Rusiuoti', command=lambda: self.search_type())
        mygtukas.grid(row=2, column=3, sticky=W)

    def search_type(self):
        global a
        a = os.listdir(self.path_laukas.get())
        print(a)
        try:
            if any('.txt' in s for s in a):
                global txt_path, txt_list
                txt_list = []
                txt_path = self.path_laukas.get() + '\\Txt'
                os.mkdir(self.path_laukas.get() + '\\Txt')
            if any('.jpg' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Jpg')
                global jpg_path
                jpg_path = self.path_laukas.get() + '\\Jpg'
                global jpg_list
                jpg_list = []
            if any('.png' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Png')
                global png_path
                png_path = self.path_laukas.get() + '\\Png'
                global png_list
                png_list = []
            if any('.docx' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Word')
                global docx_path
                docx_path = self.path_laukas.get() + '\\Word'
                global docx_list
                docx_list = []
            if any('.pptx' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Power Point')
                global pptx_path
                pptx_path = self.path_laukas.get() + '\\Power Point'
                global pptx_list
                pptx_list = []
            if any('.html' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Html')
                global html_path
                html_path = self.path_laukas.get() + '\\Html'
                global html_list
                html_list = []
            if any('.css' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Css')
                global css_path
                css_path = self.path_laukas.get() + '\\Css'
                global css_list
                css_list = []
            if any('.js' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Js')
                global js_path
                jpg_path = self.path_laukas.get() + '\\Js'
                global js_list
                js_list = []
            if any('.mp4' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Mp4')
                global mp4_path
                mp4_path = self.path_laukas.get() + '\\Mp4'
                global mp4_list
                mp4_list = []
            if any('.mov' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Mov')
                global mov_path
                mov_path = self.path_laukas.get() + '\\Mov'
                global mov_list
                mov_list = []
            if any('.zip' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Zip')
                global zip_path
                zip_path = self.path_laukas.get() + '\\Zip'
                global zip_list
                zip_list = []
            self.sort_files()
        except FileExistsError:
                self.uzrasas_error['text'] = 'Please delete all directories named by file endings'

    def sort_files(self):
        global a
        try:
            for each in a:
                if '.txt' in each:
                    txt_list.append(each)
                if '.jpg' in each:
                    jpg_list.append(each)
                if '.png' in each:
                    png_list.append(each)
                if '.docx' in each:
                    docx_list.append(each)
                if '.pptx' in each:
                    pptx_list.append(each)
                if '.html' in each:
                    html_list.append(each)
                if '.css' in each:
                    css_list.append(each)
                if '.js' in each:
                    js_list.append(each)
                if '.mp4' in each:
                    mp4_list.append(each)
                if '.mov' in each:
                    mov_list.append(each)
                if '.zip' in each:
                    zip_list.append(each)
        except NameError:
            asd = 5
        self.move_files()

    def move_files(self):
        for each in txt_list:
            shutil.move(self.path_laukas.get() + '\\' + each, txt_path)
        for each in jpg_list:
            shutil.move(self.path_laukas.get() + '\\' + each, jpg_path)
        for each in png_list:
            shutil.move(self.path_laukas.get() + '\\' + each, png_path)
        for each in docx_list:
            shutil.move(self.path_laukas.get() + '\\' + each, docx_path)
        for each in pptx_list:
            shutil.move(self.path_laukas.get() + '\\' + each, pptx_path)
        for each in html_list:
            shutil.move(self.path_laukas.get() + '\\' + each, html_path)
        for each in css_list:
            shutil.move(self.path_laukas.get() + '\\' + each, css_path)
        for each in js_list:
            shutil.move(self.path_laukas.get() + '\\' + each, js_path)
        for each in mp4_list:
            shutil.move(self.path_laukas.get() + '\\' + each, mp4_path)
        for each in mov_list:
            shutil.move(self.path_laukas.get() + '\\' + each, mov_path)
        for each in zip_list:
            shutil.move(self.path_laukas.get() + '\\' + each, zip_path)
        self.done()

    def done(self):
        self.uzrasas_error['text'] = 'Done'
