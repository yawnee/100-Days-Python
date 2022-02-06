import smtplib
import datetime as dt
import random
import pandas as pd

# ---------------------------- Dates  ------------------------------- #

now = dt.datetime.now()
day_of_week = now.weekday()

# ---------------------------- Files ------------------------------- #

with open('./data/email.txt', mode='r') as username, open('./data/password.txt', mode='r') as password, open('./data/sender.txt', mode='r') as sender:
    username = username.read()
    password = password.read()
    sender = sender.read()

data = pd.read_csv("./quotes.txt")
quote_list = data['quote'].to_list()
random_quote = random.choice(quote_list)

# ---------------------------- Email ------------------------------- #

# Debugging
print(quote_list)
print(random_quote)
print(day_of_week)

if day_of_week == 6:
    # Instructor way of doing it
    # with open('./quote_list') as quote_file:
    #     all_quotes = quote_file.readlines()
    #     quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username, to_addrs=sender, msg=f'Subject: Monday Motivation\n\n{random_quote}')
        print("Email has been sent!")
        connection.close()








