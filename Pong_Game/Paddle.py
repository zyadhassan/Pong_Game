SCREEN_W=800
SCREEN_H=600
from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,right=False):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.color("white")

        if right:
             self.setposition(x=350,y=0)

        else:
            self.setposition(x=-350, y=0)


    def up(self):
        if self.ycor()<=240:
            self.setposition(x=self.xcor(),y=self.ycor()+20)



    def down(self):
        if self.ycor()>=-240:
            self.setposition(x=self.xcor(), y=self.ycor() - 20)