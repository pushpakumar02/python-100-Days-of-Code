import requests
from twilio.rest import Client
# import os
# from twilio.http.http_client import TwilioHttpClient for ref. see 317 time_stamp 4:00

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "2bd6dbc67eb62f17bfdbefeeec94d5bb"  # os.environ.get("OWM_API_KEY")
account_sid = "ACb18cf2014d34e5c4fd3b365892a06127"
auth_token = "3368a068ed3986515753bd21417358d5"  # os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": 13.19165,
    "lon": 79.53151,  
    # "lat": 17.58,
    # "lon": 139.55, # Australia/Brisbane/mar20,24
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0][" id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token)  # ,http_client=proxy_client
    message = client.messages \
        .create(
        body="It's going to rain today.Remember to bring an ☔",
        from_='+19164720365',
        to='+91 63794 68663'
    )

    print(message.status)
