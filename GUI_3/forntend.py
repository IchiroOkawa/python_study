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
    global input,display
    if input == '0':
        input = '1'
    else:
        input += '1'        
    display.set(input)

def click_two():
    global input,display
    if input == '0':
        input = '2'
    else:
        input += '2'
    display.set(input)

def click_three():
    global input,display
    if input == '0':
        input = '3'
    else:
        input += '3'
    display.set(input)

def click_four():
    global input,display
    if input == '0':
        input = '4'
    else:
        input += '4'
    display.set(input)

def click_five():
    global input,display
    if input == '0':
        input = '5'
    else:
        input += '5'
    display.set(input)

def click_six():
    global input,display
    if input == '0':
        input = '6'
    else:
        input += '6'
    display.set(input)

def click_seven():
    global input,display
    if input == '0':
        input = '7'
    else:
        input += '7'
    display.set(input)

def click_eight():
    global input,display
    if input == '0':
        input = '8'
    else:
        input += '8'
    display.set(input)

def click_nine():
    global input,display
    if input == '9':
        input = '9'
    else:
        input += '9'
    display.set(input)

def click_zero():
    global input
    if input == '0':
        pass
    else:
        input += '0'
        display.set(input)

# make window
root = tk.Tk()

# name window
root.title('The calculator')

# fit size
root.geometry('300x200')

# fix size
# root.resizable(width=False,height=False)

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
two_button = tk.Button(
    bnt_frame,
    text='2',
    cursor='hand2',
    command = click_two
)
three_button = tk.Button(
    bnt_frame,
    text='3',
    cursor='hand2',
    command = click_three
)
four_button = tk.Button(
    bnt_frame,
    text='4',
    cursor='hand2',
    command = click_four
)
five_button = tk.Button(
    bnt_frame,
    text='5',
    cursor='hand2',
    command = click_five
)
six_button = tk.Button(
    bnt_frame,
    text='6',
    cursor='hand2',
    command = click_six
)
seven_button = tk.Button(
    bnt_frame,
    text='7',
    cursor='hand2',
    command = click_seven
)
eight_button = tk.Button(
    bnt_frame,
    text='8',
    cursor='hand2',
    command = click_eight
)
nine_button = tk.Button(
    bnt_frame,
    text='9',
    cursor='hand2',
    command = click_nine
)
zero_button = tk.Button(
    bnt_frame,
    text='0',
    cursor='hand2',
    command = click_zero
)

# label
display = tk.StringVar(value='0')
label = tk.Label(textvariable=display)

# deploy frame
bnt_frame.pack(fill=tk.X)

# deploy contents
plus_button.pack()
minus_button.pack()
times_button.pack()
division_button.pack()
one_button.pack()
two_button.pack()
three_button.pack()
four_button.pack()
five_button.pack()
six_button.pack()
seven_button.pack()
eight_button.pack()
nine_button.pack()
zero_button.pack()
label.pack() 

# show window
root.mainloop()