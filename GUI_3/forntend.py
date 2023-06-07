import tkinter as tk
import backend
import math

input = '0'
memory  = 0
# 0 is initial 1 is plus 2 is minus 3 is times 4 is devision
session = 0
cnt = False
al_or_not = False
after_eq = False
 
def click_equal():
    global session,memory,display,cnt,input,after_eq
    if session == 0:
        try:
            memory = int(input)
        except:
            memory = float(input)
    elif session == 1:
        try:
            memory += int(input)
        except:
            memory += float(input)
        display.set(str(memory))
        cnt = True
    elif session == 2:
        try:
            memory -= int(input)
        except:
            memory -= float(input)
        display.set(str(memory))
        cnt = True
    elif session == 3:
        try:
            memory *= int(input)
        except:
            memory *= float(input)
        display.set(str(memory))
        cnt = True
    elif session == 4:
        if input == '0':
            display.set('Error')
            try:
                memory /= int(input)
            except:
                memory /= float(input)
            display.set(str(memory))
            cnt = True
    after_eq = True

def click_plus():
    global session,memory,display,cnt,input,after_eq
    if after_eq:
        cnt = True
    elif session == 0:
        try:
            memory = int(input)
        except:
            memory = float(input)
        cnt = True       
    elif session == 1:
        try:
            memory += int(input)
        except:
            memory += float(input)
        display.set(str(memory))
        cnt = True
    elif session == 2:
        try:
            memory -= int(input)
        except:
            memory -= float(input)
        display.set(str(memory))
        cnt = True
    elif session == 3:
        try:
            memory *= int(input)
        except:
            memory *= float(input)
        display.set(str(memory))
        cnt = True
    elif session == 4:
        if input == '0':
            display.set('Error')
            try:
                memory /= int(input)
            except:
                memory /= float(input)
            display.set(str(memory))
            cnt = True
    
    session = 1
    after_eq = False

def click_minus():
    global session,memory,display,cnt,input,after_eq
    if after_eq:
        cnt = True
    elif session == 0:
        try:
            memory = int(input)
        except:
            memory = float(input)
        cnt = True  
    elif session == 1:
        try:
            memory += int(input)
        except:
            memory += float(input)
        display.set(str(memory))
        cnt = True
    elif session == 2:
        try:
            memory -= int(input)
        except:
            memory -= float(input)
        display.set(str(memory))
        cnt = True
    elif session == 3:
        try:
            memory *= int(input)
        except:
            memory *= float(input)
        display.set(str(memory))
        cnt = True
    elif session == 4:
        if input == '0':
            display.set('Error')
            try:
                memory /= int(input)
            except:
                memory /= float(input)
            display.set(str(memory))
            cnt = True

    session = 2
    after_eq = False

def click_times():
    global session,memory,display,cnt,input,after_eq
    if after_eq:
        cnt = True
    elif session == 0:
        try:
            memory = int(input)
        except:
            memory = float(input)
        cnt = True  
    elif session == 1:
        try:
            memory += int(input)
        except:
            memory += float(input)
        display.set(str(memory))
        cnt = True
    elif session == 2:
        try:
            memory -= int(input)
        except:
            memory -= float(input)
        display.set(str(memory))
        cnt = True
    elif session == 3:
        try:
            memory *= int(input)
        except:
            memory *= float(input)
        display.set(str(memory))
        cnt = True
    elif session == 4:
        if input == '0':
            display.set('Error')
            try:
                memory /= int(input)
            except:
                memory /= float(input)
            display.set(str(memory))
            cnt = True
    
    session = 3
    after_eq = False

def click_devision():
    global session,memory,display,cnt,input,after_eq
    if after_eq:
        cnt = True
    elif session == 0:
        try:
            memory = int(input)
        except:
            memory = float(input)
        cnt = True  
    elif session == 1:
        try:
            memory += int(input)
        except:
            memory += float(input)
        display.set(str(memory))
        cnt = True
    elif session == 2:
        try:
            memory -= int(input)
        except:
            memory -= float(input)
        display.set(str(memory))
        cnt = True
    elif session == 3:
        try:
            memory *= int(input)
        except:
            memory *= float(input)
        display.set(str(memory))
        cnt = True
    elif session == 4:
        if input == '0':
            display.set('Error')
            try:
                memory /= int(input)
            except:
                memory /= float(input)
            display.set(str(memory))
            cnt = True
    
    session = 4
    after_eq = False

def click_one():
    global input,display,cnt,al_or_not,c
    if input == '0' or cnt:
        input = '1'
        cnt = False
    else:
        input += '1'
    al_or_not = False
    c.set('C')
    display.set(input)

def click_two():
    global input,display,cnt,al_or_not,c
    if input == '0' or cnt:
        input = '2'
        cnt = False
    else:
        input += '2'
    al_or_not = False
    c.set('C')
    display.set(input)

