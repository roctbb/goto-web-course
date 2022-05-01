import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    price = random.randint(30, 130)

    # Чтобы не смешивать код на питоне и HTML, можно вынести HTML страницу в отдельный файл - шаблон (template)
    # Шаблоны должны храниться в подпапке templates
    # Фишка шаблонов - возможность подставлять внутрь них переменные с помощью кода {{ имя переменной }} внутри шаблона
    # Здесь мы просим фласк "отрендерить шаблон" index.html и передаем туда переменную price (посмотри в файле index.html, как она вставляется)
    return render_template('index.html', price=price)

app.run(debug=True)