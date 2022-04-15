from tkinter import *
import sqlite3
from collections import deque

""" the above libraries are essential for this file to run"""

# let q be the object to  the deque class
q = deque()

# connection to database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# empty lists to append later
number = []
patients = []
z = []

# select all the items in the schedules table in the database
sql = "SELECT * FROM schedules"
res = c.execute(sql)
# iterate through the items in the sql
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)
    # for the found items in lists append them to the deque
    q.appendleft(r)
# print the deque
print(q)


# this class has the graphical user interface to show the items saved in the database
class Application:
    # initialize the class
    def __init__(self, master):
        self.master = master

        self.x = 0

        # heading
        self.heading = Label(master, text="Appointments", font=('arial 60 bold'), fg='green')
        self.heading.place(x=350, y=0)

        # button to terate through the list of  students in the database
        self.change = Button(master, text="Next student", width=25, height=2, bg='steelblue', command=self.func)
        self.change.place(x=500, y=600)
        self.n = Label(master, text="", font=('arial 200 bold'))
        self.n.place(x=500, y=100)
        self.pname = Label(master, text="", font=('arial 80 bold'))
        self.pname.place(x=300, y=400)
        self.items = []

        # a function to update the text

    def func(self):
        try:
            self.n.config(text=str(number[self.x]))
            self.pname.config(text=str(patients[self.x]))
            self.x += 1
        except IndexError as error:
            print(error)
            print("No more appointments")

# call the class
root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()
