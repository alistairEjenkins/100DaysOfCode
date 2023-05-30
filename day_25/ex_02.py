# squirrel census

import pandas

colors = ['Gray', 'Cinnamon', 'Black']

def fur_count(color):
    return len(data[data["Primary Fur Color"] == color])

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")

count = [fur_count(color) for color in colors]
fur_color_data ={
    "Fur Color": colors,
    "Count": count,
}

squirrel_fur_count = pandas.DataFrame(fur_color_data)
squirrel_fur_count.to_csv("squirrel_count.csv")