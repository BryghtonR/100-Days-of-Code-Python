from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("340x500")
        self.window.config(bg=THEME_COLOR)

        #---Score Display---
        score = 0
        self.score_line = Label(text=f"Score:{score}", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_line.place(x=200, y=20)

        #---White Background for Quiz Question---
        self.white_canvas = Canvas()
        self.white_canvas.create_rectangle(20, 0, 320, 250, outline="white", fill="white")
        self.white_canvas.config(bg=THEME_COLOR, highlightbackground=THEME_COLOR)
        self.white_canvas.place(x=0, y=80)

        #---Quiz Question---
        self.question_line = Label(text="Question Text Here! asdf asdfasdf asdfas asdf asd d  d fasdf asdf", font=("Arial", 20, "bold"), bg="white", wraplength=250)
        self.question_line.place(x=50, y=100)

        #---True Button---
        true_img = PhotoImage(file="images/true.png")
        self.true_canvas = Button()
        self.true_canvas.config(image=true_img)
        self.true_canvas.config(bg=THEME_COLOR, highlightbackground=THEME_COLOR)
        self.true_canvas.place(x=40, y=350)

        #---False Button---
        false_img = PhotoImage(file="images/false.png")
        self.false_canvas = Button()
        self.false_canvas.config(image=false_img)
        self.false_canvas.config(bg=THEME_COLOR, highlightbackground=THEME_COLOR)
        self.false_canvas.place(x=190, y=350)

        # self.get_next_question()

        self.window.mainloop()

    # def get_next_question(self):
    #     q_text = self.quiz.next_question()
    #     self.white_canvas.itemconfig(self.question_line, text=q_text)