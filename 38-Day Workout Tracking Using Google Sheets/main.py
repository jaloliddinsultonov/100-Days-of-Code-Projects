import requests
from datetime import datetime
import os

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    # All information("x-app-id", "x-app-key", etc.) moved into Environmental Variables
    "x-app-id": os.environ['X-APP-ID'],
    "x-app-key": os.environ["X-APP-KEY"],
    "x-remote-user-id": os.environ["X-REMOTE-USER-ID"]
}

user_params = {
    "query": input("Tell me which exercise you did? "),
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 183.64,
    "age": 21
}

response = requests.post(url=nutritionix_endpoint, json=user_params, headers=headers)
data = response.json()['exercises']

today = datetime.now()

for item in data:
    # This data is also moved into Environmental Variable
    sheety_endpoint = os.environ['SHEETY_ENDPOINT']
    body = {
        'workout': {
            "date": today.strftime("%Y/%m/%d"),
            "time": today.strftime("%X"),
            "exercise": item['name'].title(),
            "duration": item['duration_min'],
            "calories": item['nf_calories']
        }
    }

    headers_sheety = {
        # This token below moved into Environmental Variable
        "Authorization": os.environ['AUTHORIZATION']
    }

    response = requests.post(url=sheety_endpoint, json=body, headers=headers_sheety)
    # print(response.text)
