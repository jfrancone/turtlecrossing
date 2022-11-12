from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.speed("fastest")

    def move(self):
        x = self.xcor()
        new_y = ((self.ycor()) + MOVE_DISTANCE)
        self.goto(x, new_y)
