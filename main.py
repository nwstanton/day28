from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    s_rest = SHORT_BREAK_MIN * 60
    l_rest = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(l_rest)
        title.config(text="Long Rest", fg=RED)
    elif reps % 2 == 0:
        count_down(s_rest)
        title.config(text="Short Rest", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    # example of dynamic typing
    if count_sec == 0:
        count_sec = "00"
    elif count_sec <10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        chk.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tm_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tm_png)
timer_text = canvas.create_text(103,130, text="00:00", font=("aireal", 24, "bold"), fill="white")
canvas.grid(column=1, row=1)


title = Label(text="Timer", font=("arieal", 24, "bold"), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)

start_btn = Button(text="START", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="RESET", command=reset_timer)
reset_btn.grid(column=2, row=2)

chk = Label(font=("arieal", 24, "bold"), bg=YELLOW, fg=GREEN)
chk.grid(column=1, row=2)

window.mainloop()
