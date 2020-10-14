

from tkinter import *
import tkinter as tk


def load_gui(self):
    # Labels
    self.lbl_fname = tk.Label(self.master, text="First Name: ")
    self.lbl_fname.grid(row=0, column=0, padx=(26, 0),
                        pady=(15, 0), sticky=N+W)
    self.lbl_lname = tk.Label(self.master, text="Last Name: ")
    self.lbl_lname.grid(row=2, column=0, padx=(26, 0),
                        pady=(15, 0), sticky=N+W)
    self.lbl_phone = tk.Label(self.master, text="Phone Number: ")
    self.lbl_phone.grid(row=4, column=0, padx=(26, 0),
                        pady=(15, 0), sticky=N+W)
    self.lbl_email = tk.Label(self.master, text="Email: ")
    self.lbl_email.grid(row=6, column=0, padx=(26, 0),
                        pady=(15, 0), sticky=N+W)
    self.lbl_course = tk.Label(self.master, text="Current Course: ")
    self.lbl_course.grid(row=8, column=0, padx=(26, 0),
                         pady=(15, 0), sticky=N+W)
    # Text boxes
    self.txt_fname = tk.Entry(self.master, text="")
    self.txt_fname.grid(row=1, column=0, columnspan=2, padx=(26, 0),
                        pady=(15, 0), sticky=N+W+E)
    self.txt_lname = tk.Entry(self.master, text="")
    self.txt_lname.grid(row=3, column=0, columnspan=2, padx=(26, 0),
                        pady=(15, 0), sticky=N+W+E)
    self.txt_phone = tk.Entry(self.master, text="")
    self.txt_phone.grid(row=5, column=0, columnspan=2, padx=(26, 0),
                        pady=(15, 0), sticky=N+W+E)
    self.txt_email = tk.Entry(self.master, text="")
    self.txt_email.grid(row=7, column=0, columnspan=2, padx=(26, 0),
                        pady=(15, 0), sticky=N+W+E)
    self.txt_course = tk.Entry(self.master, text="")
    self.txt_course.grid(row=9, column=0, columnspan=2, padx=(26, 0),
                         pady=(15, 0), sticky=N+W+E)

    # Scrollbar
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lst_list1 = Listbox(
        self.master, exportselection=0, yscrollcommand=self.scrollbar1.set, width=40)
    self.lst_list1.bind('<<ListboxSelect>>',
                        lambda event: onSelect(self, event))
    self.scrollbar1.config(command=self.lst_list1.yview)
    self.scrollbar1.grid(row=1, column=7, rowspan=9,
                         padx=(0, 0), pady=(0, 0), sticky=N+E+S)
    self.lst_list1.grid(row=1, column=2, rowspan=9, columnspan=5, padx=(
        40, 0), pady=(0, 0), sticky=N+E+S+W)

    # Buttons
    self.btn_submit = tk.Button(self.master, width=12, height=2,
                                text='Submit', command=lambda: addToList(self))
    self.btn_submit.grid(row=10, column=0, padx=(25, 0),
                         pady=(45, 10), sticky=W)


if __name__ == "__main__":
    pass
