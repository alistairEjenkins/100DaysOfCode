
fruits = ["apple", "banana", "pear"]

def make_pie(index):

    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(f"Making {fruit} pie!")

make_pie(4)
make_pie(2)
make_pie(1)
