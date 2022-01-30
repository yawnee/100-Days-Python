# Dictionary comprehension
# new_dict = {new_key: new_value for (key, value) in dictionary.items() if test}
# passed_students = {student: score for (student, score) in students_scores.items() if score > 50}

import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# Generates random scores of each student
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)
print("")

# Takes previous dictionary 'students_score' and generates new list of those who passed > 50
passed_students = {student: score for (student, score) in students_scores.items() if score > 50}
print(passed_students)
print("")

# Creates a list of words and counts their letters
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
results = {word: len(word) for word in sentence.split()}
print(results)
print("")

# Creates a list by converting cel to Fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: temp_c*9/5+32 for (day, temp_c) in weather_c.items()}
print(weather_f)
print("")

student_dict = {
    "student": ["Angela", "James", "lily"],
    "score": [65, 76, 98]
}
# Looping through dictionaries:
# for (key, value) in student_dict.items()
#   print(key)

# Panda with dictionaries
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print("")

# Loop through a data frame and pull the keys
for (key, value) in student_data_frame.items():
    print(key)
print("")

# loop through rows of a data frame to pull the rows
for (index, row) in student_data_frame.iterrows():
    print(row)
print("")

# loop through rows of a data frame to pull both the rows with students
for (index, row) in student_data_frame.iterrows():
    print(row.student)
print("")

# loop through to only pull from filter Angela student of the row students
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.student)
print("")



