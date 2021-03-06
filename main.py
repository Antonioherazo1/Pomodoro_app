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
SECS_PER_MIN = 60
reps = 0
checks = ''
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    check_marks.config(text='')
    timer_label.config(text='Timer')
    canvas.itemconfig(timer_text, text="00:00")




# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global checks
    global reps
    reps += 1
    if 0 < reps < 9:
        if reps % 2 == 0:
            count_down(SHORT_BREAK_MIN * SECS_PER_MIN)
            checks += "✓"
            timer_label.config(text='Break', fg=PINK)
            label_color = 'pink'
            check_marks.config(text=checks)
        else:
            count_down(WORK_MIN * SECS_PER_MIN)
            timer_label.config(text='Work', fg=GREEN)
            label_color = 'green'
    else:
        count_down(LONG_BREAK_MIN * SECS_PER_MIN)
        timer_label.config(text='Break', fg=RED)
        label_color = 'red'


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
    elif reps < 9:
        print(reps)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# timer label
timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)
timer_label.config(padx=10, pady=10)

# image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# start bottom
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# check marks
check_marks = Label(text=checks, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=3)

window.mainloop()
