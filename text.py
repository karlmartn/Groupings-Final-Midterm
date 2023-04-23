import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Enter your text:")
label.pack()

text_field = tk.Entry(root)
text_field.pack()

root.mainloop()