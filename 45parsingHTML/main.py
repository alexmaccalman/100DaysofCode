from turtle import ScrolledCanvas
from urllib import request
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="titlelink") # must add a _ to not clash with class key word
article_text = []
article_links = []

for article in articles:
    article_text.append(article.getText())
    article_links.append(article.get("href"))


scores = soup.find_all(class_="score")

#article_scores = [score.getText().split(" ")[0] score in scores]
article_scores = []
for score in scores:
    article_scores.append(int(score.getText().split(" ")[0]))

print(article_scores)
   
max_value = max(article_scores)
max_index = article_scores.index(max_value)
max_text = article_text[max_index]
max_link = article_links[max_index]

print(f"{max_text} from the link {max_link} has a count of {max_value}")