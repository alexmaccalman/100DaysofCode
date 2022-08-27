from datetime import datetime
from datetime import timedelta
from email import message
from http import client
from turtle import title
from urllib import response
import requests
from twilio.rest import Client
from decouple import config

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = config("STOCK_API_KEY")
NEWS_API_KEY = config("NEWS_API_KEY")

TWILLO_SID = config("TWILLO_SID")
TWILLO_AUTH_TOKEN = config("TWILLO_AUTH_TOKEN")


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

today = datetime.now()
yesterday = str(today - timedelta(days = 1)).split(" ")[0]
day_before = str(today - timedelta(days = 2)).split(" ")[0]

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,

}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterday_close = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])

# another way to do this instead of using datetime is with a list comprehension
data = stock_response.json()["Time Series (Daily)"] # this is a dict
# [new_value for (key, value) in dictionary.items()]
data_list = [value for (key, value) in data.items()] # items() turns dict into a list
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

#2. - Get the day before yesterday's closing stock price
day_before_close = float(stock_data["Time Series (Daily)"][day_before]["4. close"])
# or
day_before_closing_price = data_list[1]["4. close"]

#3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_diff = (yesterday_close - day_before_close)
up_down = None
if positive_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
#4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = round(positive_diff / yesterday_close * 100)

#5. - If TODO4 percentage is greater than 5 then print("Get News").
   ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
   
if abs(percent_diff) > 2:
    news_parameters = {
        "q": "tesla",
        "from": str(datetime.today()),
        "sortBy": "popularity",
        "language": "en",
        "apikey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
   

#7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    article_list = news_data["articles"][:3]
    
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#8. - Create a new list of the first 3 article's headline and description using list comprehension.
    # [new_item for item in list]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percent_diff}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in article_list]
   
    
    # for article in article_list:
    #     title = article["title"]
    #     print(title)
#9. - Send each article as a separate message via Twilio. 
    client = Client(TWILLO_SID, TWILLO_AUTH_TOKEN)
    for article in formatted_articles:
        message= client.messages.create(
            body=article,
            from_='+12183967334',
            to='+19107977144',
        )
    print(message.status)

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

