from flask import Flask

app = Flask(__name__)

# функция вызовется, когда пользователь в браузере наберет АДРЕСХОСТА/ (зайдет на главную страницу сайта)
@app.route('/')
def index():
    # возвращаем HTML код, который увидит пользователь
    return """
        <html>
            <head>
                <title>Вупсень или пупсень?</title>
            </head>
            <body>
                <h1>Научись отличать Вупсеня от Пупсеня!</h1>
                <ul>
                    <li><a href="/vupsen">Это Вупсень!</a></li>
                    <li><a href="/pupsen">Это Пупсень!</a></li>
                </ul>
            </body>
        </html>
    """


# TODO: Сделай так, чтобы на странице выводилась картинка с Вупсенем из интернета
# PS. Для этого нужен тэг img: http://htmlbook.ru/html/img
@app.route('/vupsen')
def vupsen_page():
    pass


# TODO: Здесь добавь страницу /pupsen, на которой будет картинка с пупсенем

app.run(debug=True)