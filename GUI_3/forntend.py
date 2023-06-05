import tkinter as tk
import backend

input = ''
 
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
    except:
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
    except:
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
    except:
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
    except:
        answer.set('Error!')

def click_one():
    input += '1'

# make window
root = tk.Tk()

# name window
root.title('The calculator')

# fit size
root.geometry('300x200')

# fix size
root.resizable(width=False,height=False)

# make frame
bnt_frame = tk.Frame(root,padx=5,pady=5,relief=tk.RAISED)

# make button
plus_button = tk.Button(
    bnt_frame,
    text= '+',
    cursor='hand2',
    command=lambda: click_plus(a, b)
)
minus_button = tk.Button(
    bnt_frame,
    text= '-',
    cursor='hand2',
    command=lambda: click_minus(a, b)
)
times_button = tk.Button(
    bnt_frame,
    text= '*',
    cursor='hand2',
    command=lambda: click_times(a, b)
)
division_button = tk.Button(
    bnt_frame,
    text= '/',
    cursor='hand2',
    command=lambda: click_devision(a, b)
)
one_button = tk.Button(
    bnt_frame,
    text='1',
    cursor='hand2',
    command = click_one
)

# set answer as widget 
answer = tk.StringVar()
# make label
label = tk.Label(textvariable=answer)

# message
message = tk.Label(text='anwer:')

# deploy frame
top_frame.pack(fill=tk.X)
bnt_frame.pack(fill=tk.X)

# deploy contents
plus_button.pack(side=tk.LEFT,padx=15)
minus_button.pack(side=tk.LEFT,padx=15)
times_button.pack(side=tk.LEFT,padx=15)
division_button.pack(side=tk.LEFT,padx=15)
message.pack()
label.pack() 

# show window
root.mainloop()