# grid() lines up widgets on the screen using rows and columns

from tkinter import *
from tkinter import ttk

root = Tk()

Label(root, text="First Name").grid(row=0, sticky=W, padx=4)
# Entry widget allows the user to enter info
Entry(root).grid(row=0, column=1, sticky=E, pady=4)

Label(root, text="Last Name").grid(row=1, sticky=W, padx=4)
Entry(root).grid(row=1, column=1, sticky=E, pady=4)

Button(root, text="Submit").grid(row=3)

# Label(root, text="First Name").grid(row=0, sticky=W, padx=4)
# Entry(root).grid(row=2, column=1, sticky=E, pady=4)


root.mainloop()