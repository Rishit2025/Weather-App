import os
import requests
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_key = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"\nWeather in {city}: {temp}°C, {desc.capitalize()}")
    else:
        print(f"Error: {data.get('message', 'Unknown error')}")

city = input("Enter city name: ").strip()
get_weather(city)
