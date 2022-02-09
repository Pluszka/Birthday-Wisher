import pandas as pd
import datetime as dt

data = pd.read_csv('birthdays.csv')
data = data.to_dict(orient='records')
print(data)
current_day = dt.datetime.today().day
current_month = dt.datetime.today().month

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

