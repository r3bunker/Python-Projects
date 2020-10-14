from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
from tkinter.filedialog import askopenfile
from tkinter import filedialog


# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file():
    file = askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
    if file is not None:
        content = file.read()
        print(content)


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame
        self.master = master
        self.master.minsize(650, 250)
        self.master.maxsize(650, 250)

        CenterWindow(self, 600, 400)
        self.master.title("Check Files")
        self.master.configure(bg="lightgray")

        self.master.protocol("WM_DELETE_WINDOW",
                             lambda: ask_quit(self))
        arg = self.master

        load_gui(self)


def CenterWindow(self, w, h):
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordiantes to center window
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def load_gui(self):

    # Text boxes
    self.txt_browse1 = tk.Entry(
        self.master, text="")
    self.txt_browse1.grid(row=1, column=1, columnspan=3, padx=(26, 0),
                          pady=(60, 0), sticky=N+W+E)
    self.txt_browse2 = tk.Entry(
        self.master, text="")
    self.txt_browse2.grid(row=2, column=1, columnspan=3, padx=(26, 0),
                          pady=(10, 0), sticky=N+W+E)

    # Buttons
    self.btn_browse1 = tk.Button(self.master, width=15, height=2,
                                 text='Browse...', command=lambda: open_file())
    self.btn_browse1.grid(row=1, column=0, padx=(25, 0),
                          pady=(60, 0), sticky=W)
    self.btn_browse2 = tk.Button(self.master, width=15, height=2,
                                 text='Browse...', command=lambda: open_file())
    self.btn_browse2.grid(row=2, column=0, padx=(25, 0),
                          pady=(10, 10), sticky=W)
    self.btn_checkForFiles = tk.Button(
        self.master, width=15, height=3, text='Check for files...')
    self.btn_checkForFiles.grid(row=3, column=0, padx=(25, 0), pady=(10, 10))
    self.btn_closeProgram = tk.Button(
        self.master, width=15, height=3, text='Close Program', command=lambda: ask_quit(self))
    self.btn_closeProgram.grid(row=3, column=2, padx=(
        350, 0), pady=(10, 10), sticky=S+E)


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
