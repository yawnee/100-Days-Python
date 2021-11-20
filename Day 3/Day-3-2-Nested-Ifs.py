# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?" ))
# # == is when value 1 is checking is the same value of value 2
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Please pay $5")
#     elif age >= 12 and age <= 18:
#         print("Please pay $7")
#     elif age > 18:
#         print("Please pay $12")
# else:
#     print("You cannot ride the rollercoaster!")

#########################################################################################

# BMI Calculator task
# BMI = weight / height**2(m**2)
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
height = int(height)
weight = int(weight)

print(height)
print(weight)

bmi = ((weight / (height ** 2)))
print(round(bmi,2))

#I didn't need to do ranges, I could have made each elif less
if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi < 25:
    print("You are normal weight")
elif bmi > 25 and bmi < 30:
    print("you are overweight")
elif bmi > 30 and bmi < 35:
    print("You are obese")
elif bmi > 35:
    print("You are clinically obese")



