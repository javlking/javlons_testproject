# javlons_testproject
Script + flask web + postgrs for testproject

Ссылка на документ Google Sheets https://docs.google.com/spreadsheets/d/1zswu1uvw8mX3fWxcBVgukX5gSrY5BHFKbWgTjaQdPK0/edit?usp=sharing

Для начала в консоли пропишите команду git clone https://github.com/javlking/testproject.git

Затем cd javlons_testproject/

Потом нужно установить необходимые библиотеки: pip install -r requirements.txt

Заходим в папку с проектом: cd project/

В этой папке есть файл app.py - Это основной файл для запуска сайта
set FLASK_APP=app.py (Windows)
export FLASK_APP=app.py (Linux)

flask run и переходим по ссылке


# Также нужно запустить сам скрипт он находится внутри папки functions: cd functions/

# Файл main.py является основным и его нужно запустить чтобы скрипт работал

Файл utils.py хранит в себе функции

Файл database.py подключение и работа с БД (postgresql)

Файл handlers.py подключение к ТГ боту (https://t.me/kanalserv) - на этот канал приходит сообщение о просрочке

Файл credents.json хранит токены для GOOGLE API


На сайте для фронтенда использовал bootstrap, html дабы пока не знаком с React)