def click_three():
    global input,display,cnt,al_or_not,c
    if input == '0' or cnt:
        input = '3'
        cnt = False
    else:
        input += '3'
    al_or_not = False
    c.set('C')
    display.set(input)

def click_four():
    global input,display,cnt,al_or_not,c
    if input == '0' or cnt:
        input = '4'
        cnt = False
    else:
        input += '4'
    al_or_not = False
    c.set('C')
    display.set(input)

def click_five():
    global input,display,cnt,al_or_not,c
    if input == '0' or cnt:
        input = '5'
        cnt = False
    else:
        input += '5'
    al_or_not = False
    c.set('C')
    display.set(input)

def click_six():
    global input,display,cnt,al_or_not,c
    if input == '0' or cnt:
        input = '6'
        cnt = False
    else:
        input += '6'
    al_or_not = False
    c.set('C')
    display.set(input)

def click_seven():
    global input,display,cnt,al_or_not,c
    if input == '0' or cnt:
        input = '7'
        cnt = False
    else:
        input += '7'
    al_or_not = False
    c.set('C')
    display.set(input)

def click_eight():
    global input,display,cnt,al_or_not,c
    if input == '0' or cnt:
        input = '8'
        cnt = False
    else:
        input += '8'
    al_or_not = False
    c.set('C')
    display.set(input)

def click_nine():
    global input,display,cnt,al_or_not,c
    if input == '0' or cnt:
        input = '9'
        cnt = False
    else:
        input += '9'
    al_or_not = False
    c.set('C')
    display.set(input)

def click_zero():
    global input,al_or_not,c,cnt
    if input == '0' or cnt:
        input = '0'
        cnt = False
    else:
        input += '0'
    display.set(input)
    al_or_not = False
    c.set('C')

def click_clear():
    global input,al_or_not,memory,session,display,c
    if al_or_not:
        memory = 0
        session = 0 
        al_or_not = False
        cnt = False
        c.set('C')
    else:
        if memory != 0:
            input = '0'
            display.set('0')
            al_or_not = True
            c.set("AC")
        else:
            input = ''
            display.set('0')

def click_dot():
    global input,display
    if '.' in input:
        pass
    else:
        input += '.'
    display.set(input)

def click_root():
    global input,display
    try:
        input = math.sqrt(int(input))
        display.set(str(input))
    except:
        display.set("Error")

# make window
root = tk.Tk()

# name window
root.title('The calculator')

# fit size
root.geometry('200x200')

# fix size
root.resizable(width=False,height=False)

# make frame
text_frame = tk.Frame(root,padx=10,pady=10)
bnt_frame = tk.Frame(root,padx=10,pady=10,relief=tk.RAISED)

# make button
equal_button = tk.Button(
    bnt_frame,
    text='=',
    cursor='hand2',
    command=click_equal
)
plus_button = tk.Button(
    bnt_frame,
    text= '+',
    cursor='hand2',
    command=click_plus
)
minus_button = tk.Button(
    bnt_frame,
    text= '-',
    cursor='hand2',
    command=click_minus
)
times_button = tk.Button(
    bnt_frame,
    text= '*',
    cursor='hand2',
    command=click_times
)
division_button = tk.Button(
    bnt_frame,
    text= '/',
    cursor='hand2',
    command=click_devision
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
c = tk.StringVar(value='C')
clear_button = tk.Button(
    bnt_frame,
    textvariable=c,
    command = click_clear
)
dot_button = tk.Button(
    bnt_frame,
    text='.',
    command = click_dot
)
root_button = tk.Button(
    bnt_frame,
    text='√',
    command=click_root
)

# label
display = tk.StringVar(value='0')
label = tk.Label(text_frame,textvariable=display)

# deploy frame
text_frame.pack(fill=tk.X)
bnt_frame.pack(fill=tk.X)

# deploy contents
label.pack(side=tk.TOP)
plus_button.grid(row = 0, column = 4)
minus_button.grid(row = 1, column = 4)
times_button.grid(row = 2, column = 4)
division_button.grid(row = 3, column = 4)
equal_button.grid(row = 4, column = 4)
clear_button.grid(row = 0, column = 0)
dot_button.grid(row= 0,column = 1)
one_button.grid(row=1,column=0)
two_button.grid(row=1,column=1)
three_button.grid(row=1,column=2)
four_button.grid(row=2,column=0)
five_button.grid(row=2,column=1)
six_button.grid(row=2,column=2)
seven_button.grid(row=3,column=0)
eight_button.grid(row=3,column=1)
nine_button.grid(row=3,column=2)
zero_button.grid(row=4,column=1)
root_button.grid(row=0,column=2)

# show window
root.mainloop()