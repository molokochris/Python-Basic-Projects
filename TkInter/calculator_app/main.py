from tkinter import *
from tkinter import ttk

# root = Tk()

class Calculator:
    cal_val = 0.0
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def __init__(self, root):
        
        self.entry_val = StringVar(root, value="")
        
        root.title("Calculator")
        
        root.geometry("400x400")
        
        root.resizable(width=True, height=False)
        
        style = ttk.Style()
        
        style.configure("TButton",
                        font="Serif 15",
                        padding=10)
        
        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)
        self.number_entry = ttk.Entry(root,
                                      textvariable=self.entry_val,
                                      width=50)
        self.number_entry.grid(row=0, columnspan=4)

        # Top Row Buttons
        self.button7 = ttk.Button(root, text="7",
            command=lambda: self.button_press("7")).grid(row=1,
                                                         column=0)
        
        self.button8 = ttk.Button(root, text="8",
            command=lambda: self.button_press("8")).grid(row=1,
                                                         column=1)
        
        self.button9 = ttk.Button(root, text="9",
            command=lambda: self.button_press("9")).grid(row=1,
                                                         column=2)
        
        self.button_div = ttk.Button(root, text="/",
        command=lambda: self.math_button_press("/")).grid(row=1,
                                                         column=3)

        # Second Row Buttons
        # self.button4 = ttk.Button(root, text="4",
        #     command=lambda: self.button_press("4")).grid(row=2,
        #                                                  column=0)
        
        # self.button5 = ttk.Button(root, text="5",
        #     command=lambda: self.button_press("5")).grid(row=2,
        #                                                  column=1)
        
        # self.button6 = ttk.Button(root, text="6",
        #     command=lambda: self.button_press("6")).grid(row=2,
        #                                                  column=2)

root = Tk()
app = Calculator(root)
root.mainloop()