from Paddle import Paddle
import time
from ball import Ball
from score_b import Score
# Setup the Screen window
from turtle import Screen
SCREEN_W=800
SCREEN_H=600
screen = Screen()
screen.setup(width=SCREEN_W, height=SCREEN_H) # Window Size 600*600
screen.bgcolor("black")  # the background is black
screen.title("Pong Game v1.0")  # the title of the window
screen.tracer(0)

paddle_left=Paddle(right=False)
paddle_right=Paddle(right=True)
ball=Ball()
board=Score()
# Screen Events
screen.listen()
screen.onkeypress(paddle_right.up,"Up")
screen.onkeypress(paddle_right.down,"Down")
screen.onkeypress(paddle_left.up,"w")
screen.onkeypress(paddle_left.down,"s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    board.print()


    if (ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce_wall()

    if ball.xcor() >330 and ball.distance(paddle_right)<50:
        ball.bounce_paddle()
    if ball.xcor() < -330 and ball.distance(paddle_left) < 50:
        ball.bounce_paddle()

    if ball.xcor()>380 or ball.xcor()<-380:
        if ball.xcor()>380:
            board.increase_L()
        else:
            board.increase_R()
        ball.reset()
        screen.update()
        time.sleep(0.8)


    ball.move()



# To keep window open
screen.exitonclick()