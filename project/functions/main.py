import gspread
from oauth2client.service_account import ServiceAccountCredentials

import requests
import time
from datetime import datetime

import utils

response = requests.get("https://www.cbr-xml-daily.ru/latest.js").json()  # Подключение к API ЦБР

rate = response["rates"]["USD"]  # Получаем курс RUB к USD

# Соединения для google API и Подключение к google API
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credents.json", scope)  # Подключение к API

client = gspread.authorize(creds)  # Авторизация

sheet = client.open("Копия test").sheet1  # Открываем нужный лист

sended_messages = []  # Временно храним отправленные в тг сообщения

while True:
    data = tuple(sheet.get_all_records())  # Получаем данные из таблицы
    last_data = []  # Создаем список для удобного отслеживания данных из таблицы

    # Пробегаемся по каждой строке таблицы
    for row in data:
        try:
            usd_to_rub = round(row['стоимость,$'] * rate ** -1, 2),  # Получаем курс

            # Если все поля заполнены то добавляем в список
            if all(row.values()) and tuple(row.values()) + usd_to_rub not in last_data:
                last_data.append(tuple(row.values()) + usd_to_rub)

                # Если дата поставки была просрочена, вызываем функцию отправки сообщения в бот
                if datetime.strptime(row['срок поставки'], "%d.%m.%Y") < datetime.now() and row not in sended_messages:
                    utils.send_message_to_tg(tuple(row.values()) + usd_to_rub)

                    sended_messages.append(row)


        # В случае ошибки, удаляем эту строку из списка
        except TypeError:
            last_data.remove(row)
            continue

    # Количество данных внутри списка (для отслеживания обновлений)
    last_data_count = len(last_data)

    # Обращаемся к функции добавления данных из таблицы в БД
    utils.send_to_database(last_data, last_data_count)

    # Делаем задержку в 1 секунду, чтобы не нагружать API
    time.sleep(1)
