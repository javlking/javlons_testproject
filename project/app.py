from flask import Flask, render_template
from functions import database

app = Flask(__name__)


# Главная страница
@app.route('/') 
def home():
    data = database.Data().get_data() # Получаем все данные из таблицы

    total_usd = tuple([i[2] for i in data]) # Получаем только цены

    return render_template('index.html', datas=data, total_usd=sum(total_usd))


# Запускаем
app.run(host='0.0.0.0')
