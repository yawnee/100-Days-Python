#calculates highest score from the list
#no max or min, use only for loops to figure this out

students_score = input("Input a list of student heights ").split()
print(students_score)

highscore = 0

for score in students_score:
    score = int(score)
    if score > highscore:
        highscore = score
print(highscore)

