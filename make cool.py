# Apply Coolness 3.0
# Python 3

from tkinter import *


def coolness():
    """ This function makes people cool.  It will return an
            error if you attempt to use it on someone who is
            already cool."""
    name = txtEntry.get()
    # List of people who are already cool. This is a tuple, meaning
    # these individuals are unchangingly cool.
    cool_people = ("tony",
                   "kevin",
                   "bryan",
                   "matt",
                   "victor",
                   "chris",
                   "ricardo")
    for cool_person in cool_people:
        # If the user inadvertently entered the name of someone
        # who is already cool.
        if cool_person == name.lower():
            result = "ERROR! Invalid usage. \n {} is already cool.".format(name)
            break
        else:
            result = "{} is now a cool person! \n CONGRATULATIONS, {}!" \
                .format(name, name)
    txtResult.config(text=result)
    txtEntry.config(text="")


# Create the root window
window = Tk()
window.title("Apply Coolness 3.0")

# Create the frame to hold the boxes & button
mainframe = Frame(window)

# We will be using grid() to place widgets in the frame, so..
mainframe.grid()

# Set the variable for the name entered by the user
name = StringVar()

# Label that tells the user what to do.
lblPrompt = Label(mainframe, text="Enter the name of the person to be made cool:")
lblPrompt.grid(column=1, row=1, columnspan=2, padx=3, pady=3)

# Box in which user enters a person's name.
txtEntry = Entry(mainframe)
txtEntry.grid(column=1, row=2, padx=3, pady=3)

# The button that activates the coolness function.
btnCool = Button(mainframe, text="Make Cool!", command=coolness)
btnCool.grid(column=2, row=2, padx=3, pady=3)

lblResult = Label(mainframe, text="Result:")
lblResult.grid(column=1, row=3, sticky=W, padx=3, pady=3)

# Box that displays the result of the procedure.
txtResult = Label(mainframe, width=20, height=5, bd="3", relief=SUNKEN)
txtResult.grid(column=1, row=4, columnspan=2, sticky=(E, W))

# Set the focus to the entry box so the user won't have to
# click on it first.
txtEntry.focus()
window.mainloop()