sentence = "what is the airspeed velocity of an unladen swallow?"
word_list = sentence.split(' ')

letter_count = {word: len(word) for word in word_list}
print(letter_count)

def temp_c_to_f(temp):

    return temp * 9 /5 + 32

weather_c = {
    "Monday" : 12,
    "Tuesday" : 14,
    "Wednesday" : 15,
    "Thursday" : 14,
    "Friday" : 21,
    "Saturday" : 22,
    "Sunday" : 24,
}

weather_f = {day: temp_c_to_f(temp) for day, temp in weather_c.items()}
print(weather_f)