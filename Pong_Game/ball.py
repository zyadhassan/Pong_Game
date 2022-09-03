from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=15
        self.y_move=15
        self.move_speed=0.1


    def move(self):
        x=self.xcor()+self.x_move
        y=self.ycor()+self.y_move
        self.setposition(x, y)

    def bounce_wall(self):
            self.y_move*=-1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed*=0.9

    def reset(self) :
        self.setposition(0, 0)
        self.bounce_paddle()
        self.move_speed=0.1


