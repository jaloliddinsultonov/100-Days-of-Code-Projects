# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_data = FlightData()


if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

print(data_manager.destination_data)
for data in data_manager.destination_data:
    flight_data.get_flight_params(data['iataCode'])
    response = flight_data.get_response(data['iataCode'])
    price = response.json()['data'][0]['price']
    departure_city = response.json()['data'][0]['cityFrom']
    departure_airport_iata = response.json()['data'][0]["cityCodeFrom"]
    arrival_city = response.json()['data'][0]['cityTo']
    arrival_airport_iata = response.json()['data'][0]['cityCodeTo']
    outbound_date = response.json()['data'][0]["local_departure"]
    inbound_date = response.json()['data'][0]['local_arrival']
    print(f"{data['city']}: {price} PLN")
    if data['lowestPrice'] >= price:
        notification_manager = NotificationManager(price, departure_city, departure_airport_iata, arrival_city,
                                                   arrival_airport_iata, outbound_date, inbound_date)
        notification_manager.send_message()
