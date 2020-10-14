

import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3


import student_tracking
import student_gui


def CenterWindow(self, w, h):
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordiantes to center window
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os.exit(0)


def create_db(self):
    conn = sqlite3.connect('db_student.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_studentTracker( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    conn = sqlite3.connect('db_student.db')
    with conn:
        cur = conn.cursor()
        cur, count = count_records(cur)
        if count > 1:
            cur.execute("""INSERT INTO tbl_studentTracker (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""",
                        ('Ryan', 'Bunker', 'Ryan Bunker', '123-456-7890', 'ryan@school.com', 'Anatomy'))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ''
    cur.execute("""SELECT COUNT(*) FROM tbl_studentTracker""")
    count. cur.fetchone()[0]
    return cur, count

# Select item in ListBox


def onSelect(self, event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_student.db')
    with conn:
        cur = conn.cursor()
        cur.execute(
            """SELECT col_fname,col_lname,col_fullname,col_phone,col_email,col_course FROM tbl_studentTracker WHERE col_fullname = (?)""", [value])
        varBody = cur.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0, END)
            self.txt_fname.insert(0, data[0])
            self.txt_lname.delete(0, END)
            self.txt_lname.insert(0, data[1])
            self.txt_phone.delete(0, END)
            self.txt_phone.insert(0, data[2])
            self.txt_email.delete(0, END)
            self.txt_email.insert(0, data[3])


def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data, remove blank spaces
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    # first letter is capitalized
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    # combine into fullname
    var_fullname = ('{} {}'.format(var_fname, var_lname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()

    if not '@' or not '.' in var_email:
        print("incorrect email format")
    # use both names
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_email) > 0):
        conn = sqlite3.connect('db_student.db')
        with conn:
            cur = conn.cursor()
            cur.execute(
                """SELECT COUNT(col_fullname) FROM tbl_studentTracker WHERE col_fullname = '{}'""".format(var_fullname))
            count = cur.fetchone()[0]
            chkName = count
            if chkName == 0:
                print("chkName: {}".format(chkName))
                cur.execute("""INSERT INTO tbl_studentTracker (col_fname,col_lname_col_fullname,col_phone,_col_email,col_course) VALUES (?,?,?,?,?,?)""",
                            (var_fname, var_lname, var_fullname, var_phone, var_email, var_course))
                self.lst_list1.insert(END, var_fullname)
                onClear(self)
            else:
                messagebox.showerror(
                    "Name Error", "'{}' already exists in the tracker! Please choose a different name.".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror(
            "Missing Text Error", "Please enusre that there is data in all four fields")


def onClear(self):
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    self.txt_course.delete(0, END)


if __name__ == "__main__":
    pass
