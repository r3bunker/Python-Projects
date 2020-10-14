# Python Ver:   3.8.5
#
# Author:       Ryan Bunker
#
# Purpose:      Student tracking
#
# Tested Os:    This code was written and tested to work with Windows 10

from tkinter import *
import tkinter as tk

import student_func
import student_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame
        self.master = master
        self.master.minsize(600, 500)
        self.master.maxsize(600, 500)

        student_func.CenterWindow(self, 600, 400)
        self.master.title("Student Tracking")
        self.master.configure(bg="darkgreen")

        self.master.protocol("WM_DELETE_WINDOW",
                             lambda: student_func.ask_quit(self))
        arg = self.master

        student_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
