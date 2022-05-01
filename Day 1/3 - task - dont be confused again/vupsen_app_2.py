from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vupsen')
def vupsen_page():
    link = "https://static.wikia.nocookie.net/luntik/images/9/9b/%D0%92%D1%83%D0%BF%D1%81%D0%B5%D0%BD%D1%8C-2.png/revision/latest/scale-to-width-down/145?cb=20181030170410&path-prefix=ru"
    description = "Несмотря на свой характер, Вупсеню не чужды страхи. В серии «Трусишка Вупсень», он не может спрыгнуть с батута, потому что боится высоты. В серии «Обманщики», Вупсень по этой же причине не соглашается на шутку с обрывом."

    # Поскольку для каждого персонажа HTML код будет одиниковым (за исключением нескольких строк - имени, описания и ссылки на картинку)
    # мы можем использовать один и тот же шаблон на страницах всех персонажей, подставляя только то, что меняется
    return render_template('actor.html', name="Вупсень", description=description, img=link)

@app.route('/pupsen')
def pupsen_page():
    # TODO: используй шаблон actor.html чтобы вывести информацию о Пупсене
    pass

# TODO: добавь страницы еще хотя бы двух персонажей

app.run(debug=True)
