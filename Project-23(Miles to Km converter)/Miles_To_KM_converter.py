from tkinter import *

from pygame.display import update

window = Tk()
window.title("Miles to KM converter")


label1 = Label(text = "Miles", font = ("Ariel", 20, "normal"))
label1.grid(row = 0, column = 2)

label2 = Label(text = "is equal to", font = ("Ariel", 20, "normal"))
label2.grid(row = 1, column = 0)

label3 = Label(text = "0", font = ("Ariel", 20, "normal"))
label3.grid(row = 1, column = 1)


label4 = Label(text = "Km", font = ("Ariel", 20, "normal"))
label4.grid(row = 1, column = 2)


entry = Entry(width = 10, font = ("Arial", 20, "normal"))
entry.grid(row = 0, column = 1)
entry.insert(END, string = "0")


def update_num():
    label3.config(text = round(float(entry.get()) * 1.609344, 2))

button = Button(text = "Calculate", font= ("Arial", 24, "normal"), command= update_num)
button.grid(row = 2, column = 1)

window.mainloop()
