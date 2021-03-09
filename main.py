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
reps = 1
timer = None
marks = ''
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global marks
    window.after_cancel(timer)
    label1.config(text='Timer')
    marks = ''
    canvas.itemconfig(timer_text, text='00:00')
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        label1.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        label1.config(text='Break', fg=PINK)
    else:
        count_down(WORK_MIN)
        label1.config(text='Work', fg=GREEN)
    reps += 1




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

import math
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
        # print(len(str(count_sec)))
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        global marks
        marks = ''
        session_mark = math.floor(reps/2)
        for i in range(session_mark):
            marks += '✔'
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Tomato')

window.config(padx=100, pady=50, bg=YELLOW)
label1 = Label(text='Timer', font=(FONT_NAME, 35))
label1.config(fg=GREEN, bg=YELLOW)
label1.grid(row=1, column=2)

start_button = Button(text='Start', highlightthickness=0, font=('Arial', 15), command=start_timer)
start_button.config(fg='blue', bg=YELLOW)
start_button.grid(row=3, column=1)

reset_button = Button(text='Reset', font=('Arial', 15), highlightthickness=0, command=reset_timer)
reset_button.config(fg='blue', bg=YELLOW)
reset_button.grid(row=3, column=3)

check_mark = Label(font=('Arial', 20))
check_mark.config(fg=GREEN, bg=YELLOW)
check_mark.grid(row=4, column=2)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text='00:00', font=(FONT_NAME, 30, 'bold'), fill='white')
canvas.grid(row=2, column=2)
window.mainloop()
