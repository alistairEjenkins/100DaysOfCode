from turtle import Screen, Turtle

import pandas

screen = Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle(shape=image)

turt = Turtle()
turt.hideturtle()
turt.penup()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


def on_map(answer_state):
    state_data = data[data.state == answer_state]
    turt.goto(int(state_data.x), int(state_data.y))
    turt.write(answer_state, font=('Arial', 11, 'normal'))


try:
    guessed_already = pandas.read_csv("guessed_already.csv")
    guessed_already = guessed_already['state'].to_list()
except:
    guessed_already = []
else:
    for state in guessed_already:
        on_map(state)

playing = True
while playing:
    answer_state = screen.textinput(title=f"{len(guessed_already)}/50 States Correct",
                                    prompt="Can you name another state?").title()
    if answer_state == 'Exit':
        guessed_already_data = {'state': guessed_already}
        d = pandas.DataFrame(guessed_already_data)
        d.to_csv("guessed_already.csv")
        break
    if answer_state in all_states:
        if answer_state not in guessed_already:
            on_map(answer_state)
            guessed_already.append(answer_state)
        else:
            screen.textinput(title="Oops!", prompt=f"You have already guessed {answer_state}. Try again.")

    if len(guessed_already) == 50:
        playing = False

# TODO: reload
