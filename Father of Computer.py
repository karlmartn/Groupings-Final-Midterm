import tkinter as tk

class MyWindow:
    def __init__(self, win):

        self.lbl1 = tk.Label(win, text="Charles Babbage", bg="Light Blue")
        self.lbl1.place(x=100, y=100)


root = tk.Tk()
mywin = MyWindow(root)
root.title("Father of Computer")
root.mainloop()