from tkinter import *
from tkinter import filedialog
from modules import istorija
from sys import platform
import _tkinter
import os
import shutil



def check(path):
    if os.path.isdir(path):
        return
    else:
        os.mkdir(path)


class Langas:
    def __init__(self):
        self.os = ''
        self.root = Tk()
        self.root.title('Rūšiuoklė')
        self.root.geometry('700x150')
        self.root.resizable(0, 0)

        self.current_path = os.getcwd()

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

        browse_button = Button(self.root, text='Browse', command=lambda: self.get_path())
        browse_button.config(font=('Courrier', 11))
        browse_button.grid(row=3, column=3, sticky=W)

        self.path_laukas = Entry(self.root)
        self.path_laukas.config(font=('Courrier', 11))
        self.path_laukas.insert(END, self.current_path)
        self.path_laukas.grid(row=3, column=1, ipadx=100)

        self.uzrasas_error = Label(self.root, text='')
        self.uzrasas_error.config(font=('Courrier', 11))
        self.uzrasas_error.grid(row=4, columnspan=2)

        mygtukas = Button(self.root, text='Rusiuoti', command=lambda: self.check_platform())
        mygtukas.grid(row=3, column=4, sticky=W)

    def get_path(self):
        new_path = filedialog.askdirectory(initialdir=os.path.dirname(self.current_path), mustexist=True)
        self.path_laukas.delete(0, END)
        self.path_laukas.insert(END, new_path + '/')

    def check_platform(self):
        if platform == 'linux' or platform == 'linux2':  # Linux
            self.search_type()
            self.os = 'linux'
        elif platform == 'darwin':  # OS X
            self.search_type_mac()
            self.os = 'mac'
        elif platform == 'win32':  # Windows
            self.search_type()
            self.os = 'win'

    def search_type(self):  # Check for file types, and create dirs for them on WINDOWS OR LINUX
        self.uzrasas_error['text'] = ''
        istorija.create_file()
        global a
        a = os.listdir(self.path_laukas.get())
        if any('.txt' in s for s in a):  # Txt
            global txt_path, txt_list
            txt_list = []
            txt_path = self.path_laukas.get() + '\\Txt'
            check(txt_path)
        if any('.jpg' in s for s in a):  # Jpg
            global jpg_path, jpg_list
            jpg_list = []
            jpg_path = self.path_laukas.get() + '\\Jpg'
            check(jpg_path)
        if any('.png' in s for s in a):  # Png
            global png_path, png_list
            png_path = self.path_laukas.get() + '\\Png'
            png_list = []
            check(png_path)
        if any('.docx' in s for s in a):  # Word
            global docx_path, docx_list
            docx_path = self.path_laukas.get() + '\\Word'
            docx_list = []
            check(docx_path)
        if any('.pptx' in s for s in a):  # Power Point
            global pptx_path,pptx_list
            pptx_path = self.path_laukas.get() + '\\Power Point'
            pptx_list = []
            check(pptx_path)
        if any('.xlsx' in s for s in a):  # Excel
            os.mkdir(self.path_laukas.get() + '\\Excel')
            global xlsx_path, xlsx_list
            xlsx_path = self.path_laukas.get() + '\\Excel'
            xlsx_list = []
            check(xlsx_path)
        if any('.pdf' in s for s in a):  # Pdf
            os.mkdir(self.path_laukas.get() + '\\Pdf')
            global pdf_path, pdf_list
            pdf_path = self.path_laukas.get() + '\\Pdf'
            pdf_list = []
            check(pdf_path)
        if any('.rar' in s for s in a):  # Rar
            os.mkdir(self.path_laukas.get() + '\\Rar Archive')
            global rar_path, rar_list
            rar_path = self.path_laukas.get() + '\\Rar Archive'
            rar_list = []
            check(rar_path)
        if any('.mp4' in s for s in a):  # Mp4
            os.mkdir(self.path_laukas.get() + '\\Mp4')
            global mp4_path, mp4_list
            mp4_path = self.path_laukas.get() + '\\Mp4'
            mp4_list = []
            check(mp4_path)
        if any('.mov' in s for s in a):  # Mov
            os.mkdir(self.path_laukas.get() + '\\Mov')
            global mov_path, mov_list
            mov_path = self.path_laukas.get() + '\\Mov'
            mov_list = []
            check(mov_path)
        if any('.zip' in s for s in a):  # Zip
            os.mkdir(self.path_laukas.get() + '\\Zip')
            global zip_path, zip_list
            zip_path = self.path_laukas.get() + '\\Zip'
            zip_list = []
            check(zip_path)

        self.sort_files()

    def search_type_mac(self):  # Check for file types, and create dirs for them on MAC
        self.uzrasas_error['text'] = ''
        istorija.create_file()
        global a
        a = os.listdir(self.path_laukas.get())
        if any('.txt' in s for s in a):  # Txt
            global txt_path, txt_list
            txt_list = []
            txt_path = self.path_laukas.get() + '\Txt'
            check(txt_path)
        if any('.jpg' in s for s in a):  # Jpg
            global jpg_path, jpg_list
            jpg_list = []
            jpg_path = self.path_laukas.get() + '\Jpg'
            check(jpg_path)
        if any('.png' in s for s in a):  # Png
            global png_path, png_list
            png_path = self.path_laukas.get() + '\Png'
            png_list = []
            check(png_path)
        if any('.docx' in s for s in a):  # Word
            global docx_path, docx_list
            docx_path = self.path_laukas.get() + '\Word'
            docx_list = []
            check(docx_path)
        if any('.pptx' in s for s in a):  # Power Point
            global pptx_path,pptx_list
            pptx_path = self.path_laukas.get() + '\Power Point'
            pptx_list = []
            check(pptx_path)
        if any('.xlsx' in s for s in a):  # Excel
            global xlsx_path, xlsx_list
            xlsx_path = self.path_laukas.get() + '\Excel'
            xlsx_list = []
            check(xlsx_path)
        if any('.pdf' in s for s in a):  # Pdf
            global pdf_path, pdf_list
            pdf_path = self.path_laukas.get() + '\Pdf'
            pdf_list = []
            check(pdf_path)
        if any('.rar' in s for s in a):  # Rar
            global rar_path, rar_list
            rar_path = self.path_laukas.get() + '\Rar Archive'
            rar_list = []
            check(rar_path)
        if any('.mp4' in s for s in a):  # Mp4
            global mp4_path, mp4_list
            mp4_path = self.path_laukas.get() + '\Mp4'
            mp4_list = []
            check(mp4_path)
        if any('.mov' in s for s in a):  # Mov
            global mov_path, mov_list
            mov_path = self.path_laukas.get() + '\Mov'
            mov_list = []
            check(mov_path)
        if any('.zip' in s for s in a):  # Zip
            global zip_path, zip_list
            zip_path = self.path_laukas.get() + '\Zip'
            zip_list = []
            check(zip_path)

        self.sort_files()

    def sort_files(self):  # Sort all found files into lists
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
        if self.os == 'linux' or self.os == 'win':
            self.move_files()
        else:
            self.move_files_mac()

    def move_files(self):  # Move files from current dir to 'File type' dirs WIN OR LINUX
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

    def move_files_mac(self):  # Move files from current dir to 'File type' dirs MAC
        if 'txt_list' in globals() or 'txt_list' in locals():
            for each in txt_list:
                istorija.mark_file(each, self.path_laukas.get(), txt_path)
                shutil.move(self.path_laukas.get() + each, txt_path)
        if 'jpg_list' in globals() or 'jpg_list' in locals():
            for each in jpg_list:
                istorija.mark_file(each, self.path_laukas.get(), jpg_path)
                shutil.move(self.path_laukas.get() + each, jpg_path)
        if 'png_list' in globals() or 'png_list' in locals():
            for each in png_list:
                istorija.mark_file(each, self.path_laukas.get(), png_path)
                shutil.move(self.path_laukas.get() + each, png_path)
        if 'docx_list' in globals() or 'docx_list' in locals():
            for each in docx_list:
                istorija.mark_file(each, self.path_laukas.get(), docx_path)
                shutil.move(self.path_laukas.get() + each, docx_path)
        if 'pptx_list' in globals() or 'pptx_list' in locals():
            for each in pptx_list:
                istorija.mark_file(each, self.path_laukas.get(), pptx_path)
                shutil.move(self.path_laukas.get() + each, pptx_path)
        if 'xlsx_list' in globals() or 'xlsx_list' in locals():
            for each in xlsx_list:
                istorija.mark_file(each, self.path_laukas.get(), xlsx_path)
                shutil.move(self.path_laukas.get() + each, xlsx_path)
        if 'pdf_list' in globals() or 'pdf_list' in locals():
            for each in pdf_list:
                istorija.mark_file(each, self.path_laukas.get(), pdf_path)
                shutil.move(self.path_laukas.get() + each, pdf_path)
        if 'rar_list' in globals() or 'rar_list' in locals():
            for each in rar_list:
                istorija.mark_file(each, self.path_laukas.get(), rar_path)
                shutil.move(self.path_laukas.get() + each, rar_path)
        if 'mp4_list' in globals() or 'mp4_list' in locals():
            for each in mp4_list:
                istorija.mark_file(each, self.path_laukas.get(), mp4_path)
                shutil.move(self.path_laukas.get() + each, mp4_path)
        if 'mov_list' in globals() or 'mov_list' in locals():
            for each in mov_list:
                istorija.mark_file(each, self.path_laukas.get(), mov_path)
                shutil.move(self.path_laukas.get() + each, mov_path)
        if 'zip_list' in globals() or 'zip_list' in locals():
            for each in zip_list:
                istorija.mark_file(each, self.path_laukas.get(), zip_path)
                shutil.move(self.path_laukas.get() + each, zip_path)
        self.done()

    def done(self):
        self.uzrasas_error['text'] = 'Done'
