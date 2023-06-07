from turtle import Turtle

CENTER = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.draw_score()



    def draw_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=CENTER, font=FONT)

    def update_score(self):
        self.score +=1
        self.draw_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align=CENTER, font=FONT)

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as file:
                file.write(str(self.high_score))
        self.score =0
        self.draw_score()