from urllib import response
from decouple import config
import requests


SHEETY_TOKEN = config("SHEETY_TOKEN")
SHEETY_ENDPOINT = config("SHEETY_ENDPOINT")
sheety_headers = {
    "Authorization": "Bearer " + SHEETY_TOKEN,
    "Content-Type": "application/json"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __inti__(self):
        self.destination_data = []

    def getdata(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
        data = response.json()["prices"]
        self.destination_data = data
        return self.destination_data

    def update_destination_city(self):
        for city in self.destination_data:
            id = city["id"]
            updatejson = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{id}",
                headers=sheety_headers,
                json=updatejson
            )
            
            