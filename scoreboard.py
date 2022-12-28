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
        self.goto(POSITION)
        self.write(f'Level: {level}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(-10,0)
        self.color('black')
        self.write(f'Hit by a car!😵\n Game Over :(', move = False, align = ALIGNMENT, font = ("Deja Vu Sans Mono", 30, "bold"))
        self.color('white')
        self.write(f'Hit by a car!😵\n Game Over :(', move = False, align = ALIGNMENT, font = ("Deja Vu Sans Mono", 30, "normal"))

    def beat_high_score(self):
        self.goto(-10, -235)
        self.color('black')
        self.write(f'You beat your high score!🏅', move = False, align = ALIGNMENT, font = ("Deja Vu Sans Mono", 15, "bold"))
        self.color('white')
        self.write(f'You beat your high score!🏅', move = False, align = ALIGNMENT, font = ("Deja Vu Sans Mono", 15, "normal"))

    def end_message(self, level):
        self.goto(POSITION)
        self.print_level(level)
        self.goto(0, 0)
        self.color('black')
        self.write(f'Play again soon!🐢', move = False, align = ALIGNMENT, font = ("Deja Vu Sans Mono", 30, "bold"))
        self.color('white')
        self.write(f'Play again soon!🐢', move = False, align = ALIGNMENT, font = ("Deja Vu Sans Mono", 30, "normal"))





    


# write level on top
# write game over when you lose
