import tkinter as tk

data = {'Variable': ['a', 'a^2', 'a^3'],
        '1': [25, 32, 18],
        '2': [2, 4, 8],
        '3': [3, 9, 27],
        '4': [4, 16, 64]}

win = tk.Tk()
win.geometry("500x200+10+10")
win.title("Table Implementation")

tk.Label(win, text="Variable").grid(row=0, column=0)
for i, var in enumerate(data['Variable']):
    tk.Label(win, text=var).grid(row=0, column=i+1)

tk.Label(win, text="1").grid(row=1, column=0)
for i, val in enumerate(data['1']):
    tk.Label(win, text=val).grid(row=1, column=i+1)

tk.Label(win, text="2").grid(row=2, column=0)
for i, val in enumerate(data['2']):
    tk.Label(win, text=val).grid(row=2, column=i+1)

tk.Label(win, text="3").grid(row=3, column=0)
for i, val in enumerate(data['3']):
    tk.Label(win, text=val).grid(row=3, column=i+1)

tk.Label(win, text="4").grid(row=4, column=0)
for i, val in enumerate(data['4']):
    tk.Label(win, text=val).grid(row=4, column=i+1)

win.mainloop()








