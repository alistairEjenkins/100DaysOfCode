from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle(-350)
right_paddle = Paddle(350)
score_left =0
score_right =0
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, "q")
screen.onkey(left_paddle.down, "a")
screen.onkey(right_paddle.up, "p")
screen.onkey(right_paddle.down, "l")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    scoreboard.draw_scoreboard()
    ball.move()

    # ball hit wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce('y')

    # ball hit paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce('x')

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score +=1

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score +=1
    # if ball hit paddle
    #   bounce in x

    # point scored
screen.exitonclick()