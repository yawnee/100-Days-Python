from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

BG_COLOR = "black"

screen = Screen()
screen.setup(width=1280, height=720)
screen.bgcolor(BG_COLOR)
screen.title("My Pong Game")
screen.tracer(0)

score = Scoreboard()
paddle1 = Paddle((550, 0))
paddle2 = Paddle((-550, 0))
ball = Ball()
ball.ball_spawn()

screen.listen()
# Player 1 Controls
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")
# Player 2 Controls
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.00001)
    ball.ball_move()

    # collision with the goal net
    if ball.xcor() > 620 or ball.xcor() < -620:
        # Player 1 scores
        if ball.xcor() > 620:
            score.increase_score()
        # Player 2 scores
        elif ball.xcor() < -620:
            score.increase_score2()
        # Game ends
        if score.score == 10 or score.score2 == 10:
            score.game_over()
            game_is_on = False
        # Ball respawn after score
        ball.ball_spawn()

    # Ball bounce on top / bottom walls
    if ball.ycor() > 350 or ball.ycor() < -350:
        ball.ball_bounce_wall()

    # Detect collision with paddle

    print(ball.heading())
    if ball.distance(paddle2) > 600 and ball.xcor() > 600 or ball.distance(paddle1) > 600 and ball.xcor() > -600:
        ball.ball_paddle()
        ball.ball_speed()


screen.exitonclick()
