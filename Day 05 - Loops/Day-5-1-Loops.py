#For loop
# example: for item in list_of_items:
#                               do something
#
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

print(type((student_heights)))
total_height = 0
total_students = 0

for height in student_heights:
  total_height += height

for students in student_heights:
  total_students += 1

print(round(total_height / total_students, 2))

