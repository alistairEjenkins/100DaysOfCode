# monday motivational quotes
import datetime as dt
import smtplib
from random import choice

with open("quotes.txt") as quotes_file:
    quote_list = quotes_file.readlines()

print(quote_list)

now = dt.datetime.now()
if now.weekday() == 4:
    quote_choice = choice(quote_list)

    my_email = "alistairTestSender@gmail.com"
    password = "hkuiwnaisxfutvns"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="alistairedwardjenkins@gmail.com",
                            msg=f"Subject:Hey it's Monday!\n\n{quote_choice}.")
