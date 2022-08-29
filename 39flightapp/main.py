#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from types import NoneType
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import date, datetime, timedelta
data_manager = DataManager()
flight_search = FlightSearch()

# Flight Deal Google Sheet: https://docs.google.com/spreadsheets/d/1UN0acIEONu09HVY0p6H8U5J2U9de7T_UWfiEqefelLg/edit#gid=0

FROM_LOCATION = "BWI"
NIGHTS_IN_DESTINATION_FROM = 4
NIGHTS_IN_DESTINATION_TO = 7
HOW_FAR_OUT_TO_SEARCH = 60

# populate the iataCodes if they are not already
sheet_data = data_manager.getdata()
for item in sheet_data:
    if item["iataCode"] == "":
        city = item["city"]
        iataCode = flight_search.get_destination_code(city)
        item["iataCode"] = iataCode

data_manager.destination_data = sheet_data
data_manager.update_destination_city()

tomorrow = datetime.now() + timedelta(days=1) 
end_date = tomorrow + timedelta(days=HOW_FAR_OUT_TO_SEARCH)
tomorrow = tomorrow.strftime("%d/%m/%Y")
end_date = end_date.strftime("%d/%m/%Y")

for item in sheet_data:
    flight_data = flight_search.check_flight(
        FROM_LOCATION, 
        destination = item['iataCode'], 
        from_time = tomorrow,
        to_time = end_date,
        nights_in_dst_from = NIGHTS_IN_DESTINATION_FROM,
        nights_in_dst_to = NIGHTS_IN_DESTINATION_TO
    )
    try:
        flight_data.print_flight()
    except AttributeError:
        print("Could not find a flight")
        

