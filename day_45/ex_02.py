import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com")

yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, 'html.parser')

titles = soup.find_all('tr', class_='athing')
spans = [title.find('span', class_="titleline") for title in titles]
refs = [span.a.get("href") for span in spans]
links = [span.a.text for span in spans]


points = []
for score in soup.find_all(name="td", class_="subtext"):
    if score.find(name="span", class_="score"):
        points.append(int(score.getText().split()[0]))
    else:
        points.append(0)

unranked_data = [{'href' : refs[n], 'link' : links[n], 'points': points[n]} for n in range(len(refs))]

def most_votes(article):
    return article['points']

unranked_data.sort(key=most_votes, reverse=True)
for ranked in unranked_data:
    print(ranked)










