from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title(titlestring="Ping Pong game")
screen.setup(width=800, height=600)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
is_game_on = True
while is_game_on:
    time.sleep(0.04)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()



screen.exitonclick()
