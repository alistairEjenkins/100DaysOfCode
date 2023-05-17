
student_scores = input("Input a list of student scores: \n>> ").split()
print(student_scores)

high_score = 0
for score in student_scores:
    score = int(score)
    if score > high_score:
        high_score = score

print(f"The highest student score is: {high_score}")