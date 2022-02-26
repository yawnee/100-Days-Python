from bs4 import BeautifulSoup
import lxml
import requests

# SITE NOT AVAILABLE ANYMORE URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

with open("Empire.html", encoding="utf8") as file:
    empire_html = file.read()
# print(empire_html)
soup = BeautifulSoup(empire_html, "html.parser")

# print(soup.prettify())

all_movies = soup.find_all(name="h3", class_='title')
print(all_movies)

movies_titles = [movie.getText() for movie in all_movies]
print(movies_titles[::-1])
movies = movies_titles[::-1]

with open ('movies.txt', mode='w') as file:
    for movie in movies:
        file.write(f'{movie}\n')

for each_title in range(len(movies_titles) - 1, -1, -1):
    print(movies_titles[each_title])


