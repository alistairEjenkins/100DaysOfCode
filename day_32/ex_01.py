import smtplib

my_email = "alistairTestSender@gmail.com"
password = "hkuiwnaisxfutvns"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="alistairedwardjenkins@gmail.com",
                        msg="Subject:hello\n\nThis is the email body.")
