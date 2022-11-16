# name = "Angela"
# letters_list = [letter for letter in name]
# print(letters_list)
# range(1,5)
#
# new_range = [n*2 for n in range(1,5)]
# print(new_range)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# short_names = [name.upper() for name in names if len(name)<5]
# print(short_names)
#
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
#
# import random
#
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)
#
# passed_students = {student:score for (student, score) in students_scores.items() if score > 60}
# print(passed_students)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76,  98]
}
#
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

