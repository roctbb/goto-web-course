import requests
from sqlite3 import connect
from bs4 import BeautifulSoup

# будем искать обложки к альбомам на https://www.discogs.com/

connection = connect("../../Day 2/3 - task - cd database/cd-database.sqlite")
cursor = connection.execute("SELECT * FROM discs")

URL = "https://www.discogs.com/ru/search/"

for disc in cursor.fetchall():
    id = disc[0]
    artist = disc[1]
    title = disc[2]

    search_query = artist + " " + title

    print("Searching {}...".format(search_query))

    answer = requests.get(URL, params={
        "q": search_query
    })

    # TODO: Достаньте из html кода ссылку на обложку, если она там есть и сохраните в БД
    # TODO 2: Перейдите на страницу альбома и достаньте треклист
    # TODO 3: Интегрируйте поиск обложки в код сервиса по управлению библиотекой дисков из второго дня


    break

