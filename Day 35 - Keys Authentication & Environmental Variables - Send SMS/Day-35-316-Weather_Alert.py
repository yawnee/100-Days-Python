import requests
from twilio.rest import Client

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'

with open('./data/settings.txt', mode='r') as data:
    list_settings = data.read().splitlines()
    weather_params = {
        'lat': list_settings[0],
        'lon': list_settings[1],
        'appid': list_settings[2],
        'exclude': 'current,minutely,daily'
    }

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with open('./data/phone_number.txt', mode='r') as data_phone:
        data_phone_list = data_phone.read().splitlines()
        account_sid = data_phone_list[0]
        auth_token = data_phone_list[1]
        FROM = data_phone_list[2]
        TO = data_phone_list[3]

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain!",
        from_=FROM,
        to=TO
    )
    print(message.status)
