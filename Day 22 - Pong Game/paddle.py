from turtle import Turtle

START_POSITION = 'PASS'
MOVE_DISTANCE = 20
UP = 90
DOWN = 135


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.paddle = Turtle(shape="square")
        self.paddle.shapesize(stretch_wid=0.5, stretch_len=5)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(position)
        self.paddle.setheading(90)

    def up(self):
        if self.paddle.ycor() < 300:
            self.paddle.forward(30)

    def down(self):
        if self.paddle.ycor() > -300:
            self.paddle.backward(30)

