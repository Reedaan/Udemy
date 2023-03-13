import requests
from datetime import datetime

MY_LAT = 49.968529
MY_LONG = 19.975340
# response = requests.get(url="http://api.open-notify.org/iss-now.json")

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()
sunrise = sunrise.split("T")

print(sunrise)
print(time_now)


