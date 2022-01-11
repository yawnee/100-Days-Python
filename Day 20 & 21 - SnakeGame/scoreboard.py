from turtle import Turtle
STYLE = ('arial', 25, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align='center', font=STYLE)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=STYLE)
