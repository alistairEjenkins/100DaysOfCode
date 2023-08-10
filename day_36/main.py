import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

load_dotenv()
stock_api_key = os.getenv('STOCK_API_KEY')
news_api_key = os.getenv('NEWS_API_KEY')
textbot_api_key = os.getenv('TEXTBOT_API_KEY')

SYMBOL = 'TSLA'


def date_calc(week_day):
    if week_day == 6:
        last_day = now - timedelta(days=2)
    elif week_day == 0:
        last_day = now - timedelta(days=3)
    else:
        last_day = now - timedelta(days=1)

    if week_day == 1:
        first_day = last_day - timedelta(days=3)
    else:
        first_day = last_day - timedelta(days=1)

    return str(first_day), str(last_day)


def stock_price_change(data):
    first_day_close = float(data["Time Series (Daily)"][first_day]["4. close"])
    last_day_close = float(data["Time Series (Daily)"][last_day]["4. close"])
    change = last_day_close - first_day_close
    percentage_change = change / last_day_close

    if percentage_change < 0:
        return f"🔻{percentage_change:.2f}%", percentage_change
    else:
        return f"🔺{percentage_change:.2f}%", percentage_change


def format_message(data):
    message = ''
    if len(data['articles']) < 3:
        num = len(data['articles'])
    else:
        num = 4
    for n in range(num):
        message += f"{SYMBOL} {change_string}\n" \
                   f"Headline: {data['articles'][n]['title']}\n" \
                   f"URL: {data['articles'][n]['url']}\n"

    return message

def telegram_bot_sendtext(bot_message):
    bot_token = textbot_api_key
    bot_chatID = '5851971639'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    # return response.json()


now = datetime.now().date()
week_day = now.weekday()
first_day, last_day = date_calc(week_day)

# for day in range(7):
#     now = datetime.now().date() - timedelta(days=day)
#     print(now)
#     print(date_calc(now.weekday()))

stock_endpoint = 'https://www.alphavantage.co/query'

params = {
    'function': "TIME_SERIES_DAILY_ADJUSTED",
    'symbol': SYMBOL,
    'interval': '60min',
    'apikey': stock_api_key,
}

response = requests.get(url=stock_endpoint, params=params)
response.raise_for_status()
data = response.json()
change_string, change = stock_price_change(data)

news_endpoint = "https://newsapi.org/v2/everything"

params = {
    'qInTitle': 'Tesla Inc',
    'apiKey': news_api_key,
}

response = requests.get(url=news_endpoint, params=params)
response.raise_for_status()
data = response.json()
print(data)
message = format_message(data)

if abs(change) > 0.01:
    telegram_bot_sendtext(message)
