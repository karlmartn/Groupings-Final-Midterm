import tkinter as tk
from tkinter import messagebox

class QuizApp(tk.Tk):import tkinter as tk
from tkinter import messagebox

class QuizApp(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.title("Quiz Generator")
        self.geometry("400x300")

        self.questions = questions
        self.score = 0
        self.current_question = 0
        self.selected_option = tk.StringVar()

        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        self.question_label = tk.Label(self, text="", font=("Arial", 12), wraplength=380)
        self.question_label.pack(pady=10)

        self.option_radio_buttons = []
        options_frame = tk.Frame(self)
        options_frame.pack(pady=10)
        for i in range(4):
            option = tk.Radiobutton(options_frame, text="", variable=self.selected_option, value=str(i + 1))
            option.pack(anchor="w")
            self.option_radio_buttons.append(option)

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)

        self.score_label = tk.Label(self, text="Score: 0")
        self.score_label.pack()

    def load_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])

            options = question["options"]
            for i in range(4):
                self.option_radio_buttons[i].config(text=options[i])

            self.selected_option.set("")
        else:
            self.show_result()

    def submit_answer(self):
        if self.selected_option.get():
            question = self.questions[self.current_question]
            if self.selected_option.get() == question["correct_answer"]:
                self.score += 1

            self.current_question += 1
            self.score_label.config(text="Score: {}".format(self.score))

            self.load_question()
        else:
            messagebox.showwarning("Warning", "Please select an option.")

    def show_result(self):
        result_message = "Quiz Completed!\nYour Score: {}/{}\n\nAnswer Key:\n".format(self.score, len(self.questions))
        for i, question in enumerate(self.questions):
            result_message += "\n{}. {}".format(i + 1, question["correct_answer"])
        messagebox.showinfo("Quiz Completed", result_message)
        self.destroy()

# Computer Engineering Quiz Data
ce_questions = [
   {
       "question": "Which of the following is an example of an input device?",
       "options": ["Keyboard", "Monitor", "Printer", "Speaker"],
       "correct_answer": "1"
   },
   {
       "question": "What does CPU stand for?",
       "options": ["Central Processing Unit", "Computer Processing Unit", "Control Processing Unit",
                   "Central Programmable Unit"],
       "correct_answer": "1"
   },
   {
       "question": "What is the binary representation of the decimal number 10?",
       "options": ["1010", "1001", "1100", "1111"],
       "correct_answer": "1"
   },
   {
       "question": "Which programming language is commonly used for web development?",
       "options": ["Java", "C++", "Python", "JavaScript"],
       "correct_answer": "4"
   }
]

# Create Computer Engineering Quiz App Instance
app = QuizApp(ce_questions)
app.mainloop()

