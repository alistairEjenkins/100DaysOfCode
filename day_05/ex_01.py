
student_heights = input("Input a list of student heights: \n>> ").split()
print(student_heights)

total = 0
length = 0
for height in student_heights:
    total += int(height)
    length += 1
average_height = total / length

print(f"The average student height is {round(average_height)}cm")