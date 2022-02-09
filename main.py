import pandas as pd
import datetime as dt
import smtplib
from data import password, login
from random import choice

birthdays_data = pd.read_csv('birthdays.csv')
birthdays_data = birthdays_data.to_dict(orient='records')
print(birthdays_data)
current_day = dt.datetime.today().day
current_month = dt.datetime.today().month

my_email = login
my_password = password
letters = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']
wishes = []
for letter in letters:
    with open(letter) as file:
        file = file.read()
        wishes.append(file)
print(wishes)

for person in birthdays_data:
    if current_month == person['month'] and current_day == person['day']:
        for row in birthdays_data:
            connection = smtplib.SMTP('smtp.gmail.com')
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=row['email'],
                                msg=f'Subject:Happy Birthday\n\n{choice(wishes).replace("[NAME]", row["name"])}')
