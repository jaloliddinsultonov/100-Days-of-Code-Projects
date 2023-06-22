from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lbl = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_lbl.grid(row=0, column=1,)

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.quiz_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Quiz",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, pady=20, columnspan=2)

        # Buttons
        self.check_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.check_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        self.cross_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.cross_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lbl.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz.")
            # Disabling buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        # Line 56 and lines 60-61 are the same
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)