import requests
from datetime import datetime

USERNAME = "jaloliddin"
TOKEN = "sultonovjaloliddin"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

# Create the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
print(response.text)

# Update the graph's pixel data
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230706"

pixel_data_new = {
    "quantity": "99"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_data_new, headers=header)
# print(response.text)

# Delete the graph's pixel data
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=pixel_delete_endpoint, headers=header)
# print(response.text)