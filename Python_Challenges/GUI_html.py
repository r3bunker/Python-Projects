from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
from tkinter.filedialog import askopenfile
from tkinter import filedialog
import webbrowser as wb
from bs4 import BeautifulSoup


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame
        self.master = master
        self.master.minsize(650, 250)
        self.master.maxsize(650, 250)

        CenterWindow(self, 600, 400)
        self.master.title("HTML body editor")
        self.master.configure(bg="lightblue")

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
        self.master, text="", )
    self.txt_browse1.grid(row=1, column=1, columnspan=3, rowspan=2, padx=(26, 0),
                          pady=(60, 0), sticky=N+W+E)

    # Labels
    self.lbl_body = tk.Label(self.master, width=15, height=2,
                             text='Body text: ')
    self.lbl_body.grid(row=1, column=0, padx=(25, 0),
                       pady=(60, 0), sticky=W)
    # Buttons
    self.btn_commit = tk.Button(
        self.master, width=15, height=3, text='Commit', command=lambda: retrieve_input(self))
    self.btn_commit.grid(row=2, column=2, padx=(25, 0), pady=(10, 10))
    self.btn_newWebPage = tk.Button(
        self.master, width=15, height=3, text='Make New Webpage', command=lambda: makeHTML(self))
    self.btn_newWebPage.grid(row=3, column=0, padx=(25, 0), pady=(10, 10))
    self.btn_closeProgram = tk.Button(
        self.master, width=15, height=3, text='Close Program', command=lambda: ask_quit(self))
    self.btn_closeProgram.grid(row=3, column=2, padx=(
        370, 0), pady=(10, 10), sticky=S+E)


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)


def makeHTML(self):
    f = open("webpageGenerator.html", "w")
    html = ("""
    <html>
        <body>
            <h1>
                Summersale
            </h1>
        </body>
    </html>
    """)

    # soup = BeautifulSoup(html, 'html.parser')
    # h1_tag = soup.h1

    # new_tag = soup.new_h1()
    # new_tag.string = retrieve_input(self)
    # h1_tag.i.replace_with(new_tag)
    f.write(html)
    f.close()
    url = "webpageGenerator.html"
    wb.open(url)


def retrieve_input(self):
    input = self.txt_browse1.get()  # "1.0", 'end-1c'


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()