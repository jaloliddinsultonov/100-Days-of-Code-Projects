import pandas
import smtplib
import datetime as dt
import random, os

now = dt.datetime.now()
day = now.day
month = now.month

email = "reenoxgooglov@gmail.com"
password = "mzbwcvsdbsyhahms"

# We open the birthday.csv file using pandas library and save it to the variable "data"
data = pandas.read_csv("birthdays.csv")
# We are changing list "data", to a dictionary "data_dictionary" with orient="records"
data_dictionary = data.to_dict(orient="records")
for data in data_dictionary:
    # If today's day and month matches someone's birthday in data_dictionary, we run the code
    if data['month'] == month and data['day'] == day:
        # These two lines of code will give a path to open a text file, which was chosen randomly below
        birthday_wish = random.choice(os.listdir("letter_templates"))
        path = os.path.join("letter_templates", birthday_wish)
        with open(path) as file:
            content = file.read()
            wish = content.replace("[NAME]", data['name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=data['email'],
                msg=wish
            )