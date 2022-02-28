from bs4 import BeautifulSoup
import requests


date_answer = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
#date_answer = '2000-08-12' # debugging

URL = f'https://www.billboard.com/charts/hot-100/{date_answer}/'
response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

song_title = soup.find_all(name="h3", id='title-of-a-story', class_="a-no-trucate")
song_list = [each_song.getText().replace("\n", "") for each_song in song_title]

with open(f"songs_of_{date_answer}.txt", mode="w") as file:
    number = 0
    for each_song in song_list:
        number = number + 1
        print(f'{number}) {each_song}')
        file.write(f'{number}) {each_song}')





