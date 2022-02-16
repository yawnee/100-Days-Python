import requests
from twilio.rest import Client
import os

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
LAT = os.environ.get('LAT')
LON = os.environ.get('LON')
APP_ID = os.environ.get('APP_ID')

weather_params = {
    'lat': LAT,
    'lon': LON,
    'appid': APP_ID,
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
    account_sid = os.environ.get('ACCOUNT_ID')
    auth_token = os.environ.get('AUTH_TOKEN')
    FROM = os.environ.get('FROM_PHONE')
    TO = os.environ.get('TO_PHONE')
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain!",
        from_=FROM,
        to=TO
    )
    print(message.status)
