from tkinter import *
import os
import shutil
from modules import istorija


class Langas:
    def __init__(self):
        self.root = Tk()
        self.root.title('Rūšiuoklė')
        self.root.geometry('700x150')
        self.root.resizable(0, 0)
        apibudinimas1 = Label(self.root, text='Ši programa skirta rušiuoti failams. Noredami testi į Path lauka įrašykite kelia iki direktorijos.')
        apibudinimas1.config(font=('Courrier', 11))
        apibudinimas1.grid(row=0, columnspan=2)

        apibudinimas2 = Label(self.root, text='Ir paspauskite mygtuką Rušiuoti.')
        apibudinimas2.config(font=('Courrier', 11))
        apibudinimas2.grid(row=1, columnspan=2, sticky=W)

        apibudinimas3 = Label(self.root, text='Failas "Edit history.txt" bus sukurtas tam paciam aplanke kur yra programa.')
        apibudinimas3.config(font=('Courrier', 11))
        apibudinimas3.grid(row=2, columnspan=2, sticky=W)

        path_uzrasas = Label(self.root, text='Path:')
        path_uzrasas.config(font=('Courrier', 11))
        path_uzrasas.grid(row=3, column=0, sticky=E)

        self.path_laukas = Entry(self.root)
        self.path_laukas.config(font=('Courrier', 11))
        self.path_laukas.insert(END, os.getcwd())
        self.path_laukas.grid(row=3, column=1, ipadx=100)

        self.uzrasas_error = Label(self.root, text='')
        self.uzrasas_error.config(font=('Courrier', 11))
        self.uzrasas_error.grid(row=4, columnspan=2)

        mygtukas = Button(self.root, text='Rusiuoti', command=lambda: self.search_type())
        mygtukas.grid(row=3, column=3, sticky=W)

    def search_type(self):
        self.uzrasas_error['text'] = ''
        istorija.create_file()
        global a
        a = os.listdir(self.path_laukas.get())
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
            if any('.xlsx' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Excel')
                global xlsx_path
                xlsx_path = self.path_laukas.get() + '\\Excel'
                global xlsx_list
                xlsx_list = []
            if any('.pdf' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Pdf')
                global pdf_path
                pdf_path = self.path_laukas.get() + '\\Pdf'
                global pdf_list
                pdf_list = []
            if any('.rar' in s for s in a):
                os.mkdir(self.path_laukas.get() + '\\Rar Archive')
                global rar_path
                rar_path = self.path_laukas.get() + '\\Rar Archive'
                global rar_list
                rar_list = []
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
            if '.xlsx' in each:
                xlsx_list.append(each)
            if '.pdf' in each:
                pdf_list.append(each)
            if '.rar' in each:
                rar_list.append(each)
            if '.mp4' in each:
                mp4_list.append(each)
            if '.mov' in each:
                mov_list.append(each)
            if '.zip' in each:
                zip_list.append(each)
        self.move_files()

    def move_files(self):
        if 'txt_list' in globals() or 'txt_list' in locals():
            for each in txt_list:
                istorija.mark_file(each, self.path_laukas.get(), txt_path)
                shutil.move(self.path_laukas.get() + '\\' + each, txt_path)
        if 'jpg_list' in globals() or 'jpg_list' in locals():
            for each in jpg_list:
                istorija.mark_file(each, self.path_laukas.get(), jpg_path)
                shutil.move(self.path_laukas.get() + '\\' + each, jpg_path)
        if 'png_list' in globals() or 'png_list' in locals():
            for each in png_list:
                istorija.mark_file(each, self.path_laukas.get(), png_path)
                shutil.move(self.path_laukas.get() + '\\' + each, png_path)
        if 'docx_list' in globals() or 'docx_list' in locals():
            for each in docx_list:
                istorija.mark_file(each, self.path_laukas.get(), docx_path)
                shutil.move(self.path_laukas.get() + '\\' + each, docx_path)
        if 'pptx_list' in globals() or 'pptx_list' in locals():
            for each in pptx_list:
                istorija.mark_file(each, self.path_laukas.get(), pptx_path)
                shutil.move(self.path_laukas.get() + '\\' + each, pptx_path)
        if 'xlsx_list' in globals() or 'xlsx_list' in locals():
            for each in xlsx_list:
                istorija.mark_file(each, self.path_laukas.get(), xlsx_path)
                shutil.move(self.path_laukas.get() + '\\' + each, xlsx_path)
        if 'pdf_list' in globals() or 'pdf_list' in locals():
            for each in pdf_list:
                istorija.mark_file(each, self.path_laukas.get(), pdf_path)
                shutil.move(self.path_laukas.get() + '\\' + each, pdf_path)
        if 'rar_list' in globals() or 'rar_list' in locals():
            for each in rar_list:
                istorija.mark_file(each, self.path_laukas.get(), rar_path)
                shutil.move(self.path_laukas.get() + '\\' + each, rar_path)
        if 'mp4_list' in globals() or 'mp4_list' in locals():
            for each in mp4_list:
                istorija.mark_file(each, self.path_laukas.get(), mp4_path)
                shutil.move(self.path_laukas.get() + '\\' + each, mp4_path)
        if 'mov_list' in globals() or 'mov_list' in locals():
            for each in mov_list:
                istorija.mark_file(each, self.path_laukas.get(), mov_path)
                shutil.move(self.path_laukas.get() + '\\' + each, mov_path)
        if 'zip_list' in globals() or 'zip_list' in locals():
            for each in zip_list:
                istorija.mark_file(each, self.path_laukas.get(), zip_path)
                shutil.move(self.path_laukas.get() + '\\' + each, zip_path)
        self.done()

    def done(self):
        self.uzrasas_error['text'] = 'Done'
