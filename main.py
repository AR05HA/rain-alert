import os
import smtplib
import requests

API_KEY = os.environ.get("OWM_API_KEY")
my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

MY_LAT = 7.317704
MY_LNG = 80.276411

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
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
  with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="aroshachamik@gmail.com",
        msg="Subject:It's Raining!!\n\n Bring an Umbrella",
    )
