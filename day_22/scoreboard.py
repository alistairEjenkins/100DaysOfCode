from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 60, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,200)
        self.l_score = 0
        self.r_score = 0
        self.draw_scoreboard()

    def draw_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score}         {self.r_score}", align=ALIGN, font=FONT)












