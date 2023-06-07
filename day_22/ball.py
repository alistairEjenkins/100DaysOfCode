from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.deflect_x = 1
        self.deflect_y = 1

    def bounce(self, direction):

        match direction:
            case 'x':self.deflect_x *= -1
            case 'y':self.deflect_y *= -1
            case other:
                self.deflect_x *= -1
                self.deflect_y *= -1

    def reset_position(self):
        self.home()
        self.bounce('xy')


    def move(self):

        new_x = self.xcor() + 10 * self.deflect_x
        new_y = self.ycor() + 10 * self.deflect_y
        self.goto(new_x, new_y)
