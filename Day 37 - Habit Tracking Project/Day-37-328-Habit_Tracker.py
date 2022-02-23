import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = 'yawnny'
TOKEN = 'stV5fOvh20Ctn6bueAbH'
GRAPH_ID = 'graph1'

user_params = {
    "token": TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

today = datetime.now()
# Can also do this:
# today = datetime(year=2022, month=02, day=23)
print(today.strftime('%Y%m%d'))

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input('How many kilometers did you cycle today? '),
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# Updating the graph with a new value below
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    'quantity': '4.5'
}
# Updating the graph with a new value below
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# deleting values
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.put(url=delete_endpoint, headers=headers)
print(response.text)
