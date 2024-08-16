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
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text= '')
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    print(reps)

    if reps == 8:
        mins = LONG_BREAK_MIN * 60
        reps = 1
        timer_label.config(text= "Break", fg=RED)
    elif reps % 2 != 0:
        mins = WORK_MIN * 60
        timer_label.config(text="Work", fg= GREEN)
        reps += 1
    elif reps % 2 == 0:
        mins = SHORT_BREAK_MIN * 60
        timer_label.config(text="Break" , fg=PINK)
        reps += 1
    count_down(mins)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f" {count_min}:{count_sec} ")
    if count > 0:
      timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_marks = ''
        for i in range(math.floor((reps - 2) / 2)):
            check_marks += "✔️"
        check_mark.config(text=check_marks)
        print(check_marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark = Label(font=(FONT_NAME, 16, "bold"), fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

start_button = Button(text= "Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command= reset)
reset_button.grid(column= 2, row=2)

window.mainloop()
