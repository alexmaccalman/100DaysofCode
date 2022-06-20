from re import X


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

dic = {word:len(word) for word in sentence.split()}
print(dic)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# new_dict ={new_key:new_value for (key, value) in dict.items() if test}

weather_f = {day:((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}
print(weather_f)
