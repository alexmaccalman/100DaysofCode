import requests

class GuessName:
    def __init__(self, name):
        self.params = {
            "name": name
        }

    def get_gender(self):
        GENDER_ENDPOINT = "https://api.genderize.io"
        response = requests.get(GENDER_ENDPOINT, params=self.params)
        gender_data = response.json()
        return gender_data['gender']

    def get_age(self):
        AGE_ENDPOINT = 'https://api.agify.io'
        response = requests.get(AGE_ENDPOINT, params=self.params)
        age_data = response.json()
        return age_data['age']

# guess = GuessName("alex")
# print(guess.get_gender())
# print(guess.get_age())

