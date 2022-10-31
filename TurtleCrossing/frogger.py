from turtle import Turtle

class Frog(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("triangle")
        self.start_pos()

    def start_pos(self):
        start_x_cor = 0
        start_y_cor = -280
        self.goto(start_x_cor, start_y_cor)
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)