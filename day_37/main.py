import requests
from datetime import datetime
#https://pixe.la/v1/users/alancoding/graphs/graph1

USERNAME = 'alancoding'
TOKEN = 'bwrwtgbwtwt4gt42hh'

graph_id = 'graph1'
pixela_endpoint = "https://pixe.la/v1/users"

# Create new user
# params = {
#     'token': 'bwrwtgbwtwt4gt42hh',
#     'username': 'alancoding',
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }
# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

# create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    'X-USER-TOKEN': TOKEN,
}

# params = {
#     'id': graph_id,
#     'name': 'My reading Graph',
#     'unit': 'Pages',
#     'type': 'int',
#     'color': 'shibafu'
#
# }
#
# response = requests.post(url=graph_endpoint, json=params, headers=headers)
# print(response.text)

# add_pixel

add_pixel_endpoint = f"{graph_endpoint}/{graph_id}"

today = datetime(year=2023, month=7, day=16).strftime('%Y%m%d')

# params = {
#     'date': today,
#     'quantity': '50',
# }
#
# response = requests.post(url=add_pixel_endpoint, json=params, headers=headers)
# print(response.text)

# put

put_endpoint = f"{add_pixel_endpoint}/{today}"

params = {
    'quantity': '150',
}

response = requests.put(url=put_endpoint, json=params, headers=headers)
print(response.text)

# delete
delete_endpoint = f"{put_endpoint}"

params = {
    'date' : today,
}

response = requests.delete(url=delete_endpoint, json=params, headers=headers)
print(response.text)