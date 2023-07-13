import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "GNuUHMPfLt4TPaMmpedzrTsO4KEW6tc9"

header = {
    "apikey": TEQUILA_API_KEY
}


class FlightSearch:

    def get_destination_code(self, city_name):
        body_params = {"term": city_name}
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=header, params=body_params)
        data = response.json()['locations'][0]
        code = data['code']
        return code