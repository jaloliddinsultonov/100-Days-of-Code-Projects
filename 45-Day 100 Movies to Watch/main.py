import requests
from bs4 import BeautifulSoup
import lxml
import pandas
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "lxml")
all_movies_tag = soup.find_all("h3", class_="title")
list_of_movies = [movie.getText() for movie in all_movies_tag]
list_of_movies = list_of_movies[::-1]  # reverses the items in the list

df = pandas.DataFrame(list_of_movies)
df.to_csv("movies.txt", index=False)

# 2 way

with open("movie.txt", mode="w", encoding="utf-8") as file:
    for movie in list_of_movies:
        file.write(f"{movie}\n")






