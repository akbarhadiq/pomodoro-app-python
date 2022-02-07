from tkinter import *
# from time import *
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
REPS = 0
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global REPS
    window.after_cancel(TIMER)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS

    REPS = REPS + 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    count_minute = math.floor(count/60)
    count_second = count % 60

    if count_second < 10:
        count_second = f"0{count_second}"

    if count_second == 0:
        count_second = "00"

    # Set the timer text
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        # Add checkmark for finished 25 minute session
        for _ in range(0, math.floor(REPS/2)):
            mark += "✔"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


# Create a tkinter canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Create the canvas tomato.png
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
# Create the canvas text for the timer
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Create the timer text Label
timer_label = Label(text="Timer", fg=GREEN)
timer_label.grid(column=2, row=1)
timer_label.config(bg=YELLOW, font=(FONT_NAME, 40, "italic"))


# Create the start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)

# Create the reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

# Windows + . (Windows 10 Emoji keyboard)
# Create the checkmark label
checkmark = Label(pady=10, bg=YELLOW, fg=GREEN)
checkmark.grid(column=2, row=3)

window.mainloop()
