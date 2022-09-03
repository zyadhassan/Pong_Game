from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score=0
        self.l_score=0


    def Left_Score(self):

        self.goto(-100,180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

    def Right_Score(self):

        self.goto(100,180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))


    def increase_L(self):
        self.l_score+=1
        self.print()

    def increase_R(self):
        self.r_score += 1
        self.print()

    def print(self):
        self.clear()
        self.Left_Score()
        self.Right_Score()