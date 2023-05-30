from random import randint
names = ['alan', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']
scores = [44,66,36,56,16,98]

student_scores = {name:randint(35,100) for name in names}
print(student_scores)

student_passes = {name:student_scores[name]>60 for name in names}
print(student_passes)

sentence = "What is the Airspeed of an Unladen Swallow?"
word_lengths = {word: len(word) for word in sentence.split(" ")}
print(word_lengths)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
def convert_to_f(temp):

    return temp * 9 / 5 + 32

weather_f = {day:convert_to_f(temp) for day, temp in weather_c.items()}
print(weather_f)




