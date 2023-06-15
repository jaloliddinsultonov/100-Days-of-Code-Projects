import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 52.229675  # Warsaw's latitude
MY_LONG = 21.012230  # Warsaw's longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    # Here we are trying to take an hour of a sunrise
    sunrise = int(sunrise.split("T")[1].split(":")[0])
    sunset = data['results']['sunset']
    # Here we are trying to take an hour of a sunset
    sunset = int(sunset.split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour

    if current_hour >= sunset or current_hour <= sunrise:
        return True


# Here we are checking whether iss is over our location, and it's dark or not
while True:
    # Here every 60 seconds code, which is below is running
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="reenoxgooglov@gmail.com", password="mzbwcvsdbsyhahms")
            connection.sendmail(
                from_addr="reenoxgooglov@gmail.com",
                to_addrs="sultonovjaloliddin07@gmail.com",
                msg=f"Subject:Look UP👆\nHey bro it's ISS over you. LOOK UP."
            )


