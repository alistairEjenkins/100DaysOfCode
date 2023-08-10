import os

import requests
from dotenv import load_dotenv

MY_LAT = 52.46
MY_LONG = -2.11

load_dotenv()
weather_api_key = os.getenv('WEATHER_API_KEY')
stock_api_key = os.getenv('STOCK_API_KEY')
text_bot_api = os.getenv('BOT_API_KEY')


def rain_forecast(weather_data):
    for hour in weather_data["hourly"][:12]:
        for weather in hour["weather"]:
            return weather['id'] < 700


def telegram_bot_sendtext(bot_message):
    bot_token = text_bot_api
    bot_chatID = '5851971639'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': weather_api_key,
    'exclude': 'minutely,current,daily,',
}

data = requests.get(url='https://api.openweathermap.org/data/3.0/onecall', params=parameters)
weather_data = data.json()

if rain_forecast(weather_data):
    forecast_message = telegram_bot_sendtext("Rain on way!")
else:
    forecast_message = telegram_bot_sendtext("It's a clear day today.")
