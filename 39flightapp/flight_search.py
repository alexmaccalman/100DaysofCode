from decouple import config
import requests
from flight_data import FlightData



TEQUILA_API_KEY = config("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"

tequila_header = {
    "apikey": TEQUILA_API_KEY,
    "Content-Type": "application/json",
}
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city):
        tequila_params = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(url=TEQUILA_ENDPOINT, params=tequila_params, headers=tequila_header)
        data = response.json()["locations"]
        code = data[0]["code"]
        return code

    def check_flight(self, city, destination, from_time, to_time, nights_in_dst_from, nights_in_dst_to):
        
        search_params = {
            "fly_from": city,
            "fly_to": destination,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": nights_in_dst_from,
            "nights_in_dst_to": nights_in_dst_to,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD",
        }

        # tequila_header = {
        #     "apikey": TEQUILA_API_KEY,
        #     "Content-Type": "application/json",
        # }

        response = requests.get(url=SEARCH_ENDPOINT, params=search_params, headers=tequila_header)

        #print(response.text)

        try:
            flights = response.json()["data"][0]
        except IndexError:
            print(f"No flights found from {city} to {destination}")
            return None

        flight_data = FlightData(
            price = flights["price"],
            origin_city = flights["cityFrom"],
            origin_airport = flights["flyFrom"],
            destination_city = flights["cityTo"],
            destination_airport = flights["flyTo"],
            out_date = flights["route"][0]["local_departure"].split("T")[0],
            out_time = flights["route"][0]["local_departure"].split("T")[1],
            out_airline = flights["route"][0]["airline"],
            out_flight = flights["route"][0]["flight_no"],
            return_date = flights["route"][1]["local_departure"].split("T")[0],
            return_time = flights["route"][1]["local_departure"].split("T")[1],
            return_airline = flights["route"][1]["airline"],
            return_flight = flights["route"][1]["flight_no"]
        )
        return flight_data





