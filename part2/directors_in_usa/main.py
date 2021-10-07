# Режиссеры из США
# Нам требуется узнать, сколько фильмов
# снял каждый режиссер из США.
# Обратите внимание, что в столбце country
# встречаются и перечисления стран.
# Для удобства отсортируйте выдачу по убыванию
# и выведите первые 15 результатов
# Пример результата:
#
# Данные нужно вывести в следующем формате:
# Квентин Тарантино: 6 фильмов
# Ларс Фон Триер: 5 фильмов
# Гай Ричи: 10 фильмов
#
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------
import sqlite3

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("")  # TODO измените код запроса
cur.execute(sqlite_query)
executed_query = cur.fetchall()
result = ""
# TODO Результат запроса сохраните в переменной result
# для последующей выдачи в требуемом формате
con.close()

if __name__ == '__main__':
    print(result)
