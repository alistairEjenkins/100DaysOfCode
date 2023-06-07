# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", 'a') as file:
    file.write("\nNew text ..")

with open("new_file.txt", 'w') as file:
    file.write("new file created and written to.")

with open("\Users\alist\OneDrive\Documents\GitHub\100DaysOfCode\day_24\new_file.txt") as file:
    contents = file.read()
    print(contents)