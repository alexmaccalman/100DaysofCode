from urllib import response
import requests
from datetime import datetime
from decouple import config

pixela_endpoint = "https://pixe.la/v1/users"
GRAPH = "graph1"
TOKEN = config("TOKEN")
USERNAME = config("USERNAME")
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = str(datetime.now()).split(" ")[0].replace("-", "")
# another way to get time see https://www.w3schools.com/python/python_datetime.asp
today = datetime.now().strftime("%Y%m%d")


post_pixel = {
    "date": today,
    "quantity": input("Enter number of kms"),
}

response = requests.post(url=f"{graph_endpoint}/{GRAPH}", json=post_pixel, headers=headers)
print(response.text)

# response = requests.put(url=f"{graph_endpoint}/{GRAPH}/{today}", json=post_pixel, headers=headers)
# print(response.text)

# response = requests.delete(url=f"{graph_endpoint}/{GRAPH}/{today}", headers=headers)
# print(response.text)