# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com

import smtplib
import datetime as dt

with open('./data/email.txt', mode='r') as username, open('./data/password.txt', mode='r') as password, open('./data/sender.txt', mode='r') as sender:
    username = username.read()
    password = password.read()
    sender = sender.read()

# Example 1: No with
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=username, password=password)
# connection.sendmail(from_addr=username, to_addrs=sender, msg='Hello')
# connection.close()

# Example 2: With
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=username, password=password)
#     connection.sendmail(from_addr=username, to_addrs=sender, msg='Hello')
#     connection.close()

# Learning Date Time
now = dt.datetime.now()
year = now.year  # once you do "now" you can tab into more attributes
month = now.month
day_of_week = now.weekday()
print(now)
print(year)
print(month)
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)


