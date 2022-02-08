import smtplib
from random import choice
import datetime as dt

email_day = 1
current_day_of_week = dt.datetime.now().weekday()

with open('quotes.txt') as file:
    quotes = file.readlines()

my_email = 'TTe2sTT@gmail.com'
password = 'day32test.'
if email_day == current_day_of_week:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='te1st@yahoo.com',
                            msg=f'Subject:Quote\n\n{choice(quotes)}')
