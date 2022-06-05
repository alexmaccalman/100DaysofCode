# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#          temperature.append(int(row[1]))

# print(temperature)

import pandas as pd



data = pd.read_csv("weather_data.csv")
print(data)