import os

class NotificationManager:

    def __init__(self, price, departure_city, departure_airport_iata, arrival_city, arrival_airport_iata, outbound_date,
                 inbound_date):
        self.price = price
        self.departure_city = departure_city
        self.departure_airport_iata = departure_airport_iata,
        self.arrival_city = arrival_city,
        self.arrival_airport_iata = arrival_airport_iata,
        self.outbound_date = outbound_date,
        self.inbound_date = inbound_date

    def send_message(self):
        from twilio.rest import Client

        account_sid = 'AC5180ed732e7cb90ee25b4adda424a3a7'
        auth_token = '5a68365ff055bded510b8dafb54ae438'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+14847490842',
            body=f"Low price alert! Only {self.price} to fly from {self.departure_city}-{self.departure_airport_iata} "
                 f"to {self.arrival_city}-{self.arrival_airport_iata}, from {self.outbound_date} to {self.inbound_date}.",
            to='+48733677206'
        )

        print(message.sid)
