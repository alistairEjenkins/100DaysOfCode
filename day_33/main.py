import datetime as dt
import smtplib
import time

import requests

MY_LAT = 52.456779
MY_LONG = -2.112620
MY_EMAIL = "alistairTestSender@gmail.com"
MY_PASSWORD = "hkuiwnaisxfutvns"
RECIEVER = "alistairedwardjenkins@gmail.com"


def find_utc_hour(time):
    hour = int(time.split("T")[1].split(":")[0])
    return hour


def night_time(rise, set, hour):
    return hour < rise or hour > set


def iss_in_range(lat, lng):
    return abs(lat - MY_LAT) <= 5 and abs(lng - MY_LONG) <= 5


paramters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=paramters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
sunrise_hour = find_utc_hour(sunrise)
sunset_hour = find_utc_hour(sunset)
current_hour = dt.datetime.now().hour

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()
iss_lat = float(iss_data['iss_position']['latitude'])
iss_lng = float(iss_data['iss_position']['longitude'])

while True:
    if night_time(sunrise_hour, sunset_hour, current_hour):
        if iss_in_range(iss_lat, iss_lng):
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=f"{RECIEVER}",
                                    msg=f"Subject:ISS Overhead look up!"
                                        f"\n\nLook up the the sky, you might see the Internationl"
                                        f"Space Station")
    time.sleep(120)
