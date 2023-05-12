from tkinter import *

class ListBoxTest:
    def __init__(self):
        self.root = Tk()
        self.root.title('Selection Box')
        self.root.geometry('300x300')
        self.list_box_1 = Listbox(self.root, selectmode=EXTENDED)
        self.list_box_1.pack()
        self.delete_button = Button(self.root, text="Delete", command=self.DeleteSelection)
        self.delete_button.pack()
        self.text_box = Entry(self.root, bd=1)
        self.text_box.pack()
        self.add_button = Button(self.root, text="Insert", command=self.AddSelection)
        self.add_button.pack()

        self.list_box_1.insert(1, "C++")
        self.list_box_1.insert(2, "Python")
        self.list_box_1.insert(3, "HTML")
        self.list_box_1.insert(4, "Java")

        self.root.mainloop()

    def DeleteSelection(self):
        items = self.list_box_1.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.list_box_1.delete(idx, idx)
            pos = pos + 1

    def AddSelection(self):
        item = self.text_box.get()
        if item != "":
            self.list_box_1.insert(END, item)
        self.text_box.delete(0, END)


lbt = ListBoxTest()

