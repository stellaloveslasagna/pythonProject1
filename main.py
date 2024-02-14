from tkinter import *
from tkinter.ttk import *

def perform_operation():
    operation = operation_var.get()
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    answer_label.configure(text=result)


root = Tk()
root.title("GUI Calculator")

title_label = Label(root, text="Calculator")
title_label.grid(row=0, column=0, columnspan=3)

calculator_image = PhotoImage(file="calc3.png")
image_label = Label(root, image=calculator_image)
image_label.grid(row=2, column=0, columnspan=3, pady=10)

number1_label = Label(root, text="Enter first number:")
number1_label.grid(row=1, column=0, pady=5, padx=5)

number2_label = Label(root, text="Enter second number:")
number2_label.grid(row=1, column=1, pady=5, padx=5)

number1_entry = Entry(root)
number1_entry.grid(row=2, column=0, pady=5, padx=5)

number2_entry = Entry(root)
number2_entry.grid(row=2, column=1, pady=5, padx=5)

operation_var = StringVar(root)
operation_var.set('+')  # Default operation

operation_menu = OptionMenu(root, operation_var, '+', '-', '*', '/')
operation_menu.grid(row=2, column=2, pady=5, padx=5)

calculate_button = Button(root, text="Calculate", command=perform_operation)
calculate_button.grid(row=2, column=3, pady=5, padx=5)

answer_label = Label(root, text="Result: ")
answer_label.grid(row=3, column=0, columnspan=4, pady=5, padx=5)

root.mainloop()
