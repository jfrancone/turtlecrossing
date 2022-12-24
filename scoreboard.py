from turtle import Turtle
FONT = ("Courier", 15, "normal")
POSITION = (240, 250)
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(POSITION)
        self.print_level()

    def print_level(self):
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1


# write level on top
# write game over when you lose
