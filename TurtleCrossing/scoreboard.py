from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.game_level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"Level: {self.game_level}", align="center", font=("Courier", 20, "normal"))

    def next_level(self):
        self.game_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 60, "normal"))
        