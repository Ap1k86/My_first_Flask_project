import json
# ---- Ш П А Р Г А Л К А ----
# r — открывает файл только для чтения.
# w — открывает файл только для записи.
#      (Удаляет содержимое файла, если файл существует; если файл не существует, создает новый файл для записи)
# w+ — открывает файл для чтения и записи.
#      (Удаляет содержимое файла, если файл существует; если файл не существует, создает новый файл для чтения и записи)
# a+ - открывает файл для чтения и записи.
#      (Информация добавляется в конец файла)
# b - открытие в двоичном режиме.

# Абсолютный путь (path) - показывает точное местонахождение файла
# Относительный путь (path) - показывает путь к файлу относительно какой-либо "отправной точки"

# JSON — текстовый формат обмена данными, основанный на JavaScript (похож на словарь Python)


# Класс для работы с файлами
class File:

    # Записать текст из "text" в файл по пути "path"
    @staticmethod
    def write_text(text: str, path: str):
        # Открыть файл как объект и временно поместить его в переменную "file"
        with open(path, mode="a") as f:
            # Объект файл будет жить только в этом теле и по окончанию закроется и сохранится
            f.write(text)

    # Прочитать текст из файла по пути "path"
    @staticmethod
    def read_text(path: str):
        # Открыть файл как объект и временно поместить его в переменную "file"
        with open(path, mode="r") as f:
            return f.read()

    # Записать словарь/список из "data" в файл по пути "path"
    @staticmethod
    def write_json(data: dict or list, path: str):
        with open(path, mode="a") as f:
            json.dump(data, f)

    # Прочитать словарь/список из файла по пути "path"
    @staticmethod
    def read_json(path: str):
        with open(path, mode="r") as f:
            return json.load(f)