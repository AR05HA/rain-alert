import os
import smtplib
import requests
from email.message import EmailMessage

API_KEY = os.environ.get("OWM_API_KEY")
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
to_email = os.environ.get("TO_EMAIL")

my_lat = os.environ.get("MY_LAT")
my_lng = os.environ.get("MY_LNG")

parameters = {
    "lat": my_lat,
    "lon": my_lng,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast", params=parameters
)
response.raise_for_status()

data = response.json()
will_rain = False

for hour_data in data["list"]:
    for condition in hour_data["weather"]:
        if condition["id"] < 700:
            will_rain = True

if will_rain:
    msg = EmailMessage()
    msg["Subject"] = "🌧️ Rain Alert: Grab an Umbrella!"
    msg["From"] = my_email
    msg["To"] = to_email
    msg.set_content("Rain is expected in your area. Don't forget your umbrella before heading out!")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.send_message(msg)
