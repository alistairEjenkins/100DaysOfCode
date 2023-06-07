# turtle crossing

from turtle import Turtle, Screen
from random import choice, randint
from time import sleep

STARTING_MOVE_DISTANCE = 20
MOVE_INCREMENT = 10
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
LANES = [y for y in range(-280,300,20)]
STARTING_POSITION = (0, -260)

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing")
screen.bgcolor("black")
screen.tracer(0)


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(choice(COLORS))
        self.setpos(300, choice(LANES))
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):

        self.bk(self.speed)

    def accelerate(self):

        car.speed += MOVE_INCREMENT

class CarManager:

    def __init__(self):

        self.all_cars = []

    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 6:
            self.all_cars.append(Car())

    def move_cars(self):

        for car in self.all_cars:
            car.move()

    def level_up(self):

        for car in self.all_cars:
            car.accelerate()




class Timmy(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.left(90)
        self.penup()
        self.go_to_start()

    def move(self):

        new_y = self.ycor() + STARTING_MOVE_DISTANCE
        self.goto(0,new_y)

    def at_finish(self):

        return self.ycor() > 260

    def go_to_start(self):

        self.goto(STARTING_POSITION)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.level = 0
        self.setpos(-280, 250)
        self.display_level()

    def display_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=("Courier", 24, "bold"))

    def increase_level(self):
        self.level +=1
        self.display_level()

    def display_game_over(self):
        self.home()
        self.write("GAME OVER", align='center', font=("Courier", 24, "bold"))


timmy = Timmy()
screen.listen()
screen.onkey(timmy.move,"m")

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()

    sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            scoreboard.display_game_over()

    # detect road crossed
    if timmy.at_finish():
        timmy.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()