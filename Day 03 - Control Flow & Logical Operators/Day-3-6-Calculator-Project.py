# Don't change the code below
print("Welcome to the love calculator!")
name1 = input("what is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

# < 10 or greater than 90 say "coke and mentos"
# between 40 - 50 "alright
# otherwise "score"
#Count how many times LOVE occurs in the name

#Write your code below this line
#Hint use lower fountion and count
# "Yawnee".lower() = yawnee
# "Yawnee".count("a") = 1

#Output example
# your score is 42, you are alright together

name1.lower() #you can match both names together by doing combined_string = name1 + name2 then lower casing it
name2.lower()
#True 1
t1 = name1.count("t")
r1 = name1.count("r")
u1 = name1.count("u")
ee1 = name1.count("e")
#True 2
t2 = name2.count("t")
r2 = name2.count("r")
u2 = name2.count("u")
ee2 = name2.count("e")

T_final = int(t1+t2)
R_final = int(r1+r2)
U_final = int(u1+u2)
EE_final = int(ee1+ee2)
Total1 = (T_final + R_final + U_final + EE_final)

print(f'T occurs {T_final} times')
print(f'R occurs {R_final} times')
print(f'U occurs {U_final} times')
print(f'E occurs {EE_final} times')
print(f"Total = {Total1}")
print("")

#love 1
l1 = name1.count("l")
o1 = name1.count("o")
v1 = name1.count("v")
e1 = name1.count("e")
#Love 2
l2 = name2.count("l")
o2 = name2.count("o")
v2 = name2.count("v")
e2 = name2.count("e")

L_final = int(l1+l2)
R_final = int(o1+o2)
U_final = int(v1+v2)
E_final = int(e1+e2)
Total2 = (L_final + R_final + U_final + E_final)

print(f'T occurs {l1 + l2} times')
print(f'R occurs {o1 + o2} times')
print(f'U occurs {v1 + v2} times')
print(f'E occurs {e1 + e2} times')
print(f"Total = {Total2}")
print("")
final_total = str(Total1) + str(Total2)
print(f"Your love score = {final_total}")
int_final_total = int(final_total)
print("")
if int_final_total <= 10 or int_final_total >= 90:
    print(f"Your score is {int_final_total}, you go together like coke and mentos.")
elif 50 >= int_final_total >= 40:
    print(f"Your score is {int_final_total}, you're alright together")
else:
    print(f"Your score is {int_final_total}, you are whatever")

### the cleaner code from the course, good to know!!

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")



