from database import Data
from handlers import bot


# Функция для загрузки данных из таблицы в базу
def send_to_database(last_data, last_data_count):
    all_data = Data()
    check = all_data.get_data()
    
    # Если данных в таблице больше чем данные в БД, добавляем в базу
    if len(check) < last_data_count:
        all_data.create_data(last_data)


    # Если данных в таблице меньше чем данные в БД, удаляем из базы
    elif len(check) > last_data_count:
        for i in check:
            if i not in last_data:
                all_data.delete_data_from_db(i[0])
    

    # Если данных в таблице равно к данным в БД, проверяем и если нужно изменяем
    elif len(check) == last_data_count:
        for i in last_data:
            all_data.update_or_create_data(i[0], i[1:])


# Функция предупреждения о просроченной поставке
def send_message_to_tg(notify):
    text = f'Уведомление о поставке\n\nНомер заказа: {notify[1]}\nСтоимость в $: {notify[2]}\nСтоимость в ₽: {notify[-1]}\'' \
           f'\n\nСрок поставки: {notify[3]}'

    bot.send_message(-1001504002441, text)
