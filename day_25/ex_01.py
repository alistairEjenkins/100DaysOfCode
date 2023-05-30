import csv
import pandas

# with open("weather_data.csv", "r") as data:
#     data = data.readlines()
#     for entry in data:

with open('weather_data.csv', 'r') as data_file:
    data = csv.reader(data_file)
    data = list(data)
    temperatures = [int(entry[1]) for entry in data[1:]]

print(temperatures)

data = pandas.read_csv('weather_data.csv')
print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()

average_temp = sum(temp_list) / len(temp_list)

print(average_temp)
print(data["temp"].mean())

print(data["temp"].max())

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday_temp = data[data.day == "Monday"].temp
print(f"Celcius: {float(monday_temp)}; Fahrenheit: {float(monday_temp * 9 / 5 + 32)}")

data = {
    "students": ["alan", "bob", "charles"],
    "scores": [76, 76, 45]
}

data = pandas.DataFrame(data)
data.to_csv("students.csv")




