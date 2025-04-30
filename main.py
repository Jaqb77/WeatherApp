import time
from services.fetch_weather import fetch_weather
from services.logs_txt import logsRead, logsWrite
from services.excel_file import saveToExcel
from datetime import datetime
from config import Config

def start():
    weather = fetch_weather(Config.API_KEY, Config.CITY)
    logsWrite(Config.LOG_FILENAME, f"{datetime.now()}: Pobrano dane pogodowe miasta: {Config.CITY}\n")
    logsRead(Config.LOG_FILENAME)
    saveToExcel(Config.EXCEL_FILENAME, weather)

while True:
    try:
        start()
        print('pobrano dane')
    except Exception as e:
        print(e)
        logsWrite(f"{datetime.now()}: Wystapil blad {e} podczas pobierania danych dla miasta: {Config.CITY}\n")

    time.sleep(5)

