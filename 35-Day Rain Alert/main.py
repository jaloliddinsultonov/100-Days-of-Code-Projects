import requests


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
# I changed api_key, but it should be the working one to run the code
api_key = "58c55e4df594fcfb27971ad0977706d5sjy15"

weather_params = {
    "lat": 44.686580,
    "lon": 10.663220,
    "exclude": "hourly",
    "appid": api_key

}

response = requests.get(OWM_Endpoint, params=weather_params)
data = response.json()['weather'][0]
print(data)
if data['id'] < 700:
    print("Bring an umbrella")