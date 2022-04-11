from tkinter import *

class MultiChoiceGUI:
    def __init__(self, parent):
        root_frame = Frame(parent)
        root_frame.grid()

        self.question = MultiChoiceQuestion()
        Label(root_frame, text = "Question:").grid(row = 0, column = 0)
        Label(root_frame, text = self.question.question).grid(row = 0, column = 1)
        choices_frame = Frame(root_frame)
        choices_frame.grid(row = 1, column = 1)
        self.choice_var = Variable(parent, value="n")
        for choice in self.question.choices:
            Radiobutton(choices_frame, text = choice, variable = self.choice_var, value = choice, command = self.choice_changed).grid()

        self.check_label = Label(root_frame, text="", font=("Helvetica", 18, "bold"))
        self.check_label.grid(row = 2, column = 1)

    def choice_changed(self):
        self.check_label["text"] = "Correct!" if self.question.is_correct_answer(self.choice_var.get()) else "Incorrect!"
        


class MultiChoiceQuestion:
    def __init__(self):
        self.question = "Which of these is NOT a city?"
        self.choices = [
            "England",
            "New York",
            "London",
            "Barcelona"
        ]
        self.correct_answer = "England"
    
    def is_correct_answer(self, selected):
        return selected == self.correct_answer

if __name__ == "__main__":
    root = Tk()
    MultiChoiceGUI(root)
    root.mainloop()