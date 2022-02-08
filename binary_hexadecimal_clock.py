import datetime
from time import strftime
from tkinter import ttk
import math
import tkinter as tk
import sys,os

def to_binary(dec, width):
    x = width - 1
    answer = ""

    while x >= 0:
        current_power = math.pow(2, x)
        # how many powers of two fit into dec?
        how_many = int(dec / current_power)
        answer += str(how_many)
        dec -= how_many * current_power
        x -= 1
    return answer

def draw_vertical_line(x):
    main_canvas.create_line(x+17,start_y+20,x+17,start_y - 60, fill="white")

def fill_dots(times_to_use, x,length):

    tup = tens_and_ones(times_to_use)
    for num in tup:
        binary_string = to_binary(num, length)
        length =4
        x += right_step
        y = start_y
        for bit in reversed(binary_string):
            coord = x, y, x + dot_size, y + dot_size
            if bit == '1':
                main_canvas.create_oval(coord, fill="blue")
            else:
                main_canvas.create_oval(coord, fill="ghost white")
            y -= 15

    return x

def tens_and_ones(num):
    tens = int(num / 10)
    ones = num % 10
    return tens, ones

def run(master):

    t = datetime.datetime.now()
    time_collection = t.hour, t.minute, t.second
    x = 15
    length =2
    for val in time_collection:
        # val is the numeric value, x is horizontal offset, length is how many dots tall the stack will be
        x = fill_dots(val, x,length)
        draw_vertical_line(x)
        length =4
    main_canvas.pack()
    main_canvas.after(200, run, master)


root = tk.Tk()
root.geometry('200x300')

# Normal Clock
def my_time():
    time_string = strftime('%H:%M:%S') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds     

time_format = 24
if len(sys.argv) >= 2:
    time_format = sys.argv[1]

my_font=('times',28,'bold') # display size and style
l1 = tk.Label(root,font=my_font,bg='yellow')
l1.pack(anchor = "center")

my_time()


# Binary clock
start_y = 150
right_step = 20
dot_size = 15

main_canvas = tk.Canvas(root, bg="black", height=500, width=200)
run(main_canvas)

root.mainloop()