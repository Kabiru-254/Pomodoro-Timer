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
marks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_clock():
    global reps, marks
    reps = 0
    marks = ""
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text=marks)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_secs)
        title_label.config(text="Long Break", fg=RED, font=(FONT_NAME, 20, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_secs)
        title_label.config(text="Short Break", font=(FONT_NAME, 20, "bold"), fg=PINK)
    else:
        count_down(work_secs)
        title_label.config(text="WORK!", font=(FONT_NAME, 20, "bold"), fg=GREEN)
        global marks
        marks += "✓"
        tick_label.config(text=marks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Counter")
window.config(pady=50, padx=100, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
title_label.grid(row=1, column=2)

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canvas.grid(row=2, column=2)

start_button = Button(text="START", bg=YELLOW, font=(FONT_NAME, 17), padx=10, pady=10, highlightthickness=0,
                      command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="RESET", bg=YELLOW, font=(FONT_NAME, 17), padx=10, pady=10, highlightthickness=0,
                      command=reset_clock)
reset_button.grid(row=3, column=3)

tick_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
tick_label.grid(row=4, column=2)

window.mainloop()
