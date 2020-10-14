import tkinter as tk
from tkinter import *


win = Tk()
f = Frame(win)
b1 = Button(f, text="one")
b2 = Button(f, text="two")
b3 = Button(f, text="three")

b1.pack(side=LEFT, padx=10, pady=10)
b2.pack(side=LEFT, padx=10, pady=10)
b3.pack(side=LEFT, padx=10, pady=10)

l = Label(win, text="what is happening")
l.pack()
f.pack()


def but1():
    print("Button one was pushed")


b1.configure(command=but1)

v = StringVar()
e = Entry(win, textvariable=v)
e.pack()
v.get()
v.set("this is set by the program")

lb = Listbox(win, height=3)
lb.pack()
lb.insert(END, "first entry")
lb.insert(END, "second entry")
lb.insert(END, "third entry")
lb.insert(END, "fourth entry")

sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)
lb.curselection()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    root.mainloop()
