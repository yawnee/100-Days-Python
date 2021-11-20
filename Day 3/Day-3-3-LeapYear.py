#instructions:
#write a program givin a lap year. a normal year has 36 days, leap years have 366
#on every year that is evenly disivible by 4
#ecept every year that is evenly divisible by 100
#unless the year is also evenly divisible by 400

#Example:
# 2000 / 4 = 500 (leap)
# 2000 / 100 = 20 (not leap)
# 2000 / 400 = 5 (Leap)



#Don't change below
year = int(input("Which year do you want to check? "))
#Don't change above

#write code below

#print(year / 4)
#print(year / 100)
#print(year / 5)
# print(str(((year % 4))) + " Leap")
# print(str(((year % 100))) + " Not leap")
# print(str((year % 400)) + " Leap")

if int((year % 4)) == 0:
    if int((year % 100)) == 0:
        if int((year % 400)) == 0:
            print(f"Your year, {year} is a leap year")

        else:
            print(f"Year {year} is not a leap year!")
    else:
         print(f"Year {year} is a leap year!")
else:
    print(f"Year {year} is not a leap year!")



