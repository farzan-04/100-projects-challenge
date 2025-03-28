from itertools import count
from logging import disable
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_btn.config(state= "active")
    if timer:
        window.after_cancel(timer)
        global reps #using global keyword to affect the global variable by updating reps
        reps = 0
        canvas.itemconfig(timer_text, text = "00:00")
        title.config(text = "Timer")
        check_mark.config(text = "")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_btn.config(state= "disabled") #it will disable the start button

    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's the 2nd/4th/6th rep:
    if reps in (2, 4, 6):
        title.config(text="Break Time", fg=PINK)
        count_down(short_break_sec)
    # if it's the 8th rep:
    elif reps == 8:
        title.config(text="Break Time", fg=RED)
        count_down(long_break_sec)
    # if it's the 1st/3rd/5th/7th rep:
    else:
        title.config(text="Work Time", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60) #floor gives the largest whole number less than 4.8 (e.g) that is 4
    count_sec = count % 60
    #count_hr = math.floor(count / 60*60)
    if count_sec < 10:
        count_sec = f"0{count_sec}" #this is known as dynamic typing, changing datatype of variable dynamically each time like from int to str or vice versa. its not supported by every language
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}") #lets you update the particular text of the canvas, takes a text to be updated and a text used to update
    if count > 0:
        global timer
        #for reset and cancel it giving it a name(a variable) for e.g timer
        timer = window.after(10, count_down, count-1) #Execute a command after a time delay

    else:
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check_mark.config(text = mark, fg = GREEN)
        if reps > 8:
            reset_timer()
        else:
            start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)


canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0) #highlightthickness is used to remove/hide the border of the canvas, but in my window without it also working same
canvas.grid(row = 1, column = 1)
tomato_img = PhotoImage(file = "tomato.png") #it's a way to read through a file and to get hold of particular image at a particular location.
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 120, text = "00:00", font = ("Arial",30, "bold"), fill = "white") #fill = colour

title = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 40, "bold"))
title.grid(row = 0, column = 1)

start_btn = Button(text = "Start", font = (FONT_NAME, 20, "bold"), command= start_timer, highlightthickness= 0)
start_btn.grid(row = 2, column = 0)
stop_btn = Button(text = "Reset", font = (FONT_NAME, 20, "bold"), command= reset_timer, highlightthickness=0)
stop_btn.grid(row = 2, column = 2)

check_mark = Label(text = "", fg = GREEN )
check_mark.grid(row = 3, column = 1)
#canvas.pack()
window.mainloop()




