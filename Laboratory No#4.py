import tkinter as tk

class Calculator:
    def __init__(self, win):
        self.win = win
        win.title("Calculator")
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.display = tk.Entry(win, width=16)
        self.display.grid(row=0, column=0, columnspan=4, pady=5)
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "x"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]
        for row, buttons_row in enumerate(buttons):
            for col, button_text in enumerate(buttons_row):
                button = tk.Button(self.win, text=button_text, width=4, height=2)
                button.grid(row=row + 1, column=col, padx=2, pady=2)
                button.bind('<Button-1>', self.click_button)
        clear_button = tk.Button(self.win, text="C", width=16, height=2)
        clear_button.grid(row=5, column=0, columnspan=4, padx=2, pady=2)
        clear_button.bind('<Button-1>', self.clear_display)

    def click_button(self, event):
        text = event.widget.cget("text")
        if text.isdigit() or text == ".":
            if self.new_num:
                self.current = text
                self.new_num = False
            else:
                self.current += text
        elif text in "+-x÷":
            self.op = text
            self.new_num = True
            if self.op_pending:
                self.calculate()
            else:
                self.total = float(self.current)
                self.op_pending = True
        elif text == "=":
            self.calculate()
        self.display.delete(0, tk.END)
        self.display.insert(0, str(self.total))

    def calculate(self):
        if self.op == "+":
            self.total += float(self.current)
        elif self.op == "-":
            self.total -= float(self.current)
        elif self.op == "x":
            self.total *= float(self.current)
        elif self.op == "÷":
            self.total /= float(self.current)
        self.op_pending = False
        self.current = ""

    def clear_display(self, event):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.display.delete(0, tk.END)

win = tk.Tk()
my_calculator = Calculator(win)
win.mainloop()


