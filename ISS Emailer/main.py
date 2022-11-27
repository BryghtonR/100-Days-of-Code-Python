import requests
from datetime import datetime
import smtplib

 #---find internation space station current position---
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lng = data["iss_position"]["longitude"]
iss_lat = data["iss_position"]["latitude"]
print(iss_lng, iss_lat)

#---get my sunrise and set hour---
my_lat = 40.913410
my_lng = -77.764748
parameters = {
    "lat":my_lat,
    "lng":my_lng,
    "formatted": 1
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split(":")[0])
sunset = int(data["results"]["sunset"].split(":")[0])

#---find current time---
time_now = datetime.now().time()
time_now = time_now.hour

#---is it a good itme to look for iss?---
if my_lat > iss_lat -5 and my_lat < iss_lat +5:
    if my_lng > iss_lng -5 and my_lng < iss_lng +5:
        if time_now > sunset and time_now < sunrise:
            
            #---Email sender---
            email = "PyProgramTester@gmail.com"
            password = ""#needs primary or temp password here!
            
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(from_addr=email, to_addrs="bryghtonr@gmail.com", 
                    msg=f"Subject: ISS Reminder (Look Up!)\n\nLook up and see the Interational Space Station!")
                print("ISS Reminder Email Attempted")

            print("Look Up!")




