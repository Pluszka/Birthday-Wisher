import smtplib

my_email = 'tte2stt@gmail.com'
password = 'day32test'

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
