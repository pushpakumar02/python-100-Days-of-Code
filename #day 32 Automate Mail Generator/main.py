import smtplib
import datetime as dt
import random

# email address of the sender
MY_EMAIL = "pushpakumarpushpakumar70@gmail.com"
PASSWORD = "thpx ynll qwen mmjx"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="pushpakumar2222000@gmail.com",
            msg=f"Subject:Motivation Quote of the day\n\n{quote}"
        )


#----------------------------------------------------------------------------------------------------------------------
# using pandas

# import smtplib
# import datetime as dt
# import random
# import pandas
#
# # email address of the sender
# my_email = "pushpakumarpushpakumar70@gmail.com"
# password = "thpx ynll qwen mmjx"
#
# def sent_mail(quotes_mail):
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="pushpakumar2222000@gmail.com",
#             msg=f"Subject:Hello\n\n{quotes_mail}"
#         )
#
# quotes = pandas.read_csv("quotes.txt")
# quotes_list = pandas.read_csv("quotes.txt", header=None).values.flatten().tolist()
# quotes_mail = random.choice(quotes_list)
#
# now = dt.datetime.now()
# day = now.day
#
# if now.strftime("%A") == "Saturday":
#     sent_mail(quotes_mail)

#----------------------------------------------------------------------------------------------------------------------
# year = now.year
# month = now.month
# date_of_birth = dt.datetime(year=2000, month=2, day=22)
# print(date_of_birth)
# now.day.
