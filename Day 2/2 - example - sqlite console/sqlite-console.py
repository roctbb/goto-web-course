import sqlite3

# Подключаемся к БД
connection = sqlite3.connect("../3 - task - cd database/cd-database.sqlite")

print("GoTo SQLite console. To exit print exit...")

while True:
    query = input("SQL query:")

    if query == "exit":
        break


    try:
        # Отправляем запрос
        cursor = connection.execute(query)
        # Печатаем результат
        print(cursor.fetchall())

        # Сохраняем изменения в БД, если он были
        connection.commit()
    except:
        print("Error in query")

print("Goodbye...")
