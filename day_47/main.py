import requests
from bs4 import BeautifulSoup

preset = 40
textbot_api_key = '6300778193:AAEEhZXlKmVWwFYjnjEPG0P2_f6GVigwTg0'

def telegram_bot_sendtext(bot_message):
    bot_token = textbot_api_key
    bot_chatID = '5851971639'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

url = "https://uk.camelcamelcamel.com/product/B06XCBPFRN?active" \
      "=price_amazon&context=popular"

headers = {
    "User-Agent": "Defined",
    "Accept-Language": "en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
}

response = requests.get(url=url, headers=headers)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
# soup = BeautifulSoup(webpage, "lxml")

price_tag = soup.find(name="span", class_="green")
price = float(price_tag.text.split("£")[1].strip())

desc = soup.find(name="a", style="overflow-wrap: break-word;")
desc = desc.text

if price < preset:
      telegram_bot_sendtext(f"PRICE DROPPED:\n{desc}\n"
                            f"New price: £{price:.2f}")

