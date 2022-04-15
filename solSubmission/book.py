from tkinter import *
import sqlite3
import tkinter.messagebox
"""the above libaries are important in this file"""


# a connection to the database where our information is stored for efficiency of data retrieval

conn = sqlite3.connect('database.db')

# a cursor to move around the database

c = conn.cursor()


# empty list to later append the ids from the database
ids = [0]


'''-------here we build a tkinter window to display our program
          that will also be a representation of our user interface when students book 
          appointments----'''

# this class has functions for the graphical user interface
class Application:
    # initialize the class
    def __init__(self, master):
        self.master = master
        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='lightgreen')
        self.left.pack(side=LEFT)
        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        #** labels for the window**

        self.heading = Label(self.left, text="WELLNESS CENTER", font=('arial 40 bold'), fg='black',
                             bg='lightgreen')
        self.heading.place(x=0, y=0)

        # ** students names

        self.name = Label(self.left, text="Student's Name", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.name.place(x=0, y=100)

        # to show their age
        self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.age.place(x=0, y=140)

        # appointment time
        self.time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.time.place(x=0, y=260)

        # Entries for all labels============================================================
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        ''' inorder to keep our database up to date with information
            that has been keyed in by a student, we create a submit button'''

        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue',
                             command=self.add_appointment)
        self.submit.place(x=300, y=340)

        # getting the number of appointments fixed to view in the log using the ids in the database
        sql2 = "SELECT ID FROM schedules "
        self.result = c.execute(sql2)
        # iterate through the id rows
        for self.row in self.result:
            self.id = self.row[0]
            # append the id
            ids.append(self.id)

        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids) - 1]

        # displaying the logs in our right frame
        self.logs = Label(self.right, text="Logs", font='arial 28 bold', fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Total Appointments till now :  " + str(self.final_id))

    # to execute the program we need a function to call when the submit button is clicked
    def add_appointment(self):

        # getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.time_ent.get()

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # adding to the database
            sql = "INSERT INTO 'schedules' (name, age, time) VALUES(?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for " + str(self.val1) + " has been created")

            self.box.insert(END, 'Appointment fixed for ' + str(self.val1) + ' at ' + str(self.val3))





# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
