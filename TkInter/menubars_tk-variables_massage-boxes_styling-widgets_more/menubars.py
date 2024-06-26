from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def quit_app():
    root.quit()

def show_about(event=None):
    messagebox.showwarning(
        "About",
        "This awesome was made in 2024"
    )

root = Tk()

the_menu = Menu(root)

# ---------- File Menu ---------

file_menu = Menu(the_menu, tearoff=0)

file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_app)

the_menu.add_cascade(label="File", menu=file_menu)

# --------- Font Menu ---------

text_font = StringVar()
text_font.set("Times")

def change_font(event=None):
    print("Font Picked: ", text_font.get())

font_menu = Menu(the_menu, tearoff=0)

font_menu.add_radiobutton(label="Times",
                          variable=text_font,
                          command=change_font)

font_menu.add_radiobutton(label="Courier",
                          variable=text_font,
                          command=change_font)

font_menu.add_radiobutton(label="Ariel",
                          variable=text_font,
                          command=change_font)

# --------- View Menu ---------

view_menu = Menu(the_menu, tearoff=0)

line_numbers = IntVar()
line_numbers.set(1)

view_menu.add_checkbutton(label="Line Numbers",
                          variable=line_numbers)

view_menu.add_cascade(label="Fonts", menu=font_menu)

the_menu.add_cascade(label="View", menu=view_menu)

# --------- Help Menu ---------

help_menu = Menu(the_menu, tearoff=0)

'''
    OSX, Windows and Linux use the following options
    Command-O, Shift+Ctrl+S, Command-Option-Q with the
    modifiers Control, Ctrl, Option, Opt, Alt, Shift,
    and Command
'''

help_menu.add_command(label="About",
                      accelerator="Alt-A",
                      command=show_about)

the_menu.add_cascade(label="Help", menu=help_menu)

root.bind("<Command-A>", show_about)
root.bind("<Command-a>", show_about)


root.config(menu=the_menu)

root.mainloop()