from tkinter import *

QUESTION = "Which of these is NOT a city?"

ANSWERS = [
    "England",
    "New York",
    "London",
    "Barcelona"
]

CORRECT_ANSWER = ANSWERS.index("England")

class MultiChoiceGUI:
    def __init__(self, parent):
        root_frame = Frame(parent)
        root_frame.grid()

        self.question = MultiChoiceQuestion(QUESTION, ANSWERS, CORRECT_ANSWER)

class MultiChoiceQuestion:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
    
    def is_correct_answer(self, selected):
        return selected == self.correct_answer

if __name__ == "__main__":
    root = Tk()
    MultiChoiceGUI(root)
    root.mainloop()