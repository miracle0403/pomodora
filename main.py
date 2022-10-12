import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
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
def reset():
    window.after_cancel(timer)
    global reps
    reps = 0
    title_label.config(text="TIMER", fg=GREEN)
    text2.config(text="", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    if reps == 0:
        title_label.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN * 60)
        reps += 1
    elif reps == 1:
        title_label.config(text="SHORT BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        reps += 1
        text2.config(text="✔", fg=GREEN)
    elif reps == 2:
        title_label.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN * 60)
        reps += 1
    elif reps == 3:
        title_label.config(text="SHORT BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        reps += 1
        text2.config(text="✔✔", fg=GREEN)

    elif reps == 4:
        title_label.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN * 60)
        reps += 1
    elif reps == 5:
        title_label.config(text="SHORT BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        reps += 1
        text2.config(text="✔✔✔", fg=GREEN)

    elif reps == 6:
        title_label.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN * 60)
        reps += 1
    elif reps == 7:
        title_label.config(text="LONG BREAK", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
        reps +=1
        text2.config(text="✔✔✔✔", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(number):
    if number > -1:
        minutes = math.floor(number / 60)
        seconds = round(number % 60)
        if len(str(minutes)) < 2:
            minutes = "0" + str(minutes)
        if len(str(seconds)) < 2:
            seconds = "0" + str(seconds)
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        global timer
        timer = window.after(1000, count_down, number - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Start")
window.config(padx=100, pady=50, bg=YELLOW)

# timr label
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

# tomato canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# text1
text2 = Label(text="", font=(FONT_NAME, 10, "bold"))
text2.grid(column=1, row=2)

text1 = Button(text="Start", bg=RED, command=start_timer, font=(FONT_NAME, 10, "bold"))
text1.grid(column=0, row=3)

text3 = Button(text="Reset", bg=GREEN, command=reset, font=(FONT_NAME, 10, "bold"))
text3.grid(column=2, row=3)

window.mainloop()
