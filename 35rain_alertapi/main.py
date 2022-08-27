from urllib import request, response
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

# https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1&newCustomer=true
# https://www.pythonanywhere.com/user/amaccalman/tasks_tab/
# https://apilist.fun/


OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
api_keyold = "5fcb4ec58e5335c846537e6365a711e1"
api_key = "a1d5030a6d4d4631003e27a0fbf462b4"
MY_LAT = 39.56633021926093 # Your latitude
MY_LONG = -76.33500179850502 # Your longitude

account_sid = 'AC04033c01600bf128ac2d856110e3b496'
auth_token = 'ffd966332a8451d983272a397ea67970'


TEST_LAT = 42.112894
TEST_LONG = -70.796805

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
        print(will_rain)

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️.",
        from_='+12183967334',
        to='+19107977144'
    )
    print(message.status)


#print(weather_data["hourly"][:12]["weather"][0]["id"])
