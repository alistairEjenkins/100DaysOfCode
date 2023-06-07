# # file not found
# with open("file.txt") as file:
#     file.read()
#
# # keyerror:
# a_dict = {"key": "value"}
# print(a_dict["non-existant key"])
#
# # indexerror
# fruit = ["apple", "banana", "plum"]
# print(fruit[4])
#
# # typeerror:
# print("text" + 6)

# catch exceptions
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    contents = file.read()
    print(contents)
finally:
    file.close()
    raise TypeError("This is an error I made up")

h = float(input("H: "))
w = int(input("W: "))

if h > 3:
    raise ValueError("Human height should not be over 3m")
bmi = w/h ** 2

