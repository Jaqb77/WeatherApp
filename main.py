import time
from services.fetch_weather import fetch_weather
from services.logs_txt import logsRead, logsWrite
from services.excel_file import saveToExcel
from services.mongodb import save_to_mongo
from datetime import datetime
from config import Config

CITY = input("Podaj nazwe miasta: ")
print("1. zapisuj do pliku excel")
print("2. zapisuj do MongoDB")
print("3. zapisuj do MongoDB i pliku excel")
OPERATION = int(input("Wybierz rodzaj operacji: "))

def start():
    weather = fetch_weather(Config.API_KEY, CITY)
    logsWrite(Config.LOG_FILENAME, f"{datetime.now()}: Pobrano dane pogodowe miasta: {Config.CITY}\n")

    match OPERATION:
        case 1:
            saveToExcel(Config.EXCEL_FILENAME, weather)
        case 2:
            save_to_mongo(weather)
        case 3:
            save_to_mongo(weather)
            saveToExcel(Config.EXCEL_FILENAME, weather)
        case _:
            print("Nie rozpoznano operacji")

while True:
    try:
        start()
        print('pobrano dane')
    except Exception as e:
        print(e)
        logsWrite(f"{datetime.now()}: Wystapil blad {e} podczas pobierania danych dla miasta: {Config.CITY}\n")

    time.sleep(10)

