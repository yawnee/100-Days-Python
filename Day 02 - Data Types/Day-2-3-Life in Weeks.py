#Create a program using f string for how many days,
#weeks and months you have left if we live 90 years old
# 1 year = 365 days, 52 weeks, 12 months

age = input("What is your current age? ")
age = 90 - int(age)
age_days = age * 365
age_weeks = age * 52
age_months = age * 12

print(f"You have {age_days} days, {age_weeks} weeks, and {age_months} months")


