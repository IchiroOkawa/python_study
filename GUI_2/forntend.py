import tkinter as tk
import backend
 
def click_plus(a,b):
    global answer
    try:
        # get score
        a = a.get()
        b = b.get()
        # reset inputs
        input_a.delete(0,tk.END)
        input_b.delete(0,tk.END)
        # set answer
        answer.set(backend.plus(a, b))
    except tk.TclError:
        answer.set('Error!')

def click_minus(a,b):
    global answer
    try:
        # get score
        a = a.get()
        b = b.get()
        # reset inputs
        input_a.delete(0,tk.END)
        input_b.delete(0,tk.END)
        # set answer
        answer.set(backend.minus(a, b))
    except tk.TclError:
        answer.set('Error!')

def click_times(a,b):
    global answer
    try:
        # get score
        a = a.get()
        b = b.get()
        # reset inputs
        input_a.delete(0,tk.END)
        input_b.delete(0,tk.END)
        # set answer
        answer.set(backend.times(a, b))
    except tk.TclError:
        answer.set('Error!')

def click_devision(a,b):
    global answer
    try:
        # get score
        a = a.get()
        b = b.get()
        # reset inputs
        input_a.delete(0,tk.END)
        input_b.delete(0,tk.END)
        # set answer
        answer.set(backend.devided(a, b))
    except tk.TclError:
        answer.set('Error!')

# make window
root = tk.Tk()

# name window
root.title('The calculator')

# a is widget variation
a = tk.IntVar()
# make input
input_a = tk.Entry(textvariable=a)

# b is widget variation
b = tk.IntVar()
# make input
input_b = tk.Entry(textvariable=b)

# make button
plus_button = tk.Button(
    text= '+',
    cursor='hand2',
    command=lambda: click_plus(a, b)
)
minus_button = tk.Button(
    text= '-',
    cursor='hand2',
    command=lambda: click_minus(a, b)
)
times_button = tk.Button(
    text= '*',
    cursor='hand2',
    command=lambda: click_times(a, b)
)
division_button = tk.Button(
    text= '/',
    cursor='hand2',
    command=lambda: click_division(a, b)
)

# set answer as widget 
answer = tk.StringVar()
# make label
label = tk.Label(textvariable=answer)

# deploy contents
input_a.pack()
input_b.pack()
plus_button.pack()
label.pack() 

# show window
root.mainloop()