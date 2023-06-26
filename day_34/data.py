import requests

parameters = {
    'amount': 10,
    'type': 'boolean',
}
endpoint = "https://opentdb.com/api.php?"

response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']
print(question_data)
