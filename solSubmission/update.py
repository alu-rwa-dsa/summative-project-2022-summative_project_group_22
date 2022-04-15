from tkinter import *
import tkinter.messagebox
import sqlite3
from collections import deque
"""the above imported libraries are imporatnt in the file"""

# assign an object for the class deque
q = deque

# connect to the databse
conn = sqlite3.connect('database.db')
c = conn.cursor()
# from the table in the database select all the items
sql = "SELECT * FROM schedules"
res = c.execute(sql)

# this class has the graphical user interface functions from the library tkinter
class Application:
    def __init__(self, master):
        self.master = master
        # heading label
        self.heading = Label(master, text="Update Appointments", fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        # search criteria -->name
        self.name = Label(master, text="Enter student's Name", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        # entry for  the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280, y=62)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=102)

    # function to search
    def search_db(self):
        self.input = self.namenet.get()

        # execute sql and select the name that matches what the user is searching for
        sql = "SELECT * FROM schedules WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.time = self.row[3]
            # diaplay all the row items of the selcted row
            print(self.row)

        # creating the update form
        self.uname = Label(self.master, text="student's Name", font=('arial 18 bold'))
        self.uname.place(x=0, y=140)

        self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
        self.uage.place(x=0, y=180)

        self.utime = Label(self.master, text="Appointment Time", font=('arial 18 bold'))
        self.utime.place(x=0, y=300)
        """
        entries for each labels==========================================================
        ===================filling the search result in the entry box to update
        """
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=140)
        self.ent1.insert(END, str())

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=180)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=300)
        self.ent3.insert(END, str(self.time))

        # button to execute update
        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=400, y=380)

        # button to delete
        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=380)

    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get()  # updated name
        self.var2 = self.ent2.get()  # updated age
        self.var3 = self.ent3.get()  # updated phone

        # to update the age of a student from the edatabase select the age that matches what the user is searching for
        query = "UPDATE schedules SET name=?, age=?,time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.namenet.get(),))
        conn.commit()
        # for a successful update display the message below
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")

    def delete_db(self):
        # delete the appointment using a kname serach
        sql2 = "DELETE FROM schedules WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        # for a succesful deletion display the message below
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        # deletion of an item from the linked list
        q.pop()



# creating the object
root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(False, False)
root.mainloop()
