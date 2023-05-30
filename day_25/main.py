from turtle import Screen, Turtle

import pandas

screen = Screen()
screen.title("U.S. State Game")
image ="blank_states_img.gif"
screen.addshape(image)
turtle = Turtle(shape=image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_already = []
playing = True
turt = Turtle()
turt.hideturtle()
turt.penup()

while playing:
    answer_state = screen.textinput(title=f"{len(guessed_already)}/50 States Correct", prompt="Can you name another state?").title()
    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        if answer_state not in guessed_already:
            state_data = data[data.state == answer_state]
            turt.setpos(int(state_data.x), int(state_data.y))
            turt.write(answer_state, font=('Arial', 11, 'normal'))
            guessed_already.append(answer_state)
        else:
            screen.textinput(title="Oops!", prompt=f"You have already guessed {answer_state}. Try again.")
    if len(guessed_already) == 50:
        playing = False


# TODO: reload

