import tkinter as tk

class MyWindow:
    def __init__(self, win):

        self.lbl1 = tk.Label(win, text="Laboratory Activity 3")
        self.lbl1.place(x=200, y=20)
        self.lbl2 = tk.Label(win, text="Submitted to:Mam Sayo")
        self.lbl2.place(x=200, y=40)




root = tk.Tk()
root.geometry("200x200+10+10")
root.title("Label")
mywin = MyWindow(root)
root.mainloop()