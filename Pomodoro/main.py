from tkinter import *
import math

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
def restart_clicked():
    global reps
    
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    check_marks.config(text="")
    title_label.config(text="Pomodoro")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_clicked():
    global reps
    reps += 1

    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(5)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg=PINK)
        count_down(6)
    else:
        title_label.config(text="Work Time", fg=GREEN)
        count_down(7)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds == 0:
        seconds = "00"
    if count < 10:
        seconds = "0" + str(count)
    canvas.itemconfig(timer_text, text=(f"{minutes}:{seconds}"))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_clicked()
        check_marks.config(text=("✔"*math.floor(reps/2)))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Label
title_label = Label(text="Pomodoro", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 36, "bold"))
title_label.grid(row=0, column=1)

#Tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#Start Button
start_button = Button(text="Start", command=start_clicked)
start_button.grid(row=2, column=0)

#Restart Button
restart_button = Button(text="Restart", command=restart_clicked)
restart_button.grid(row=2, column=2)

#Check Mark (Total pomodoros counter)
check_marks = Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 12, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()