#API endpoint = the location of where the API is, usually the URL
# Example: api.coinbase.com, http://api.open-notify.org/iss-now.json
# Error codes:
# 1XX = Informational
# 2XX = Success
# 3XX = Redirection
# 4XX = Client Error
# 5XX = Server Error

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
response.raise_for_status()

data = response.json()['iss_position']['longitude']
longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']
print(data)
print(longitude, latitude)

