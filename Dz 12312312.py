import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

DB_NAME = "weather.db"
URL = "https://www.timeanddate.com/weather/ukraine/kyiv"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS temperature_data (
            datetime TEXT,
            temperature REAL
        )
    """)
    conn.commit()
    conn.close()

def get_temperature():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    temp_tag = soup.find("div", class_="h2")
    if temp_tag:
        temp_text = temp_tag.text.strip().split("°")[0]
        try:
            return float(temp_text)
        except ValueError:
            print("Не вдалося конвертувати температуру.")
            return None
    else:
        print("Температуру не знайдено.")
        return None

def insert_temperature(temperature):
    now = datetime.now().isoformat()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO temperature_data (datetime, temperature) VALUES (?, ?)", (now, temperature))
    conn.commit()
    conn.close()
    print(f"{now}: Температура {temperature}°C записана.")

def main():
    init_db()
    while True:
        temperature = get_temperature()
        if temperature is not None:
            insert_temperature(temperature)
        else:
            print("Пропущено запис через помилку.")
        time.sleep(1800)

if __name__ == "__main__":
    main()
