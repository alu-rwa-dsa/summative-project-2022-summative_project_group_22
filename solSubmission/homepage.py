""" Here we create sort of like a homepage with a menu of what the student would want
    if one would want to schedule an appointment they are prompted to book and after that then they
    can come back to feedback and say what it has been and that's how we measure our practicability

"""
# a function that has a menu with options for the user
def home_page():
    print("***The Wellness Center***\n")
    print("***WELCOME***\nHere we prioritise and advocate for your well-being!")
    print("Start Here~~~~~\n")
    print("[1] Book Appointment")
    print("[2] Feedback")
    print("[0] Exit")
# calling the function
home_page()
# a variable to take in the user's input
choice = int(input("Enter your choice: "))

#  using the while condition loop through the options available for the user

while choice != 0:
# for number 1 pick the book.py file will be displayed
    if choice == 1:
        from book import *
# for number 2 pick the feedback.py file will be displayed
    elif choice == 2:
        from feedback import save_info
# any other picked number will display the message below
    else:
        print("choice invalid")












