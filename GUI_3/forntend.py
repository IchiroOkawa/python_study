import tkinter as tk
import backend

input = ''
memory  = 0
# 0 is none 1 is plus 2 is minus 3 is times 4 is devision
session = 0
cnt = False
al_or_not = False
 
def click_equal():
    global session,memory,display,cnt,input
    if session == 0:
        memory = int(input)
        display.set('0')
    elif session == 1:
        memory += int(input)
        display.set(str(memory))
        cnt = True
    elif session == 2:
        memory -= int(input)
        display.set(str(memory))
        cnt = True
    elif session == 3:
        memory *= int(input)
        display.set(str(memory))
        cnt = True
    elif session == 4:
        memory /= int(input)
        display.set(str(memory))
        cnt = True

def click_plus():
    global session,memory,display,cnt,input
    if session == 0:
        memory = int(input)
        input = ''
        display.set('0')
    elif session == 1:
        memory += int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    elif session == 2:
        memory -= int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    elif session == 3:
        memory *= int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    elif session == 4:
        memory /= int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    
    session = 1

def click_minus():
    global session,memory,display,cnt,input
    if session == 0:
        memory = int(input)
        input = ''
        display.set('0')
    elif session == 1:
        memory += int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    elif session == 2:
        memory -= int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    elif session == 3:
        memory *= int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    elif session == 4:
        memory /= int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    
    session = 2

def click_times():
    global session,memory,display,cnt,input
    if session == 0:
        memory = int(input)
        input = ''
        display.set('0')
    elif session == 1:
        memory += int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    elif session == 2:
        memory -= int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    elif session == 3:
        memory *= int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    elif session == 4:
        memory /= int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    
    session = 3

def click_devision():
    global session,memory,display,cnt,input
    if session == 0:
        memory = int(input)
        input = ''
        display.set('0')
    elif session == 1:
        memory += int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    elif session == 2:
        memory -= int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    elif session == 3:
        memory *= int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    elif session == 4:
        memory /= int(input)
        input = ''
        display.set(str(memory))
        cnt = True
    
    session = 4

def click_one():
    global input,display,cnt
    if input == '0' or cnt:
        input = '1'
        cnt = False
    else:
        input += '1'        
    display.set(input)

def click_two():
    global input,display,cnt
    if input == '0' or cnt:
        input = '2'
        cnt = False
    else:
        input += '2'
    display.set(input)

def click_three():
    global input,display,cnt
    if input == '0' or cnt:
        input = '3'
    else:
        input += '3'
    display.set(input)

def click_four():
    global input,display,cnt
    if input == '0' or cnt:
        input = '4'
    else:
        input += '4'
    display.set(input)

def click_five():
    global input,display,cnt
    if input == '0' or cnt:
        input = '5'
    else:
        input += '5'
    display.set(input)

def click_six():
    global input,display,cnt
    if input == '0' or cnt:
        input = '6'
    else:
        input += '6'
    display.set(input)

def click_seven():
    global input,display,cnt
    if input == '0' or cnt:
        input = '7'
    else:
        input += '7'
    display.set(input)

def click_eight():
    global input,display,cnt
    if input == '0' or cnt:
        input = '8'
    else:
        input += '8'
    display.set(input)

def click_nine():
    global input,display,cnt
    if input == '0' or cnt:
        input = '9'
    else:
        input += '9'
    display.set(input)

def click_zero():
    global input
    if input == '0' or cnt:
        input = '0'
    else:
        input += '0'
        display.set(input)

def click_clear():
    global input,al_or_not,memory,session,display,c
    if al_or_not:
        memory = 0
        session = 0 
        al_or_not = False
        cnt = False
        c.set('C')
    else:
        input = ''
        display.set('0')
        al_or_not = True
        c.set("AC")

def click_dot():
    global input,display
    if input in '.':
        pass
    else:
        input += '.'
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
equal_button.pack()
clear_button.pack()
dot_button.pack()
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