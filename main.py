import pandas as pd
import datetime as dt
import smtplib

data = pd.read_csv('birthdays.csv')
data = data.to_dict(orient='records')
print(data)
current_day = dt.datetime.today().day
current_month = dt.datetime.today().month

my_email = 'tte2stt@gmail.com'
my_password = 'day32test'
letters = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']
wishes = []
for letter in letters:
    with open(letter) as file:
        file = file.read()
        wishes.append(file)
print(wishes)
# for row in data:
#     connection = smtplib.SMTP('smtp.gmail.com')
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs=row['email'], smg='Happy Birthday\n\n')


