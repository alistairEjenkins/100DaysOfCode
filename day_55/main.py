from flask import Flask
from random import randint
app = Flask(__name__)

secret_num = randint(0,9)
print(secret_num)

@app.route('/')
def home():
    return "<h1> Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route('/<int:guess>')
def num_guessed(guess):

    if guess < secret_num:
        return "<h1> Too low! Guess again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif guess > secret_num:
        return "<h1> Too High! Guess again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return f"<h1> You have guessed the secret number, {secret_num}</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True)


