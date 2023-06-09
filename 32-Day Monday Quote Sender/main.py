import smtplib
import datetime as dt
import random

# Here write your own email and password
email = "reenoxgooglov@gmail.com"
password = "mzbwcvsdbsyhahms"

now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt") as file:
    content = file.readlines()

quote = random.choice(content)

# First we check whether it's Monday or not (0 == Monday)
if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="aladdinjakubowski@gmail.com",  # Here you put receiver's email
            msg=f"Subject:Monday Quote\n{quote}"
        )
