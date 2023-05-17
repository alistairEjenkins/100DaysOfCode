# treasure map

def show_map():
    print(f"{row1}\n{row2}\n{row3}\n")

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

map = [row1, row2, row3]
show_map()


position = input("Where do you want to put the treasure?")
column, row = int(position[0]), int(position[1])
map[column - 1][row - 1] = 'X'

show_map()