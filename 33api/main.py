
from datetime import datetime
import requests
from datetime import datetime

# 1XX: Hold on something is happening, process still going
# 2xx: Here we go, everything was sucessfull, you should get data you expected
# 3XX: Go Away, you don't have permission to get this thing
# 4XX You screwed up, me as the requester (404 means it does'nt exist)
# 5XX:I screwed up, the server, server may be down
# httpstatuses.com

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response) # returns a response code
# print(response.status_code)

# response.raise_for_status() # if error, this will raise the appropriate status code reason

# data = response.json()["iss_position"]
# print(data)

# longitude = data["longitude"]
# latitude = data["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)
MY_LAT = 39.56619
MY_LONG = -76.33530
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)
