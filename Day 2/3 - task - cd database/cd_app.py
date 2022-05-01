from flask import Flask, render_template, request, redirect
from sqlite3 import connect

app = Flask(__name__)

@app.route('/')
def index():
    conn = connect("cd-database.sqlite")
    # поисковый запрос, args вместо form, тк тип запроса - GET
    query = request.args.get('search')
    cursor = conn.execute("SELECT * FROM discs WHERE artist like ? or title like ?", ["%{}%".format(query), "%{}%".format(query)])

    discs = cursor.fetchall()

    # conn.commit() не нужен, тк мы не ничего не меняли

    return render_template("index.html", discs=discs, query=query)

@app.route('/add')
def add_page():
    return render_template("add.html")

@app.route('/add', methods=['post'])
def add_disc():
    artist = request.form.get('artist')
    title = request.form.get('title')
    type = request.form.get('type')

    # TODO: добавь внесение ссылки на картинку и описания

    if not artist or not title or type not in ['CD', 'SACD', 'Vinyl']:
        return redirect('/add')

    conn = connect("cd-database.sqlite")

    # TODO: добавь внесение ссылки на картинку и описания
    # Обратите внимание на знаки вопроса вместо прямой подстановки, это нужно для защиты от SQLinj
    conn.execute("INSERT INTO discs (artist, title, disc_type) VALUES (?, ?, ?)", [artist, title, type])
    # сохраняем изменения
    conn.commit()

    return redirect('/')

@app.route('/edit/<int:id>')
def edit_page(id):
    # TODO: добавь шаблон для редактирования и отправьте его пользователю
    # TODO: не забудь подставить текущие значения полей, для этого нужно взять из базу выбранный диск
    # SELECT * FROM discs WHERE id = ?
    pass

@app.route('/edit/<int:id>', methods=['post'])
def edit_disc(id):
    # TODO: сохрани изменения в базу если все поля заполнены
    # UPDATE discs SET artist = ?, title = ?, disc_type = ? WHERE id = ?
    return redirect('/')

# TODO: добавь обработчик для страницы удаления диска

app.run(debug=True)