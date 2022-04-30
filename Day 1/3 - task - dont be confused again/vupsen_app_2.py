from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vupsen')
def vupsen_page():
    link = ""
    description = "Несмотря на свой характер, Вупсеню не чужды страхи. В серии «Трусишка Вупсень», он не может спрыгнуть с батута, потому что боится высоты. В серии «Обманщики», Вупсень по этой же причине не соглашается на шутку с обрывом."
    return render_template('actor.html', name="Вупсень", description=description, img=link)

@app.route('/pupsen')
def pupsen_page():
    # TODO: используй шаблон actor.html чтобы вывести информацию о Пупсене
    pass

# TODO: добавь страницы еще нескольких персонажей

app.run(debug=True)
