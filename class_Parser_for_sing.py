import requests
from bs4 import BeautifulSoup


# Парсер гороскопа для овна.
class ParsingForSing:

    def __init__(self):
        self.sing = None

    # Метод определения гороскопа для знаков зодиака по дням.
    def get_fastParser(self):
        url = "https://horo.mail.ru/prediction/aries/yesterday/"
        html = requests.get(url=url).text
        soup = BeautifulSoup(html, "html.parser")
        self.sing = soup.find("div", class_="article__text").text
        return self.sing


