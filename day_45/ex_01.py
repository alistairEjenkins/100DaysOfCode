from bs4 import BeautifulSoup

with open("website.html", 'r', encoding="utf8", ) as file:
    data = file.read()

print(data)

soup = BeautifulSoup(data, 'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)

all_anchors = soup.find_all(name='a')

for tag in all_anchors:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name='h1', id="name")
print(heading)

section_heading = soup.find(name='h3', class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)
