from cgi import test
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
def reset_timer():
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="", fg=GREEN, bg=YELLOW)
    window.after_cancel(timer)
    global reps
    reps = 0
   

    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED, bg=YELLOW)
        count__down(long_break_sec)
    #if it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK, bg=YELLOW)
        count__down(short_break_sec)
    else:  #if it's the 1st/3rd/5th/7th rep:
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW)
        count__down(work_sec)

    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count__down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
 
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count__down,  count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_label.config(text=marks, fg=GREEN, bg=YELLOW)


       


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#create a label
timer_label = Label(font=(FONT_NAME, 50, "bold"))
timer_label.config(text="Timer", fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)


check_label = Label(font=("Arial", 8, "bold"))
#check_label.config(text=checks, fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)



#create buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)





window.mainloop()
