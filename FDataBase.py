import sqlite3


# Класс для записи и чтения данных из базу данных.
class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    # Метод получения данных из базы данных.
    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print("Ошибка чтения из Базы данных")

        return []

    # Метод добавления данных в базу данных.
    def addPost(self, name, topic, article):
        try:
            self.__cur.execute("INSERT INTO mainmenu VALUES(NULL, ?, ?, ?)", (name, topic, article))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в базу данных' + str(e))
            return False

        return True

    def addComment(self, name_for_comment, text_for_comment):
        try:
            self.__cur.execute("INSERT INTO comments VALUES(NULL, ?, ?)", (name_for_comment, text_for_comment))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в базу данных' + str(e))
            return False

        return True

