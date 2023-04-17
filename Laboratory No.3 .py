import tkinter as tk


class MyWindow:
    def __init__(self, win):

        self.lbl1 = tk.Label(win, text="Laboratory Activity 3")
        self.lbl1.place(x=200, y=20)
        self.lbl2 = tk.Label(win, text="Submitted to:Mam Sayo")
        self.lbl2.place(x=200, y=40)
        self.lbl3 = tk.Label(win, text="<--- Click Here")
        self.lbl3.place(x=250, y=120)

        self.txt1 = tk.Entry(win, bd=1)
        self.txt1.place(x=200, y=80)



        def change_color():
            fg_color = self.txt1.cget("foreground")
            if button['bg'] == 'orange':
                button['bg'] = 'blue'
                if fg_color == 'black':
                    self.txt1.config(fg='blue')
                elif fg_color == 'blue':
                    self.txt1.config(fg='orange')
                else:
                    self.txt1.config(fg='black')
            else:
                button['bg'] = 'orange'
                if fg_color == 'black':
                    self.txt1.config(fg='blue')
                elif fg_color == 'blue':
                    self.txt1.config(fg='orange')
                else:
                    self.txt1.config(fg='black')


        button = tk.Button(win, text="Button", command=change_color)
        button.place(x=200, y=120)


root = tk.Tk()
root.geometry("600x400+10+10")
mywin = MyWindow(root)
root.mainloop()