from tkinter import *
from tkinter.ttk import *

def add_two():
    print(int(number1_entry.get()) + int(number2_entry.get()))
    answer_label.configure(text=int(number1_entry.get()) + int(number2_entry.get()))

root =Tk()
root.title("Gui Calculator")
title_label = Label(root, text="Calculator in progress")
title_label.grid(row=0, column=0, columnspan=3)

number1_label = Label(root, text="Enter a number below")
number1_label.grid(row=2, column=0, pady=10, padx=10)

calculator_image = PhotoImage(file="calc3.png")
image_label = Label(root, image=calculator_image)
image_label.grid(row=2, column=0, columnspan=3, pady=10)

number2_label = Label(root, text="Enter a number below")
number2_label.grid(row=2, column=1, padx=10)


number1_entry = Entry(root)
number1_entry.grid(row=3, column=0)

number2_entry = Entry(root)
number2_entry.grid(row=3, column=1)

add_button = Button(root, text="+", command=add_two)
add_button.grid(row=3, column=2)

result_label = Label(root, text="+")
result_label.grid(row=4, column=0)

add_button = Button(root, text="=", command=add_two)
add_button.grid(row=3, column=3)

answer_label = Label(root, text="___")
answer_label.grid(row=4, column=1)

root.mainloop()