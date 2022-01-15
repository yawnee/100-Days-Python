from turtle import Turtle

STYLE = ('arial', 25, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.score2 = 0
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'P1 Score: {self.score} : P2 Score: {self.score2}', align='center', font=STYLE)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def increase_score2(self):
        self.score2 += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=STYLE)
        print("game over")

