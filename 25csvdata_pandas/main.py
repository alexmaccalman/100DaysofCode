import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(type(data))
#print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

# temp_max = data["temp"].max()
# print(temp_max)

# def convert_to_f(cel):
#     return (cel * 1.8) +32

# monday = data[data.day == "Monday"]
# print(convert_to_f(monday.temp))

#create a dataframe frm scratch

# how many grey, red, and black
# buidl new dataframe

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(list(data.columns))

fur = data["Primary Fur Color"].value_counts()
#fur.rename(['fur color', 'count'])
fur.index.name = 'fur color'
fur.name = 'count'

fur.to_csv("squirrel_count.csv")

