import os
import sqlite3

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, g, flash
from translate import Translator

# Импорт класса по работе с базой данных.
from FDataBase import FDataBase
# Импортирую парсер гороскопа.
from class_horoscopeParser import ParsingHoroscope

# Импорт парсера гороскопа для знаков зодиака.

# Объект парсинга гороскопов.
obj_horoscope = ParsingHoroscope()

# Получение данных от сайта "https://horo.mail.ru/prediction/".
horoscope_yesterday = obj_horoscope.get_horoscope_yesterday()
horoscope_today = obj_horoscope.get_horoscope_today()
horoscope_tomorrow = obj_horoscope.get_horoscope_tomorrow()
horoscope_week = obj_horoscope.get_horoscope_week()
horoscope_month = obj_horoscope.get_horoscope_month()
horoscope_year = obj_horoscope.get_horoscope_year()

# Конфигурации.
DATABASE = '/app.db'
DEBUG = True
SECRET_KEY = '123yffgffcff'

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '123yffgffcff'

# Ссылка на текущий каталог базы данных.
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'app.db')))


# Функция для установления соединения с базой данных.
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


# Функция для создания базы данных.
def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:  # 'r' - Открываю файл на чтение!
        db.cursor().executescript(f.read())  # Выполняем скрипты.
    db.commit()  # Записываем в базу данных.
    db.close()  # Закрываем соединение.


# Основная страница. Today.
@app.route("/сегодня", methods=['POST', 'GET'])
@app.route("/today", methods=['POST', 'GET'])
@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html', horoscope_today=horoscope_today)

    if request.method == 'POST':
        return render_template('index.html', horoscope_today=horoscope_today)


# Основная страница. yesterday
@app.route("/вчера", methods=['POST', 'GET'])
@app.route("/yesterday", methods=['POST', 'GET'])
def yesterday():
    if request.method == 'GET':
        return render_template('yesterday.html', horoscope_yesterday=horoscope_yesterday)

    if request.method == 'POST':
        return render_template('yesterday.html', horoscope_yesterday=horoscope_yesterday)


# Основная страница. tomorrow
@app.route("/завтра", methods=['POST', 'GET'])
@app.route("/tomorrow", methods=['POST', 'GET'])
def tomorrow():
    if request.method == 'GET':
        return render_template('tomorrow.html', horoscope_tomorrow=horoscope_tomorrow)

    if request.method == 'POST':
        return render_template('tomorrow.html', horoscope_tomorrow=horoscope_tomorrow)


# Основная страница. Week
@app.route("/неделя", methods=['POST', 'GET'])
@app.route("/week", methods=['POST', 'GET'])
def week():
    if request.method == 'GET':
        return render_template('week.html', horoscope_week=horoscope_week)

    if request.method == 'POST':
        return render_template('week.html', horoscope_week=horoscope_week)


# Основная страница. Month
@app.route("/месяц", methods=['POST', 'GET'])
@app.route("/month", methods=['POST', 'GET'])
def month():
    if request.method == 'GET':
        return render_template('month.html', horoscope_month=horoscope_month)

    if request.method == 'POST':
        return render_template('month.html', horoscope_month=horoscope_month)


# Основная страница. Year
@app.route("/год", methods=['POST', 'GET'])
@app.route("/year", methods=['POST', 'GET'])
def year():
    if request.method == 'GET':
        return render_template('year.html', horoscope_year=horoscope_year)

    if request.method == 'POST':
        return render_template('year.html', horoscope_year=horoscope_year)


# Гороскоп для каждого знака.
@app.route("/horoscope_for_sing", methods=['POST', 'GET'])
def horoscope_for_sing():
    if request.method == 'GET':
        return render_template('horoscope_for_sing.html')

    if request.method == 'POST':
        zodiac = request.form['value1']
        date = request.form['value2']
        print(zodiac)
        print(date)

        # Функция определения гороскопа для знаков зодиака по дням.
        # :) Альтернатива была написать 72 метода для парсинга с сайта.
        def get_fastParser():
            url = f"https://horo.mail.ru/prediction/{zodiac}/{date}/"
            html = requests.get(url=url).text
            soup = BeautifulSoup(html, "html.parser")
            sing = soup.find("div", class_="article__text").text
            return sing

        translator = Translator(from_lang="English", to_lang="Russian")
        data_for_rus = translator.translate(date)
        zodiac_for_rus = translator.translate(zodiac)
        return render_template('horoscope_for_sing.html', DATA=data_for_rus.upper(), ZODIAC=zodiac_for_rus,
                               TEXT=get_fastParser())


# Соединение с БД, если оно еще не установлено.
def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


# forum.
@app.route("/forum", methods=['POST', 'GET'])
def forum():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'GET':
        return render_template('forum.html', menu=dbase.getMenu())

    if request.method == 'POST':
        if len(request.form['name']) > 0 and len(request.form['topic']) > 0 and len(request.form['article']) > 0:
            res = dbase.addPost(request.form['name'], request.form['topic'], request.form['article'])
            if not res:
                flash('Статья не добавлена', category='error')
            else:
                flash('Статья успешно добавлена!', category='success')
        else:
            flash("Где-то, что-то паламалася.", category="error")

    return render_template('forum.html', menu=dbase.getMenu())


# Закрываем соединение с базой данных, если оно было установлено.
def close_db(error):
    if hasattr(g, 'link_db'):  # Если в "g" существует свойство "link_db" значит соединение установлено.
        g.link_db.close()  # Закрываем соединение.


# Ловим ошибку связанную с вводом несуществующей страницы.
@app.errorhandler(404)
def errorNotFount(error):
    return render_template('error404.html', title="Страница не найдена")


# Ловим ошибку связанную с вводом несуществующей страницы.
@app.errorhandler(AttributeError)
def errorNotFount(error):
    return render_template('AttributeError.html', title="Страница не найдена")


if __name__ == "__main__":
    app.run()
