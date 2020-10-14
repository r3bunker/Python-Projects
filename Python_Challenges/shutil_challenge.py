import shutil
import os
import datetime as dt
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from tkinter import filedialog


today = dt.datetime.now().date()


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
    self.txt_source = tk.Entry(
        self.master, textvariable='')
    self.txt_source.grid(row=1, column=1, columnspan=3, padx=(26, 0),
                         pady=(60, 0), sticky=N+W+E)
    self.txt_destination = tk.Entry(
        self.master, textvariable='')
    self.txt_destination.grid(row=2, column=1, columnspan=3, padx=(26, 0),
                              pady=(10, 0), sticky=N+W+E)

    # Buttons
    self.btn_source = tk.Button(self.master, width=15, height=2,
                                text='Source Folder...', command=lambda: getSourcePath(self))
    self.btn_source.grid(row=1, column=0, padx=(25, 0),
                         pady=(60, 0), sticky=W)
    self.btn_destination = tk.Button(self.master, width=15, height=2,
                                     text='Destination Folder...', command=lambda: getDestinationPath(self))
    self.btn_destination.grid(row=2, column=0, padx=(25, 0),
                              pady=(10, 10), sticky=W)
    self.btn_checkForFiles = tk.Button(
        self.master, width=15, height=3, text='Scan Files...', command=lambda: fileCheck(self))
    self.btn_checkForFiles.grid(row=3, column=0, padx=(25, 0), pady=(10, 10))
    self.btn_closeProgram = tk.Button(
        self.master, width=15, height=3, text='Close Program', command=lambda: ask_quit(self))
    self.btn_closeProgram.grid(row=3, column=2, padx=(
        350, 0), pady=(10, 10), sticky=S+E)


def getSourcePath(self):
    sourcePath = StringVar()
    folder_selected = filedialog.askdirectory()
    self.txt_source.insert(0, folder_selected)


def getDestinationPath(self):
    destinationPath = StringVar()
    folder_selected = filedialog.askdirectory()
    self.txt_destination.insert(0, folder_selected)


def fileCheck(self):
    source = self.txt_source.get()
    destination = self.txt_destination.get()
    for file in os.listdir(source):
        filetime = dt.datetime.fromtimestamp(
            os.path.getctime(os.path.join(source, file)))
        print(filetime)
        if filetime.date() == today:
            print(file + ' Needs to be moved')
            # we are saying move the files respresented by 'i' to their new destination
            shutil.copy(os.path.join(source, file), destination)
        else:
            print(file + ' stays in folder')


def ask_quit(self):
    self.master.destroy()
    os._exit(0)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
