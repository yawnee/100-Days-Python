#Code to add extra cost at the end

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?" ))
# == is when value 1 is checking is the same value of value 2
price = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Child tickets are $5")
        price = 5
    elif age >= 12 and age <= 18:
        print("Youth tickets are $7")
        price = 7
    elif age > 18:
        print("Adult tickets are $12")
        price = 12
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        print("Extra $3")
        price += 3
        print(f"Your final price is {price}")
    else:
        print(f"Your final price is {price}")
else:
    print("You cannot ride the rollercoaster!")