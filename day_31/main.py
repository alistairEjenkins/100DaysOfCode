from random import choice
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"

timer = None
next_word = {}

data = pandas.read_csv("data/french_words.csv")
words_to_learn = data.to_dict(orient="records")
print(len(words_to_learn))


def word_known():
    words_to_learn.remove(next_word)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/french_words.csv", index=False)
    next_card()


def display_card(side, next_word):
    if side == 'french':
        canvas.itemconfig(canvas_image, image=card_front_img)
        canvas.itemconfig(title_text, text="French", fill='black')
        canvas.itemconfig(word_text, text=next_word['French'], fill='black')
    else:
        canvas.itemconfig(canvas_image, image=card_back_img)
        canvas.itemconfig(title_text, text="English")
        canvas.itemconfig(word_text, text=next_word['English'])


def next_card():
    global flip_timer, next_word
    window.after_cancel(flip_timer)
    try:
        next_word = choice(words_to_learn)
    except KeyError:
        print("no more words!")
    else:
        display_card('french', next_word)
        flip_timer = window.after(3000, display_card, 'english', next_word)


# ----------------------------------- DRAW UI ----------------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=('Arial', 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=word_known)
right_button.grid(row=1, column=1)

flip_timer = window.after(3000, next_card)
window.mainloop()
