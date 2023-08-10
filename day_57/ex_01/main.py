from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

AGE_URL = 'https://api.agify.io'
GENDER_URL = 'https://api.genderize.io'

app = Flask(__name__)

def get_data(url, name, category):

    parameters = {
        'name': name
    }

    response = requests.get(url, params=parameters)
    response.raise_for_status()
    data = response.json()
    return data[category]


@app.route('/')
def home():

    random_number = randint(1,10)
    year = datetime.now().year
    return render_template('index.html', r_number=random_number, yr=year)
@app.route('/guess/<string:name>')
def guess_age(name):

    age = get_data(AGE_URL, name, 'age')
    gender = get_data(GENDER_URL, name, 'gender')
    print(age, gender)

    return render_template('age-guesser.html', name=name, age=age, gender=gender)



if __name__ == '__main__':
    app.run(debug=True)