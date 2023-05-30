
nums = [1,2,3]

new_nums = [n+1 for n in nums]
print(new_nums)

name = "alan"
new_name = [letter for letter in name]
print(new_name)

new_range = [n*2 for n in range(1,5)]
print(new_range)

names = ['alan', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

cap_names = [name.capitalize() for name in names if len(name) > 4]
print(cap_names)

nums = [1,1,2,3,5,8,13,21,34,55]
square_nums = [n*n for n in nums]
print(square_nums)

evens = [n for n in nums if n % 2 == 0]
print(evens)


with open('file1.txt', 'r') as data:
    data1 = [int(line) for line in (data.readlines())]

with open('file2.txt', 'r') as data:
    data2 = [int(line) for line in (data.readlines())]

overlap = [num for num in data1 if num in data2]
print(overlap)


