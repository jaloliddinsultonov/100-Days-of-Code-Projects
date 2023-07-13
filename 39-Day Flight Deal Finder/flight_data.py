import requests
from datetime import datetime, timedelta
from data_manager import DataManager


class FlightData:
    # This class is responsible for structuring the flight data.

    def __init__(self):
        self.flight_params = {}
        self.data_manager = DataManager()
        self.departure_airport_code = "WAW"
        self.departure_city = "Warsaw"
        self.now = datetime.now()
        self.date_to = self.now + timedelta(days=30)*6  # (6 months from today)

    def get_flight_params(self, fly_to):
        self.flight_params = {
            "fly_from": self.departure_airport_code,
            "fly_to": fly_to,
            "date_from": self.now.strftime("%d/%m/%Y"),
            "date_to": self.date_to.strftime("%d/%m/%Y"),
            "curr": "PLN",
        }
        return self.flight_params

    def get_response(self, city):
        header = {
            "apikey": "GNuUHMPfLt4TPaMmpedzrTsO4KEW6tc9"
        }
        response = requests.get(url=f"https://api.tequila.kiwi.com/v2/search", headers=header, params=self.get_flight_params(fly_to=city))
        return response