import pandas

student_dict = {
    "student" : ['alan', 'stan', 'clive'],
    "score" : [67, 67, 34],
}

for key, val in student_dict.items():
    print(key, val)

student_df = pandas.DataFrame(student_dict)

for key, val in student_df.iterrows():
    print(val.student, val.score)

