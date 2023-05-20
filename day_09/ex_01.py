student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student, mark in student_scores.items():
    if mark > 90:
        grade = "Outstanding"
    elif mark > 80:
        grade = "Exceeds Expectations"
    elif mark > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[student] = grade

print(student_grades)

