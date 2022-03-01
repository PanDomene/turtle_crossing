from turtle import Screen
import time
import random
from player import Player
from truck import Truck
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
score = Score()
screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

game_on = True
score.write("Level: 1", align='center', font=("Courier", 16, "normal"))
cars = []
prob = 0.11
sleep_time = 0.02

while game_on:
    time.sleep(0.02)
    screen.update()
    new_car = random.random()
    if new_car < prob:
        cars.append(Truck(score.level/2))
    for car in cars:
        car.move()
    for car in cars:
        if player.distance(car) < 30 and car.ycor() - 19 < player.ycor() < car.ycor() + 19:
            game_on = False
            score.game_over()
    if player.ycor() >= 280:
        # sleep_time += increase
        prob *= 1.25
        player.reset()
        score.level_up()
        for car in cars:
            car.speed = 5*score.level/2

screen.exitonclick()
