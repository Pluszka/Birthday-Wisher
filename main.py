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

for row in data:
   connection = smtplib.SMTP('smtp.gmail.com')
   connection.starttls()
   connection.login(user=my_email, password=my_password)
   connection.sendmail(from_addr=my_email, to_addrs=row['email'],
                       smg='Happy Birthday\n\n')
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

