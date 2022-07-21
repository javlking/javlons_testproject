# testproject
Script + flask web for testproject
Для начала в консоли пропишите команду git clone https://github.com/javlking/testproject.git

Потом нужно установить необходимые библиотеки: pip install -r requirements.txt

Заходим в папку с проектом: cd project/

В этой папке есть файл app.py - Это основной файл для запуска сайта
set FLASK_APP=app.py (Windows)
export FLASK_APP=app.py (Linux)

flask run и переходим по ссылке


Также нужно включить сам скрипт: cd functions/

Файл main.py является основным и его нужно запустить чтобы скрипт работал

Файл utils.py хранит в себе функции

Файл database.py подключение и работа с БД

Файл handlers.py подключение к ТГ боту (https://t.me/kanalserv) - на этот канал приходит сообщение о просрочке

Файл credents.json хранит токены для GOOGLE API


На сайте для фронтенда использовал bootstrap, html дабы пока не знаком с React)
