import requests
from bs4 import BeautifulSoup
import lxml # instead of html.parser
from decouple import config
from twilio.rest import Client


# https://camelcamelcamel.com/ 

#browser headers obtained from http://myhttpheader.com/
USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"
ACCEPTLANGIAGE = "en-US,en;q=0.9"

AMAZOMURL = "https://www.amazon.com/gp/product/B07YRSFLV7/ref=ox_sc_act_image_1?smid=A19YMF0PU8R9GC&psc=1"
PRICETHRESHOLD = 20

headers = {
    "User-Agent":  USERAGENT,
    "Accept-Language": ACCEPTLANGIAGE,    
}

response = requests.get(url=AMAZOMURL, headers=headers)
#response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")
#print(soup.prettify())
price_whole = soup.find(name = "span", class_="a-price-whole")
price_fraction = soup.find(name = "span", class_="a-price-fraction")
price = float(price_whole.get_text() + price_fraction.getText())

#get variables
account_sid = config("ACCOUNT_SID")
auth_token = config("AUTH_TOKEN")
if price < PRICETHRESHOLD:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"The price is now ${price} on Amazon",
        from_='+12183967334',
        to='+19107977144'
    )
    print(message.status)
