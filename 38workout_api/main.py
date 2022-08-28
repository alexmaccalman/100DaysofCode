from re import X
from socket import TCP_NODELAY
from time import strftime
from decouple import config
import requests
from datetime import date, datetime

APP_ID = config("APP_ID")
APP_KEY = config("APP_KEY")
TOKEN = config("TOKEN")
GENDER = "male"
WEIGHT_KG = "190.5"
HEIGHT_CM = "86"
AGE = "51"
WORKOUT_ENDPOINT = config("WORKOUT_ENDPOINT")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0",
}

body = input("Enter what you did: ")

user_params = {
    "query": body,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)
data = response.json()

# find date and time
today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

workout_headers = {
    "Authorization": "Bearer " + TOKEN,
    "Content-Type": "application/json"
}
for exercise in data["exercises"]:
    workout_params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(url=WORKOUT_ENDPOINT, json=workout_params, headers=workout_headers)
    print(response.text)