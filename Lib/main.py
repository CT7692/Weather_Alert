import requests
import os
from twilio.rest import Client


twi_sid = os.environ.get("TWILIO_SID")
t_auth_token = os.environ.get("TWI_AUTH_TOKEN")

def api_resp(my_response):
    will_rain = False
    jdata = my_response.json()
    for entry in jdata['list']:
        for line in entry['weather']:
            if line['id'] < 600:
                will_rain = True
    if will_rain:
        client = Client(twi_sid, t_auth_token)
        message = client.messages.create(
            body="Bring coat and umbrella.",
            from_=os.environ.get("SOME_NUM"),
            to='+16362845670'
        )

parameters = {
    "lat": 38.781151,
    "lon":-90.486931,
    "appid": os.environ.get("OWM_APP_ID"),
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters, timeout=60)
response.raise_for_status()
api_resp(response)
