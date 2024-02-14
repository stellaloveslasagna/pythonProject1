from tkinter import *
import random

def mouse_clicked(event):
    print(canvas.find_overlapping(event.x, event.y, event.x, event.y))
    if bob in canvas.find_ovelapping(event.x, event.y, event.x, event.y):
        print("You hit bob!")
    else:
        print("You missed ")


def move_stuff():
    global x_vel, y_vel
    canvas.move(bob, x_vel, y_vel)
    #print(canvas.coords(bob))
    if canvas.coords(bob)[2] > 800 or canvas.coords(bob)[0] < 0:
        x_vel = -x_vel
    if canvas.coords(bob)[3] > 600 or canvas.coords(bob)[1] < 0:
        y_vel = -y_vel
        canvas.itemconfig(bob, fill=f"#{random.randint(0, 0xFFFFFF):06x})")

    else:
        y_vel += 1


    canvas.create_rectangle(*canvas.coords(bob))

    window.after(16, move_stuff)


window = Tk()
canvas = Canvas(window, width="800", height="600", background="lightblue")
canvas.pack()

bob = canvas.create_rectangle(100, 100, 200, 200, fill="pink")

x_vel = 4
y_vel = 4

move_stuff()
canvas.bind("<Button-1>", mouse_clicked())
window.mainloop()