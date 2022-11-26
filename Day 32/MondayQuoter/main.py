# import smtplib

# email = "PyProgramTester@gmail.com"
# password = #needs primary or temp password here!

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(from_addr=email, to_addrs="bryghtonr@gmail.com", 
#         msg="Subject: Hello World\n\nThis is the body of the email")



#spectial steps for enabling emailing via gmail:
    # use port number:   smtplib.SMTP("smtp.gmail.com", port=587)
    # enable 2 step verifications under user setting/security
        # generate a specific password for your app setting/security/app password


import random
import datetime
import smtplib

with open("quotes.txt", "r") as quotes:
    lines = quotes.readlines()
    my_quote = random.choice(lines)
now = datetime.datetime.now()
day_of_week = now.weekday()
print(day_of_week)
if day_of_week == 5:
    email = "PyProgramTester@gmail.com"
    password = "iorrjuenrbcqwlui"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="bryghtonr@gmail.com", 
            msg=f"Subject: Monday Quote of the Day\n\n{my_quote}")
        print("Monday Quote Attempted")
