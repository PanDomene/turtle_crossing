from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.setposition(-240, 260)
        self.level = 1

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align='center', font=("Courier", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Courier', 22, "normal"))
