from turtle import Turtle
import random


class Truck(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed*5
        self.color((random.random(), random.random(), random.random()))
        self.shape('square')
        self.shapesize(1, 2)
        self.penup()
        self.setheading(180)
        self.setposition(320, random.randint(-240, 240))

    def move(self):
        self.forward(self.speed)
