import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import pprint

load_dotenv()
spotipy_client_id = os.getenv('SPOTIPY_CLIENT_ID')
spotipy_client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
spotipy_redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

#date = input("Which date do you want to travel to YYYY-MM-DD")
#url = f'https://www.billboard.com/charts/hot-100/{date}/'
#
url = 'https://www.billboard.com/charts/hot-100/2000-08-12'
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, "html.parser")

titles = soup.select(selector="ul li h3#title-of-a-story")
titles = [title.string.strip() for title in titles]
print(titles)
#
# artists = soup.select("span.c-label.a-no-trucate")
# artists= [artist.string.strip() for artist in artists]
# print(artists)

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
tracks = []
for title in titles:
    try:
        result = spotipy.search(q=f'spotify:track:{title}:year:2000')
    except:
        continue
    else:
        pprint(result)

