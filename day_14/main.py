# Higher/Lower game

import random
from art import logo, vs
from game_data import data
def unique_choice(choice_a):

    choice_b = random.choice(data)
    while choice_b == choice_a:
        choice_b = choice(data)

    return choice_b

def correct_answer(answer, followers_a, followers_b):

    if answer == 'A':
        return followers_a > followers_b
    else:
        return followers_b > followers_a


score = 0
first_question = True
playing = True
while playing:
    print(logo)
    if first_question:
        choice_a = random.choice(data)
    else:
        choice_a = choice_b
    print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
    print(vs)
    choice_b = unique_choice(choice_a)
    print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
    choice = input("Who has the more followers? Type 'A' or 'B': ").upper()
    if correct_answer(choice, choice_a['follower_count'], choice_b['follower_count']):
        score += 1
        print(f"That is correct! Your score is {score}")
        first_question = False
    else:
        print(f"Sorry, you were incorrect. Game over. Final score : {score}")
        playing = False 