import requests
from datetime import datetime

#


# nutritionix API creds
app_id = 'd8ba580a'
app_key = 'fe2d3da094822eacbbe339c6ef1b7589'

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'


sheety_endpoint = 'https://api.sheety.co/7c8b86da52d9a9db556f081032f0d2dd/myWorkouts/workouts'

# sheety auth for myWorkouts project
bearer_headers = {
    "Authorization": 'Bearer pmcmc[r[o13kr[kd,c[,rrc[crc22f2',
    "Content-Type": "application/json"
}

headers = {
    'x-app-id':app_id,
    'x-app-key':app_key,
    'Content-Type':'application/json',
}

def gather_user_info():

    params = {
        'query': "ran 4 miles and swam for 10 minutes",#input("What excerise have you done? "),
        # "gender": input("Gender? "),
        # 'weight_kg': input("Weight in kg? "),
        # 'height_cm': input("Height in cm? "),
        # 'age': input("Age? "),
    }

    return params

response = requests.post(url=nutritionix_endpoint, json=gather_user_info(), headers=headers)
response.raise_for_status()
result = response.json()

for exercise in result['exercises']:
    sheet_input = {
        'workout': {
            'date': datetime.now().strftime('%d/%m/%Y'),
            'time': datetime.now().strftime("%X"),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
     }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_input, headers=bearer_headers)
    print(sheet_response.text)



