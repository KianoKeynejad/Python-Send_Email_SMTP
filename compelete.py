
import datetime as dt
import pandas
import random
import smtplib

my_email = "Email"
password = "Pass"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

people = pandas.read_csv("birthdays.csv")
bd_dict = {(row["month"], row["day"]): row for (index, row) in people.iterrows()}
print(bd_dict)

if today_tuple in bd_dict:
    bd_person = bd_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        contents = letter.read()
        final_version = contents.replace("[NAME]", bd_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=people["email"],
            msg=f"Subject:happy BD\n\n{final_version}"

import random
import smtplib
import datetime as dt
import random

my_email = "Email"
password = "Pass"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 7:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="Email",
            msg=f"Subject:quote of the day\n\n{quote}"


import smtplib
import datetime as dt

my_email = "Email"
password = "Pass"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="Email",
        msg="Subject:Hello\n\nThis is the body of the email"
    )




now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1983, month=10, day=31, hour=3)
print(date_of_birth)



with open("quotes.txt") as q:
    data = q.readlines()
    print(data)
