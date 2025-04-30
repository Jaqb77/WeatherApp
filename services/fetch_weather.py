import requests
from utils.convert import celcius, kmh

def fetch_weather(token: str, city: str):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}"

    response = requests.get(url)
    data = response.json()
    weather = {
        "name": data["name"],
        "temp": celcius(data['main']['temp']),
        "feels_like": celcius(data['main']['feels_like']),
        "humidity": data['main']['humidity'],
        "wind_speed": kmh(data['wind']['speed'])
    }
    return weather

