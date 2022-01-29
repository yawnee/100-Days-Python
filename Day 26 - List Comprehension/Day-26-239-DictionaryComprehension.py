# Dictionary comprehension
# new_dict = {new_key: new_value for (key, value) in dictionary.items() if test}
# passed_students = {student: score for (student, score) in students_scores.items() if score > 50}

import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score > 50}
print(passed_students)

