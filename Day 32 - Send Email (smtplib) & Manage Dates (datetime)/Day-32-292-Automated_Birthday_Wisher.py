import smtplib
import datetime as dt
import random
import pandas as pd

# ---------------------------- Dates  ------------------------------- #

now = dt.datetime.now()
day = now.day
month = now.month
print(f'Today is Month: {month}, and day {day}')  # debugging
print("")

# ---------------------------- Files ------------------------------- #

# Create three files and insert your credentials
with open('./data/email.txt', mode='r') as username, open('./data/password.txt', mode='r') as password:
    username = username.read()
    password = password.read()

with open('./data/letter_1.txt', mode='r') as letter_1, open('./data/letter_2.txt', mode='r') as letter_2, open(
        './data/letter_3.txt', mode='r') as letter_3:
    letter_1 = letter_1.read()
    letter_2 = letter_2.read()
    letter_3 = letter_3.read()
    letter_list = [letter_1, letter_2, letter_3]

# Convert CSV into dictionary
data = pd.read_csv("./data/birthdays.csv")
birthday_dict = data.to_dict(orient='records')

# ---------------------------- Birthday Validation Check ------------------------------- #

y = 0
for each_person in birthday_dict:
    print(f"Name: {birthday_dict[y]['name']}, Month: {birthday_dict[y]['month']}, Day: {birthday_dict[y]['day']}")  # debugging
    if birthday_dict[y]['month'] == month and birthday_dict[y]['day'] == day:
        birthday_person = birthday_dict[y]['name']
        birthday_person_email = birthday_dict[y]['email']
        birthday_message = random.choice(letter_list).replace("[NAME]", birthday_person)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=username, password=password)
            connection.sendmail(from_addr=username, to_addrs=birthday_person_email, msg=f'Subject: Happy Birthday!\n\n{birthday_message}')
            connection.close()
            print("Email has been sent!")
    else:
        print('No birthdays today')
    print("")
    y = y+1

