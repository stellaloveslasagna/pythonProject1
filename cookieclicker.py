from tkinter import *


def update_screen():
    global number_clicks
    number_clicks_label.configure(text=f"{round(number_clicks):,} clicks")
    number_clicks += rate
    if number_clicks >= 20:
        button_one_second.pack()
    if number_clicks < 20:
        button_one_second.pack_forget()
    if number_clicks >= 50:
        button_grandma.pack()
    if number_clicks < 50:
        button_grandma.pack_forget()
    window.after(16, update_screen)


def button_clicked():
    global number_clicks
    number_clicks += 1
    print(f"{number_clicks} clicks")


def one_second():
    global rate, number_clicks
    rate += 1 / 60
    number_clicks -= 20
    button_one_second.pack_forget()


def grandma():
    global rate, number_clicks
    rate += 5 / 60
    number_clicks -= 50
    button_grandma.pack_forget()


number_clicks = 0
rate = 0
window = Tk()
button = Button(window, text="Click me!", command=button_clicked)
button.pack()
button_one_second = Button(window, text="Buy Cursor (1/sec)",
                           command=one_second)
button_grandma = Button(window, text="Buy Grandma (5/sec)",
                        command=grandma)

number_clicks_label = Label(window, text="0 clicks")
number_clicks_label.pack()

update_screen()

window.mainloop()
