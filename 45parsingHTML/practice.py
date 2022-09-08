from bs4 import BeautifulSoup
import lxml # instead of html.parser

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
print(soup.a) # get this first "a" tag

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading") # class is a python key word so add a _
print(section_heading.getText())


company_url = soup.select_one(selector="p a") # sets multiple html selector tags to narrow in
print(company_url)

name = soup.select_one(selector="#name") # selects the id="name" css selector
print(name)

headings = soup.select(selector=".heading") # use . to get class="heading" css selector. returns a list of them
print(headings)