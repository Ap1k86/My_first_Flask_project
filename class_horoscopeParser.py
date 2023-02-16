import requests
from bs4 import BeautifulSoup


# Класс по работе с сайтом "https://horo.mail.ru/".
class ParsingHoroscope:

    def __init__(self):
        self.yesterday = None
        self.today = None
        self.tomorrow = None
        self.week = None
        self.month = None
        self.year = None

    # Метод определения гороскопа на вчерашний день.
    def get_horoscope_yesterday(self):
        url = "https://horo.mail.ru/prediction/yesterday/"
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, "html.parser")
        self.yesterday = soup.find("div", class_="article__text").text
        return self.yesterday

    # Метод определения гороскопа на сегодня.
    def get_horoscope_today(self):
        url = "https://horo.mail.ru/prediction/today/"
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, "html.parser")
        self.today = soup.find("div", class_="article__text").text
        return self.today

    # Метод определения гороскопа на завтрашний день.
    def get_horoscope_tomorrow(self):
        url = "https://horo.mail.ru/prediction/tomorrow/"
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, "html.parser")
        self.tomorrow = soup.find("div", class_="article__text").text
        return self.tomorrow

    # Метод определения гороскопа на неделю.
    def get_horoscope_week(self):
        url = "https://horo.mail.ru/prediction/week/"
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, "html.parser")
        self.week = soup.find("div", class_="article__text").text
        return self.week

    # Метод определения гороскопа на месяц.
    def get_horoscope_month(self):
        url = "https://horo.mail.ru/prediction/month/"
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, "html.parser")
        self.month = soup.find("div", class_="article__text").text
        return self.month

    # Метод определения гороскопа на год.
    def get_horoscope_year(self):
        url = "https://horo.mail.ru/prediction/year/"
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, "html.parser")
        self.year = soup.find("div", class_="article__text").text
        return self.year
