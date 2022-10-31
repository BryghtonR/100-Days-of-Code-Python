from turtle import Screen, Turtle
from frogger import Frog
from scoreboard import Scoreboard
from car_manager import CarManager
import random
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Frogger")
screen.tracer(0)

frog = Frog()
scoreboard = Scoreboard()

car_manager = CarManager()

screen.listen()
screen.onkeypress(frog.go_up, "Up")
screen.onkeypress(frog.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    if frog.ycor()>280:
        scoreboard.next_level()
        frog.start_pos()

    if frog.ycor()<-280:
        frog.start_pos()

    for car in car_manager.all_cars:
        if car.distance(frog) <20:
            print("game over")
            scoreboard.game_over()
            game_is_on = False
                
    car_manager.create_car()
    car_manager.move_cars()

screen.exitonclick()