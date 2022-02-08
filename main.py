import smtplib

my_email = 'TTe2sTT@gmail.com'
password = 'day32test.'

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs='te1st@yahoo.com',
                    msg='Subject:Hello\n\n'
                        'Hello world 3lvl')
connection.close()
