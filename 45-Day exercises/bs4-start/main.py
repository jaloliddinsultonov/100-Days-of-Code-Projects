from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'lxml')
print(soup.title)  # shows the whole title element
print(soup.title.name)  # shows the 'title' tag
print(soup)  # shows the whole html file
print(soup.a)  # shows the first a(anchor) tag
print(soup.p)  # shows the first p(paragraph) tag
print(soup.prettify()) # shows the indented html code, which looks more understandable