# automated birthday wish sender

import datetime as dt
import smtplib
from random import randint

import pandas

my_email = "alistairTestSender@gmail.com"
password = "hkuiwnaisxfutvns"

nephews_data = pandas.read_csv("birthdays.csv").to_dict(orient='record')

now = dt.datetime.now()

for nephew in nephews_data:
    if nephew['month'] == now.month and nephew['day'] == now.day:
        print(f"{nephew['name']} has a birthday today")
        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as letter_file:
            letter_template = letter_file.read()
            letter_template = letter_template.replace("[NAME]", nephew['name'])
            letter_template = letter_template.replace("Angela", "Uncle A.")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=f"{nephew['email']}",
                                msg=f"Subject:Happy Birthday {nephew['name']}!"
                                    f"\n\n{letter_template}")
