from tkinter import *

"""
    save info is a function that allows us to write amd read a text file
    in this text file are the feedback received from the users who already had 
    their appointment
"""


def save_info():
    gender_info = gender.get()
    feedback_info = feedback.get()
    age_info = age.get()
    # craete an empty list
    z = []

    line = " ","Gender:", gender_info, "feedback:", feedback_info, "age: ", age_info,
    y = [line.strip() for line in open("user.txt")]
    # iterate through the items in y
    for x in y:
        # add the items in the list with variable z
        z.append(y)
        # display y
    print(y)
# creating a text file that saves data
    file = open("user.txt", "a")
# enabling the write function for gender information
    file.write("Gender: " + gender_info)

    file.write("\n")
    # enabling the write function for feedback information
    file.write("your feedback:  " + feedback_info)

    file.write("\n")
    # enabling the write function for age information
    file.write("Your Age: " + str(age_info))
    file.write("\n")
# close the file
    file.close()

# have an object to the class and call the class
app = Tk()

app.geometry("500x500")
# the title of the form
app.title("WELLNESS CENTER FORMS")
# the form heading

heading = Label(text="WELLNESS CENTER", fg="black", bg="yellow", width="500", height="3", font="10")

heading.pack()
# the labels
gender_text = Label(text="Gender :")
feedback_text = Label(text="feedback :")
age_text = Label(text="Age :")

gender_text.place(x=15, y=70)
feedback_text.place(x=15, y=140)
age_text.place(x=15, y=210)

gender = StringVar()
feedback = StringVar()
age = IntVar()

# the data entry points of the form
gender_entry = Entry(textvariable=gender, width="30")
feedback_entry = Entry(textvariable=feedback, width="30")
age_entry = Entry(textvariable=age, width="30")

gender_entry.place(x=15, y=100)
feedback_entry.place(x=15, y=180)
age_entry.place(x=15, y=240)
# the button
button = Button(app, text="Submit Data", command=save_info, width="30", height="2", bg="grey")

button.place(x=15, y=290)

mainloop()