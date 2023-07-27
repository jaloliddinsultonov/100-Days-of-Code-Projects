from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'lxml')

# 2nd part

all_anchor_tags = soup.find_all(name="a")  # finds all anchor tags and puts them in a list
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())  # prints all texts between anchor tag
    print(tag.get("href"))  # prints all links in href

heading = soup.find(name="h1", id="name")  # finds the first heading which has and id="name"
print(heading)
section_heading = soup.find(name="h3", class_='heading') # finds the h3 with class='heading'
print(section_heading)  # Look how we wrote class_ , not class

name = soup.select_one(selector="#name")  # selecting the first item with an id='name'
print(name)

headings = soup.select(".heading")  # selecting all headings with class="heading"
print(headings)