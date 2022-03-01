from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(0, - 280)

    def move_up(self):
        self.setheading(90)
        self.forward(15)

    def move_down(self):
        self.setheading(270)
        self.forward(15)

    def move_right(self):
        self.setheading(0)
        self.forward(15)

    def move_left(self):
        self.setheading(180)
        self.forward(15)

    def reset(self):
        self.goto(0, - 280)
