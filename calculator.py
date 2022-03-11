from tkinter import *
import math
root = Tk()
root.title("Calculator")
# TODO:add icon

# size of calculator
root.geometry("323x450")
root.minsize(323, 400)
root.maxsize(323, 450)

# All functions:


def click_num(event):
    global user_val
    text = event.widget.cget("text")
    if(text == "c"):
        user_val.set("")
        user_input.update()
    elif(text == "^"):
        if(str(user_val.get()) == ""):
            x = 0
        else:
            x = user_val.get()
        user_val.set(F"pow({x},2)")
        user_input.update()
    elif(text == "√"):
        x = user_val.get()
        user_val.set(F"math.sqrt({x})")
        user_input.update()
    elif(text == "="):
        if user_val.get().isdigit():
            value = int(user_val.get())
        else:
            value = eval(user_input.get())
        user_val.set(value)
        user_input.update()

    else:
        user_val.set(user_val.get() + text)
        user_input.update()


# create variable
user_val = StringVar()
user_val.set("")

# Frames
input_frame = Frame(root)
input_frame.pack(anchor="nw", fill=X)
output_frame = Frame(root)
output_frame.pack(anchor="nw", fill=X, pady=5)
button_frame = Frame(root, borderwidth=2, background="white")
button_frame.pack(anchor="nw", padx=5, pady=5, fill=X)

# Entry widget for user input
user_input = Entry(input_frame, textvariable=user_val,
                   font=("Verdana 20 bold"), highlightthickness=2)
user_input.config(highlightbackground="black", highlightcolor="black")
user_input.pack(anchor="nw", fill=X, padx=10, pady=10, ipady=15)

# row 0 buttons
num_btn = Button(button_frame, text="c", padx=19, pady=5, font=(
    "Verdana 16 bold"))
num_btn.grid(row=0, column=0, padx=2, pady=2)
num_btn.bind("<Button-1>", click_num)

num_btn = Button(button_frame, text="%", padx=12, pady=5, font=(
    "Verdana 16 bold"))
num_btn.grid(row=0, column=1, padx=2, pady=2)
num_btn.bind("<Button-1>", click_num)

num_btn = Button(button_frame, text="√", padx=16, pady=5, font=(
    "Verdana 16 bold"))
num_btn.grid(row=0, column=2, padx=2, pady=2)
num_btn.bind("<Button-1>", click_num)


# 1 to 9 buttons | in row 1 to row 3
button_num = 0
for i in range(3, 0, -1):
    for j in range(0, 3):
        button_num += 1
        button_num = str(button_num)
        num_btn = Button(button_frame, text=button_num,
                         padx=18, pady=5, font=("Verdana 16 bold"))
        num_btn.grid(row=i, column=j, padx=2, pady=2)
        num_btn.bind("<Button-1>", click_num)
        button_num = int(button_num)


# column 3 buttons
num_btn = Button(button_frame, text="/", padx=19, pady=5, font=(
    "Verdana 16 bold"))
num_btn.grid(row=0, column=3, padx=2, pady=2)
num_btn.bind("<Button-1>", click_num)

num_btn = Button(button_frame, text="*", padx=18, pady=5, font=(
    "Verdana 16 bold"))
num_btn.grid(row=1, column=3, padx=2, pady=2)
num_btn.bind("<Button-1>", click_num)

num_btn = Button(button_frame, text="-", padx=21, pady=5, font=(
    "Verdana 16 bold"))
num_btn.grid(row=2, column=3, padx=2, pady=2)
num_btn.bind("<Button-1>", click_num)

num_btn = Button(button_frame, text="+", padx=18, pady=5, font=(
    "Verdana 16 bold"))
num_btn.grid(row=3, column=3, padx=2, pady=2)
num_btn.bind("<Button-1>", click_num)


# row 4 buttons
num_btn = Button(button_frame, text="0", padx=18, pady=5, font=(
    "Verdana 16 bold"))
num_btn.grid(row=4, column=0, padx=2, pady=2)
num_btn.bind("<Button-1>", click_num)

num_btn = Button(button_frame, text="^", padx=16, pady=5, font=(
    "Verdana 16 bold"))
num_btn.grid(row=4, column=1, padx=2, pady=2)
num_btn.bind("<Button-1>", click_num)

num_btn = Button(button_frame, text=".", padx=21, pady=5, font=(
    "Verdana 16 bold"))
num_btn.grid(row=4, column=2, padx=2, pady=2)
num_btn.bind("<Button-1>", click_num)

num_btn = Button(button_frame, text="=", padx=18, pady=5, font=(
    "Verdana 16 bold"))
num_btn.grid(row=4, column=3, padx=2, pady=2)
num_btn.bind("<Button-1>", click_num)


root.mainloop()
