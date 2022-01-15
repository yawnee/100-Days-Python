from turtle import Turtle
import random

SPEED = 5


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.speed("fastest")
        # self.movefaster / bounce

    def ball_spawn(self):
        self.goto(0, 0)
        if random.randint(0, 1) == 0:
            # angle_spawn = random.randint(90, 90)
            angle_spawn = random.randint(-60, 60)
        else:
            # angle_spawn = random.randint(-120, -120)
            angle_spawn = random.randint(120, 240)
        print(angle_spawn)
        self.left(angle_spawn)

    def ball_move(self):
        self.forward(SPEED)

    def ball_speed(self):
        # Does not work currently
        self.forward(SPEED)

    def ball_bounce_wall(self):
        current_angle = self.heading() * -1
        self.setheading(current_angle)

    def ball_paddle(self):
        self.left(180)
