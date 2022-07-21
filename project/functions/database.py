import psycopg2

connection = psycopg2.connect(database="da7sr1p7nl26f1",
                               user="pdtvcbecwsihgc",
                               password="9ce172ddad4c8a03c16eec42c6ad97daaacb6047766eede1f8052eac723f80a3",
                               host="ec2-34-235-198-25.compute-1.amazonaws.com")
sql = connection.cursor()

# Создаем таблицу kanal_stat с колонками (№, заказ №, стоимость $, стоимость ₽, срок поставки)
# sql.execute('CREATE TABLE kanal_stat (id INTEGER UNIQUE, order_number INTEGER , price_usd REAL, price_rub REAL, ship_date VARCHAR(155));')
# connection.commit()
# connection.close()


class Data:
    # Создаем подключения
    def __init__(self):
        self.connection = psycopg2.connect(database="da7sr1p7nl26f1",
                                           user="pdtvcbecwsihgc",
                                           password="9ce172ddad4c8a03c16eec42c6ad97daaacb6047766eede1f8052eac723f80a3",
                                           host="ec2-34-235-198-25.compute-1.amazonaws.com")
        self.sql = self.connection.cursor()

    # Функция добавления в базу
    def create_data(self, data_to_insert):
        try:
            self.sql.executemany('INSERT INTO kanal_stat (id, order_number, price_usd, ship_date, price_rub) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING;', data_to_insert)

            self.connection.commit()
       
        except Exception as e:
            pass

    # Функция получения данных из базы
    def get_data(self):
        self.sql.execute("select id, order_number, price_usd, ship_date, price_rub from kanal_stat ORDER BY id;")
        
        return self.sql.fetchall()

    # Функция удаления из базы
    def delete_data_from_db(self, id):
        self.sql.execute(f'DELETE FROM kanal_stat WHERE id={id}')
        self.connection.commit()

    # Функция обновления в базе
    def update_or_create_data(self, id, *args):
        self.sql.execute('UPDATE kanal_stat SET order_number=%s, price_usd=%s, ship_date=%s, price_rub=%s WHERE id=%s', args[0]+(id,))
        self.connection.commit()