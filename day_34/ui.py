from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.timer = None

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')

        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="", fill="black",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.display_next_question()

        self.window.mainloop()

    def display_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have reached the end of the quiz. "
                                        f"Final score: {self.quiz.score}/10")
            self.score_label(text="")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def true_pressed(self):

        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):

        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.display_next_question)
