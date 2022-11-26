import pandas 
import datetime
import os, random
import smtplib

#--- emailer info ---
name = "pyTester"
email = "PyProgramTester@gmail.com"
password = #needs primary or temp password here!

#---day and month---
now = datetime.datetime.now()
todays_month = now.month
todays_day = now.day

#--- import list of friends ---
data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict()

#---search for matching birthdays ---
for each in birthdays["month"]:
    if birthdays["month"][each] == todays_month and birthdays["day"][each] == todays_day:

        #---import random letter template ---
        with open("letter_templates/" + random.choice(os.listdir("letter_templates")), "r") as letter_1:
            letter = letter_1.read()

        # --- find replace your name and friends name ---
        letter = letter.replace("[NAME]", birthdays["name"][each])
        letter = letter.replace("Angela", name)

        #---send birthday email---
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs="bryghtonr@gmail.com", 
                msg=f"Subject: Happy Birthday!\n\n{letter}")
            print("Birthday Letter Attempted")
    
    else:
        print("No birthdays today")