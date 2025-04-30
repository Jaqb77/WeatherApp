import os
from dotenv import load_dotenv
from services.fetch_weather import fetch_weather
from services.logs_txt import logsRead, logsWrite
from datetime import datetime
load_dotenv()

API_KEY = os.environ.get("API_KEY")
CITY = os.environ.get("CITY")

try:
    weather = fetch_weather(API_KEY, CITY)
    print(weather)
    logsWrite(f"{datetime.now()}: Pobrano dane pogodowe miasta: {CITY}\n")
except Exception as e:
    print(e)
    logsWrite(f"{datetime.now()}: Wystapil blad {e} podczas pobierania danych dla miasta: {CITY}\n")

logsRead()