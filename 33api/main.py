import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) # returns a response code

# 1XX: Hold on something is happening, process still going
# 2xx: Here we go, everything was sucessfull, you should get data you expected
# 3XX: Go Away, you don't have permission to get this thing
# 4XX You screwed up, me as the requester (404 means it does'nt exist)
# 5XX:I screwed up, the server, server may be down
# httpstatuses.com
print(response.status_code)

response.raise_for_status() # if error, this will raise the appropriate status code reason

data = response.json()["iss_position"]
print(data)

longitude = data["longitude"]
latitude = data["latitude"]

iss_position = (longitude, latitude)
print(iss_position)