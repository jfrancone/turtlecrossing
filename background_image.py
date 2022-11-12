from turtle import Turtle
STARTING_POSITION = (-280, -260)


class Background_Creator(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.goto(STARTING_POSITION)
        self.draw_roads()

    def dash_line(self):
        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def new_line(self):
        x = -280
        new_y = self.ycor() + 30
        self.penup()
        self.goto(x, new_y)

    def draw_roads(self):
        for _ in range(18):
            self.dash_line()
            self.new_line()
