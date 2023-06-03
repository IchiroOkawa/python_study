import tkinter as tk
import backend

# make window
root = tk.Tk()

# name window
root.title('The calculator')

# a is widget variation
a = tk.StringVar()

# make input
input_a = tk.Entry(textvariable=a)

# b is widget variation
b = tk.StringVar()

# make input
input_b = tk.Entry(textvariable=b)

# make button
puls_button = tk.Button(
    text= '+',
    command=lambda:text.set()
)

# deploy contents
input_a.pack()
input_b.pack()

# show window
root.mainloop()