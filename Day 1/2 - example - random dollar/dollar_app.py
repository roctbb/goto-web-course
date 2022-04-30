import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    price = random.randint(30, 130)
    return render_template('index.html', price=price)

app.run(debug=True)