import tkinter as tk

root = tk.Tk()

def change_color(event):
    if label['fg'] == 'orange':
        label['fg'] = 'blue'
    else:
        label['fg'] = 'orange'

label = tk.Label(root, text="Click me!", fg='orange')
label.pack()

label.bind('<Button-1>', change_color)

root.mainloop()