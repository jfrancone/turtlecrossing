from turtle import Turtle
FONT = ("Courier", 15, "normal")
POSITION = (240, 250)
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(POSITION)

    def print_level(self, level):
        self.clear()
        self.write(f'Level: {level}', align=ALIGNMENT, font=FONT)

    


# write level on top
# write game over when you lose
