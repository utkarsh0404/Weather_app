import requests
import json

city = input("Enter a City Name: ")

base_url= "https://api.openweathermap.org/data/2.5/weather"
api_key= "b2e0a9c21f42b7d219f58bd30405e4d6"

A = {
     "q":city,
     "appid":api_key,
     "units":"metric"
}

response = requests.get(base_url,A)
data=response.json()


D = data["weather"][0]["description"]
H = data["main"]["humidity"]
T = data["main"]["temp"]
print(f"the current temperature of the {city} is {T} and humidity is {H} while it's weather is {D}")
