import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, "html.parser")


titles = soup.find_all(name='h3', class_="title")
titles = [title.text for title in soup.find_all(name='h3', class_="title")]
titles.reverse()

with open("100-Greatest-movies", 'a', encoding="utf-8") as file:
    for title in titles:
        file.write(title + '\n')



