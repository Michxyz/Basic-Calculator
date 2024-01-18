import tkinter as tk
from asteval import Interpreter
"""A secure library such as asteval is used, which is designed to evaluate mathematical expressions without allowing arbitrary code execution.
asteval is not included by default in Python, so you have to install it with pip. To find out which version, see the requirements.txt file"""


class CalculatorApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#101729")
        self.master = master
        self.pack(fill="both", expand=True)
        self.create_widgets()
        self.aeval = Interpreter()


    #Calculator's funcs:
    def get_number(self, number):
        #Convert the current StringVar value to a string, add the new number, and set it back
        self.current_string = self.string_var.get()
        self.new_string= self.current_string + str(number) if self.current_string != '0' else str(number)
        self.string_var.set(self.new_string)
        
    def delete(self):
        self.current_string= self.string_var.get()
        self.new_string=self.current_string[:-1]
        self.string_var.set(self.new_string)

    def clear(self):
        self.current_string=self.string_var.get()
        self.current_string=str(0)
        self.string_var.set(self.current_string)

    def get_operator(self, operator):
        self.current_string=self.string_var.get()
        self.new_string=self.current_string+(operator)
        self.string_var.set(self.new_string)

    def execute(self):
        self.current_string=self.string_var.get()
        self.result = self.aeval(self.current_string)
        self.string_var.set(self.result)
        



    #GUI:
    def create_widgets(self):
        #Defining and placing the needed widgets for the app
        self.lbl_title=tk.Label(self, text="CASI-CALC", fg="#8a8e99", font=("Arial", 15)).grid(row=0, column=1,columnspan=3, padx=10, pady=10, ipadx=5, ipady=5)
        self.string_var = tk.StringVar(value="0") #Initialize a value to display on the entry widget
        self.entry_digits=tk.Entry(self, state="readonly", textvariable=self.string_var, font=("Helvetica", 20))
        self.entry_digits.grid(row=1, column=0,columnspan=4, padx=5, pady=10, sticky=("W","E"))
        #Buttons:
        self.btn_7=tk.Button(self, text="7", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_number(7))
        self.btn_7.grid(row=2, column=0, padx=10, pady=10, sticky=("W","E"))
        self.btn_8=tk.Button(self, text="8", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_number(8))
        self.btn_8.grid(row=2, column=1, padx=10, pady=10, sticky=("W","E"))
        self.btn_9=tk.Button(self, text="9", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_number(9)).grid(row=2, column=2, padx=10, pady=10, sticky=("W","E"))
        self.btn_delete=tk.Button(self, text="DEL", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=self.delete).grid(row=2, column=3, padx=10, pady=10,  sticky=("W","E"))
        self.btn_clear=tk.Button(self, text="CLEAR", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=self.clear).grid(row=2, column=4, padx=10, pady=10,  sticky=("W","E"))

        self.btn_4=tk.Button(self, text="4", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_number(4)).grid(row=3, column=0, padx=10, pady=10, sticky=("W","E"))
        self.btn_5=tk.Button(self, text="5", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_number(5)).grid(row=3, column=1, padx=10, pady=10, sticky=("W","E"))
        self.btn_6=tk.Button(self, text="6", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_number(6)).grid(row=3, column=2, padx=10, pady=10, sticky=("W","E"))
        self.btn_multiply=tk.Button(self, text="X", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_operator("*")).grid(row=3, column=3, padx=10, pady=10, sticky=("W","E"))
        self.btn_divide=tk.Button(self, text="/", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_operator("/")).grid(row=3, column=4, padx=10, pady=10, sticky=("W","E"))

        self.btn_1=tk.Button(self, text="1", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_number(1)).grid(row=4, column=0, padx=10, pady=10, sticky=("W","E"))
        self.btn_2=tk.Button(self, text="2", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_number(2)).grid(row=4, column=1,padx=10, pady=10, sticky=("W","E"))
        self.btn_3=tk.Button(self, text="3", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_number(3)).grid(row=4, column=2, padx=10, pady=10, sticky=("W","E"))
        self.btn_sum=tk.Button(self, text="+", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_operator("+")).grid(row=4, column=3, padx=10, pady=10, sticky=("W","E"))
        self.btn_subtract=tk.Button(self, text="-", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_operator("-")).grid(row=4, column=4, padx=10, pady=10, sticky=("W","E"))

        self.btn_0=tk.Button(self, text="0", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_number(0)).grid(row=5, column=0,padx=10, pady=10, sticky=("W","E"))
        self.btn_point=tk.Button(self, text=".", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_operator(".")).grid(row=5, column=1,padx=10, pady=10, sticky=("W","E"))
        self.btn_left_parenthesis=tk.Button(self, text="(", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_operator("(")).grid(row=5, column=2, padx=10, pady=10, sticky=("W","E"))
        self.btn_right_parenthesis=tk.Button(self, text=")", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.get_operator(")")).grid(row=5, column=3, padx=10, pady=10, sticky=("W","E"))
        self.btn_execute=tk.Button(self, text="EXE", bg="#8a8e99", font=("Helvetica", 15), fg="white",command=lambda: self.execute()).grid(row=5, column=4 ,padx=10, pady=10, sticky=("W","E"))

    


if __name__=="__main__":
    root=tk.Tk()
    root.geometry("450x400")
    root.title("Basic Calculator app")
    app=CalculatorApp(master=root)
    app.mainloop()