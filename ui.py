from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="question_text", width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=25)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self) -> None:
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)        
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            messagebox.showinfo(title="Game Over", message=f"Final Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    
    def answer_true(self) -> None:
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self) -> None:
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct: bool) -> None:
        if is_correct:
            messagebox.showinfo(title="Result", message=f"Correct! Score: {self.quiz.score}")
        else:
            messagebox.showinfo(title="Result", message=f"Wrong :( Score: {self.quiz.score}")
        self.get_next_question()