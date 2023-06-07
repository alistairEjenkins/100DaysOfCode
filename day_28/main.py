from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 4
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 2
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    start_button.config(state=NORMAL)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps +=1

    start_button.config(state=DISABLED)
    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1

    if reps > 8:
        reps =0
    else:
        if reps % 8 == 0:
            title_label.config(text="Break", fg=RED)
            count_down(long_break_sec)
        elif reps % 2 == 1:
            title_label.config(text="Work!", fg=GREEN)
            count_down(work_sec)
        else:
            title_label.config(text="Break", fg=PINK)
            count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def format_time(seconds_left):

    minutes = seconds_left // 60
    seconds = seconds_left % 60
    formatted_minutes = ''
    if minutes < 10:
        formatted_minutes = f"0{minutes}"
    else:
        formatted_minutes = f"{minutes}"
    formatted_seconds = ''
    if seconds < 10:
        formatted_seconds = f"0{seconds}"
    else:
        formatted_seconds = f"{seconds}"
    return formatted_minutes + ":" + formatted_seconds

def count_down(count):

    formatted_time = format_time(count)
    canvas.itemconfig(timer_text, text=formatted_time)
    if count >0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmark_label.config(text=f"{CHECKMARK} " * (reps // 2))
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text =  canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

checkmark_label = Label(text="", bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset).\
    grid(row=2, column=2)


window.mainloop()

